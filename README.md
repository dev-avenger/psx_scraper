PSX Scrapper
------------
This is scrapper which will scrap dps.psx.com.pk website for provided stocks using scrapy python
Following will details ho to setup the project start using the scrapper

`pip install -r requirements.txt`

Create a database with following credentials

`host='localhost'
user='wsl_root'
password='Password123@'
database='psx_database'`


To execute this scrapper use the following command

`scrapy crawl psx_spider`

If you want output in data.csv file then use the following command

`scrapy crawl psx_spider -o data.csv`

