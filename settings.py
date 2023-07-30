from dotenv import load_dotenv
import os
import pathlib
load_dotenv()


TG_TOKEN = os.getenv('TG_TOKEN')
PROJECT_ROOT = pathlib.Path(os.path.abspath(os.curdir))
MEDIA_ROOT = PROJECT_ROOT / './media'

LAST_PHOTO = MEDIA_ROOT / './photos/last_photo.jpg'
SCHOOL_PHOTO = MEDIA_ROOT / './photos/school_photo.jpg'

GPT_VOICE = MEDIA_ROOT / './voices/gpt.ogg'
SQL_VOICE = MEDIA_ROOT / './voices/sql_vs_nosql.ogg'
FIRST_LOVE_VOICE = MEDIA_ROOT / './voices/first_love.ogg'
