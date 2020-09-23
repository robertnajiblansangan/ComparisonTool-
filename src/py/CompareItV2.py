from datetime import datetime

import deepdiff
import pandas as pd
from UnwantedDataFilter import filterDict
from XMLFileExtractor import extractXml

PSA2_FOLDER_PATH = '../../PSA2'
PSA_FOLDER_PATH = '../../PSA'

# Extract XML Files and convert it to Dictionary (CntrNumber will be the key)

newTliDataDict = extractXml(PSA_FOLDER_PATH)
oldTliDataDict = extractXml(PSA2_FOLDER_PATH)

# Remove unmatched Container number for data dict.

newTliDataFinalDict = filterDict(newTliDataDict, oldTliDataDict)
oldTliDataFinalDict = filterDict(oldTliDataDict, newTliDataDict)

# Compare the two dictionary and Generate Excel for found Discrepancy

diff = deepdiff.DeepDiff(oldTliDataFinalDict, newTliDataFinalDict)
# print(json.dumps(json.loads(diff.to_json()), indent=4))

#Export discrepancy Dictionary to Excel

today = datetime.now()
dateAndTimeToday = today.strftime("%d-%m-%Y %H_%M_%S")

df = pd.DataFrame.from_dict(diff.get('values_changed'), orient='index') # convert dict to dataframe
df.to_csv('../../DISCREPANCIES/'+dateAndTimeToday+'.csv')

print (df)