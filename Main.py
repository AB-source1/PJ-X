import sys
import datetime 
import csv
import argparse

def extract_dates(file_path):
    start_date = None
    end_date = None
    with open(file_path,"r") as file:
        reader = csv.reader(file)
        for row in reader:
            key = row[0].strip().lower()
            value = row[1].strip()
            
            if key == "start_date":
                start_date = value
            
            elif key == "end_date":
                end_date = value
            
    if not start_date or not end_date:
        raise ValueError("Start Date or End Date not found in the CSV.")    # Attempt at error messaging to show info to user
    
    return start_date,end_date

def generate_date_range(start_date, end_date):
    start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    
    date_list = [(start + datetime.timedelta(days=i)).strftime("%Y-%m-%d")            #This I copied  
                 for i in range((end - start).days + 1)]
    print(date_list)
    
    return date_list

def write_csv(out_file, dates):
    with open(out_file,'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Dates"])  # Header
        for date in dates:
            writer.writerow([date])


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
