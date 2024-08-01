##############################################################################
# UBUNTU
##############################################################################

scp /path/to/file user@server:/path/to/destination # Copy file from local to server

scp /home/zhao/data/test.txt zw@10.150.69.247: /C:/Users/zw/Desktop/summary
或
scp /home/zhao/data/test.txt zw@10.150.69.247: /C:/Users/zw/Desktop/summary/tt.txt


df -h # Check the amount of free space

sudo ufw status # Check status
sudo ufw allow from remote_IP_address to any port 3306 # Allow external ip to access port

scp user@remote_host:remote_file local_file # download: remote -> local
scp local_file user@remote_host:remote_file # upload: local -> remote

service elasticsearch restart # Restart elasticsearch service

sudo -s # Log as root

cat /proc/<process_id>/maps   # Show the current virtual memory usage of a Linux process

ip r # Display ip of the server

lsof -i :9000 # List process running on port 9000

journalctl -u minio.service -n 100 --no-pager # List last 100 logs for specific service

sudo resize2fs /dev/disk/by-id/scsi-0DO_example # Resize volume

ps -ax | grep myprocessname # Search processes
kill -9 PROCESS_ID # Kill process PID

1. 给我获取某台电脑的文件 

curl