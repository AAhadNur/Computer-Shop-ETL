"""
Configuration and Connection String for PostgreSQL Database

This Python script configures database connection settings for a PostgreSQL database using the 'python-decouple' library.
It reads environment variables from a '.env' file to obtain database credentials, such as username, password, host, and
database name. It then constructs a connection string to connect to the PostgreSQL database.

Attributes:
- username (str): Database username.
- password (str): Database password.
- host (str): Database host or address.
- database_name (str): Name of the database.
- connection_string (str): PostgreSQL connection string.

Usage:
1. Create a '.env' file with the required database credentials.
2. Run this script to read the credentials and construct the connection string.
3. Use the 'connection_string' to connect to the PostgreSQL database.

Author: [Abdul Ahad]
"""

import os
from decouple import AutoConfig

# .env file path
ENV_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_FILE = os.path.join(ENV_BASE_DIR, '..', '.env')

config = AutoConfig(search_path=ENV_FILE)


username = config('username')
password = config('password')
host = config('host')
database_name = config('database_name')

connection_string = "postgresql://" + username + \
    ':' + password + '@' + host + '/' + database_name
