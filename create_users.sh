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

# Check if the database exists
if ! mysql -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SHOW DATABASES LIKE '$DATABASE_NAME'" | grep "$DATABASE_NAME" > /dev/null; then
  echo "Database '$DATABASE_NAME' does not exist. Please create the database first."
  exit 1
fi

# Create the users table
mysql -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "USE $DATABASE_NAME; CREATE TABLE users (userid INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255) NOT NULL UNIQUE, first_name VARCHAR(255), last_name VARCHAR(255), user_email VARCHAR(255) NOT NULL UNIQUE);"

# Populate users table with 5 entries
mysql -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "USE $DATABASE_NAME; INSERT INTO users (username, first_name, last_name, user_email) VALUES ('user1', 'First1', 'Last1', 'user1@example.com'), ('user2', 'First2', 'Last2', 'user2@example.com'), ('user3', 'First3', 'Last3', 'user3@example.com'), ('user4', 'First4', 'Last4', 'user4@example.com'), ('user5', 'First5', 'Last5', 'user5@example.com');"

# Check if all operations were successful
if [ $? -eq 0 ]; then
  echo "Users table created and populated successfully."
else
  echo "Failed to create or populate users table."
  exit 1
fi

exit 0