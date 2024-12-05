import paramiko

hostname=""
port=33
username="yatanim"
password=""

client = paramiko.SSHClient() # Create an SSH client object

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Automatically add the server's host key if it's missing (security feature)

try:
    client.connect(hostname,port=port,username=username, password=password)
    stdin,stdout,stderr = client.exec_command('ls-l')
    output = stdout.read().decode(
    print("command output":)
    print(output)

    errors = stderr.read().decode()

    if errors:
        print("errror:")
        print(errors)

    )
finally:
    client.close()