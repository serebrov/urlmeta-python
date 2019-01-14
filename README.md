Asyncio-based implementation of the url parser service: for a given URL, it loads a webpage, parses and returns json with metadata (title, description, etc).

Similar node.js service is [here](https://github.com/serebrov/urlmeta-nodejs).

The docker-based setup can be launched with `make up`, performance tests (using ApacheBench) - with `make ab-sanic` and `make ab-japronto`.

Without docker: run `python app/app_sanic.py` and `python app/app_japronto.py` appropriately.

Curl examples:

```
# sanic
curl http://localhost:8000/url-parser\?target\=https://www.nytimes.com

# japronoto:
curl http://localhost:8080/url-parser\?target\=https://www.nytimes.com
```

Sidenote about python ansyncio library and related tools:
* asyncio - the library implementing similar to node.js architecture in python, with event loop and asyncronous I/O operations. 
  * Note: CPU-intense tasks block the event loop, in python such tasks can be run in separate thread (in node.js forked into a separate process, which is heavier than thread; in golang there are goroutines that are even lighter than threads)
* asyncio - base library, included into python standard library, it has event loop, implemented in python
* [uvloop](https://github.com/magicstack/uvloop) - alternative event loop implementation, based on uvlib, can be installed / enabled on top of asyncio
* [aiohttp](https://aiohttp.readthedocs.io/en/stable/) - framework based on asyncio, [github](https://github.com/aio-libs/aiohttp)
* [sanic](https://sanic.readthedocs.io/en/latest/) - another framework based on anyncio and uvloop
Sanic — Sanic 18.12.0 documentation
* [japronto](https://github.com/squeaky-pl/japronto) - yet another, experimental, framework based on asyncio and uvloop, goal is performance
* More resources: https://github.com/timofurrer/awesome-asyncio
