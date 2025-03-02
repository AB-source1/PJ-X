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
                start_date = datetime.datetime.strptime(value, "%Y-%m-%d")
                print("start date :",value)
            elif key == "end_date":
                end_date  = datetime.datetime.strptime(value, "%Y-%m-%d")
                print("End date :",value)

    if not start_date or not end_date:
        raise ValueError("Start Date or End Date not found in the CSV.")    # Attempt at error messaging to show info to user
    
    return start_date,end_date

def generate_date_range(start_date, end_date):
    
    date_list = [(start_date + datetime.timedelta(days=i))            #This I copied  
                 for i in range((end_date - start_date).days + 1)]
    print(date_list)
    
    return date_list

def write_csv(out_file, dates):
    with open(out_file,'w',newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(["Dates,Weekday"])  # Header
        for date in dates:
            writer.writerow([date,is_weekday(date)])

def is_weekday(date):
    return date.weekday() < 5
 


input_file = "./input.csv"
output_file = "./output.csv"

try:
    # Extract start and end dates
    start_date, end_date = extract_dates(input_file)
    print(f"Start Date: {start_date}, End Date: {end_date}")
        
    # Generate date range
    date_list = generate_date_range(start_date, end_date)

    # Write output CSV
    write_csv(output_file, date_list)

except Exception as e: 
    print(f"Error: {e}")  