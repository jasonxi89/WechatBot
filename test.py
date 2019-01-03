import re
import pymysql
string = "买大蒜10"


sql = """insert into Products (Pname, Pquality) values ("222",333)"""

conn = pymysql.connect(host='192.168.31.168', port=3307, user='test', password='123456', db='test',
                           use_unicode=True)
cursor = conn.cursor()

try:
    cursor.execute(sql)
    conn.commit()
except:
    conn.rollback()

conn.close()



print("done")
