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


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    if msg.text == 'check':
        for row in sqlQuery('select * from orderStatus'):
            itchat.send_msg('利达单号'+ row[1] + ' ,国内快递号'+row[2], msg['FromUserName'])


if __name__ == "__main__":
    itchat.auto_login()
    itchat.run()



