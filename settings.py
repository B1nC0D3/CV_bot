from dotenv import load_dotenv
import os
import pathlib
load_dotenv()


TG_TOKEN = os.getenv('TG_TOKEN')
PROJECT_ROOT = pathlib.Path(os.path.abspath(os.curdir))
MEDIA_ROOT = PROJECT_ROOT / './media'

LAST_PHOTO = PROJECT_ROOT / './photos/last_photo.jpg'
SCHOOL_PHOTO = PROJECT_ROOT / './photos/school_photo.jpg'

GPT_VOICE = PROJECT_ROOT / './voices/gpt.ogg'
SQL_VOICE = PROJECT_ROOT / './voices/slq_vs_nosql.ogg'
FIRST_LOVE_VOICE = PROJECT_ROOT / './voices/first_love.ogg'
