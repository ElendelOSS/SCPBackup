import paramiko
from scp import SCPClient

def createClient(server, port, username, password, gss_auth, timeout=10, logging=None):
    print(server)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(server, port=port, username=username, password=password, timeout=timeout, gss_auth=gss_auth)
        if logging:
            print("Connected to {} on port {}".format(server, port))
        # SCPCLient takes a paramiko transport as an argument
        scp = SCPClient(ssh.get_transport())

        return scp
    
    except paramiko.ssh_exception.NoValidConnectionsError as NoValidConnerr:
        print("Error connecting to {} on port {}".format(server, port))
        print(NoValidConnerr)
        exit(1)

    except Exception as err:
        print("Error connecting to {} on port {}".format(server, port))
        raise(err)


def grabConfig(server, username, password, filesource, port=22, timeout=10, gss_auth=False, logging=None):

    scp = createClient(server=server, port=port, username=username, password=password, timeout=timeout, gss_auth=gss_auth, logging=logging)
    if logging:
        print("Client created")
    try:
        scp.get(filesource, local_path="/tmp/" + filesource)
        scp.close()
        if logging:
            print("Client closed")
        return True

    except Exception as err:
        print(err)
        scp.close()
        if logging:
            print("Client closed")
        return False
