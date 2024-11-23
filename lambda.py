import json
import os

def lw(event, context):

    print("i am dakshayani from bengaluru i m dev ")
    
    return {
            'statuscode' : 200,
            'body' : json.dumps('hello from dakshayani! from bengaluru by vd ')
            } 
