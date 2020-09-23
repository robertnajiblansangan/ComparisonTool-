def filterDicts(dataDict, comparingDataDict):
    toReturnDataDict = {}
    for key in dataDict:
        if key in comparingDataDict:
            toReturnDataDict[key] = dataDict.get(key)
    return toReturnDataDict
