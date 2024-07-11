#!/bin/bash


POSTGRES_HOST="10.128.0.2"
POSTGRES_DB="testdb"
POSTGRES_USER="postgres"
POSTGRES_PASSWORD="postgres"

BACKUP_DIR="/home/emre/backup"
#yoksa boyle bir dizin olusturun


backup_filename="${POSTGRES_DB}_$(date +%Y%m%d_%H%M%S).sql"


mkdir -p $BACKUP_DIR

PGPASSWORD=$POSTGRES_PASSWORD pg_dump -h $POSTGRES_HOST -U $POSTGRES_USER -d $POSTGRES_DB > $BACKUP_DIR/$backup_filename

# check dongusuu
if [ $? -eq 0 ]; then
    echo "Backup completed successfully: $backup_filename"
else
    echo "Backup failed"
fi
