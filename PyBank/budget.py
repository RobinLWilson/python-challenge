import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('C:/Users/ormon/OneDrive/Desktop/python-challenge/PyBank/Resources', 'budget_data.csv')

month= []
profit_loss = []
average_profit_loss = []
change_profit_loss = []
shift_profit_loss = []
min_max_dict = {}

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

average_change = round(average(change_profit_loss), 2)

shift_profit_loss = change_profit_loss
shift_profit_loss.insert(0, "00000")

for date in month:
    for value in shift_profit_loss:
        min_max_dict[date] = value
        shift_profit_loss.remove(value)
        break

greatest_increase = max(min_max_dict.items(), key=lambda x: int(x[1]))
greatest_decrease = min(min_max_dict.items(), key=lambda x: int(x[1]))

print(f"Total Months: {len(month)}")
print(f"Total: ${sum(profit_loss)}")   
print(f"Average Change: ${average_change}")
print("Greatest Increase in Profits: " + str(greatest_increase))
print("Greatest Decrease in Profits: " + str(greatest_decrease))

# Set variable for output file
output_file = os.path.join('C:/Users/ormon/OneDrive/Desktop/python-challenge/PyBank/analysis/', 'PyBank_Results.txt')

#  Open the output file
with open(output_file, "w") as textfile:
    textfile.write(f"Total Months: {len(month)}")
    textfile.write("\n")
    textfile.write(f"Total: ${sum(profit_loss)}")  
    textfile.write("\n")
    textfile.write(f"Average Change: ${average_change}")
    textfile.write("\n")
    textfile.write("Greatest Increase in Profits: " + str(greatest_increase))
    textfile.write("\n")
    textfile.write("Greatest Decrease in Profits: " + str(greatest_decrease))
   