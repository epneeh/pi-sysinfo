from jinja2 import Environment, PackageLoader, select_autoescape
from numpy import empty
from sanic.response import html
from sanic.response import file
from os.path import exists


env = Environment(
    loader=PackageLoader(__name__),
    autoescape=select_autoescape(['html'])
)

async def index(request):
    template = env.get_template('index.html')
    return html(template.render())

async def static(request,pth):
    sfile = './static/' + pth
    if exists(sfile):
        return await file(sfile)
    else:
        return html('',404)