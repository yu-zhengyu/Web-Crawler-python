import saveData
import MySQLdb as mdb
import sys

con = mdb.connect('localhost', 'root', 'root', 'test');
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS \
        WebData(Id INT PRIMARY KEY AUTO_INCREMENT, Title VARCHAR(25), Link text, Abstract text, Time datetime)")
    
con.close()
saveData.saveData('no til', 'no link', 'no abs', '19910402');