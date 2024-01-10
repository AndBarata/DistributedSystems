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
    plt.figure()
    # define x scale
    x = [i*10//60 for i in range(len(df_list_diff))]
    y = [i*1000 for i in df_list_diff]
    plt.plot(x, y)
    plt.ylabel("Slots difference (ms)")
    plt.xlabel("time (minutes)")
    plt.title("Slots difference")
    plt.show(block=False)

def resultsROD(df):
    print(f"\t - Total ROD:  {len(df)}")
    print(f"\t - Min offset:        {min(df.offset)}")
    print(f"\t - Max offset:        {max(df.offset)}")
    print(f"\t - Jitter offset:     {max(df.offset) - min(df.offset)}")
    print(f"\t - Mean offset:       {sum(df.offset)/len(df.offset)}")

    print(f"\t - Min rate:          {min(df.rate)}")
    print(f"\t - Max rate:          {max(df.rate)}")
    print(f"\t - Jitter rate:       {max(df.rate) - min(df.rate)}")
    print(f"\t - Mean rate:         {sum(df.rate)/len(df.rate)}")

    print(f"\t - Min delay:         {min(df.delay)}")
    print(f"\t - Max delay:         {max(df.delay)}")
    print(f"\t - Jitter delay:      {max(df.delay) - min(df.delay)}")
    print(f"\t - Mean delay:        {sum(df.delay)/len(df.delay)}")

    # Plot offset
    plt.figure()
    plt.plot(df.offset)
    plt.ylabel("Offset (s)")
    plt.xlabel("time (s)")
    plt.title("Offset")
    plt.show(block=False)

    # Plot rate
    plt.figure()
    plt.plot(df.rate)
    plt.ylabel("Rate (ppm)")
    plt.xlabel("time (s)")
    plt.title("Rate")
    plt.show(block=False)

    # Plot delay
    plt.figure()
    plt.plot(df.delay)
    plt.ylabel("Delay (s)")
    plt.xlabel("time (s)")
    plt.title("Delay")
    plt.show(block=False)

    # Plot offset, rate and delay
    plt.figure()
    plt.plot(df.offset, label="offset")
    plt.plot(df.rate, label="rate")
    plt.plot(df.delay, label="delay")
    plt.ylabel("Time (s)")
    plt.xlabel("time (s)")
    plt.title("Offset, rate and delay")
    plt.legend()




    

if __name__ == "__main__":
    version = "V2/"
    '''
    slots_no_correction = version + "log_slots_7-01_No_offset_rate" + ".csv"
    slots_no_offset = version + "log_slots_7-01_No_offset" + ".csv"
    slots_corrected = version + "log_slots_7-01_V2" + ".csv"

    clockA_no_correction = version + "log_clockA_7-01_No_offset_rate" + ".csv"
    clockA_no_offset = version + "log_clockA_7-01_No_offset" + ".csv"
    clockA_corrected = version + "log_clockA_7-01_V2" + ".csv"

    clockB_no_correction = version + "log_clockB_7-01_No_offset_rate" + ".csv"
    clockB_no_offset = version + "log_clockB_7-01_No_offset" + ".csv"
    clockB_corrected = version + "log_clockB_7-01_V2" + ".csv"


    # Slots
    df_slots_no_correction = pd.read_csv(slots_no_correction)
    df_slots_no_offset = pd.read_csv(slots_no_offset)
    df_slots_corrected = pd.read_csv(slots_corrected)

    #clock A
    df_clockA_no_correction = pd.read_csv(clockA_no_correction)
    df_clockA_no_offset = pd.read_csv(clockA_no_offset)
    df_clockA_corrected = pd.read_csv(clockA_corrected)

    #clock B
    df_clockB_no_correction = pd.read_csv(clockB_no_correction)
    df_clockB_no_offset = pd.read_csv(clockB_no_offset)
    df_clockB_corrected = pd.read_csv(clockB_corrected) 

    print("\n\nResults for no correction:")
    resultSlots(df_slots_no_correction)
    resultsROD(df_clockA_no_correction)
    
    print("\n\nResults for slots with no offset:")
    resultSlots(df_slots_no_offset)
    resultsROD(df_clockA_no_offset)

    print("\n\nResults for slots with correction:")
    resultSlots(df_slots_corrected)
    resultsROD(df_clockA_corrected)

    '''

    print("\n\n xDxdDxD")
    apagar = version + "slots_no_offset" + ".csv"
    df_apagar = pd.read_csv(apagar)
    resultSlots(df_apagar)
    plt.show()