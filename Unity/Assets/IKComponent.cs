using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[System.Serializable]
public class IKComponent
{
    [SerializeField] bool shouldUseLerp = true;
    [SerializeField] bool debugMode = true;
    [SerializeField] private Transform target;
    [SerializeField] private Transform DebugWantedPos;

    private Vector3 startPosition;
    private Vector3 wantedPosition;
    float moveTime = 0;

    public void SetTargetPosition(Vector3 newWantedPosition)
    {
        startPosition = target.transform.position;
        //wantedPosition = newWantedPosition;
        wantedPosition = DebugWantedPos.position;
        moveTime = 0;
    }

    public void MoveTarget(float delta)
    {
        if (shouldUseLerp)
        {
            moveTime += delta;
            if (moveTime > 1) 
            {
                if (debugMode) SetTargetPosition(Vector3.zero);
                else return;
            }
            
            target.transform.position = Vector3.Lerp(startPosition,wantedPosition, moveTime);
        }
        else
        {
            target.transform.position = Vector3.MoveTowards(target.transform.position, DebugWantedPos.position, 0.1f);
        }
    }
}
