
To install, first clone, then
```virtualenv -p python3 . ```
This requires at least python3.6.1

Then, do
```. bin/activate ```
```pip install -r requirements.txt```

To create the database:
```sqlite3 albums.db```
To create tables:
```python3 models.py```

To scrape first ten pages of high-scoring albums pages:
```python3 scraper.py```

To scrape some other page
```python3 $URL```

To scrape deeper/less deep on high-scoring albums
```python3 100```

If you want to crawl deeper from a single starting point, change the global
variable RECURSION_DEPTH at the start of scraper.py
