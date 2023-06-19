# Import the required files
import csv
import os

# Add the files to the output
budget_data_csv = os.path.join("Resources", "budget_data.csv")
analysis_txt = os.path.join("Analysis", "analysis.txt")

#Set the parameters for the profit variable
total_months = 0
prev_profit = 0
month_of_change = []
profit_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]
total_profit = 0

# Open csv file and convert into keys and values
with open (budget_data_csv) as profit_data:
    reader = csv.reader(profit_data)
# Read the header row
    header = next(reader)

# Create a loop to track the totals
    for row in reader:

# Add variables
        total_months = total_months + 1

# Set to read value as integer
        total_profit = total_profit + int(row[1])

# Track change in profits
        profit_change = int(row[1]) - prev_profit
        prev_profit = int(row[1])
        profit_change_list = profit_change_list + [profit_change]
        month_of_change += [row[0]]

# Calculate greatest increase in profits
        if (profit_change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = profit_change

# Calculate the great decrease in profits
        if (profit_change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profit_change

# Calculate the average of the changes
    profit_ave = sum(profit_change_list) / len(profit_change_list)

# Create analysis output
output = (
        f"\nFinancial Analysis Results\n"
        f"----------------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_profit}\n"
        f"Average Change: ${profit_ave}\n"
        f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n" 
        f"Greatest Decrease in Profits {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    )

# Print the output
print(output)

# Export the results to a text file
with open(analysis_txt, "w") as txt_file:
    txt_file.write(output)
