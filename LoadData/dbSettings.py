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
