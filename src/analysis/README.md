1. Download conda https://conda.io/miniconda.html
2. Finish installation
3. Find and run anaconda prompt
4. Install jupyter notebook by typing: `pip install jupyter`
5. Install sqlalchemy by typing: `pip install sqlalchemy`
6. Install matplotlib by typing: `pip install matplotlib`
7. Install sql_magic by typing: `pip install sql_magic`
8. After finishing your installation, simply type jupyter notebook and it will open your notebook in your default web-browser.
9. Import csv files into a brand new database in postgres. Following this snippet:
```
CREATE TABLE company (
	id	integer PRIMARY KEY,
	name	text
);
CREATE TABLE information (
	id	integer PRIMARY KEY,
	Date	timestamp,
	Open	numeric,
	High	numeric,
	Low	numeric,
	Close	numeric,
	Adj_Close	numeric,
	Volume	numeric,
	company_id	integer,
	FOREIGN KEY(company_id) REFERENCES company(id)
);

\d company

\d information

SET CLIENT_ENCODING TO 'utf8';

\copy company FROM 'C:\Users\sasa9\Desktop\stock analysis\csv\company.csv' DELIMITER ',' CSV HEADER;

\copy information FROM 'C:\Users\sasa9\Desktop\stock analysis\csv\information.csv' DELIMITER ',' CSV HEADER;
```