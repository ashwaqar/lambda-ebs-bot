#!/usr/bin/python

import boto3
ec2 = boto3.resource('ec2', region_name='us-west-2')


def lambda_handler(event, context):
    for vol in ec2.volumes.all():
        if vol.state == 'available':
                vid = vol.id
                v = ec2.Volume(vol.id)
                v.delete()
                print('Deleted ' + vid)
