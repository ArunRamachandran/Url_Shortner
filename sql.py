import sqlite3

con = sqlite3.connect('url.db')
con.execute("DROP TABLE IF EXISTS url")
con.execute("CREATE TABLE url(link TEXT, short TEXT)")
