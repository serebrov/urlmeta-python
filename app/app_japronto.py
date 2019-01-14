import asyncio

# https://github.com/squeaky-pl/japronto
from japronto import Application

from urlmeta import async_get, sync_parse, async_parse 


# This is a synchronous handler.
def synchronous(request):
    return request.Response(text='I am synchronous!')


# This is an asynchronous handler, it spends most of the time in the event loop.
# It wakes up every second 1 to print and finally returns after 3 seconds.
# This does let other handlers to be executed in the same processes while
# from the point of view of the client it took 3 seconds to complete.
async def asynchronous(request):
    for i in range(1, 4):
        await asyncio.sleep(1)
        print(i, 'seconds elapsed')

    return request.Response(text='3 seconds elapsed')


async def urlparser(request):
    url = request.query['target']
    html = await async_get(url)
    # meta = await async_parse(html)
    meta = sync_parse(html)
    return request.Response(json=meta)


app = Application()

r = app.router
r.add_route('/sync', synchronous)
r.add_route('/async', asynchronous)
r.add_route('/url-parser', urlparser)

app.run()
