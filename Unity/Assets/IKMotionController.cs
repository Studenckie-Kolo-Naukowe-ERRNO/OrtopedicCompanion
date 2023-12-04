using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;

public class IKMotionController : MonoBehaviour
{
    [SerializeField] private IKComponent entireAvatar;
    [SerializeField] private Transform animCenter;
    [SerializeField] private Vector2 multiplier;
    [SerializeField] private Vector2 massCenter;
    [SerializeField] private IKComponent[] components;
    [SerializeField] private float framerate = 30.0f;
    [SerializeField] private TextMeshProUGUI debugMultiplier;
    float nextFrameUpdate = 0;

    private void Start()
    {
        debugMultiplier.SetText($"[{multiplier.x},{multiplier.y}]");
    }
    private void Update()
    {
        for (int i = 0; i < components.Length; i++)
        {
            components[i].MoveTarget(Time.deltaTime* framerate);
        }
        entireAvatar.MoveTarget(Time.deltaTime * framerate);

        if (Time.time > nextFrameUpdate)
        {
            nextFrameUpdate = Time.time + (1/framerate);
            UpdateComponents();
        }
    }

    public void UpdateComponents()
    {
        List<Vector2> data = new List<Vector2>(PythonServer.Instance.GetData());
        for(int i=0;i<data.Count; i++)
        {
            data[i] *= multiplier;
        }
       
        if (data[0].x <= -1) 
        {
            Debug.Log($"NO CENTER {data[0].x}");
        }
        else
        {
            massCenter = data[0];
        }

        Vector2 offset = new Vector2(0, animCenter.transform.localPosition.y - massCenter.y);

        components[0].SetTargetPosition(massCenter + offset, massCenter[0] > -1.0f);
        components[1].SetTargetPosition(massCenter + data[10] + offset);
        components[2].SetTargetPosition(massCenter + data[9]  + offset);

        float offsetXaxis = massCenter.x - animCenter.transform.localPosition.x;
        entireAvatar.SetTargetPosition(new Vector2(offsetXaxis, 0), massCenter[0] > -1.0f);
    }

    public void ChangeMultiplierX(float newX)
    {
        multiplier.x = newX;
        debugMultiplier.SetText($"[{multiplier.x},{multiplier.y}]");
    }
    public void ChangeMultiplierY(float newY)
    {
        multiplier.y = newY;
        debugMultiplier.SetText($"[{multiplier.x},{multiplier.y}]");
    }
}