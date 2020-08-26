from aiohttp import web
import zerorpc
class Web:
    def __init__(self):
        self.app = web.Application()
        self.app.add_routes([web.get('/agent/list', self.agents_handle),
                             web.post('/task', self.task_handle)
        ])
        self.client = zerorpc.Client()
        self.client.connect("tcp://127.0.0.1:9000")

    async def agents_handle(self, request):

        return web.json_response(self.client.agents())
    async def task_handle(self, request):
        j = await request.json()
        task_id = self.client.add_task(j)
        return web.json_response(task_id)
    def start(self):
        web.run_app(self.app, host="0.0.0.0", port=80)
    def shutdown(self):
        pass