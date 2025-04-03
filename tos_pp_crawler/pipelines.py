import sqlite3

class SQLitePipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect('tos_pp.db')
        self.cur = self.conn.cursor()
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS policies(
                url TEXT PRIMARY KEY,
                text TEXT,
                word_count INTEGER,
                char_count INTEGER,
                polarity REAL,
                subjectivity REAL
            )
        ''')
        self.conn.commit()

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        self.cur.execute('''
            INSERT OR REPLACE INTO policies (url, text, word_count, char_count)
            VALUES (?, ?, ?, ?)
        ''', (item['url'], item['text'], item['word_count'], item['char_count']))
        self.conn.commit()
        return item