import re
import sys
import pymysql
string = "买大蒜10"

#
# sql = """insert into Products (Pname, Pquality) values ("222",333)"""
#

itemName ="好吃的"

itemName = "\""+itemName+"\""
# itemName = itemName.decode("gbk").encode("utf-8")
itemQua = "25"
sql = """insert into Products (Pname, Pquality) values ("""+ "\""+itemName+"\"" + ", "+itemQua+")"
conn = pymysql.connect(host='192.168.31.168', port=3307, user='test', password='123456', db='test', charset="utf8")
cursor = conn.cursor()

try:
    cursor.execute(sql)
    conn.commit()
except:
    conn.rollback()

conn.close()





print(sql)
print("done")
