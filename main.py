from reddit_scraper import scrape_posts
from script_generator import ScriptGenerator
from stitch_video import generate_base_video
import logging
from config import settings

logging.basicConfig(level=logging.INFO)

script_gen = ScriptGenerator()


def main():
    post_count = settings.POST_COUNT

    logging.info(f"Scraping {post_count} post(s) from reddit...")
    reddit_posts = scrape_posts(post_count)
    logging.info(f"Scraped {len(reddit_posts)} post(s) from reddit.")

    for reddit_post in reddit_posts:
        logging.info(f"Reddit post: {reddit_post.title}")

        logging.info("Generating script from reddit post...")
        script, audio_path = script_gen.generate_script(reddit_post)
        logging.info("Generated script from reddit post.")

        logging.info("Generating base video...")
        stitched_video_path = generate_base_video(settings.BASE_VIDEO_PATH, audio_path, script)
        logging.info(f"Generated base video at {stitched_video_path}")

    # upload to instagram reels


if __name__ == "__main__":
    main()
