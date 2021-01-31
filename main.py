from plyer import notification
import requests
from bs4 import BeautifulSoup
import datetime

def notify(title,message):
    notification.notify(title = title,
    message = message,
    app_icon = "coronavirus_image.ico",
    timeout = 20)


def getdata(url):
    r=requests.get(url)
    return r.text

if __name__ == '__main__':
   #notify("Vicky","WELCOME BACK")
    htmldata=getdata("https://www.mohfw.gov.in/")
    soup=BeautifulSoup(htmldata,'html.parser')

    mydata=""
    mydata+=soup.find(id="site-dashboard").get_text()
    final_words=[]
    l1=[]
    mydata=mydata[5:].split(" ")


    final_words1=mydata[15]
    the1=final_words1.replace("\xa0","")
    the_1=the1.split("\n")

    final_words2=mydata[19]
    the2=final_words2.replace("\xa0","")
    the_2=the2.split("\n")

    final_words3=mydata[34]
    the3 = final_words3.replace("\xa0", "")
    the_3 = the3.split("\n")


    for v in final_words:
        l1.append(v.strip())


    x = datetime.datetime.now()
    date = f'({x.day} {x.strftime("%b")} {x.year})'

    ntitle=f"COVID-19 CASES {date}"
    ntext=f"Active Cases- {the_1[1]}\nDischarged- {the_2[1]}\nTotal Vaccinated- {the_3[0]}"
    notify(ntitle,ntext)



















































