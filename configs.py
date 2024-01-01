import os
import re

id_pattern = re.compile(r'^.\d+$')

class Config(object):
  API_ID = int(os.environ.get("API_ID", "20036136"))
  API_HASH = os.environ.get("API_HASH", "4a16864f4b6f956f8bb6003b726133a7")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6736817570:AAHAQry1Gt5uinv7o0tq65y6kHH-I7xB-N4")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Link2_Horny_RoBot")
  DB_CHANNEL = [int(db) if id_pattern.search(db) else db for db in os.environ.get('DB_CHANNEL', '-1002139098224').split()]
  BOT_OWNER = [int(owner) if id_pattern.search(owner) else owner for owner in os.environ.get('BOT_OWNER', '6934250556').split()]
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://jonesdee2k:gdj132549s@cluster0.1qnajcm.mongodb.net/?retryWrites=true&w=majority")
  LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1002004055044")
  BANNED_USERS = set(int(x) if id_pattern.search(x) else x for x in os.environ.get('BANNED_USERS', '').split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", False))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) if id_pattern.search(x) else x for x in os.environ.get('BANNED_CHAT_IDS', '').split()))
  AUTH_USERS = [int(auth_users) if id_pattern.search(auth_users) else auth_users for auth_users in os.environ.get('AUTH_USERS', '6934250556 1825185800').split()]
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002020360256")
  ABOUT_BOT_TEXT = f"""
ᴛʜɪs ɪs ᴀ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ғᴏʀ ᴏᴡɴᴇʀ ᴀᴄᴄᴇss ᴏɴʟʏ 💀 

╭────[ 🔅Fɪʟᴇ Sᴛᴏʀᴇ Bᴏᴛ🔅]────⍟
│
┽➢❇️ᴍʏ ɴᴀᴍᴇ ➺ [𝐋𝐢𝐧𝐤 𝐒𝐭𝐨𝐫𝐞 𝐁𝐨𝐭](https://t.me/{BOT_USERNAME})
│
┽➤⭕ ʟᴀɴɢᴜᴀɢᴇ ➺ [𝐏𝐲𝐭𝐡𝐨𝐧](https://www.python.org)
│
┽➤⭕ ʟɪʙʀᴀʀʏ ➺ [𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦](https://docs.pyrogram.org)
│
┽➣♻️ᴍʏ ᴏᴡɴᴇʀ ➺ [𝐃𝐚𝐫𝐤 𝐌𝐚𝐭𝐭𝐞𝐫™](https://t.me/Dark_Matter_v4_RoBot)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
👤 Tʜɪs ʙᴏᴛ ɪs ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ ➳ [𝐃𝐚𝐫𝐤 𝐌𝐚𝐭𝐭𝐞𝐫™](https://t.me/Dark_Matter_v4_RoBot)"""
  HOME_TEXT = """
╭──〔👋 Hᴇʟʟᴏ [{}](tg://user?id={})〕──➣
│
╰➣🥰 ɪ ᴀᴍ ᴀ sᴛᴀʙʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ
╭──╯
╰────⌬
╭────⌬
╰➣🤭 ʜᴏᴘᴇ ʏᴏᴜ ᴀʀᴇ ᴇɴᴊᴏʏɪɴɢ
╭──╯
╰────⌬
╭────⌬
╰➢🎎 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : [𝐃𝐚𝐫𝐤 𝐌𝐚𝐭𝐭𝐞𝐫™](https://t.me/Dark_Matter_v4_RoBot)
╭──╯
╰─➣〔✨ ʜᴀᴠᴇ ᴀ ɴɪᴄᴇ ᴅᴀʏ ✨〕──❍
"""
  SHORTENER_API_MESSAGE = """
╭──〔♻️sʜᴏʀᴛɴᴇʀ ᴘʀᴏᴄᴇss ♻〕──➣
│
┽➢ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴀᴅᴅ/ᴜᴘᴅᴀᴛᴇ sʜᴏʀᴛɴᴇʀ👇🏻
│
┽➣<code>/shortener base_site apikey</code>
│
╰──〔🥰 ᴘʀᴏᴄᴇss ᴇɴᴅ 🥰〕──❍

╭──〔 sʜᴏʀᴛᴇɴᴇʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ 〕─❍
╰──────👇🏻
╭──────⌬
╰🌐 𝑾𝒆𝒃𝒔𝒊𝒕𝒆 ➻ 

<code>{base_site}</code>

╭──────⌬
╰🔐 𝑨𝒑𝒊 ➻ 

<code>{shortener_api}</code>

╭──────⌬
╰──〔 ʜᴇʀᴇ ᴡᴇ ɢᴏ ᴀɢᴀɪɴ 🚀〕─➣
"""
  SHORTNING_SUCCESS = """
╭──〔♻️sᴜᴄᴄᴇss ♻〕─❍
│
╰──➢〔🛡️𝐌𝐚𝐢𝐧 𝐔𝐫𝐥 🛡〕
⌬───────╯ ╰───────⌬

<code>{main_url}</code>

╭──➢〔🔗 𝐒𝐡𝐨𝐫𝐭 𝐔𝐫𝐥 🔗〕
│
╰──────────⌬

 <code>{}</code>
 
╭──────────⌬
╰──〔 ʜᴇʀᴇ ᴡᴇ ɢᴏ ᴀɢᴀɪɴ 🚀〕─➣  
"""
