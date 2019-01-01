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
    if "查单" in msg.text:
        num = re.sub("查单", "", msg.text)
        if num == "":
            for row in sqlQuery('select * from orderStatus limit 10'):
                itchat.send_msg('利达单号'+ row[1] + ' ,国内快递号'+row[2], msg['FromUserName'])
        else:
            for row in sqlQuery('select * from orderStatus limit'+num):
                itchat.send_msg('利达单号'+ row[1] + ' ,国内快递号'+row[2], msg['FromUserName'])
    if '买' in msg.text:

    if msg.text == '功能':
        itchat.send_msg('回复查单+数字显示最近单号，默认显示10，例:查单 15显示最近15个订单', msg['FromUserName'])
        itchat.send_msg('回复查买+数字显示最近下单买的东西，默认显示是，例：查买 15显示最近15个需要购买的状态', msg['FromUserName'])
        itchat.send_msg('回复买+物品+数量,下单购买物品，例：买 小熊糖 10', msg['FromUserName'])
    else:
        itchat.send_msg('没有找到指定命令，请发送 功能 查看具体命令', msg['FromUserName'])





if __name__ == "__main__":
    itchat.auto_login()
    itchat.run()
