import requests
import time

def get_price():

    url = "https://www.google.com/async/finance_wholepage_price_updates?ei=gPcoY-2_NbHJptQP-a6AqAE&rlz=1C1CHZN_enUS942US942&yv=3&cs=0&async=mids:%2Fg%2F11lky30jcs%7C%2Fm%2F016yss%7C%2Fm%2F02853rl%7C%2Fm%2F04zvfw%7C%2Fg%2F1q52gbb7v,currencies:,_fmt:jspb"

    filter = '"Upstart Holdings Inc","UPST","'

    results = requests.get(url)
    filtered_text = results.text.split(filter)[1]
    filtered_text = filtered_text.split('"')[0]
    return float(filtered_text)