# import csv

import pandas as pd

print("Results of NTP clock synchronization for semaphores\n")

# import data
slots = pd.read_csv('log_slots_5-01.csv')

# Get difference between RED and GREEN slots
errors = slots.iloc[:, 0].diff()
errors = errors[errors < 3].dropna()
print("Slots errors (RED - GREEN) - Diffrence between a semopher turn red and other green")
print(f"\tMean error: {errors.mean():.5f} | Max error: {errors.abs().max():.5f} | Min error: {errors.abs().min():.5f} | Jitter: {errors.abs().max()-errors.abs().min():.5f}\n")


offsets = pd.read_csv('log_offset_5-01.csv', decimal='.', sep=';')

# Offset clock A
offsets_A = offsets.iloc[:, 0]
offsets_B = offsets.iloc[:, 1]
print("Offset - Difference between the NTP server time and the local clock time")
print(f"\tClock_A : Mean offset: {offsets_A.abs().mean():.5f} | Max offset: {offsets_A.abs().max():.5f} | Min offset: {offsets_A.abs().min():.5f} | Jitter: {offsets_A.abs().max()-offsets_A.abs().min():.5f}")
print(f"\tClock_B : Mean offset: {offsets_B.abs().mean():.5f} | Max offset: {offsets_B.abs().max():.5f} | Min offset: {offsets_B.abs().min():.5f} | Jitter: {offsets_B.abs().max()-offsets_B.abs().min():.5f}\n")

