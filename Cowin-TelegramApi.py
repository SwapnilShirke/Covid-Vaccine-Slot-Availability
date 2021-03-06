import requests
import pandas as pd
import io
import time
import json
from datetime import date
import datetime



class Main:

    def process(self,date):

        print(date)
        url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict"
        #querystring = {"district_id": "393", "date": "31-03-2021"}
        querystring = {"district_id": "393", "date": date}



        headers = {
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
        }
        response = requests.request(
        "GET", url, headers=headers, params=querystring)

        data = response.json() 
        #print(data)
        sessions = data["sessions"]
        data_all = []
        if(len(sessions) == 0):
            print("no sessions")
        else:
            for session in sessions:
                row = "Name"+":" + session["name"]+"\n"
                row += "Block Name"+":" + session["block_name"]+"\n"
                row += "Center Id"+":" + str(session["center_id"])+"\n"
                row += "Pincode"+":" + str(session["pincode"])+"\n"
                row += "Availability"+":" + str(session["available_capacity"])+"\n"
                row += "Fee Type"+":" + str(session["fee_type"])+"\n"
                row += "Vaccine Type"+":" + session["vaccine"]+"\n"
                row += "Min Age Limit"+":" + str(session["min_age_limit"])+"\n"
                row += "Date"+":" + session["date"]+"\n"
                row += "Time Slots"+":" + str(session["slots"])+"\n"
                row += "Register at:" + "https://selfregistration.cowin.gov.in/"+"\n"
                row += " or register using UMANG app on mobile as it gives you option to book for current week \n"
                row += "-------------------------------"+"\n"
                data_all.append(row)

            str1 = ''.join(str(e) for e in data_all)
            print(str1)

            URL1 = "http://api.telegram.org/bot1592174523:AAFXnFfa3rI-Qh_0UMhCs-k-tORoJ-1SEWc/sendMessage"
            chat_id= "-1001420977771"
            text = str1
            PARAMS = {'chat_id':chat_id,'text':text}

            r = requests.get(url = URL1, params = PARAMS)

            print(r.json())




Object = Main()
today = date.today().strftime("%d-%m-%Y")

while True:
    Object.process(today)
    tomorrow = date.today() + datetime.timedelta(days=1)
    Object.process(tomorrow.strftime("%d-%m-%y"))
    time.sleep(15)
