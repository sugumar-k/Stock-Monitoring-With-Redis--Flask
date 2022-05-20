
import redis
from flask import Flask, render_template

db =redis.StrictRedis(host='127.0.0.1',port='6379',db=0,charset="utf-8",decode_responses=True)




app= Flask (__name__)
@app.route('/')
def home():
    return render_template ("base.html")

from typing import Optional,List
import redis
from pydantic import EmailStr, ValidationError,PositiveInt
from redis_om import JsonModel,Field
import json


class Item(JsonModel):
    
    name :str=Field(index=True)
    price : PositiveInt=Field(index=True)
    barcode :str=Field(index=True)
    description :str=Field(index=True)
    



@app.route("/stocks")

def stocks_page(): 
    
    
    item=Item.find().all()
    

    return render_template('stocks.html', items=item)

    

    
if __name__=="__main__":
    app.run(debug=True)

