from requests import get
import datetime


PublicIP = get("https://api.ipify.org").text

FullDate = datetime.datetime.now()

LogsFile = open("logs.txt", "a")
LogsFile.writelines("["+FullDate.strftime("%d")+"/"+FullDate.strftime("%m")+"/"+FullDate.strftime("%y")+"|"+FullDate.strftime("%X")+"]"+" "+PublicIP+"\n")
LogsFile.close()

