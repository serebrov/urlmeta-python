# import uvloop
# import asyncio

from sanic import Sanic
from sanic.response import json

from urlmeta import async_get, sync_parse, async_parse 

app = Sanic()

@app.route('/url-parser')
async def urlparser(request):
    url = request.args['target'][0]
    html = await async_get(url)
    # meta = await async_parse(html)
    meta = sync_parse(html)
    return json(meta)

if __name__ == '__main__':
    # asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    app.config.update({'ACCESS_LOG': False})
    app.config.ACCESS_LOG = False
    app.run(host='0.0.0.0', port=8000, access_log=False)
