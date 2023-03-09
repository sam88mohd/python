import sys
import paramiko
import time

ip_address = "192.168.0.31"
username = "sm"
password = "123"
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.load_system_host_keys()
ssh_client.connect(hostname=ip_address, username=username, password=password)
print("Successful conncetion", ip_address)
ssh_client.invoke_shell()
remote_connection = ssh_client.exec_command('cd Desktop; mkdir work\n')
remote_connection = ssh_client.exec_command('mkdir test_folder\n')
# print (remote_connection.read())
ssh_client.close
