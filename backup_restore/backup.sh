#!/bin/bash
#----------------------------------------
# OPTIONS
#----------------------------------------
CONTAINER_NAME='deployement_database_1'  # Name of your PostgreSQL container
DATABASE='postgres'                      # PostgreSQL Database Name
REMOTE_SERVER='51.77.221.126'            # Remote Server Address
REMOTE_USER='ubuntu'                     # Remote Server SSH User
BACKUP_PATH='/home/ubuntu/deployement/backups_data/db'
DAYS_TO_KEEP=30                          # 30 days to keep backups
#----------------------------------------

# Create the backup folder if it doesn't exist
mkdir -p $BACKUP_PATH

# Backup PostgreSQL database from container
echo "Backing up database: $DATABASE"
docker exec -t $CONTAINER_NAME pg_dump -U postgres -d $DATABASE > $BACKUP_PATH/$(date +%d-%m-%Y)-$DATABASE.sql

# Transfer backup to remote server
echo "Transferring backup to remote server"
scp $BACKUP_PATH/$(date +%F)-$DATABASE.sql $REMOTE_USER@$REMOTE_SERVER:/home/ubuntu/backup/

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
