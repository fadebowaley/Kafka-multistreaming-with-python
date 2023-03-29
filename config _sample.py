import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SERVER1_HOST = os.environ.get('SERVER1_HOST')
    SERVER1_TOPIC = os.environ.get('SERVER1_TOPIC')

    SERVER2_HOST = os.environ.get('SERVER2_HOST')
    SERVER2_TOPIC = os.environ.get('SERVER2_TOPIC')

    SERVER3_HOST = os.environ.get('SERVER3_HOST')
    SERVER3_TOPIC = os.environ.get('SERVER3_TOPIC')
