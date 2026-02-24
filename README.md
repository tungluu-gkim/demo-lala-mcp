# demo-lala-mcp

A simple Python utility to test and verify PostgreSQL database connectivity. Useful for quickly checking if your database server is accessible before deploying an application.

## Requirements

- Python 3.6+
- PostgreSQL server
- `psycopg2` library

## Installation

1. Clone this repository:

```bash
git clone https://github.com/tungluu-gkim/demo-lala-mcp.git
cd demo-lala-mcp
```

2. Install the required dependency:

```bash
pip install psycopg2
```

## Usage

1. Open `test.py` and update the database credentials:

```python
DB_HOST = 'localhost'      # Your PostgreSQL host
DB_NAME = 'dnaiconsole'   # Your database name
DB_USER = 'user'           # Your database user
DB_PASSWORD = 'password'   # Your database password
DB_PORT = 5432             # Your PostgreSQL port
```

2. Run the script:

```bash
python test.py
```

3. If successful, you will see:

```
Connecting to the PostgreSQL database at localhost:5432...
Connection successful!
PostgreSQL database version: ('PostgreSQL 14.1 ...',)
Database connection closed.
```
