import csv
import os
#for your convenience
import sys

def getIndex(dateString):
	months={'Jan':0,'Feb':1,'Mar':2,'Apr':3,'May':4,'Jun':5,'Jul':6,'Aug':7,'Sep':8,'Oct':9,'Nov':10,'Dec':11}
	
	stringParts = dateString.split('-')
	year = int(stringParts[1])*100
	month = months[stringParts[0]]
	return year+month
	
def getYearMonthPair(codedValue):
	months={'Jan':0,'Feb':1,'Mar':2,'Apr':3,'May':4,'Jun':5,'Jul':6,'Aug':7,'Sep':8,'Oct':9,'Nov':10,'Dec':11}
	month = int(codedValue%100)
	year = int(codedValue/100)
	stringMonth = 'Jan'
	for access in months.keys():
		if(months[access]==month):
			stringMonth = access
	return stringMonth + '-' + str(year%100)


	
csvpath1 = 'raw_data/budget_data_1.csv'

csvpath2 = 'raw_data/budget_data_2.csv'
outPath = "output.txt"
csvSet = [csvpath2]
if(len(sys.argv)>1):
	csvSet = []
	for i, val in enumerate(sys.argv):
		if(i==0):
			continue
		elif i==1:
			csvpath1 = val
		elif i <len(sys.argv)-1:
			csvSet.append(val)
		else:
			outPath = val
			
aggregate = []
#keep an index list for easier lookup
separateIndex = []
separateValue = []
with open(csvpath1, newline='') as csvfile1:
	
	
	csvreader = csv.reader(csvfile1, delimiter=',')
	
	next(csvreader)
	
	for data_row in csvreader:
		pair = [getIndex(data_row[0]),int(data_row[1])]
		aggregate.append(pair)
		separateIndex.append( pair[0])
		separateValue.append(pair[1])

#how many additional dates we talking?
for additionalPath in csvSet:
	with open(additionalPath, newline='') as csvfile2:
		
		
		csvreader = csv.reader(csvfile2, delimiter=',')
		
		next(csvreader)
		
		for data_row in csvreader:
			pair = [getIndex(data_row[0]),int(data_row[1])]
			#if separate values. or files weren't fed in youngest first
			if(pair[0] in separateIndex):
				oldLoc = separateIndex.index(pair[0])
				aggregate[oldLoc][1]+=pair[1]
				separateValue[oldLoc]+=pair[1]
			else:	
				aggregate.append(pair)
				separateIndex .append( pair[0])
				separateValue .append( pair[1])
#we have all of our information. need to: sort all of it.
aggregate.sort(key=lambda x: x[0])
#that was easy...



totalMonths = len(aggregate)

maxVal = max(separateValue)
maxDate = separateIndex[separateValue.index(maxVal)]

minVal = min(separateValue)
minDate = separateIndex[separateValue.index(minVal)]

avgDif = (aggregate[-1][1]-aggregate[0][1])/float(totalMonths)

longTotal = sum(separateValue)

stringBuilding = 'Financial Analysis' + os.linesep
stringBuilding = stringBuilding + '------------------------' + os.linesep
stringBuilding = stringBuilding + 'Total Months: ' + str(totalMonths)+os.linesep
stringBuilding = stringBuilding + 'Total Revenue: $'+str(longTotal) + os.linesep
stringBuilding = stringBuilding + 'Average Revenue Change: $'+str(avgDif)+os.linesep
stringBuilding = stringBuilding + 'Greatest Increase in Revenue: '+ getYearMonthPair(maxDate)+ ' ($'+str(maxVal)+')'+os.linesep
stringBuilding = stringBuilding + 'Greatest Decrease in Revenue: '+ getYearMonthPair(minDate)+ ' ($'+str(minVal)+')'+os.linesep
print(stringBuilding)


with open(outPath,'w',newline='') as outputFile:
	outputFile.write(stringBuilding)
	



