import requests
import datetime
date = datetime.datetime.now().strftime("%m-%d-%Y | %X")
url = "http://192.168.78.133/remote.php/dav/files/gabe/"
headers = {
    'Authorization': "Basic Z2FiZToxMjM0NTY=",
    'Content-Type': "text/plain",
    'User-Agent': "PostmanRuntime/7.18.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "86267886-47de-47e9-9fc8-235a46c72f16,a6a8f829-3d64-4635-9221-090742a8fa43",
    'Host': "192.168.78.133",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "5",
    'Cookie': "ocf8gjmzz8vc=f2b802e61ffcd08489ea684bac74d956; oc_sessionPassphrase=LvHNQkArvf1Ww9w7eMq1pR1lqQJ4QDOhpvywF1znt2HEGKF%2BW6Pnq80%2Bmoj5tZG5fF9r5%2BlyflUffaSXCNZ774lLYGY8ll9Acd8NgorJCVBhcjKzykJSD0Wf2DvhgX1n; nc_sameSiteCookielax=true; nc_sameSiteCookiestrict=true",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }


def videoUpload():
    url = "http://192.168.78.133/remote.php/dav/files/gabe/"+ date  +".mp4"
    payload = open("Microcontrollers\'s project_Medium.mp4",'rb')
    response = requests.request("PUT", url, data=payload, headers=headers)
    if(response.status_code != 200):
        return False
    else:
        return True

def logUpload():
    return True
