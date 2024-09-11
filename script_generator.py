from openai import OpenAI
from config import Config
from reddit_scraper import RedditPost
from pathlib import Path
from openai import OpenAI

client = OpenAI(api_key=Config.OPENAI_API_KEY)


class ScriptGenerator:
    def __init__(self):
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)
        self.model = Config.OPENAI_MODEL

    def generate_script(self, post: RedditPost) -> (str, str):
        system_prompt = ("You're an expert at creating chaotic, brain-melting reads. "
                         "You’re going to read this Reddit post like a regular person who's hyped up on too much coffee and way too much internet. "
                         "First, say something wild about the post and the author. Then, describe what’s going on and read the post casually. "
                         f"Example: 'Yo, this user {post.author} just dropped the wildest take! Check this out!' "
                         "After that, go ahead and dive straight into what the post says without labeling anything. "
                         "Also, when talking about the replies, just act like you're casually reacting to them—no need to label them as 'comments' or anything formal like that.")

        post_prompt = (f"Alright, here’s the Reddit post. No labels, just go: \n"
                       f"{post.title}\n\n"
                       f"{post.content}\n\n"
                       f"{post.author} said that. Here are some replies:\n"
                       f"{' '.join(post.comments)}")

        response = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": post_prompt}
            ],
            model=self.model,
        )

        script = response.choices[0].message.content

        audio_file_name = f"audio/speech_{post.author}_{post.title}.mp3"

        speech_file_path = Path(__file__).parent / audio_file_name
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=script
        )

        response.stream_to_file(speech_file_path)

        return script, audio_file_name
