import os
from ocr_core import checkConf

directory = 'images'
recgCount = 0
totalCount = 0
print("Total dates encountered: ",totalCount)
for filename in os.listdir(directory):
    text = checkConf('{}'.format(os.path.join(directory, filename)))
    #print(filename,text)
    text_list = text.split(" ")
    totalCount += 1
    if totalCount%100 == 0:
       print(totalCount)
    for word in text_list:
       if word == "recognized":
          recgCount += 1

conf = (recgCount/totalCount)*100

print("Date Recognition Confidence: ", conf)
