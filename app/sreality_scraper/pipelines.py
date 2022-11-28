# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import psycopg2
import os

class SrealityScraperPipeline:
    def __init__(self):
        db_url = os.getenv("DATABASE_URL")
        
        self.connection = psycopg2.connect(db_url)
        
        # Create cursor, used to execute commands
        self.cur = self.connection.cursor()
        
        # Create estates table if none exists
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS estates(
            id serial PRIMARY KEY, 
            title text,
            url text
        )
        """)

    def process_item(self, item, spider):
        self.cur.execute(""" insert into estates (title, url) values (%s,%s)""", (
            item["title"],
            item["url"]
        ))

        # Execute insert of data into database
        self.connection.commit()
        return item

    def close_spider(self, spider):

        # Close cursor & connection to database 
        self.cur.close()
        self.connection.close()