using System.Net;
using System.Net.Sockets;
using System.Text;
using UnityEngine;
using System.Threading;
using System.Collections.Generic;

// https://github.com/ConorZAM/Python-Unity-Socket/blob/master/MyListener.cs

public class PythonServer : MonoBehaviour
{
    private Thread thread;
    private int connectionPort = 25001;
    private TcpListener server;
    private TcpClient client;
    
    private bool running;
    public bool IsRunning() { return running; }

    [SerializeField]private List<Vector2> data;
    public List<Vector2> GetData() { return data; }

    private void Start()
    {
        data = new List<Vector2>();
        Vector2 vec = new Vector2(0.0f, 0.0f);
        for (int i = 0; i < 17; i++)    data.Add(vec);


        // Receive on a separate thread so Unity doesn't freeze waiting for data
        ThreadStart ts = new ThreadStart(StartConnection);
        thread = new Thread(ts);
        thread.Start();
    }

    private void StartConnection()
    {
        // Create the server
        server = new TcpListener(IPAddress.Any, connectionPort);
        server.Start();
        
        Debug.Log("Server is listening");

        // Create a client to get the data stream
        client = server.AcceptTcpClient();

        // Start listening
        running = true;
        while (running) ReceiveData();

        server.Stop();
    }

    private void ReceiveData()
    {
        // Read data from the network stream
        NetworkStream nwStream = client.GetStream();
        byte[] buffer = new byte[client.ReceiveBufferSize];
        int bytesRead = nwStream.Read(buffer, 0, client.ReceiveBufferSize);

        // Decode the bytes into a string
        string dataReceived = Encoding.UTF8.GetString(buffer, 0, bytesRead);

        // Make sure we're not getting an empty string
        //dataReceived.Trim();
        if (dataReceived != null && dataReceived != "")
        {
            // Convert the received string of data to the format we are using
            data = ParseData(dataReceived);
            nwStream.Write(buffer, 0, bytesRead);
        }
    }

    private char SEPERATOR = '|';

    // Use-case specific function, need to re-write this to interpret whatever data is being sent
    private List<Vector2> ParseData(string dataString)
    {
        List<Vector2> result = new List<Vector2>();
        Debug.Log(dataString);

        // Split the elements into an array
        string[] strArray = dataString.Split(SEPERATOR);

        Vector2 vec = new Vector2(0, 0);
        for (int i = 0; i < strArray.Length; i += 2)
        {
            vec = new Vector2(
                float.Parse(strArray[i]),
                float.Parse(strArray[i + 1]));

            data[(int)(i / 2)] = vec;
        }


        return result;
    }
}
