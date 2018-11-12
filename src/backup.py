import sys
import os
import scpconfig
import s3write

def BackupByPassword(server, username, password, filesource, bucket, port=22, timeout=10, logging=None):
    if scpconfig.grabConfig(server=server,port=port,username=username,password=password,timeout=timeout,filesource=filesource, logging=logging):
        s3write.backuptoS3(
            server=server,
            bucket=bucket,
            filesource=filesource
        )
    if logging:
        print("File Write to S3 successful")


