### coping files to fro local to remote destination file 
scp localfile.txt user@remotehost:/path/to/remote/directory   or destination file name

#!/usr/bin/env bash

if [ "$#" -lt 3 ]; then
	echo "usage: usage_scp.sh PATH_TO_LOCAL_FILE IP REMOTE_USER PATH_TO_SSH_KEY"
elif ["$#" -lt 4 ]; then
	scp -o StrictHostKeyChecking=no $1 $3@$2:~/
else	
	scp -i "$4" -o  StrictHostKeyChecking=no $1 $3@$2:~/
fi

### coping files from remote to local destination file
scp user@remotehost:/path/to/remote/file.txt /local/directory

### coping files from remote to remote destination file
scp user@remotehost1:/path/to/remote/file.txt user@remotehost2:/path/to/remote/file.txt

### coping files recursively
scp -r user@remotehost:/path/to/remote/directory /local/direct
