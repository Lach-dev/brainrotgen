from reddit_scraper import scrape_posts
from script_generator import ScriptGenerator
import logging

logging.basicConfig(level=logging.INFO)

script_gen = ScriptGenerator()

def main():
    post_count = 5

    logging.info(f"Scraping {post_count} posts from reddit...")
    reddit_posts = scrape_posts(5)
    logging.info(f"Scraped {len(reddit_posts)} posts from reddit.")

    logging.info("Generating script from reddit post...")
    script, audio_path = script_gen.generate_script(reddit_posts[0])
    logging.info("Generated script from reddit post.")

    # cut videos and put together 4-1
    # overlay audio, text on top of video
    # upload to instagram reels


if __name__ == "__main__":
    main()
