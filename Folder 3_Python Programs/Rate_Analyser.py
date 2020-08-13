import csv

mysum = 0
interval = 0.1
lastVal = 0.0
with open('results.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
    with open('RxPacketTrace.txt','r') as f:
        for (i, line) in enumerate(f):
            if i > 0:
                time = float(line.split()[1])
                if time < lastVal + interval:
                    mysum += int(line.split()[9])
                else:
                    data = [time,(mysum*8/(time-lastVal))/1000000000]
                    print('{:<10f}{:>10f}'.format(data[0],data[1]))
                    filewriter.writerow([time, (mysum*8/(time-lastVal))/1000000000])
                    #print data
                    lastVal = time
                    mysum = int(line.split()[9])


