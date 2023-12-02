using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[System.Serializable]
public class IKComponent
{
    [SerializeField] string name = "default";
    [SerializeField] private Transform target;

    private Vector3 startPosition;
    [SerializeField] private Vector3 wantedPosition;
    float moveTime = 0;

    public void SetTargetPosition(Vector3 newWantedPosition)
    {
        if (target == null) return;
        startPosition = target.transform.position;
        wantedPosition = newWantedPosition;

        moveTime = 0;
    }
    public void SetTargetPosition(Vector2 newWantedPosition)
    {
        if (target == null) return;
        startPosition = target.transform.position;
        wantedPosition.x = newWantedPosition.x;
        wantedPosition.y = newWantedPosition.y;

        moveTime = 0;
    }

    public void MoveTarget(float delta)
    {
        moveTime += delta;
        if (moveTime > 1) return;
            
        target.transform.position = Vector3.Lerp(startPosition,wantedPosition, moveTime);
    }
}
