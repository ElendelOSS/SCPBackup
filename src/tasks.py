from invoke import task
import backup

@task
def backupbypassword(ctx, server, username, password, filesource, bucket, port=22, timeout=10, logging=None):
    backup.BackupByPassword(
        server=server, 
        username=username,
        password=password,
        filesource=filesource,
        bucket=bucket,
        port=port,
        timeout=timeout,
        logging=logging
    )