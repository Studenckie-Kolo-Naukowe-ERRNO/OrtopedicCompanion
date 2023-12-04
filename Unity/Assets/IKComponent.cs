using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.ProBuilder.MeshOperations;

[System.Serializable]
public class IKComponent
{
    [SerializeField] string name = "default";
    [SerializeField] private Transform target;

    private Vector3 startPosition;
    [SerializeField] private Vector3 wantedPosition;
    float moveTime = 0;

    Vector3 moveVector = Vector3.zero;
    int framesWithoutData = 0;

    public void SetTargetPosition(Vector3 newWantedPosition, bool shouldUpdate = true)
    {
        if (target == null) return;

        startPosition = target.transform.position;
        wantedPosition = shouldUpdate ? newWantedPosition : startPosition;
        /*TO-DO
         * If the update should not take place, continue moving based on the previous frame for X frames or until data is received
         */

        if (shouldUpdate)
        {
            wantedPosition = newWantedPosition;
            moveVector = wantedPosition - startPosition;
            framesWithoutData = 0;
        }
        //Something is off
        else if (framesWithoutData < 5)
        {
            wantedPosition = startPosition + moveVector;
            framesWithoutData ++;
        }
        else
        {
            wantedPosition = startPosition;
            framesWithoutData ++;
        }

        moveTime = 0;
    }

    public void MoveTarget(float delta)
    {
        moveTime += delta;
        if (moveTime > 1) return;
            
        target.transform.position = Vector3.Lerp(startPosition,wantedPosition, moveTime);
    }
}
