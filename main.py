from reddit_scraper import scrape_posts


def main():
    reddit_posts = scrape_posts(5)
    for post in reddit_posts:
        print(post.author)
        print(post.title)
    # generate script from reddit post
    # generate audio from script
    # cut videos and put together 4-1
    # overlay audio, text on top of video
    # upload to instagram reels


if __name__ == "__main__":
    main()
