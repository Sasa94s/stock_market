# Prerequisites:
1) Download conda https://conda.io/miniconda.html
2) Finish installation
3) Find and run anaconda prompt
4) Install jupyter notebook by typing: `pip install jupyter`
5) Install sqlalchemy by typing: `pip install sqlalchemy`
6) Install matplotlib by typing: `pip install matplotlib`
7) Install sql_magic by typing: `pip install sql_magic`
8) After finishing your installation, simply type jupyter notebook and it will open your notebook in your default web-browser.

# Database Setup:
- Open SQL Shell (psql)
- Connect to the database, consider it is named as `stock`:
    ```
    \c stock
    ```
- Drop `company`, `information` table if they exist:
    ```
    DROP TABLE IF EXISTS company;
    DROP TABLE IF EXISTS information;
    ```
- Setting up database, create tables running these two statements:
    ```
    CREATE TABLE company (
        id	        INTEGER PRIMARY KEY,
        name        TEXT
    );
    
    CREATE TABLE information (
        Date      timestamp,
        Open      NUMERIC,
        High      NUMERIC,
        Low       NUMERIC,
        Close     NUMERIC,
        Volume        NUMERIC,
        Ex_Dividend       NUMERIC,
        Split_Ratio       NUMERIC,
        Adj_Open      NUMERIC,
        Adj_High      NUMERIC,
        Adj_Low       NUMERIC,
        Adj_Close     NUMERIC,
        Adj_Volume        NUMERIC,
        company_id        INTEGER,
        FOREIGN KEY(company_id) REFERENCES company(id)
    );
    ```
- Import csv files into a brand new database in postgres. Following this snippet:
    ``````
    \d company
    
    \d information
    
    SET CLIENT_ENCODING TO 'utf8';
    
    \copy company FROM 'D:\stock_market\stock_market\src\analysis\data\company.csv' DELIMITER ',' CSV HEADER;
    
    \copy information FROM 'D:\stock_market\stock_market\src\analysis\data\information.csv' DELIMITER ',' CSV HEADER;
    ```