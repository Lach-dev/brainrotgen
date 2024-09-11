import os
from dotenv import load_dotenv

load_dotenv()


class settings:
    REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
    REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
    REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")
    POST_COUNT = int(os.getenv("POST_COUNT", 1))
    BASE_VIDEO_PATH = os.getenv("BASE_VIDEO_PATH", "base_videos/minecraft_parkour_a.mp4")
    SUBREDDIT_NAME = os.getenv("SUBREDDIT_NAME", "AskReddit")
