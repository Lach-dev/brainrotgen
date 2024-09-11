import praw
from config import Config

class RedditPost:
    def __init__(self, title: str, content: str, author: str, comments: list[str]):
        self.title = title
        self.content = content
        self.author = author
        self.comments = comments

    def __dict__(self):
        return {
            "title": self.title,
            "content": self.content,
            "comments": self.comments
        }


reddit = praw.Reddit(
    client_id=Config.REDDIT_CLIENT_ID,
    client_secret=Config.REDDIT_CLIENT_SECRET,
    user_agent=Config.REDDIT_USER_AGENT
)


def scrape_posts(count: int) -> list[RedditPost]:
    scraped_posts: list[RedditPost] = []

    # Select the subreddit
    subreddit = reddit.subreddit('tifu')

    top_posts = subreddit.top(limit=count, time_filter='month')

    for post in top_posts:
        print("Title: ", post.title)
        print("Content: ", post.selftext)

        comments = []
        post.comments.replace_more(limit=0)  # Fetch all comments
        for top_comment in post.comments[:10]:  # Get the top 10
            comment_content = top_comment.body
            if comment_content in ["[removed]", "[deleted]"]:
                continue
            else:
                comments.append(comment_content)

            if len(comments) == 3:
                break

        scraped_posts.append(RedditPost(post.title, post.selftext, post.author, comments))

    return scraped_posts