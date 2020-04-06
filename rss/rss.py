#!/usr/bin/env python3

import os
import time
import feedparser
import ookami


def main() -> None:
    """Accepts the webhook url, rss feeds, and past links from a save file,
    initializes the default webhook form, calls the webhook population, and makes a post request"""

    while True:
        hook = os.environ['HOOK'] if os.getenv('TOKEN') else get_hook()
        news, obvestila = parse_rss()
        links = past_links()

        form = ookami.Ookami()

        populate(news, 'Novica', links, form)
        populate(obvestila, 'Obvestilo', links, form)

        post(form, hook)
        time.sleep(300)


def get_hook() -> str:
    """Reads and returns a webhook url from a file"""

    with open('hook.txt', 'r') as rf:
        return rf.read().strip()


def parse_rss() -> tuple:
    """Returns the parsed rss feeds"""

    news_url = 'https://vss.scpet.si/vss/rss.php?sec=news'
    news = feedparser.parse(news_url)

    obvestila_url = 'https://vss.scpet.si/vss/rss.php?sec=obvestila'
    obvestila = feedparser.parse(obvestila_url)

    return news, obvestila


def past_links() -> str:
    """Reads and returns past links from a save file"""

    with open('rss.txt', 'r') as rf:
        return rf.read()


def populate(datatype: feedparser.FeedParserDict, typename: str, links: str, form) -> None:
    """Populates the form object with data in-place and writes exhausted links to the save file"""

    for entry in datatype['entries']:

        if 'EKO' in entry['title'] and 'TK' not in entry['title']:
            continue

        link = entry["link"].replace('www.scpet.net', 'vss.scpet.si')

        if link in links:
            continue

        typeid = f'{typename} (id {link.split("=")[-1]})'
        summary = entry['description'].split('&lt;br&gt;')[0]
        datetime = ' '.join(entry['published'].split()[0:4])

        with open('rss.txt', 'a') as wf:
            wf.write(f'{link}\n')

        form.embeds_fields(name=typeid, value=f'[{summary}]({link})\n{datetime}', inline=True)


def post(form, hook: str) -> None:
    """Creates a post request through a webhook if any fields were added"""

    if form.embeds_fields_count():
        form.post(hook)


if __name__ == '__main__':
    main()
