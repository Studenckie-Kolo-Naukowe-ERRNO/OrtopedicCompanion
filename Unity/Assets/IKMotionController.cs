using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class IKMotionController : MonoBehaviour
{
    [SerializeField] private IKComponent entireAvatar;
    [SerializeField] private Transform animCenter;
    [SerializeField] private Vector2 multiplier;
    [SerializeField] private IKComponent[] components;
    [SerializeField] private float framerate = 30.0f;
    float nextFrameUpdate = 0;

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
       
        Vector2 massCenter = (data[12]+data[11])/2;

        Vector2 offset = new Vector2(0, animCenter.transform.localPosition.y - massCenter.y);

        components[0].SetTargetPosition(massCenter + offset);
        components[1].SetTargetPosition(data[10] + offset);
        components[2].SetTargetPosition(data[9] + offset);

        float offsetXaxis = massCenter.x - animCenter.transform.localPosition.x;
        entireAvatar.SetTargetPosition(new Vector2(offsetXaxis, 0));
    }
}