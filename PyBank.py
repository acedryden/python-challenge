import csv
import os

#source csv: 
csv_path=r"Starter_Code\PyBank\Resources\budget_data.csv"

#declare variables: 
total_rows=0
sum_stock=0
stock_change=0
new_stock=0
sum_change=0
total_change=0

#main code:
with open(csv_path, 'r') as csv_file:
    csvreader=csv.reader(csv_file)
    header=next(csvreader)
    prev_stock=1088983
    sum_change=0
    max_num=0
    min_num=stock_change
    
    #for loop: 
    for row in csvreader:
        date=(row[0])
        total_rows=(total_rows+1)
        avg_rows=(total_rows-1)
        stock_price=(int(row[1]))
        month=row[0]
        #total stock:
        sum_stock=(sum_stock+stock_price)
        
        #stock variance:
        new_stock=int(stock_price)
        stock_change=(new_stock-prev_stock)
        prev_stock=stock_price
        sum_change+=stock_change
        
        #max stock change:
        if stock_change > max_num:
            max_num=stock_change
            max_month=month
        #min stock change: 
        if stock_change < min_num:
            min_num=stock_change
            min_month=month
avg_change=(float(sum_change/(total_rows-1))) 

#use round & float to properly display avg_change as currency to 2 decimal points:
avg_change=(round(float(avg_change),2))

#write to .txt file 
OUTPUT_PATH=os.path.join("pybank_analysis.txt")

with open(OUTPUT_PATH,'w') as textfile: 
        
        
    financial_analysis=(
        f"\n\nFinancial Analysis\n"
        f"------------------------\n"
        f"Total Months: {total_rows}\n"
        f"Total: ${sum_stock}\n"
        f"Average Change: ${avg_change}\n"
        f"Greatest Increase in Profits: {max_month} ${max_num}\n"
        f"Greatest Decrease in Profits: {min_month} ${min_num}\n")
    print(financial_analysis, end="")

    textfile.write(financial_analysis)
