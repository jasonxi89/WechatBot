import itchat
import pymysql

#check database


def sqlQuery(query):
    conn = pymysql.connect(host='192.168.31.168', port=3307, user='test', password='123456', db='test',
                           use_unicode=True)
    cursor = conn.cursor()
    cursor.execute(query)
    values = cursor.fetchall()
    conn.close()
    return values


for row in sqlQuery('select * from orderStatus'):
    print('利达单号'+ row[1] + ' ,国内快递号'+row[2])




# if __name__ == "__main__":
#     itchat.auto_login(enableCmdQR=2)
#     itchat.run()
#


