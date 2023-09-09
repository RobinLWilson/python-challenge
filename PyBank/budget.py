import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('C:/Users/ormon/OneDrive/Desktop/python-challenge/PyBank/Resources', 'budget_data.csv')

#create lists & dictionary to hold values
month= []
profit_loss = []
average_profit_loss = []
change_profit_loss = []
shift_profit_loss = []
min_max_dict = {}

# Read the csv file & split data on ,:
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header row & row 2
    header = next(csvreader)
    first_row = next(csvreader)

    #add the month cells in column 1 to the month list, starting in row 2
    month.append(first_row[0])

    #add the profit/loss cells in column 2 to the profit/loss list, starting in row 2
    profit_loss.append(int(first_row[1]))

    #set the previous profit/loss value to the cell in row 2, column 2
    previous_value = int(first_row[1])

    #loop through rows to calculate the change in profit/loss
    for row in csvreader:
        month.append(row[0])
        profit_loss.append(int(row[1]))
        change_profit_loss.append(int(row[1]) - previous_value)
        previous_value = int(row[1])

#summing function to be used to calculate average      
def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

#average function
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length 

#calculate the average change in profit/loss
average_change = round(average(change_profit_loss), 2)

#put the values from the change in profit/loss list into the "shift" list & put a null value in the first cell
shift_profit_loss = change_profit_loss
shift_profit_loss.insert(0, "00000")

#create a dictionary of the date list & the shifted change in profit/loss
for date in month:
    for value in shift_profit_loss:
        min_max_dict[date] = value
        shift_profit_loss.remove(value)
        break

#Use the lambda function to find the min & max of the change in profit/loss in the dictionary
greatest_increase = max(min_max_dict.items(), key=lambda x: int(x[1]))
greatest_decrease = min(min_max_dict.items(), key=lambda x: int(x[1]))

#print output to the terminal
print(f"Total Months: {len(month)}")
print(f"Total: ${sum(profit_loss)}")   
print(f"Average Change: ${average_change}")
print("Greatest Increase in Profits: " + str(greatest_increase))
print("Greatest Decrease in Profits: " + str(greatest_decrease))

# Set variable for output file
output_file = os.path.join('C:/Users/ormon/OneDrive/Desktop/python-challenge/PyBank/analysis/', 'PyBank_Results.txt')

#  Open the output file
with open(output_file, "w") as textfile:

    #print output to text file
    textfile.write(f"Total Months: {len(month)}")
    textfile.write("\n")
    textfile.write(f"Total: ${sum(profit_loss)}")  
    textfile.write("\n")
    textfile.write(f"Average Change: ${average_change}")
    textfile.write("\n")
    textfile.write("Greatest Increase in Profits: " + str(greatest_increase))
    textfile.write("\n")
    textfile.write("Greatest Decrease in Profits: " + str(greatest_decrease))
   