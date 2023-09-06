import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('C:/Users/ormon/OneDrive/Desktop/python-challenge/PyBank/Resources', 'budget_data.csv')

month = []
month_1_profit_loss = []
month_2_profit_loss = []
change_in_profit_loss = []
# Read the csv file & split data on ,:
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        month.append(row[0])
        month_1_profit_loss.append(row[1])
        month_2_profit_loss = list(month_1_profit_loss).pop(0)
        change_in_profit_loss = int(row[2]) - int(row[1])
  

def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length 


#average = sum(total_profit_loss) / len(total_profit_loss)
print(f"Total Months: {len(month) - 1}")
#print(f"Total: ${str(sum(month_1_profit_loss))}")   
#print(f"Average Change: ${average(change_in_profit_loss)}")

clean_csv = list(zip(month, month_1_profit_loss, month_2_profit_loss, change_in_profit_loss))
output_file = os.path.join("C:/Users/ormon/OneDrive/Desktop/python-challenge/PyBank/banking_final.csv")

#  Open the output file
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Month", "Month 1 Profit/Loss", "Month 2 Profit/Loss", "Change in Profit/Loss"])

    # Write in zipped rows
    writer.writerows(clean_csv)