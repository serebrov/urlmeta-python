import aiohttp
import asyncio
from selectolax.parser import HTMLParser 
from concurrent.futures import ProcessPoolExecutor

metadata_rules = {
  "description": {
    "rules": [
        ['meta[property="og:description"]', lambda e: e.attributes['content']],
        ['meta[name="description"]', lambda e: e.attributes['content']]
    ]
  },
  "title": {
    "rules": [
        ['meta[property="og:title"]', lambda e: e.attributes['content']],
        ['title', lambda e: e.text()]
    ]
  },
  "locale": {
    "rules": [
        ['meta[property="og:locale"]', lambda e: e.attributes['content']],
    ]
  },
  "type": {
    "rules": [
        ['meta[property="og:type"]', lambda e: e.attributes['content']],
    ]
  },
  "url": {
    "rules": [
        ['meta[property="og:url"]', lambda e: e.attributes['content']],
    ]
  },
  "image": {
    "rules": [
        ['meta[property="og:image"]', lambda e: e.attributes['content']],
    ]
  },
  "video": {
    "rules": [
        ['meta[property="og:video"]', lambda e: e.attributes['content']],
    ]
  }
}

def sync_parse(html):
    selectors = [
        'meta[property="og:description"]',
    ]

    parser = HTMLParser(html)
    meta = dict()
    for prop in metadata_rules:
        for rule in metadata_rules[prop]['rules']:
            selector = rule[0]
            callback = rule[1]
            for node in parser.css(selector):
                meta[prop] = callback(node)
                break
            else:
                meta[prop] = None
    return meta

async def async_parse(html):
    executor = ProcessPoolExecutor()
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(executor, sync_parse, html)

async def async_get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.text()
