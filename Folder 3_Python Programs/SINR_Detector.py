import csv

mysum = 0
interval = 0.1
lastVal = 0.0
with open('resultsSinr.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
    with open('RxPacketTrace.txt','r') as f:
    	for (i, line) in enumerate(f):
            if i > 0:
        	time = float(line.split()[1])
        	if time < lastVal + interval:
            #mysum += int(line.split()[9])
            		mysum = float(line.split()[12])
            	else:
            #print time
            		print time,"    ",mysum
			filewriter.writerow([time, mysum])
            		lastVal = time
            #mysum = int(line.split()[9])


