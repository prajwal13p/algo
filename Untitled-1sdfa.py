from telegram import *
from requests import *
from telegram.ext import *
import logging
import logging
import ks_api_client
from ks_api_client import ks_api
import pandas as pd
from datetime import datetime, date
import time
import calendar
import requests
import pandas as pd
import warnings
import asyncio


print("imports done")
# application = ApplicationBuilder().token("6294288055:AAEVaqcyg6VDn1TLRhCZLv0cqV5f14IB1Ug").build()
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
application = ApplicationBuilder().token("6294288055:AAEVaqcyg6VDn1TLRhCZLv0cqV5f14IB1Ug").build()

allowed_chat_ids = [621738033 ,794306298,685319417,5183798047]
not_allowed_chat_msg = "sorry you are NOT AUTHORIZED"


async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id not in allowed_chat_ids :
        print("unknown user")
        await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=not_allowed_chat_msg)
    else:
        buttons = [[InlineKeyboardButton("Login")]]
        await context.bot.send_message(chat_id=update.effective_chat.id, text= "welcome this is Delta Your Algo", reply_markup= ReplyKeyboardMarkup(buttons))


username = "PRAJWAL"
userId="PR6100"
password="130919@Pp"

accessToken="312ccc98-13e6-3503-b4d2-ff171bae93f9"
consumerKey="NcSfB8goLxL5zMLjAbe3qE_rX7Ya"
consumerSecret="kh3LwG9zNeCK0ogvbywrRQLfocka"

client = ks_api.KSTradeApi(access_token = accessToken, userid = userId, consumer_key = consumerKey,ip = "192.168.1.9", app_id = "DefaultApplication", \
host = "https://ctradeapi.kotaksecurities.com/apim", consumer_secret = consumerSecret)  







async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id not in allowed_chat_ids :
        print("unknown user")
        await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=not_allowed_chat_msg)
    else:
        users = ["kiran","prajwal","assemble"]
        buttons1 = [[KeyboardButton(users[0])],
                  [KeyboardButton(users[1])],
                  [KeyboardButton(users[2])]]
        buttons2 = [[KeyboardButton("Hedge Positon placing")]]
        chatm = update.message.text
        if chatm == "Login":
            await context.bot.send_message(chat_id=update.effective_chat.id, text="please provide the user",reply_markup= ReplyKeyboardMarkup(buttons1))
        if chatm in users:
            await   context.bot.send_message(chat_id=update.effective_chat.id, text="please provide accesscode")
        if len(chatm) == 4 :
            # await context.bot.send_message(chat_id=update.effective_chat.id , )
            accesscode = chatm
            Login = client.login(password = password)

            AC = client.session_2fa(access_code = accesscode)
            login_status = f"""https://api.telegram.org/bot6155099627:AAEz8kjIMd1NX1Bk48UcKhz_Ol5btSuf9AA/sendMessage?chat_id=-950365513&text={username} Succesfully logged In to Algo Trade Execution
  """
            requests.get(login_status)    
            await context.bot.send_message(chat_id=update.effective_chat.id, text=Login,reply_markup=ReplyKeyboardMarkup(buttons2))
        if chatm == "Hedge Positon placing":
            await context.bot.send_message(chat_id= update.effective_chat.id,text= "please enter the timings")

        if len(chatm) == 8  :    
            otm_3_time = chatm
            # global stop
            # stop =  False

            try :
                while True :
                    # break
                    print(datetime.now())
                    if datetime.now().strftime("%H") == otm_3_time[0:2] and datetime.now().strftime("%M") == otm_3_time[3:5] and int(datetime.now().strftime("%S")) == int(otm_3_time[6:8]):
                        CE_3OTM = client.place_order(order_type = "N", instrument_token = 16372, transaction_type = "BUY",\
                        quantity = 25*(1), price = 0, disclosed_quantity = 0, trigger_price = 0,\
                        tag = "string", validity = "GFD", variety = "REGULAR")
                        PE_3OTM = client.place_order(order_type = "N", instrument_token = 18733, transaction_type = "BUY",\
                        quantity = 25*(1), price = 0, disclosed_quantity = 0, trigger_price = 0,\
                        tag = "string", validity = "GFD", variety = "REGULAR")
                        await context.bot.send_message(chat_id=update.effective_chat.id, text="Hedge Position Placed successfully")
                        print("""
                        
            --------------------------Trades Are Executed-----------------------------------
                        
                        """)
                        break
            except Exception as e:
                await context.bot.send_message(chat_id=update.effective_chat.id, text=f"""Failed to Place Hedge Position 
Error : {e}""")

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id not in allowed_chat_ids :
        print("unknown user")
        await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=not_allowed_chat_msg)
    else:
        text_caps = context.args
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"""CE Strike {text_caps[0]} 
PE Strike {text_caps[1]}""")
    
# async def while_False(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     global stop
#     stop = False
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=f"while Loop stopped")

# async def while_True(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     global stop
#     stop = True
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=f"while Loop True")


# import asyncio
# from telegram import Bot

# async def send_message(bot, chat_id, message):
#     await bot.send_message(chat_id=chat_id, text=message)

# async def send_multiple_messages():

#     tasks = [start(update: Update, context: ContextTypes.DEFAULT_TYPE),
#              echo(update: Update, context: ContextTypes.DEFAULT_TYPE),
#              while_False(update: Update, context: ContextTypes.DEFAULT_TYPE),
#              while_True(update: Update, context: ContextTypes.DEFAULT_TYPE)]
    

#     await asyncio.gather(*tasks)




if __name__ == '__main__':

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    caps_handler = CommandHandler('strike', caps)
    # while_false_handler = CommandHandler('global_false', while_False)
    # while_true_handler = CommandHandler('global_true', while_True)
    
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(caps_handler)
    # application.add_handler(while_false_handler)
    # application.add_handler(while_true_handler)

    # asyncio.run(send_multiple_messages())
    application.run_polling()
    