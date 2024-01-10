clear all
close all
clc




version = "V2/";
filename = "slots_no_offset.csv";
df_slots = readtable(version + filename);

slots = calculate_diff(df_slots);





function diff_data = calculate_diff(df_slots)
    slots = df_slots.slots;

    diff_data = diff(slots);
    diff_data = diff_data(diff_data < 5);
end