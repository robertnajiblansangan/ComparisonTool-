import json
import array

with open("PSA-out/PSANEWSAMPLE.xml.json", "r") as read_file:
    newTLIjsonData = json.load(read_file)

with open("PSA2-out/PSAOLDSAMPLE.xml.json", "r") as read_file:
	oldTLIjsonData = json.load(read_file)


arrNewContainerNumbers = []
arrOldContainerNumbers = []

hashNewTliData = {}
hashOldTliData = {}

#Get All Container numbers from NEW TLI
for item in newTLIjsonData['Message-PSACOPRAR']['GroupRecord-Container_Group']['Message-PSACOPRAR']['GroupRecord-Container_Group']:
	newContainerNumber = item['Record-ContainerRec']['Field-CntNo']['#text']
	arrNewContainerNumbers.append(newContainerNumber)

#Get All Container numbers from OLD TLI
for item in oldTLIjsonData['Message-PSACOPRAR']['GroupRecord-Container_Group']['Message-PSACOPRAR']['GroupRecord-Container_Group']:
	oldContainerNumber = item['Record-ContainerRec']['Field-CntNo']['#text']
	arrOldContainerNumbers.append(oldContainerNumber)


# Remove all unmatched SVVD in OLD TLI
for item in oldTLIjsonData['Message-PSACOPRAR']['GroupRecord-Container_Group']['Message-PSACOPRAR']['GroupRecord-Container_Group']:
	oldContainerNumber = item['Record-ContainerRec']['Field-CntNo']['#text']
	if oldContainerNumber in arrNewContainerNumbers:
		hashOldTliData[oldContainerNumber] = item

# Remove all unmatched SVVD in NEW TLI
for item in newTLIjsonData['Message-PSACOPRAR']['GroupRecord-Container_Group']['Message-PSACOPRAR']['GroupRecord-Container_Group']:
	newContainerNumber = item['Record-ContainerRec']['Field-CntNo']['#text']
	if newContainerNumber in arrOldContainerNumbers:
		hashNewTliData[newContainerNumber] = item

open("PSA-out/PSANewSamplefinal.xml", "w")

f = open("PSA-out/PSANewSamplefinal.xml", "a+")
for value in sorted(hashNewTliData.items()):
	f.write(json.dumps(value, indent=4, sort_keys=True) + ",\n")


open("PSA2-out/PSAOldSamplefinal.xml", "w")

f = open("PSA2-out/PSAOldSamplefinal.xml", "a+")
for value in sorted(hashOldTliData.items()):

	f.write(json.dumps(value, indent=4, sort_keys=True) + ",\n")