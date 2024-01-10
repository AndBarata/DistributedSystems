import pandas as pd
import matplotlib.pyplot as plt


def resultSlots(df):
    df_list = df.slots.tolist()

    # difference between slots minor than 7
    df_list_diff = [df_list[i+1] - df_list[i] for i in range(len(df_list)-1) if df_list[i+1] - df_list[i] < 5]
   
    print(f"\t - Total slots:  {len(df_list)}")
    print(f"\t - Min:          {min(df_list_diff)}")
    print(f"\t - Max:          {max(df_list_diff)}")
    print(f"\t - Jitter:       {max(df_list_diff) - min(df_list_diff)}")
    print(f"\t - Mean:         {sum(df_list_diff)/len(df_list_diff)}")

    # Plot slots's difference
    plt.figure
    plt.plot(df_list_diff)
    plt.ylabel("Slots difference (s)")
    plt.xlabel("time (s)")
    plt.title("Slots difference")
    plt.show()

    
    

if __name__ == "__main__":
    slots_no_correction = "log_slots_7-01_No_offset_rate" + ".csv"
    slots_no_offset = "log_slots_7-01_No_offset" + ".csv"
    slots_corrected = "log_slots_7-01_V2" + ".csv"

    df_slots_no_correction = pd.read_csv(slots_no_correction)
    df_slots_no_offset = pd.read_csv(slots_no_offset)
    df_slots_corrected = pd.read_csv(slots_corrected)

    print("\n\nResults for slots with no correction:")
    resultSlots(df_slots_no_correction)
    
    print("\n\nResults for slots with no offset:")
    resultSlots(df_slots_no_offset)

    print("\n\nResults for slots with correction:")
    resultSlots(df_slots_corrected)
    