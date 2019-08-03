import csv
import os


file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")


total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
net_total = 0


with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

   
    header = next(reader)

    
    first_row = next(reader)
    total_months = total_months + 1
    net_total = net_total + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

       
        total_months = total_months + 1
        net_total = net_total + int(row[1])

        
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

net_monthly_avg = sum(net_change_list) / len(net_change_list)


