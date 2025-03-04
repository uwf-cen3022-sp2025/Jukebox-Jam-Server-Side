#!/bin/bash

# Database name
DATABASE_NAME="JukeboxJam_db"

# MySQL username and password from environment variables
MYSQL_USER="${MYSQL_USER}"
MYSQL_PASSWORD="${MYSQL_PASSWORD}"

# Check if MySQL is installed
if ! command -v mysql &> /dev/null; then
  echo "MySQL is not installed. Please install MySQL and try again."
  exit 1
fi

# Check if the database already exists
if mysql -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SHOW DATABASES LIKE '$DATABASE_NAME'" | grep "$DATABASE_NAME" > /dev/null; then
  echo "Database '$DATABASE_NAME' already exists."
  exit 0 # Exit gracefully if the database exists.
fi

# Create the database
mysql -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "CREATE DATABASE $DATABASE_NAME;"

# Check if the database was created successfully
if [ $? -eq 0 ]; then
  echo "Database '$DATABASE_NAME' created successfully."
else
  echo "Failed to create database '$DATABASE_NAME'."
  exit 1
fi

exit 0