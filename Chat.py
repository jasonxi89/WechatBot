import itchat
import pymysql
import re


def sqlQuery(query):
    conn = pymysql.connect(host='192.168.31.168', port=3307, user='test', password='123456', db='test',
                           use_unicode=True)
    cursor = conn.cursor()
    cursor.execute(query)
    values = cursor.fetchall()
    conn.close()
    return values
# reply msg depends on what i got


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    if '查' in msg.text:
        num = re.sub('查', "", msg.text)
        if num == "":
            for row in sqlQuery('select * from orderStatus limit 10'):
                itchat.send_msg('利达单号'+ row[1] + ' ,国内快递号'+row[2], msg['FromUserName'])
        else:
            for row in sqlQuery('select * from orderStatus limit'+num):
                itchat.send_msg('利达单号'+ row[1] + ' ,国内快递号'+row[2], msg['FromUserName'])
    if msg.text == '功能':
        itchat.send_msg('回复查+数字显示最近单号，默认显示10，例如:查15现在最近15个订单', msg['FromUserName'])


if __name__ == "__main__":
    itchat.auto_login()
    itchat.run()



