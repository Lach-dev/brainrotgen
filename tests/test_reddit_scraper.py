from reddit_scraper import scrape_posts


def test_scrape_posts():
    results = scrape_posts(5)
    assert len(results) == 5
    for result in results:
        assert result.title
        assert result.content
        assert result.author
        assert result.comments
        assert len(result.comments) == 3
        for comment in result.comments:
            assert comment
            assert len(comment) > 0
            assert len(comment) <= 1000
            assert comment != "[removed]"
            assert comment != "[deleted]"
