import csv
import os
#for your convenience
import sys

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}



	
csvpath1 = 'raw_data/employee_data1.csv'

csvpath2 = 'raw_data/employee_data2.csv'
outPath = "output.txt"
csvSet = [csvpath1, csvpath2]
if(len(sys.argv)>1):
	csvSet = []
	for i, val in enumerate(sys.argv):
		if(i==0):
			continue
		elif i <len(sys.argv)-1:
			csvSet.append(val)
		else:
			outPath = val
			
#keep an index list for easier lookup
separateIndex = []


with open(outPath,'w',newline='') as outputFile:
	csvwriter = csv.writer(outputFile, delimiter=',')
	
	headerRow = ['Emp ID','First Name','Last Name','DOB','SSN','State']
	csvwriter.writerow(headerRow)
	
	#how many additional dates we talking?
	for additionalPath in csvSet:
		with open(additionalPath, newline='') as inputFile:
			
			
			csvreader = csv.reader(inputFile, delimiter=',')
			#kill the header
			next(csvreader)
			
			for data_row in csvreader:
				outputRow = []
				outputRow.append(int(data_row[0]))
				if(outputRow[0] in separateIndex):
					continue
				separateIndex.append(outputRow[0])
				
				nameList = data_row[1].split(' ',1)
				outputRow.append(nameList[0])
				outputRow.append(nameList[-1])
				
				dateSplit = data_row[2].split('-',2)
				outputRow.append(dateSplit[1]+'/'+dateSplit[2]+'/'+dateSplit[0])
				
				outputRow.append('***-**-'+data_row[3][-4:])
				
				outputRow.append(us_state_abbrev[data_row[4]])
				
				csvwriter.writerow(outputRow)
				
