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
        for ac in open("u.txt").read().split("\n"):
            username = str(ac)
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
