import requests
import json
r = requests.get("https://data.taipei/api/v1/dataset/36847f3f-deff-4183-a5bb-800737591de5?scope=resourceAquire")
data = json.loads(r.text)
data = data["result"]["results"]
myfile = open("data.txt","w",encoding="utf-8")
# l = len(data["result"]["results"])
for i in range(len(data)):
    s = ""
    if ".jpg" in data[i]["file"]:
        s += data[i]["stitle"]+","+data[i]["longitude"]+","+data[i]["latitude"]+","+data[i]["file"][:data[i]["file"].find(".jpg")+4]+"\n"
    elif ".JPG" in data[i]["file"]:
        s += data[i]["stitle"]+","+data[i]["longitude"]+","+data[i]["latitude"]+","+data[i]["file"][:data[i]["file"].find(".JPG")+4]+"\n"
    else:
        s += data[i]["stitle"]+","+data[i]["longitude"]+","+data[i]["latitude"]+","+data[i]["file"][:data[i]["file"].find(".png")+4]+"\n"
    myfile.writelines(s)
myfile.close()