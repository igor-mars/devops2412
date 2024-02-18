import paramiko
import sys

# Define the range of server IPs
start_ip = 108
end_ip = 108

# Root password to set
new_password = 'We2Ar-Mars!24#'

# SSH credentials for servers
ssh_username = 'root'
ssh_key_filename = '/path/to/your/ssh/key'  # Optional if using key-based authentication

# Loop through the server range
for server_number in range(start_ip, end_ip + 1):
    server_ip = f'rtb{server_number}-hq1.rtbsrv.com'  # Replace with the actual server IP or hostname

    try:
        ssh_password = getpass.getpass(f'Enter SSH password for {server_ip}: ')
        # Create an SSH client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the server
        ssh_client.connect(server_ip, username=ssh_username, password=ssh_password)

        # Change the root password
        stdin, stdout, stderr = ssh_client.exec_command(f'echo "root:{new_password}" | chpasswd')

        # Check if the password change was successful
        if not stderr.read():
            print(f'Successfully changed the root password for {server_ip} to {new_password}')
        else:
            print(f'Failed to change the root password for {server_ip}')

        # Close the SSH connection
        ssh_client.close()

    except Exception as e:
        print(f'Error connecting to {server_ip}: {str(e)}')

print('Password change process completed.')
