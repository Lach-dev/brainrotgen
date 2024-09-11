from reddit_scraper import scrape_posts
from script_generator import ScriptGenerator
from stitch_video import generate_base_video
import logging

logging.basicConfig(level=logging.INFO)

script_gen = ScriptGenerator()


def main():
    post_count = 1

    logging.info(f"Scraping {post_count} posts from reddit...")
    reddit_posts = scrape_posts(post_count)
    logging.info(f"Scraped {len(reddit_posts)} posts from reddit.")

    logging.info("Generating script from reddit post...")
    script, audio_path = script_gen.generate_script(reddit_posts[0])
    logging.info("Generated script from reddit post.")

    logging.info("Generating base video...")
    stitched_video_path = generate_base_video("base_videos/minecraft_parkour_a.mp4", audio_path, script)
    logging.info(f"Generated base video at {stitched_video_path}")

    # upload to instagram reels


if __name__ == "__main__":
    main()
