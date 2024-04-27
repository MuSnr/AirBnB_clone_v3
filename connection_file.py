from sqlalchemy import create_engine

# SQL commands to prepare MySQL server
sql_commands = """
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
"""

# MySQL connection string
connection_string = 'mysql+mysqlconnector://hbnb_dev:hbnb_dev_pwd@localhost/hbnb_dev_db'

# Create an engine
engine = create_engine(connection_string, echo=True)

# Execute the SQL commands
with engine.connect() as connection:
    for command in sql_commands.split(';'):
        connection.execute(command)
