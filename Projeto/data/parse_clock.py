import re
import pandas as pd

# Open the text file and read its contents
with open('log_clockB_7-01_V2.txt', 'r') as file:
    lines = file.readlines()

offsets = []
rates = []
delays = []

for line in lines:
    # Use regular expressions to find 'offset', 'rate', and 'delay' in the line
    offset = re.search(r'offset:([-+]?[0-9]*\.?[0-9]+)', line)
    rate = re.search(r'rate:([-+]?[0-9]*\.?[0-9]+)', line)
    delay = re.search(r'delay:0:00:00.([0-9]+)', line)

    # If a match is found, append the matched value to the corresponding list
    # If no match is found, append None
    offsets.append(offset.group(1) if offset else None)
    rates.append(rate.group(1) if rate else None)
    delays.append(delay.group(1) if delay else None)

# Convert the matches to a DataFrame
data = pd.DataFrame({
    'offset': offsets,
    'rate': rates,
    'delay': delays
})

# Save the DataFrame to a CSV file
data.to_csv('log_clockB_7-01_V2.csv', index=False)