# Get All Container numbers from inputed XML File

def extractJson(jsonData):
    cntrGroupRecDict = {}
    for item in jsonData['Message-PSACOPRAR']['GroupRecord-Container_Group']:
        try:
            cntrNum = item['Record-ContainerRec']['Field-CntNo']
            cntrGroupRecDict[cntrNum] = item['Record-ContainerRec']
        except:
            print("Exception Occured in JsonExtractor")
    return cntrGroupRecDict
