#!/usr/bin/env python3

import sys
import os
import time
from typing import Tuple

import feedparser
from feedparser import FeedParserDict
from ookami import Ookami


def main() -> None:
    """
    Central point of the program, invoking sub-functions and fetching their potential returns
    :return: None
    """
    hook: str = os.environ['HOOK'] if os.getenv('TOKEN') else get_hook()

    news: FeedParserDict
    obvestila: FeedParserDict
    news, obvestila = parse_rss()

    links: str = past_links()
    form: Ookami = Ookami()

    populate(news, 'Novica', links, form)
    populate(obvestila, 'Obvestilo', links, form)

    post(form, hook)


def get_hook() -> str:
    """
    Reads the webhook url from file and returns it
    :return: webhook url as a string
    """
    with open('../data/hook.txt', 'r') as rf:
        return rf.read().strip()


def parse_rss() -> Tuple[FeedParserDict, FeedParserDict]:
    """
    Requests the news and obvestila rss feeds, parses them (xml format) and returns them as a tuple
    :return: tuple-packed pair of parsed xml rss feed objects
    """
    news_url: str = 'https://vss.scpet.si/vss/rss.php?sec=news'
    news: FeedParserDict = feedparser.parse(news_url)

    obvestila_url: str = 'https://vss.scpet.si/vss/rss.php?sec=obvestila'
    obvestila: FeedParserDict = feedparser.parse(obvestila_url)

    return news, obvestila


def past_links() -> str:
    """
    Read the data of exhausted links from a log file and returns it as a single string
    :return: exhausted links as a single string
    """
    try:
        with open('../data/links.log', 'r') as rf:
            return rf.read()
    except FileNotFoundError:
        open('../data/links.log', 'a').close()


def populate(datatype: FeedParserDict, typename: str, links: str, form: Ookami) -> None:
    """
    Filters rss entries by content, builds a discord form object via the ookami class,
    saves exhausted links to a local log file and populates the form object
    :param datatype: parsed xml rss feed object
    :param typename: string-based type tag
    :param links: exhausted links as a single string
    :param form: empty shell of a form object of ookami class
    :return: None
    """
    for entry in datatype['entries']:

        if 'EKO' in entry['title'] and 'TK' not in entry['title']:
            continue

        link: str = entry["link"].replace('www.scpet.net', 'vss.scpet.si')

        if link in links:
            continue

        typeid: str = f'{typename} (id {link.split("=")[-1]})'
        summary: str = entry['description'].split('&lt;br&gt;')[0]
        datetime: str = ' '.join(entry['published'].split()[0:4])

        with open('../data/links.log', 'a') as wf:
            wf.write(f'{link}\n')

        form.embeds_fields(name=typeid, value=f'[{summary}]({link})\n{datetime}', inline=True)


def post(form: Ookami, hook: str) -> None:
    """
    Pushes a webhook post to the specified channel webhook url
    :param form: built and populated ookami form
    :param hook: discord channel webhook url
    :return: None
    """
    if form.embeds_fields_count():
        form.post(hook)


if __name__ == '__main__':
    path: str = os.path.dirname(__file__)
    os.chdir(path)

    while True:
        try:
            main()
        except Exception as exc:
            sys.exit(f'Exception during main() funct execution: {exc}')

        time.sleep(300)  # 5 minutes
