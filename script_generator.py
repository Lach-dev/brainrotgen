from config import settings
from reddit_scraper import RedditPost
from pathlib import Path
from openai import OpenAI
from functools import lru_cache

client = OpenAI(api_key=settings.OPENAI_API_KEY)


class ScriptGenerator:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.OPENAI_MODEL

    @lru_cache(maxsize=128)
    def generate_script(self, post: RedditPost) -> (str, str):
        audio_file_name = f"audio/speech_{post.author}_{post.title}.mp3"

        system_prompt = ("You will be provided with a reddit post and its replies."
                         "Introduce the post and mention the author. Then read the contents of the post."
                         "After that, mention the replies to the post. Do not provide any labels. Do not say Author: Title: Content: etc."
                         "This is a post from r/AskReddit. Introduce the post like you are a narrator. Say something like "
                         "the user {post.authr} asked: "
                         "then read the post. After that, say something like here are some replies: and read the replies."
                         "like 'one user said: or 'another user replied:'.")

        post_prompt = (f"Here’s the Reddit post. No labels: \n"
                       f"author: {post.author}\n\n"
                       f"title: {post.title}\n\n"
                       f"content: {post.content}\n\n"
                       f"Here are some replies:\n"
                       f"{' '.join(post.comments)}")

        response = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": post_prompt}
            ],
            model=self.model,
            max_tokens=250
        )

        script = response.choices[0].message.content

        speech_file_path = Path(__file__).parent / audio_file_name
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=script
        )

        response.stream_to_file(speech_file_path)

        return script, audio_file_name
