import pandas as pd

# Open the text file and read its contents
version = "V2/"
file_name = version + 'clockB_corrected_delayV2'
with open(file_name + ".txt", 'r') as file:
    lines = file.readlines()

offsets = []
rates = []
delays = []

for i, line in enumerate(lines):
    if line.find('offset') != -1:
        offsets.append(float(line.split(':')[1]))
        
    elif line.find('rate') != -1:
        rates.append(float(line.split(':')[1]))
    
    elif line.find('delay') != -1:
        delays.append(float(line.split(':')[-1]))

    print("DEBUG: ", i)

    #print(f'\nLine {i}: {line}\n{offsets}, {rates}, {delays}')

# Convert the matches to a DataFrame
data = pd.DataFrame({
    'offset': offsets,
    'rate': rates,
    'delay': delays
})

# Save the DataFrame to a CSV file
data.to_csv(file_name + '.csv', index=False)

df = pd.read_csv(file_name + '.csv')
print(df.tail())