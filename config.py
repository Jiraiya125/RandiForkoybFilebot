#(©)CodeXBotz




import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6433122327:AAFamzobcAFdQvOg5kGQzeplNN7pY40vFr8")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "23783960"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ed9a02483a7ae4e018036a4da6f0027f")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001780719412"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1390875822"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://hganimefilesharebot:Z3FRY0kQ9CKktFcd@cluster0.3mjdtix.mongodb.net/?retryWrites=true&w=majority")
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", DB_URI)
DB_NAME = os.environ.get("DATABASE_NAME", "ainzbot")

#desi fsub / Simple fsub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001777988475"))
# Req Fsubs
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001939031666"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1001939031666"))


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first} , Thanks for using me :D @HG_Anime ⚡.")
try:
    ADMINS=[1390875822]
    for x in (os.environ.get("ADMINS", "1390875822").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "👋 Hello {first}!\nPlease Join our channel First [ᴛᴀᴘ ᴏɴ ᴊᴏɪɴ ⚡] then\n Download by tapping on ⚡Try Again \nThank You ❤️")

#Start pic 
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/90e97f2ee363e5a4b0af2.jpg")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "🚫 Please Avoid Direct Messages. I'm Here merely for file sharing!"

#Auto delete by HG Anime
AUTO_DEL = os.environ.get("AUTO_DEL", "True")
DEL_TIMER = int(os.environ.get("DEL_TIMER", "600"))
DEL_MSG = "<b> Baka! Files will be deleted After {time}. Save them to the Saved Message now! </b>"

#Trippy_xt


ADMINS.append(OWNER_ID)
ADMINS.append(1390875822)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
