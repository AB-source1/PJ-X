import sys
import datetime 
import csv

print(sys.argv)
start_date = sys.argv[1]
end_date = sys.argv[2]
print("Start date :",start_date)
print("End date :",end_date)

d1 = datetime.datetime.fromisoformat(start_date)
print(d1)
d2 = datetime.datetime.fromisoformat(end_date)
x = d1
while x < d2 :
    print(x)
    x = x + datetime.timedelta(days=1)


outfile=open('./output.csv','w')
writer=csv.writer(outfile)
writer.writerow(["SNo", "States", "Dist", "Population"])
writer.writerow([1, "cali", 200, 200000])
