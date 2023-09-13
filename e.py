from telethon import TelegramClient, sync, errors
from telethon.sessions import StringSession
from telethon.tl.functions.account import CheckUsernameRequest, UpdateUsernameRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import SendMessageRequest
from datetime import datetime
import random, time, requests, telebot , os
R = '\033[1;31m'
y = '\033[1;33m'
G= "\033[1;92m"
chat_id = input('- Enter Id : ')
token = input('- Enter Token : ')
try:
	bot = telebot.TeleBot(token)
except:
	exit('- Trun On Vpn / Error Token Bot')
def check(client, username):
    global bot
    global chat_id
    requ = requests.get("https://fragment.com/username/" + username)
    if '<span class="tm-section-header-status tm-status-avail">Available</span>' in requ.text:
        print(y+"Username For Sale : " + username)
        return "sale"
    time.sleep(2)
    try:
        result = client(CheckUsernameRequest(username=username))
        if result:
            print(G+"Username Available : " + username)
            bot.send_message(chat_id=chat_id,text=username)
        else:
            print(R+"Username Not Available : " + username)
    except errors.FloodWaitError as timb:
        print(f'You Have Been Blocked Wait {timb.seconds}')
        time.sleep(timb.seconds)
    except errors.UsernameInvalidError:
        print(R+"Username Invalid : " + username)
    except errors.rpcbaseerrors.BadRequestError:
        print(R+"Username Banned : " + username)

def username(client):
    AB = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    num = '1234567890'
    while True:
        mm = str("".join(random.choice(AB) for i in range(1)))
        nn = str("".join(random.choice(AB) for i in range(1)))
        ww = str("".join(random.choice(num) for i in range(1)))
        hh = str("".join(random.choice(AB) for i in range(1)))
        c = (mm + "_" + mm + "_" +nn )
        c1 = (mm +nn+ ww + ww + ww)
        c2 = (mm + "_" + ww + "_" + ww)
        c3 = (mm + "_" + nn + "_" + mm)
        c4 = (mm + "_" + mm + "_" + mm)
        c5 = (hh  + "_" + mm + "_" + mm)
        c6 = (mm +ww + mm +ww + mm)
        c7 = (mm  +mm + mm +ww + ww)
        c8 = (mm +ww + mm +mm + mm )
        user = (c,c1,c2,c3,c4,c5,c6,c7,c8)
        username = str("".join(random.choice(user)))
        check(client, username)
api_id = input('- Enter Api_Id : ')
api_hash = input('- Enter Api_Hash : ')
def session1():
    client = TelegramClient(StringSession(), api_id, api_hash)
    client.start()
    session = client.session.save()
    client.disconnect()
    return session
def main():
    session = session1()
    client = TelegramClient(StringSession(session), api_id, api_hash)
    try:
    	client.start()
    except:
    	exit('- Error Api_Id , Api_Hash')
    client(JoinChannelRequest('@proxy_telegram13'))
    os.system('clear')
    username(client)
    client.disconnect()
main()
