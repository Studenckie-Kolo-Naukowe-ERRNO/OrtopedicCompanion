using System.Net;
using System.Net.Sockets;
using System.Text;
using UnityEngine;
using System.Threading;
using System.Collections.Generic;
using System;

// https://github.com/ConorZAM/Python-Unity-Socket/blob/master/MyListener.cs

public class PythonServer : MonoBehaviour
{
    public static PythonServer Instance;
    private TcpListener listener;
    // Create handle to connected tcp client. 
    private TcpClient client;
    // Background thread for TcpServer workload.
    private Thread listenerThread;
    private const int connectionPort = 25001;

    bool running = true;


    [SerializeField]private List<Vector2> data = new List<Vector2>();
    private const char SEPERATOR = '|';

    public List<Vector2> GetData() { return data; }
    private void Start()
    {
        if (Instance == null) Instance = this;
        else 
        {
            Destroy(gameObject);
            return;
        } 
        for (int i = 0; i < 17; i++) data.Add(Vector2.zero);

        // Receive on a separate thread so Unity doesn't freeze waiting for data
        listenerThread = new Thread(new ThreadStart(IncomingData));
        listenerThread.IsBackground = true;
        listenerThread.Start();
    }
    private void OnDestroy()
    {
        running = false;
    }
    private void OnApplicationQuit()
    {
        running = false;
    }
    private void IncomingData()
    {
        listener = new TcpListener(IPAddress.Parse("127.0.0.1"), 25001);
        listener.Start();
        Debug.Log("Server is listening");
        Byte[] bytes = new Byte[1024];

        running = true;
        while (running)
        {
            using (client = listener.AcceptTcpClient())
            {			
                using (NetworkStream stream = client.GetStream())// Get a stream object for reading 		
                {
                    int length;
                    // Read incomming stream into byte arrary. 						
                    while ((length = stream.Read(bytes, 0, bytes.Length)) != 0)
                    {
                        var incommingData = new byte[length];
                        Array.Copy(bytes, 0, incommingData, 0, length); 							
                        string clientMessage = Encoding.ASCII.GetString(incommingData);
                        ParseData(clientMessage);
                    }
                    //byte[] response = Encoding.UTF8.GetBytes("Hello from the server!");
                    //nwStream.Write(response, 0, response.Length);
                }
            }
        }
        listener.Stop();
        Debug.Log("Server closed");
    }

    // Use-case specific function, need to re-write this to interpret whatever data is being sent
    private void ParseData(string dataString)
    {
        dataString=dataString.Replace('.', ',');
        string[] strArray = dataString.Split(SEPERATOR);

        Vector2 vec = new Vector2(0, 0);
        for (int i = 0; i < strArray.Length-1; i += 2)
        {
            float x = -0.13f;
            float y = -0.13f;
            if (float.TryParse(strArray[i], out float xx))  x = xx; 
            else  Debug.LogWarning($"Cant parse pos X {i}/{strArray.Length} : {strArray[i]}"); 

            if (float.TryParse(strArray[i + 1], out float yy))  y = yy; 
            else  Debug.LogWarning($"Cant parse pos Y {i + 1}/{strArray.Length} : {strArray[i + 1]}");

            data[(int)(i / 2)]=(new Vector2(x, y));
        }
    }
}
