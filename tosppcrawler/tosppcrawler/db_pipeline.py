import sqlite3

class SQLitePipeline:
    def open_spider(self, spider):
        self.connection = sqlite3.connect("tospp_data.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tos_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                url TEXT,
                text TEXT
            )
        ''')
        self.connection.commit()

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        self.cursor.execute('''
            INSERT INTO tos_data (title, url, text) VALUES (?, ?, ?)
        ''', (item.get('title'), item.get('url'), item.get('text')))
        self.connection.commit()
        return item
