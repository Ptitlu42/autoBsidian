from dotenv import load_dotenv
import os

class Config:
    def __init__(self):
        load_dotenv()
        self.LOCAL_PATH = os.getenv("LOCAL_PATH")
        self.REMOTE_PATH = os.getenv("REMOTE_PATH")
        self.REMOTE_URL = os.getenv("REMOTE_URL")
        self.SYNC_INTERVAL = os.getenv("SYNC_INTERVAL")

