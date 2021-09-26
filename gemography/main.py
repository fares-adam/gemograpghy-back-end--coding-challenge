from flask import Flask
import requests
import datetime





app = Flask(__name__)



@app.route('/', methods=['GET'])
def fun():
    #getting yesterdays date
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    timeiso = yesterday
    #api url
    url = f"https://api.github.com/search/repositories?q=created:>{timeiso}&sort=stars&order=desc"

    payload={}
    headers = {}
    
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()








app.run(port=5000, debug=True)
