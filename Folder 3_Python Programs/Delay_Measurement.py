import csv

mysum = 0
interval = 0.1
lastVal = 0.0
with open('resultsDelays.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
    with open('DlPdcpStats.txt','r') as f:
    	for (i, line) in enumerate(f):
           if  str(line.split()[0]) == 'Rx':
	    if i > 0:
        	#1time = float(line.split()[1])
        	#2if time < lastVal + interval:
            #mysum += int(line.split()[9])
            		mysum = (float(line.split()[6]))/100000
            	#3else:
            #print time
            		print i,"    ",mysum
			filewriter.writerow([i, mysum])
            		#4lastVal = time
            #mysum = int(line.split()[9])


