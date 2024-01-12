import pandas as pd

versao = "V2/"
file_name = versao + 'slots_corrected_delay'
with open(file_name + ".txt", 'r') as file:
    lines = file.readlines()

slots = []

for i, line in enumerate(lines):
    if line.find('INFO') != -1:
        slots.append(float(line.split('@')[1]))

data = pd.DataFrame({
    'slots': slots
})

# Save the DataFrame to a CSV file
data.to_csv(file_name + '.csv', index=False)

df = pd.read_csv(file_name + '.csv')
print(df.tail())