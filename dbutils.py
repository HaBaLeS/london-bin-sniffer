import sqlite3




class SqliteDataStore:
    """ DAO providing access to a Sqlite3 Database """

    def executeAndCommit(self,sql,args):
        c = self.conn.cursor()
        c.execute(sql,args)
        self.conn.commit()

    def execute(self,sql,args):
        c = self.conn.cursor()
        c.execute(sql,args)

    def commit(self):
        self.conn.commit()
        
    def initDB(self):
        c = self.conn.cursor()

        try:
             c.execute('select * from dataline limit 1')
        except sqlite3.OperationalError, err:
	    	#create schma
		c.execute('create table dataline (ts integer, mac text)')
		c.execute('create table mac2Man (mac text, man text)')
            #knownMacs tabelle

    def __init__(self, databaseURI):
        self.conn = sqlite3.connect(databaseURI)
        self.initDB()
