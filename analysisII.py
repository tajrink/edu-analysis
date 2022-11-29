import csv

list_data = []
with open("states_all.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    for row in reader:
        list_data.append(row)
state_data = [row for row in list_data if row["STATE"]=="NEW_YORK"] 
clean_data=[row for row in state_data if row["AVG_MATH_4_SCORE"]!=""]  

['1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', 
'2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2019']

 
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
        
print(percent_change(clean_data,"2003","2005","AVG_MATH_4_SCORE"))

['1992', '2000', '2003', '2005', '2007', '2009', '2011', '2013', '2015', '2017', '2019']

for i in range (len(years)-1):
    year1=years[i]
    year2=years[i+1]
    print(percent_change(clean_data,year1,year2,"AVG_MATH_4_SCORE"))
    
    
    
    

