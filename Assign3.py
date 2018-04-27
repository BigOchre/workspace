import pandas as pd
import matplotlib.pyplot as pop
import numpy as np
import csv

#widths to look for
codes = [5,15,5,15,2,4,1,1,1,1,1,1,10,4,6,6,6,6,6,6,6,6,6]
heads=['SU_UIC','SU_NAME','M_CMD_UIC','M_CMD_NAME',
	'WPN_CODE','WPN-DENSITY','MISSION_CODE','INTENSITY_CODE',
	'TERRAIN_CODE','TARGET_FIRE','WEATHER_CODE','DAY/NIGHT','DATE',
	'RNDS_1_EXPENDED','RNDS_2_EXPENDED','RNDS_3_EXPENDED',
	'RNDS_4_EXPENDED','RNDS_5_EXPENDED','RNDS_6_EXPENDED',
	'RNDS_7_EXPENDED','RNDS_8_EXPENDED','RNDS_9_EXPENDED',]
#read data files
data_in = []

def readData(file):
	with open(file, "r") as ins:
		for line in ins:
			data_in.append(line)
	#print("file: " + file + " read")

readData("RG338.COLEDV.AM68")
readData("RG338.COLEDV.AM69")
readData("RG338.COLEDV.AM70")

#consolidate files
outputList = []
 
for line in data_in:
    idx = 0
    lineList = []
    for i in codes:
        upper = idx+i
        lineList.append(line[idx:upper])
        idx = upper
    outputList.append(lineList)

data_out = []

#turn some strings into integers and get rid of that conspiracy theory col

for oplist in outputList:
  row = []	
  for x in range(4):
    row.append(oplist[x].strip())
  for x in range(4,12):
    row.append(int(oplist[x]))
  for x in range(13,23):
    row.append(int(oplist[x]))
  data_out.append(row)

#print("data consolidated")

#write csv file
#output_csv = open('output.csv','w+', newline ='')
#writer = csv.writer(output_csv, delimiter=',')
#writer.writerows(data_out)
#output_csv.close()
#print("file created")

df = pd.DataFrame(data_out, columns = heads)

print("assign3 finished");
#year 1st battalion, 40th field artillery used most 105mm HE
#what day, or list of days did 1st/40th report most ammunition
#how many times did bat report ammunition expeditures under heavy firing intensity/light?