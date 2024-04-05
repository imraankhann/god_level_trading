from pickle import NONE
import time
from httplib2 import Credentials
import requests
import json
import math
from datetime import datetime
from pytz import timezone
import numpy as np
import pandas as pd
from  telegram import Bot
import asyncio

# def strRed(skk): return "\033[91m {}\033[00m".format(skk)
# def strGreen(skk): return "\033[92m {}\033[00m".format(skk)
# def strYellow(skk): return "\033[93m {}\033[00m".format(skk)
# def strLightPurple(skk): return "\033[94m {}\033[00m".format(skk)
# def strPurple(skk): return "\033[95m {}\033[00m".format(skk)
# def strCyan(skk): return "\033[96m {}\033[00m".format(skk)
# def strLightGray(skk): return "\033[97m {}\033[00m".format(skk)
# def strBlack(skk): return "\033[98m {}\033[00m".format(skk)
# def strBold(skk): return "\033[1m {}\033[0m".format(skk)

# This program notifies when Bank Nifty trades near GOD LEVEL. 
# GOD LEVEL need to be updated by calculating few values in ce_pe_levels.csv file. 
# You can take reversal trades if Bank nifty trades near GOD LEVEL.

now = datetime.now()
format = "%d-%m-%Y %H:%M:%S %Z%z"
now_utc = datetime.now(timezone('UTC'))
now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
ocTime = now_asia.strftime(format)
fName = now_asia.strftime(format)
tdate = fName.split(" IST")
nowTime = tdate[0]
print(nowTime)
curWeekday = datetime.today().weekday()
dtTime = fName.split(" IST")
dt = dtTime[0].split(" ")
isHolidayNxtDay = ""
reqTime = ocTime[11:16]
reqSec = ocTime[14:16]
intTime = int(reqTime[0:2])
intSec = int(reqSec)
counter = 0

b_token = '5817461626:AAHp1IIIMkQGWFTqIuu84lYOoxlO8KS7CZo'
#nse_ch_token = '5771720913:AAH0A70f0BPtPjrOCTrhAb9LR7IGFBVt-oM'
channel_id = '@swingTradeScreenedStocks'
#nse_ch_id = '-703180529'


#Fetch Updated Index values from csv file
nsedf_ce = pd.read_csv('./ce_pe_levels.csv',usecols=['CE_Levels'],nrows=1)
nsedf_pe = pd.read_csv('./ce_pe_levels.csv',usecols=['PE_Levels'],nrows=1)
bnfdf_ce = pd.read_csv('./ce_pe_levels.csv',usecols=['CE_Levels'],nrows=2)
bnfdf_pe = pd.read_csv('./ce_pe_levels.csv',usecols=['PE_Levels'],nrows=2)
nse_ce_levels = nsedf_ce['CE_Levels'].loc[nsedf_ce.index[0]]
nse_pe_levels = nsedf_pe['PE_Levels'].loc[nsedf_pe.index[0]]
bnf_ce_levels = bnfdf_ce['CE_Levels'].loc[bnfdf_ce.index[1]]
bnf_pe_levels = bnfdf_pe['PE_Levels'].loc[bnfdf_pe.index[1]]

bot = Bot(token=b_token)

#Notify Index values To Telegram Channel before 9AM
if intTime==12 and intSec in range(32,40):
#if intTime==16 and intSec in range(15,35):
    #t_url = "https://api.telegram.org/bot6377307246:AAEuJAlBiQgDQEa03yNmKQJmZbXyQ0WINOk/sendMessage?chat_id=-996001230&text="+"======================\n"+nowTime+"\n======================"+"\nWELCOME TO AI BOT TRADING"+"\n======================"+"\nBOT STARTED SUCCESSFULLY..!"+"\n======================\n"+"TODAY's INDEX LEVELS\n"+"======================\n"+"NIFTY CE LEVEL: "+str(nse_ce_levels)+"\n"+"=========================\n"+"NIFTY PE LEVEL: "+str(nse_pe_levels)+"\n"+"=========================\n"+"BNF CE LEVEL: "+str(bnf_ce_levels)+"\n=========================\n"+"BNF PE LEVEL: "+str(bnf_pe_levels)+"\n=========================\n"+"NOTE : ONLY FOR EDUCATIONAL PURPOSE."+"\n----------------------------------------------"+"\nI AM NOT SEBI REG..!"+"\n-----------------------------------"+"\nTRADE AT YOUR OWN RISK..!"+"\n---------------------------------\n"+"WISH YOU PROFITABLE DAY..!"
    #  t_url = "https://api.telegram.org/bot5817461626:AAHp1IIIMkQGWFTqIuu84lYOoxlO8KS7CZo/sendMessage?chat_id=-703180529&text="+"======================\n"+nowTime+"\n======================"+"\nWELCOME TO AI BOT TRADING"+"\n======================"+"\nBOT STARTED SUCCESSFULLY..!"+"\n======================\n"+"TODAY's INDEX LEVELS\n"+"======================\n"+"NIFTY CE LEVEL: "+str(nse_ce_levels)+"\n"+"=========================\n"+"NIFTY PE LEVEL: "+str(nse_pe_levels)+"\n"+"=========================\n"+"BNF CE LEVEL: "+str(bnf_ce_levels)+"\n=========================\n"+"BNF PE LEVEL: "+str(bnf_pe_levels)+"\n=========================\n"+"NOTE : ONLY FOR EDUCATIONAL PURPOSE."+"\n----------------------------------------------"+"\nI AM NOT SEBI REG..!"+"\n-----------------------------------"+"\nTRADE AT YOUR OWN RISK..!"+"\n---------------------------------\n"+"WISH YOU PROFITABLE DAY..!"
    #  requests.post(t_url) 
    asyncio.run(bot.send_message(chat_id=channel_id,text="======================\n"+nowTime+"\n======================"+"\nWELCOME TO GOD LEVEL TRADING"+"\n======================"+"\nBOT STARTED SUCCESSFULLY..!"+"\n======================\n"+"TODAY's GOD LEVELS\n"+"======================\n"+"NIFTY RES LEVEL: "+str(nse_ce_levels)+"\n"+"=========================\n"+"NIFTY SUP LEVEL: "+str(nse_pe_levels)+"\n"+"=========================\n"+"BNF RES LEVEL: "+str(bnf_ce_levels)+"\n=========================\n"+"BNF SUP LEVEL: "+str(bnf_pe_levels)+"\n=========================\n"+"NOTE : ONLY FOR EDUCATIONAL PURPOSE.\n"+"=========================\n"+"TRADE ONLY BTW 12:30 PM - 3:15 PM"+"\n----------------------------"+"\nI AM NOT SEBI REG..!"+"\n------------------------------"+"\nTRADE AT YOUR OWN RISK..!"+"\n----------------------------\n"+"WISH YOU PROFITABLE DAY..!"+"\n------------------------------"))
c = datetime.now()
runTm = c.strftime('%H:%M:%S')

#Keep Running below code from 9AM to 3PM
if intTime >= 21 and intTime < 22:
        while(intTime<23 ):
            if intTime>23:
                break;
            c = datetime.now()
            runTime = c.strftime('%H:%M:%S')
            print("Nifty CE Levels : ",nse_ce_levels)
            print("Nifty PE Levels : ",nse_pe_levels)
            print("BNF CE Levels : ",bnf_ce_levels)
            print("BNF PE Levels : ",bnf_pe_levels)
            nifty_ce_minus_range = nse_ce_levels - 10 
            print("Nifty CE minus range : ",nifty_ce_minus_range)
            nifty_ce_plus_range = nse_ce_levels + 5
            print("Nifty CE plus range : ", nifty_ce_plus_range)

            nifty_pe_minus_range = nse_pe_levels - 5 
            print("Nifty PE minus range : ",nifty_pe_minus_range)
            nifty_pe_plus_range = nse_ce_levels + 10
            print("Nifty PE plus range : ", nifty_pe_plus_range)

            bnf_ce_minus_range = bnf_ce_levels - 10 
            print("Bnf CE minus range : ",bnf_ce_minus_range)
            bnf_ce_plus_range = bnf_ce_levels + 10
            print("Bnf CE plus range : ", bnf_ce_plus_range)

            bnf_pe_minus_range = bnf_pe_levels - 10 
            print("Bnf PE minus range : ",bnf_pe_minus_range)
            bnf_pe_plus_range = bnf_pe_levels + 10
            print("Bnf PE plus range : ", bnf_pe_plus_range)

            # Method to get nearest strikes
            def round_nearest(x, num=50): return int(math.ceil(float(x)/num)*num)
            def nearest_strike_bnf(x): return round_nearest(x, 100)
            def nearest_strike_nf(x): return round_nearest(x, 50)


            # Urls for fetching Data
            url_oc = "https://www.nseindia.com/option-chain"
            url_bnf = 'https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY'
            url_nf = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'
            #url_finNif = 'https://www.nseindia.com/api/option-chain-indices?symbol=FINNIFTY'
            url_indices = "https://www.nseindia.com/api/allIndices"

            # Headers
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                    'accept-language': 'en,gu;q=0.9,hi;q=0.8',
                    'accept-encoding': 'gzip, deflate, br'}

            sess = requests.Session()
            cookies = dict()

        # Local methods

            def set_cookie():
                request = sess.get(url_oc, headers=headers, timeout=60)
                cookies = dict(request.cookies)


            def get_data(url):
                set_cookie()
                response = sess.get(url, headers=headers, timeout=60, cookies=cookies)
                if (response.status_code == 401):
                    set_cookie()
                    response = sess.get(url_nf, headers=headers,
                                        timeout=60, cookies=cookies)
                if (response.status_code == 200):
                    return response.text
                return ""


            def set_header():
                global bnf_ul
                global nf_ul
                global bnf_nearest
                global nf_nearest
                response_text = get_data(url_indices)
                data = json.loads(response_text)
                for index in data["data"]:
                    if index["index"] == "NIFTY 50":
                        nf_ul = index["last"]
                        print("nifty")
                    if index["index"] == "NIFTY BANK":
                        bnf_ul = index["last"]
                        print("banknifty")
                bnf_nearest = nearest_strike_bnf(bnf_ul)
                nf_nearest = nearest_strike_nf(nf_ul)


            # Showing Header in structured format with Last Price and Nearest Strike
            # def print_header(index="", ul=0, nearest=0):
            #     print(strPurple(index.ljust(12, " ") + " => ") + strLightPurple(" Last Price: ") +
            #         strBold(str(ul)) + strLightPurple(" Nearest Strike: ") + strBold(str(nearest)))


            # def print_hr():
            #     print(strYellow("|".rjust(70, "-")))

            def send_lastprice():
                global nf_ul
                global nf_nearest
                response_text = get_data(url_indices)
                data = json.loads(response_text)
                nf_nearest = 0
                nf_ul = 0
                for index in data["data"]:
                    if index["index"] == "NIFTY 50":
                        nf_ul = index["last"]
                        #print(nf_ul)
                        nf_nearest = nearest_strike_nf(nf_ul)
                return nf_ul

            def send_Bnflastprice():
                global bnf_ul
                global bnf_nearest
                response_text = get_data(url_indices)
                data = json.loads(response_text)
                bnf_nearest = 0
                bnf_ul = 0
                for index in data["data"]:
                    if index["index"] == "NIFTY BANK":
                        bnf_ul = index["last"]
                        #print(bnf_ul)
                        bnf_nearest = nearest_strike_bnf(bnf_ul)
                return bnf_ul

            #print_header("Nifty", nf_ul, nf_nearest)
            print("NIFTY CMP : ",send_lastprice())
            print("BNF CMP : ",send_Bnflastprice())
            counter= counter+1
            niftyLastPrice = int(send_lastprice())
            bnfLastPrice = int(send_Bnflastprice())
            print("Run Time : ", runTime)
            print("Counter : ", counter)
        

            if(niftyLastPrice in range(nse_ce_levels, nse_pe_levels) and niftyLastPrice in range(nifty_ce_plus_range, nifty_ce_plus_range)):
                #t_url = "https://api.telegram.org/bot6377307246:AAEuJAlBiQgDQEa03yNmKQJmZbXyQ0WINOk/sendMessage?chat_id=-996001230&text="+"======================\n"+dt[0]+"-"+runTime+"\n======================\n"+"PYTHON-BOT FOR TODAY's LEVELS\n"+"======================\n"+"NIFYT CMP : "+str(niftyLastPrice)+"\n======================\n"+"NIFTY TRADING NEAR BO LEVEL: "+str(nifty_ce_plus_range)+"\n"+"\n=========================\n"+"CHOOSE STRIKE : "+str(nearest_strike_nf(nf_ul))+"\n=========================\n"+"NOTE : ONLY FOR EDUCATIONAL PURPOSE.\n"+"---------------------------------\n"+"I AM NOT SEBI REG..!"+"\n----------------------------------"+"\nTRADE AT YOUR OWN RISK..!"
                #requests.post(t_url)
                asyncio.run(bot.send_message(chat_id=channel_id,text="======================\n"+dt[0]+"-"+runTime+"\n======================\n"+"AI-BOT FOR TODAY's GOD LEVELS\n"+"======================\n"+"NIFTY CMP : "+str(niftyLastPrice)+"\n======================\n"+"NIFTY TRADING NEAR RES LEVEL: "+str(nifty_ce_plus_range)+"\n"+"\n=========================\n"+"CHOOSE STRIKE : "+str(nearest_strike_nf(nf_ul))+"\n=========================\n"+"NOTE : ONLY FOR EDUCATIONAL PURPOSE.\n"+"=========================\n"+"TRADE BTW 12:30 PM - 3:15 PM"+"\n---------------------------------\n"+"I AM NOT SEBI REG..!"+"\n----------------------------------"+"\nTRADE AT YOUR OWN RISK..!"))

            if(niftyLastPrice in range(nse_ce_levels, nse_pe_levels) and niftyLastPrice in range(nifty_pe_plus_range, nifty_pe_plus_range)):
                #t_url = "https://api.telegram.org/bot6377307246:AAEuJAlBiQgDQEa03yNmKQJmZbXyQ0WINOk/sendMessage?chat_id=-996001230&text="+"======================\n"+dt[0]+"-"+runTime+"\n======================\n"+"PYTHON-BOT FOR TODAY's LEVELS\n"+"======================\n"+"NIFYT CMP : "+str(niftyLastPrice)+"\n======================\n"+"NIFTY TRADING NEAR BO LEVEL: "+str(nifty_pe_minus_range)+"\n"+"\n=========================\n"+"CHOOSE STRIKE : "+str(nearest_strike_nf(nf_ul))+"\n=========================\n"+"NOTE : ONLY FOR EDUCATIONAL PURPOSE.\n"+"-----------------------------------\n"+"I AM NOT SEBI REG..!"+"\n---------------------------------"+"\nTRADE AT YOUR OWN RISK..!"
                #requests.post(t_url)
                asyncio.run(bot.send_message(chat_id=channel_id,text="======================\n"+dt[0]+"-"+runTime+"\n======================\n"+"AI-BOT FOR TODAY's GOD LEVELS\n"+"======================\n"+"NIFTY CMP : "+str(niftyLastPrice)+"\n======================\n"+"NIFTY TRADING NEAR SUP LEVEL: "+str(nifty_pe_minus_range)+"\n"+"\n=========================\n"+"CHOOSE STRIKE : "+str(nearest_strike_nf(nf_ul))+"\n=========================\n"+"NOTE : ONLY FOR EDUCATIONAL PURPOSE.\n"+"=========================\n"+"TRADE BTW 12:30 PM - 3:15 PM"+"-----------------------------------\n"+"I AM NOT SEBI REG..!"+"\n---------------------------------"+"\nTRADE AT YOUR OWN RISK..!"))
        

            if(bnfLastPrice in range(bnf_ce_levels, bnf_pe_levels) and bnfLastPrice in range(bnf_ce_plus_range, bnf_ce_plus_range)):
                #t_url = "https://api.telegram.org/bot6377307246:AAEuJAlBiQgDQEa03yNmKQJmZbXyQ0WINOk/sendMessage?chat_id=-996001230&text="+"======================\n"+dt[0]+"-"+runTime+"\n======================\n"+"PYTHON-BOT FOR TODAY's LEVELS\n"+"======================\n"+"NIFYT CMP : "+str(bnfLastPrice)+"\n======================\n"+"NIFTY TRADING NEAR BO LEVEL: "+str(bnf_ce_plus_range)+"\n"+"\n=========================\n"+"CHOOSE STRIKE : "+str(nearest_strike_nf(bnf_ul))+"\n=========================\n"+"NOTE : ONLY FOR EDUCATIONAL PURPOSE.\n"+"---------------------------------\n"+"I AM NOT SEBI REG..!"+"\n----------------------------------"+"\nTRADE AT YOUR OWN RISK..!"
                #requests.post(t_url)
                asyncio.run(bot.send_message(chat_id=channel_id,text="======================\n"+dt[0]+"-"+runTime+"\n======================\n"+"AI-BOT FOR TODAY's GOD LEVELS\n"+"======================\n"+"BNF CMP : "+str(bnfLastPrice)+"\n======================\n"+"BNF TRADING NEAR RES LEVEL: "+str(bnf_ce_plus_range)+"\n"+"\n=========================\n"+"CHOOSE STRIKE : "+str(nearest_strike_nf(bnf_ul))+"\n=========================\n"+"NOTE : ONLY FOR EDUCATIONAL PURPOSE.\n"+"=========================\n"+"TRADE BTW 12:30 PM - 3:15 PM"+"---------------------------------\n"+"I AM NOT SEBI REG..!"+"\n----------------------------------"+"\nTRADE AT YOUR OWN RISK..!"))

            if(bnfLastPrice in range(bnf_ce_levels, bnf_pe_levels) and bnfLastPrice in range(bnf_pe_plus_range, bnf_pe_plus_range)):
            #t_url = "https://api.telegram.org/bot6377307246:AAEuJAlBiQgDQEa03yNmKQJmZbXyQ0WINOk/sendMessage?chat_id=-996001230&text="+"======================\n"+dt[0]+"-"+runTime+"\n======================\n"+"PYTHON-BOT FOR TODAY's LEVELS\n"+"======================\n"+"NIFYT CMP : "+str(bnfLastPrice)+"\n======================\n"+"NIFTY TRADING NEAR BO LEVEL: "+str(bnf_pe_minus_range)+"\n"+"\n=========================\n"+"CHOOSE STRIKE : "+str(nearest_strike_nf(bnf_ul))+"\n=========================\n"+"NOTE : ONLY FOR EDUCATIONAL PURPOSE.\n"+"-----------------------------------\n"+"I AM NOT SEBI REG..!"+"\n---------------------------------"+"\nTRADE AT YOUR OWN RISK..!"
            #requests.post(t_url)
                asyncio.run(bot.send_message(chat_id=channel_id,text="======================\n"+dt[0]+"-"+runTime+"\n======================\n"+"AI-BOT FOR TODAY's GOD LEVELS\n"+"======================\n"+"BNF CMP : "+str(bnfLastPrice)+"\n======================\n"+"BNF TRADING NEAR SUP LEVEL: "+str(bnf_pe_minus_range)+"\n"+"\n=========================\n"+"CHOOSE STRIKE : "+str(nearest_strike_nf(bnf_ul))+"\n=========================\n"+"NOTE : ONLY FOR EDUCATIONAL PURPOSE.\n"+"=========================\n"+"TRADE BTW 12:30 PM - 3:15 PM"+"-----------------------------------\n"+"I AM NOT SEBI REG..!"+"\n---------------------------------"+"\nTRADE AT YOUR OWN RISK..!"))

        
            time.sleep(120)

if(intTime>=15):
    print("PROGRAM EXIT AT : ", runTm)
    exit()