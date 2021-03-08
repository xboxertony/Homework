import requests
import json
r = requests.get("https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json")
data = json.loads(r.text)
data = data["result"]["results"]
myfile = open("data.txt","w",encoding="utf-8")
# l = len(data["result"]["results"])
for i in range(len(data)):
    s = data[i]["stitle"]+","+data[i]["longitude"]+","+data[i]["latitude"]+","
    n = float("inf")
    if ".jpg" in data[i]["file"]:
        n = min(n,data[i]["file"].find(".jpg")+4)
    if ".JPG" in data[i]["file"]:
        n = min(n,data[i]["file"].find(".JPG")+4)
    if ".png" in data[i]["file"]:
        n = min(n,data[i]["file"].find(".png")+4)
    s+=data[i]["file"][:n]+"\n"
    myfile.writelines(s)
myfile.close()