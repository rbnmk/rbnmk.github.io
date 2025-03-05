from textwrap import dedent
import urllib.parse
import re

x_intent = "https://x.com/intent/tweet"
bluesky_sharer = "https://bsky.app/intent/compose"
include = re.compile(r"blog/[1-9].*")

def on_page_markdown(markdown, **kwargs):
    page = kwargs['page']
    config = kwargs['config']
    if not include.match(page.url):
        return markdown

    page_url = config.site_url+page.url
    page_title = urllib.parse.quote(page.title+'\n')

    return markdown + dedent(f"""
    [Share on :simple-x:]({x_intent}?text={page_title}&url={page_url}){{ .md-button }}
    [Share on :simple-bluesky:]({bluesky_sharer}?u={page_url}){{ .md-button }}
    """)