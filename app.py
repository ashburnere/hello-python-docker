from flask import Flask
import os
import socket
import datetime
import sys

visitCount = 0
# log the start time of the app
f = open("app.log", "a")
startLogText = str(datetime.datetime.now()) + " Started Python web app! Installed Python version is " + str(sys.version) + "\n"
f.write(startLogText) 
f.close()
print("logging to stdout: " + startLogText)

app = Flask(__name__)

@app.route("/")
def hello():
    # increment the global visit count and log the message
    global visitCount
    visitCount += 1
    currentTime = datetime.datetime.now()
    f = open("app.log", "a")
    logText=str(currentTime) + " New request received (total visits " + str(visitCount) + ")\n"
    f.write(logText)
    f.close()
    print("DEBUG TO STDOUT: " + logText)

    html = "<h3>Hello {name}!</h3>" \
	   "<h3>{started}</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Current time:</b> {currentTime}<br/>" \
           "<b>Visits:</b> {visitCount}"
    return html.format(name=os.getenv("NAME", "world"), started=startLogText, hostname=socket.gethostname(), currentTime=currentTime, visitCount=visitCount)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
