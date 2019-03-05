Asyncio-based implementation of the url parser service: for a given URL, it loads a webpage, parses and returns json with metadata (title, description, etc).

Similar node.js service is [here](https://github.com/serebrov/urlmeta-nodejs).
Similar rust service is [here](https://github.com/serebrov/urlmeta-rust).

The docker-based setup can be launched with `make up`, performance tests (using ApacheBench) - with `make ab-sanic` and `make ab-japronto`.

Without docker: run `python app/app_sanic.py` and `python app/app_japronto.py` appropriately.

Curl examples:

```
# sanic is running on port 8000

curl http://localhost:8000/url-parser\?target\=https://www.python.org/
{
    "description": "The official home of the Python Programming Language",
    "title": "Welcome to Python.org",
    "locale": null,
    "type": "website",
    "url": "https://www.python.org/",
    "image": "https://www.python.org/static/opengraph-icon-200x200.png",
    "video": null
}

curl http://localhost:8000/url-parser\?target\=https://www.youtube.com/watch\?v\=fJ9rUzIMcZQ
{
    "description": "Subscribe to the official Queen channel Here http://bit.ly/Subscribe2Queen Taken from A Night At The Opera, 1975. Queen - 'Bohemian Rhapsody' Click here to b...",
    "title": "Queen - Bohemian Rhapsody (Official Video) - YouTube",
    "locale": null,
    "type": "video.other",
    "url": "https://www.youtube.com/watch?v=fJ9rUzIMcZQ",
    "image": "https://i.ytimg.com/vi/fJ9rUzIMcZQ/hqdefault.jpg",
    "video": null
}
```

```
# japronoto is runnin on port 8080

curl http://localhost:8080/url-parser\?target\=https://www.python.org/
{
    "description": "The official home of the Python Programming Language",
    "title": "Welcome to Python.org",
    "locale": null,
    "type": "website",
    "url": "https://www.python.org/",
    "image": "https://www.python.org/static/opengraph-icon-200x200.png",
    "video": null
}

curl http://localhost:8080/url-parser\?target\=https://www.youtube.com/watch\?v\=fJ9rUzIMcZQ
{
    "description": "Subscribe to the official Queen channel Here http://bit.ly/Subscribe2Queen Taken from A Night At The Opera, 1975. Queen - 'Bohemian Rhapsody' Click here to b...",
    "title": "Queen - Bohemian Rhapsody (Official Video) - YouTube",
    "locale": null,
    "type": "video.other",
    "url": "https://www.youtube.com/watch?v=fJ9rUzIMcZQ",
    "image": "https://i.ytimg.com/vi/fJ9rUzIMcZQ/hqdefault.jpg",
    "video": null
}
```

Sidenote about python ansyncio library and related tools:

- asyncio - the library implementing similar to node.js architecture in python, with event loop and asyncronous I/O operations.
  - Note: CPU-intense tasks block the event loop, in python such tasks can be run in separate process (same in node.js, it can be forked into a separate process; in golang there are goroutines that are even lighter than threads)
- asyncio - base library, included into python standard library, it has event loop, implemented in python
- [uvloop](https://github.com/magicstack/uvloop) - alternative event loop implementation, based on uvlib, can be installed / enabled on top of asyncio
- [aiohttp](https://aiohttp.readthedocs.io/en/stable/) - framework based on asyncio, [github](https://github.com/aio-libs/aiohttp)
- [sanic](https://sanic.readthedocs.io/en/latest/) - another framework based on anyncio and uvloop
  Sanic — Sanic 18.12.0 documentation
- [japronto](https://github.com/squeaky-pl/japronto) - yet another, experimental, framework based on asyncio and uvloop, goal is performance
- More resources: https://github.com/timofurrer/awesome-asyncio
