using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class IKMotionController : MonoBehaviour
{
    [SerializeField] private IKComponent[] components;
    [SerializeField] private float framerate = 30.0f;

    private void Update()
    {
        for (int i = 0; i < components.Length; i++)
        {
            components[i].MoveTarget(Time.deltaTime* framerate);
        }
    }
}
