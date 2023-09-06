import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('C:/Users/ormon/OneDrive/Desktop/python-challenge/PyBank/Resources', 'budget_data.csv')

month= []
profit_loss = []
average_profit_loss = []
change_profit_loss = []

# Read the csv file & split data on ,:
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    first_row = next(csvreader)
#    print(header)
    month.append(first_row[0])
    profit_loss.append(int(first_row[1]))
    previous_value = int(first_row[1])
#    print(previous_value)

    #read the rows & place into lists
    for row in csvreader:
    #    print(row)
        month.append(row[0])
        profit_loss.append(int(row[1]))
        change_profit_loss.append(int(row[1]) - previous_value)
        previous_value = int(row[1])
        
#print(change_profit_loss)
def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length 

max_profit_loss = max(profit_loss)
min_profit_loss = min(profit_loss)

#average = sum(total_profit_loss) / len(total_profit_loss)
print(f"Total Months: {len(month)}")
print(f"Total: ${sum(profit_loss)}")   
print(f"Average Change: ${average(change_profit_loss)}")

print("The largest is: ", max_profit_loss)
print("The smallest is: ", min_profit_loss)