# python-sample-data-server

## Initial Setup
```
python3 -m pip install virtualenv
python3 -m virtualenv venv
source ./venv/bin/activate

pip -V # show if we are using venv

pip install flask
```

## Create SQLite table
```
>>> import sqlite3
>>> conn = sqlite3.connect("people.db")
>>> columns = [
...     "id INTEGER PRIMARY KEY",
...     "last_name VARCHAR UNIQUE",
...     "first_name VARCHAR",
...     "timestampe DATETIME"
... ]
>>> create_table_cmd = f"CREATE TABLE person ({','.join(columns)})"
>>> conn.execute(create_table_cmd)
```