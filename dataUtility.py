# reads and writes data
import datetime
import json
import os.path


# priceFile = "prices"
# transactionFile = "transactions"
# assetsFile = "assets"

#should accept fileType as one of the above
#dataToWrite should be a responseJson
def writeToFile(fileType, dataToWrite):
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    path = fileType + date

    if os.path.isfile(path):
        f = open(path,"a+")
    else:
        f = open(path, "w+")
        f.write(fyleType)
        f.write("\n")
        f.write(date)
        f.write("\n\n")

    if (is_json(dataToWrite)):
        currentTime = now.strftime("%H-%M-%S")
        f.write(currentTime)
        f.write("\n")
        f.write(dataToWrite)
        f.write("\n")

    f.close()



    
def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError, e:
    # try a dump and load in the case its an json_object

    return False
  return True
