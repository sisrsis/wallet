from flask import Flask , request 
from database import Mysql
from datetime import datetime



app = Flask(__name__)
db = Mysql(host='',user='',password='',database='')

@app.route('/ping')
def ping():
        return "ping"

@app.route('/price/',methods=['GET'])
def price():
        time = datetime.now()
        time = int(time.timestamp())
        try:
                coin =  str(request.args['coin'])
                price = str(request.args['price'])
        except:
                return {"status":401}
        db.insert(coin,{"price":price,"times":time})
        return f"{price} {coin}"
