#!/bin/bash

# Check if backup file is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <backup_file>"
    exit 1
fi

# Drop existing schema
docker exec -i deployement_database_1 psql -U postgres -d postgres -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"

# Restore the database from specified backup file
docker exec -i deployement_database_1 psql -U postgres -d postgres < "/home/ubuntu/backup/$1"

echo "Database restore completed successfully."


to excute do => ./restore.sh 2024-04-26-postgres.dump
