# DBMS-2023

## Preparation

- Construct test database: `source FULLPATH/DBMS-2023/sql_src/testdb.sql;`
- Start flask server: `python DBMS-2023/flaskr/app.py`
- Open user homepage: http://127.0.0.1:5000/user?card_id=789
- Make sure the `DBMS-2023/.env` contains the correct environment. Please find `DBMS-2023/flaskr/.env.template` for more details.

## Structure

### Identity

+ Youbike employees
+ Youbike users
+ Youbike manager

### Usage

1. For youbike employees
    - Check profile
    - Check controlled locations and bikes
    - Check history of users' rentings
2. For youbike users
   - Rent bikes from any location where possible
   - Return bike to any location
   - Check his own profile
   - Check his own renting history
   - Check remaining bikes at any location
3. For youbike manager
   - List all subordinate
   - Check specific subordinate's responsibility
