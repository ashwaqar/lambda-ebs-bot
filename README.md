# lambda-ebs-bot
A lambda function to delete the available (unattached) EBS volumes.

`serverless.yml` contains nessasary role to allow access to ec2 from lambda and triggers the function every 1 minute.
