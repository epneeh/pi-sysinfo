from ctypes import util
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

BASE_URL = "http://localhost:9090/"

async def index(request):
    template = env.get_template('index.html')
    cpu_util = utils.cpu_percent()
    cpu_freq = utils.cpu_freq()
    cpu_temp = utils.cpu_temp()
    ram = utils.ram()
    swap = utils.swap()
    
    data = {
        "base_url" : BASE_URL,
        "judul" : "Raspi System Info",
        "cpu_percent" : cpu_util,
        "cpu_freq" : cpu_freq,
        "temps" : cpu_temp,
        "ram" : ram,
        "swap" : swap
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
    if type == "cpu_util":
        j = utils.cpu_percent()
    elif type == "freq":
        j =  utils.cpu_freq()
    elif type == "temp":
        j = utils.cpu_temp()
    elif type == "ram":
        j = utils.ram()
    elif type == "swap":
        j = utils.swap()
    else:
        j = {}
    return json(j)
