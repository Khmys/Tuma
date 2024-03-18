import re
import asyncio
import datetime
import logging
import random
import requests
from telegram import Update, Chat as TGChat, Message
from telegram.constants import ParseMode



url_pattern = r'https?://\S+|www\.\S+'

#MID
mda_id = [-1001243018219, -1001940292479, 1639229634, -1002074709474]
shwaibu = [-1001703214814, -1002123252747, -1001822851357]
Mawaidha1 = -1001148345121

#Mawaidha
async def mawaidha(update, context):
    message = update.message
    chat_id = message.chat_id
    caption = message.caption or ""
    caption = await safisha(caption)

    if chat_id in mda_id:
        await context.bot.send_video(chat_id=Mawaidha1, video=message.video.file_id, caption=f"<blockquote>❖ @Mawaidha1</blockquote>\n\n{caption[:120]}", parse_mode='HTML')  # Caption fupi
    else:
        if re.search(url_pattern, caption):
            await context.bot.send_video(chat_id=Mawaidha1, video=message.video.file_id, caption=f"<blockquote>❖ @Mawaidha1</blockquote>\n\n{caption[:115]}", parse_mode='HTML')
        else:
            await context.bot.send_video(chat_id=Mawaidha1, video=message.video.file_id, caption=f"<blockquote>❖ @Mawaidha1</blockquote>\n\n{caption}", parse_mode='HTML')


#Khadija Audio na Document
async def khadija(update, context):
    message = update.message
    chat_id = message.chat_id
    mda = "<a href='https://t.me/Mawaidha1'>⏯︎ Mawaidha</a>"

    caption = message.caption or ""
    caption = await safisha(caption)

    if message.document:
        await context.bot.send_document(chat_id=Mawaidha1, document=message.document.file_id, caption=caption, parse_mode=ParseMode.HTML)

    if message.audio:
        await context.bot.send_audio(chat_id=Mawaidha1, audio=message.audio.file_id, caption=f"{mda}\n\n{caption}", parse_mode=ParseMode.HTML)


 #Afya
async def afyazetu(update: Update, context):
    message = update.message
    if message.video:
            caption = message.caption or ""
            caption = await safisha(caption)

            await context.bot.send_video(chat_id= -1001080236618, video=message.video.file_id, caption=f"@Jitibu\n\n{caption}")

    if message.photo:
            await context.bot.copy_message(chat_id= -1001080236618, from_chat_id=message.chat.id, message_id=message.id)



# Tech
Huduma = -1001297333544
url_pattern = r'https?://\S+|www\.\S+'

async def technology(update, context):
    message = update.message
    caption = message.caption or ""
    caption = await safisha(caption)
    huduma = "<a href='https://t.me/Huduma'>〽︎ Teknolojia </a>"

    if message.video:
        if re.search(url_pattern, caption):
            # Remove URLs from the caption
            caption = re.sub(url_pattern, '', caption)
            await context.bot.send_video(chat_id=-1001297333544, video=message.video.file_id, caption=f"{huduma}\n\n{caption[:120]}",
                                   parse_mode='HTML')
        else:
            await context.bot.send_video(chat_id=Huduma, video=message.video.file_id, caption=f"{huduma}\n\n{caption}",
                                   parse_mode='HTML')

    if message.document:
        await context.bot.send_document(chat_id=-1001297333544, document=message.document.file_id, caption=f"{huduma}\n\n{caption}", parse_mode='HTML')



# Handler kwa HabariTz
# Viungo vya HTML
Htz = "<a href='https://t.me/HabariTz'>Swahili News</a>"
Fresh = "<a href='https://t.me/RefreshChat'>Refresh 💬</a>"
html_links = [Htz, Fresh]


# Kazi ya kuchagua kiungo cha HTML kwa njia ya kiharusi
async def generate_random_link() -> str:
    return random.choice(html_links)

News_Chat = [-1001917191739, -1001989553280]
#2 group
vido = [-1001987939772]
url_pattern = r'https?://\S+|www\.\S+'


async def habaritz(update: Update, context):
        message: Message = update.message
        chat_id = message.chat.id

        if message and (message.photo or message.video):
            caption = message.caption or ""
            if not caption:
                await context.bot.copy_message(chat_id= -1001248885302, from_chat_id=message.chat.id, message_id=message.id)
                return

            if caption and "Saved by @InstantMediaBot" not in caption and "Saved by @download_it_bot" not in caption:
                await context.bot.copy_message(chat_id= -1001248885302, from_chat_id=message.chat.id, message_id=message.id)
                return
            else:
                video_file = message.video.file_id
                caption = await safisha(caption)

                # Chagua kiungo cha HTML kwa njia ya kiharusi
                random_link = await generate_random_link()

                if chat_id in News_Chat:
                    if re.search(url_pattern, caption):
                        await context.bot.send_video(chat_id= -1001248885302, video=video_file, caption=f"{random_link}\n{caption[:100]}", parse_mode='HTML')
                    else:
                        await context.bot.send_video(chat_id= -1001248885302, video=video_file, caption=f"{random_link}\n{caption}", parse_mode='HTML')

                elif chat_id in vido:
                    # caption fupi
                    await context.bot.send_video(chat_id= -1001248885302, video=video_file, caption=f"{random_link}\n{caption[:120]}", parse_mode='HTML')





#Kimataifa
# Handler kwa picha za vituo
async def kimataifaa(update: Update, context):
    message = update.message

    if message is not None and hasattr(message, 'chat'):
        chat_id = message.chat.id

        if message.photo or message.video:
            caption = message.caption or ""

            if not caption:
                await context.bot.copy_message(chat_id=-1001248885302, from_chat_id=message.chat.id, message_id=message.id)
                return

            else:
                video_file = None
                photo_file = None

                if message.video:
                    video_file = message.video.file_id
                elif message.photo:
                    if len(message.photo) > 0:
                        photo_file = message.photo[-1].file_id

                caption = await safisha(caption)
                random_link = await generate_random_link()

                if message.video:
                    await context.bot.send_video(chat_id=-1001248885302, video=video_file, caption=f"{random_link}\n{caption}", parse_mode='HTML')
                else:
                    await context.bot.send_photo(chat_id=-1001248885302, photo=photo_file, caption=f"{random_link}\n{caption}", parse_mode='HTML')



#Kuondoa maneno yasiyo faa kwenye caption
async def usafi(update, context):
    message = update.message
    caption = message.caption
    caption = await safisha(caption)

    if update.effective_chat.type == 'private':
        if message.video:
            await context.bot.send_video(chat_id=update.effective_chat.id, video=message.video.file_id, caption=caption)

        if message.document:
            await context.bot.send_document(chat_id=update.effective_chat.id, document=message.document.file_id, caption=caption)

        if message.audio:
            await context.bot.send_audio(chat_id=update.effective_chat.id, audio=message.audio.file_id, caption=caption)


#kubadilisha link za x
async def replacelink(update, context):
    message_text = update.message.text
    url_options = ["fxtwitter.com", "twittpr.com", "fixupx.com", "i.fixupx.com"]
    replaced_x = message_text.replace("twitter.com", random.choice(url_options))
    await context.bot.send_message(chat_id=update.effective_chat.id, text=replaced_x)

#Kubadilisha Link za Inst
async def replaceinstalink(update, context):
    message_text = update.message.text
    replaced_text = message_text.replace("instagram", "ddinstagram")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=replaced_text)


async def replacetktlink(update, context):
    message_text = update.message.text
    replaced_text = message_text.replace("tiktok.com", "vxtiktok.com")
    await update.message.reply_text(text=replaced_text)


#Caption
async def safisha(caption):
    if "Saved by @InstantMediaBot" in caption or "Saved by @download_it_bot" in caption:
        caption = caption.replace("Saved by @InstantMediaBot", "")
        caption = caption.replace("Saved by @download_it_bot", "")
        return caption.strip()
    else:
        return caption


async def remove_urls(text):
    url_pattern = await r'https?://\S+|www\.\S+'
    text_without_urls = await re.sub(url_pattern, '', text)
    return text_without_urls

async def kagua(caption):
    if caption and "Saved by @InstantMediaBot" not in caption and "Saved by @download_it_bot" not in caption:
        return await caption


#Copy
async def nakili(update, context):
    message = update.effective_user
    await context.bot.copy_message(chat_id=-1001297333544, from_chat_id=update.effective_chat.id, message_id=message.message_id)