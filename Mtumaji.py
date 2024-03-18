#V 20.7
import re
import Hss
import logging
import asyncio
import random
import datetime
import requests
from telegram.constants import ParseMode
from telegram import Update, Chat as TGChat, Message
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)


bot_token = "6136666252:AAGvIFrEJu9D1y93fa09y1joFdk8QHXE24Q"

# Kuanzisha logger
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)




#Start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user.to_dict()
    muda = datetime.datetime.now().strftime("%I: %M: %S")
    first_name = user['first_name']
    txt = f"Karibu, <u>{first_name}</u> Jiunge na \n1. @Mawaidha1\n2. @Jitibu\n3. @Huduma\nKwasasa ni Saa {muda}"
    await context.bot.send_message(chat_id=user['id'], text=txt, parse_mode='HTML')



#Mawaidha
Mawaidha_ID = [-1001243018219, -1001703214814, -1001940292479, -1001160231264, -1002074709474, -1002123252747, -1001822851357] #Grp ID

async def mawaidha(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        await Hss.mawaidha(update, context)
    except Exception as e:
        error_message = f"Kwenye Handle ya Mawaidha Hitilafu imejitokeza: {str(e)}"
        await context.bot.send_message(chat_id= -1001334156926, text=error_message)





#Khadija Audio na Document
async def khadija(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        await Hss.khadija(update, context)

    except Exception as e:
        error_message = f"Kwenye Handle ya Mawaidha Hitilafu imejitokeza: {str(e)}"
        await context.bot.send_message(chat_id= -1001334156926, text=error_message)



#Afya
# Chat IDs
Uzima = -1001980705407
async def afyayako(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        await Hss.afyazetu(update, context)

    except Exception as e:
        error_message = f"Kwenye Handle ya Mawaidha Hitilafu imejitokeza: {str(e)}"
        await context.bot.send_message(chat_id=-1001334156926, text=error_message)



#Huduma teknolojia
chat_ids = [-1001978645421, -1001394087336]  # Post
async def teknolonia(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        caption = update.message.caption
        if caption and "Saved by @InstantMediaBot" not in caption and "Saved by @download_it_bot" not in caption:
            await Hss.nakili(update, context)
            return
        else:
            await Hss.technology(update, context)

    except Exception as e:
        error_message = f"Kwenye Handle ya Huduma Hitilafu imejitokeza: {str(e)}"
        await context.bot.send_message(chat_id= -1001334156926, text=error_message)



#HabariTz
Group_ids = [-1001978152770, -1001917191739, -1001989553280, -1001987939772]
#1. over_view 2. News 3. 2chat 4. vido
async def habaritz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        await Hss.habaritz(update, context)

    except Exception as e:
        error_message = f"Kwenye Handle ya habaritz Hitilafu imejitokeza: {str(e)}"
        await context.bot.send_message(chat_id= -1001334156926, text=error_message)




#Kimataifa
Vituos = [-1001534508873, -1001399596484]
async def kimataifa(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
            await Hss.kimataifaa(update, context)

    except Exception as e:
        error_message = f"Kwenye handle ya kimataifa Hitilafu imejitokeza: {str(e)}"
        await context.bot.send_message(chat_id=-1001334156926, text=error_message)




#Usafishaji
async def usafishaji(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    caption = update.message.caption or ""
    try:
        if "Saved by @InstantMediaBot" in caption or "Saved by @download_it_bot" in caption:
        	await Hss.usafi(update, context)
    except Exception as e:
        error_message = f"Kwenye handle ya usafishaji Hitilafu imejitokeza: {str(e)}"
        await context.bot.send_message(chat_id= -1001334156926, text=error_message)


watumiaji = [1041455290, 654648997, 1587594400, 1639229634, -1002117935045, -1001193133668, -1001632824805, -1001742806325, -1001666964121]
async def replace_link(update, context):
    try:
        message = update.message
        chat_id = message.chat_id
        text = message.text

        if re.search(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text):
            if "twitter.com" in text:
                await Hss.replacelink(update, context)
            if "instagram" in text:
                await Hss.replaceinstalink(update, context)
            if "tiktok.com" in text:
                await Hss.replacetktlink(update, context)

    except Exception as e:
        error_message = f"An error occurred in the replace_link handler: {str(e)}"
        await context.bot.send_message(chat_id= -1001334156926, text=error_message)



#Hitilafu
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    error_message = f'Update "{update}" caused error "{context.error}"'
    await context.bot.send_message(chat_id= -1001334156926, text=error_message)





def main() -> None:

        application = Application.builder().token(bot_token).build()

        #Start
        application.add_handler(CommandHandler("start", start))

        # MDA
        application.add_handler(MessageHandler(filters.Chat(Mawaidha_ID) & (filters.VIDEO), mawaidha))



        #Khadija
        application.add_handler(MessageHandler(filters.Chat(Mawaidha_ID) & (filters.Document.ALL | filters.AUDIO), khadija))


        # AFA
        application.add_handler(MessageHandler(filters.Chat(Uzima) & (filters.VIDEO | filters.PHOTO), afyayako))


        # HDM
        application.add_handler(MessageHandler(filters.Chat(chat_ids) & (filters.VIDEO | filters.PHOTO | filters.Document.ALL), teknolonia))


        #HabariTz
        application.add_handler(MessageHandler(filters.Chat(Group_ids) & (filters.VIDEO | filters.PHOTO), habaritz))

        application.add_handler(MessageHandler(filters.Chat(Vituos) & (filters.PHOTO | filters.VIDEO), kimataifa))


#Handle ya kusafisha Caption
        application.add_handler(MessageHandler(filters.ChatType.PRIVATE & (filters.VIDEO | filters.AUDIO | filters.Document.ALL | filters.PHOTO), usafishaji))


        application.add_handler(MessageHandler(filters.Chat(watumiaji) & (filters.Entity("url")), replace_link))

        application.add_error_handler(error_handler)


        # Run the bot until the user presses Ctrl-C
        application.run_polling(allowed_updates=Update.ALL_TYPES, timeout=120)
        asyncio.sleep(30)




if __name__ == '__main__':
    main()








