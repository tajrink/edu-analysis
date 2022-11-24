import csv

list_data = []
with open("states_all.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    for row in reader:
        list_data.append(row)
        
        
        
state_data = [row for row in list_data if row["STATE"]=="NEW_YORK"]    
        
#print(state_data)      

clean_data=[row for row in state_data if row["AVG_MATH_4_SCORE"]!=""]       
        
print(clean_data)       
        
        
        
        
        
        
        
        