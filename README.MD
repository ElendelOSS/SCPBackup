# SCP Backup

Python module built to SCP objects from a container running in AWS ECS or Fargate (vpcmode)

## Usage
```yaml
Command: docker run -v ~/.aws/credentials:/root/.aws/credentials scpbackup:latest backupbypassword 192.168.1.1 backup P@ssw0rd filename.extension bucket.name
```

## To Do
* Recursive folder SCP Copy
* Better Profile/STS call sets
* Add MFA capabilities
* Tests....
