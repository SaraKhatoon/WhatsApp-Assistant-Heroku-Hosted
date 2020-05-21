from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import datetime
from datetime import datetime, timedelta
from calendar import monthrange
import json
import requests

from f0 import *
from f1 import *
from f2 import *
from f3 import *
from f4 import *
from f5 import *
from f6 import *
from f7 import *
from f8 import *
from f9 import *
 
app= Flask(__name__)


@app.route("/")
def hello():
    return "hello world !!!"


@app.route("/calci",methods=['POST', 'GET'])
def calci(msg):
    maths = msg
    ans=''
    if maths.find('+')!=-1:
        numbers=maths.split('+')
        num1=int(numbers[0].strip())
        num2=int(numbers[1].strip())
        ans=str(num1+num2)
    elif maths.find('-')!=-1:
        numbers=maths.split('-')
        num1=int(numbers[0].strip())
        num2=int(numbers[1].strip())
        ans=str(num1-num2)
    elif maths.find('*')!=-1:
        numbers=maths.split('*')
        num1=int(numbers[0].strip())
        num2=int(numbers[1].strip())
        ans=str(num1*num2)
    elif maths.find('/')!=-1:
        numbers=maths.split('/')
        num1=int(numbers[0].strip())
        num2=int(numbers[1].strip())
        if num2==0:
            ans="DBZ error"
        else:
            ans=str(num1/num2)
    else:
        ans='invalid input!!'
    print(ans)
    return ans


@app.route("/sms",methods=['POST'])
def sms_reply():
    msg=request.form.get('Body')
    if msg.find('+') != -1 or msg.find('-')!= -1 or msg.find('*')!= -1 or msg.find('/') !=-1:
        ans = calci(msg)
        print(ans)
        resp=MessagingResponse()
        resp.message("{}".format(ans))
        return str(resp)
    
    elif msg[0:2] == "@1":
        # to check if user wants feature 1
        if msg.find("today's date") != -1:
            print("f1")
            date=calender_f1()
            print(date)
            resp=MessagingResponse()
            resp.message("{}".format(date))
            return str(resp)

        # to check if user wants feature 2
        elif msg.find("tomorrow's date") != -1:
            date1=calender_f2()
            print(date1)
            resp=MessagingResponse()
            resp.message("{}".format(date1))
            return str(resp)

        # to check if user wants feature 3
        elif msg.find("isleap") != -1:
            res=calendar_f3(msg)
            print(res)
            resp=MessagingResponse()
            resp.message("{}".format(res))
            return str(resp)

        elif msg.find("days in the month of year") != -1:
            days=calendar_f4(msg)
            print(days)
            resp=MessagingResponse()
            resp.message("{}".format(days))
            return str(resp)
        elif msg.find("islamic year") != -1:
            days=calendar_f5(msg)
            print(days)
            resp=MessagingResponse()
            resp.message("{}".format(days))
            return str(resp)

    elif msg[0:2] == "@5":
        bmic = bmi_f15(msg)
        print(bmic)
        resp=MessagingResponse()
        resp.message("{}".format(bmic))
        return str(resp)

    elif msg[0:2] == "@2":
        segments = msg.split()
        
        if len(segments) == 3:
            subject=segments[1]
            module=segments[2]
            modwise=syllabus_m(subject,module)
            print(modwise)
            resp=MessagingResponse()
            resp.message("{}".format(modwise))
            return str(resp)
            
        else:    
            subject=segments[1]

            sub=syllabus_f2(subject)
            print(sub)
            resp=MessagingResponse()
            resp.message("{}".format(sub))
            return str(resp)   

    elif msg[0:2] == "@4" :
        if msg.find("top news") != -1:
            mydata = news_f1()
            print(mydata)
            resp=MessagingResponse()
            resp.message("{}".format(mydata))
            return str(resp)
        elif msg.find("top headlines") != -1:
            mydata = news_f2()
            print(mydata)
            resp=MessagingResponse()
            resp.message("{}".format(mydata))
            return str(resp)
        else:
            resp=MessagingResponse()
            resp.message("Type either\n\n*1)@2 top news* or\n*2)@2 latest news*")
            return str(resp)

    elif msg[0:2] == "@6" :
        if msg.find("today's weather")!= -1:
            mywet = weather1()
            print(mywet)
            resp=MessagingResponse()
            resp.message("{}".format(mywet))
            return str(resp)

    elif msg[0:2] == "@3":
        if msg.find("covid update")!= -1:
            covid = corona()
            print(covid)
            resp=MessagingResponse()
            resp.message("{}".format(covid))
            return str(resp)

    elif msg[0:2] == "@7":
        if msg.find("crack a joke")!= -1:
            jk = jokes()
            print(jk)
            resp=MessagingResponse()
            resp.message("{}".format(jk))
            return str(resp)

    elif msg[0:2] == "@8":
        if msg.find("quote")!= -1:
            qt = quotes()
            print(qt)
            resp=MessagingResponse()
            resp.message("{}".format(qt))
            return str(resp)

    elif msg[0:2] == "@9":
        if msg.find("namaz timings")!= -1:
            timings = namaz()
            print(timings)
            resp=MessagingResponse()
            resp.message("{}".format(timings))
            return str(resp)

    elif msg[0:2] == "@0":
        if msg.find("What can you do ?") != -1: 
            bot=dummy(msg) 
            print(bot)
            resp=MessagingResponse()
            resp.message("{}".format(bot))
            return str(resp)

    else:
        bot=""" *You Typed Wrong, Try :* \n
           @1 today's date \n
            @1 tomorrow's date \n
            @1 isleap \n
            @1 days in the month of year *month numer* *year* \n
            @1 islamic year *year* \n
            @2 *subject_name* \n
            @2 *subject_name* *module number* \n
            @3 covid update \n
            @4 top news \n
            @4 top headlines \n
            @5 *weight in kg* *height in cm* \n
            @6 today's weather \n
            @7 crack a joke \n
            @8 quote \n
            @9 namaz timings \n
            For Calculator, directly give the values
            ----------------------------------------------

        """
        print(bot)
        resp=MessagingResponse()
        resp.message("{}".format(bot))
        return str(resp)
    

    return ""

if __name__=="__main__":
    app.run(debug=True)

