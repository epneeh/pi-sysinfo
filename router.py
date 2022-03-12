from jinja2 import Environment, PackageLoader, select_autoescape
from sanic import json
from sanic.response import html
from sanic.response import file
from os.path import exists
import utils

env = Environment(
    loader=PackageLoader(__name__),
    autoescape=select_autoescape(['html'])
)

BASE_URL = "http://192.168.0.110:9090/"

async def index(request):
    template = env.get_template('index.html')
    data = {
        "base_url" : BASE_URL
        }
    return html(template.render(data))

async def static(request,pth):
    sfile = './static/' + pth
    if exists(sfile):
        return await file(sfile)
    else:
        return html('',404)

async def info(request):
    type = request.form.get("type")

    return json()