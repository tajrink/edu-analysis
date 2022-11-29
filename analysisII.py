import csv

list_data = []
with open("states_all.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    for row in reader:
        list_data.append(row)


state_data = [row for row in list_data if row["STATE"]=="NEW_YORK"] 
clean_data=[row for row in state_data if row["AVG_MATH_4_SCORE"]!=""]  
 
years=[]

for row in clean_data:
    years.append(row['YEAR'])
    
print(sorted(set(years)))

def percent_change(clean_data, year1, year2,col):
    val1=0
    val2=0
    for row in  clean_data:
        if row["YEAR"]==year1:
            val1=float(row[col])
        elif row["YEAR"]==year2:
            val2=float(row[col])
            
    percent=((val1-val2)/val1)*100
    return percent
    
for i in range (len(years)-1):
    year1=years[i]
    year2=years[i+1]
    print(percent_change(clean_data,year1,year2,"AVG_MATH_4_SCORE"))
    
    
    
    

