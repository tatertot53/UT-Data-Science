
import os
import csv


csv_path = os.path.join("..","Resources", "budget_data_1.csv")
txt_path = os.path.join("..","Resources", "bankReport01.txt")

with open(csv_path,newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    next(reader)
    revenue = []
    date = []
    dollarChanges = []
    

    for row in reader:

        revenue.append(float(row[1]))
        date.append(row[0])


    for i in range(1,len(revenue)):
        dollarChanges.append(revenue[i] - revenue[i-1])
        months = len(date)
        avgChange = sum(dollarChanges)/len(dollarChanges)
        totRevenue = sum(revenue)
        avgDollarChanges = sum(dollarChanges)/len(dollarChanges)
        maxDollarChanges = max(dollarChanges)
        minDollarChanges = min(dollarChanges)
        maxDollarChangesDate = str(date[dollarChanges.index(max(dollarChanges))])
        minDollarChangesDate = str(date[dollarChanges.index(min(dollarChanges))])
        
    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months: " + str(months))
    print("Total Revenue: $" + str(totRevenue))
    print("Average Revenue Change: $", round(avgDollarChanges))
    print("Greatest Increase in Revenue:", maxDollarChanges,"($", maxDollarChanges,")")
    print("Greatest Decrease in Revenue:", minDollarChanges,"($", minDollarChanges,")")

    
    analysis = []
    analysis.append("Financial Analysis")
    analysis.append("-----------------------------------")
    analysis.append("Total Months: $" + str(months))
    analysis.append("Total Revenue: $" + str(totRevenue))
    analysis.append("Average Revenue Change: " + str(avgChange))
    analysis.append("Greatest Increase in Revenue: $" + str(maxDollarChanges))
    analysis.append("Greatest Decrease in Revenue: $" + str(minDollarChanges))
    analysis.append("___________________________________")
        
    with open(txt_path,'a') as txtFile:
        for data in analysis:
            data = data.strip()
            txtFile.write(data).strip
           
            
            
            
 
            


    




