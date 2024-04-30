#! /bin/bash
#----------------------------------------
# OPTIONS
#----------------------------------------
CONTAINER_NAME='digitalocean-database-1'  # Name of your PostgreSQL container
DATABASE='postgres'                      # PostgreSQL Database Name (Make sure it's set correctly)
REMOTE_SERVER='51.255.49.204'            # Remote Server Address (Make sure it's set correctly)
REMOTE_USER='testt'                     # Remote Server SSH User
BACKUP_PATH='/home/nourzraibia/backups_data/db'  # Corrected the directory name
DAYS_TO_KEEP=30                          # 30 days to keep backups
#----------------------------------------
# Create the backup folder if it doesn't exist
mkdir -p $BACKUP_PATH

# Backup PostgreSQL database from container
echo "Backing up database: $DATABASE"
docker exec -t $CONTAINER_NAME pg_dump -U postgres -d $DATABASE > $BACKUP_PATH/$(date +%d-%m-%Y)-$DATABASE.dump
#copy public key to remote server
ssh-copy-id -i ~/.ssh/id_rsa.pub $REMOTE_USER@$REMOTE_SERVER
# Transfer backup to remote server
echo "Transferring backup to remote server"
scp $BACKUP_PATH/$(date +%d-%m-%Y)-$DATABASE.dump $REMOTE_USER@$REMOTE_SERVER:/home/testt/backup/
# Check if scp command was successful
if [ $? -eq 0 ]; then
  echo "Backup transferred successfully"
else
  echo "Error: Backup transfer failed"
  exit 1
fi
# Delete old backups
echo "Deleting backups older than $DAYS_TO_KEEP days"
find $BACKUP_PATH/* -mtime +$DAYS_TO_KEEP -exec rm {} \;
