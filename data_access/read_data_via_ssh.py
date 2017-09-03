'''
This code snippet shows how to read data vis SSH.
This is useful if your data is located on a remote server.

@author: panc
@time: 2017-06-05
'''

# Method 1: use subprocess
username = 'your_user_name'
hostname = 'your_hostname'
data_fpath = '/path/to/the/data/file/on/the/server'

import subprocess
ssh_f = subprocess.Popen( ['ssh', username+'@'+hostname, 'cat', data_fpath],
                          stdout=subprocess.PIPE )

data_lst = []
for line in ssh_f.stdout:
    print(line)
    data_lst.append(line)


# Method 2: use paramiko
import paramiko
import getpass

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

p = getpass.getpass()

ssh.connect(hostname, username=username, password=p)

stdin, stdout, stderr = ssh.exec_command('cat '+data_fpath)
print(stdout.readlines())
ssh.close()