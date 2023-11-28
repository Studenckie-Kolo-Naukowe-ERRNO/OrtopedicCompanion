using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class IKComponent
{
    [SerializeField] private Transform target;
    [SerializeField] private Vector3 wantedPosition;
    float snapDistance = 1f;

    public void MoveTarget(float f, float delta)
    {
        /*
        Vector3 dist = wantedPosition - target.position;

        if (dist.magnitude > snapDistance)
        {
            SnapHands();
        }
        else
        {
            rb.velocity = dist / delta;
        }

        Quaternion rotationDiff = target.rotation * Quaternion.Inverse(transform.rotation);
        rotationDiff.ToAngleAxis(out float angleInDegree, out Vector3 rotationAxis);

        Vector3 rotationDiffInDegree = angleInDegree * rotationAxis;

        rb.angularVelocity = (rotationDiffInDegree * Mathf.Deg2Rad / delta);
        */
    }
}
