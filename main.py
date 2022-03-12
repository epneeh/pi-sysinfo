from sanic import Sanic
import router as R

app=Sanic(__name__)

app.add_route(R.index,"/",methods=['GET'])
app.add_route(R.static,"/static/<pth:path>",methods=['GET'])
app.add_route(R.info,"/info/<type:str>",methods=['POST'])

if __name__ == '__main__':
    app.run("0.0.0.0",9090,fast=True)
