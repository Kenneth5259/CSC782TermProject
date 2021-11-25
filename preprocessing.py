#!/usr/bin/python
import pandas as pd

# Method to drop all columns except State and Event then Save new file
def state_event_processing(filename):
    # Read File Name
    df = pd.read_csv(filename)
    # Grab the State and Weather Type
    df = df.loc[:, df.columns.intersection(['STATE','EVENT_TYPE'])]
    # Drop the extension
    new_file_name = filename[:-4]
    # Update with columns remaining
    new_file_name = new_file_name + '_STATE_WEATHER'
    # Save the file, no index, no header (Order: STATE, EVENT)
    df.to_csv(new_file_name, sep=',', index=False, header=False)

def main():
    state_event_processing('./stormdata_2012.csv')

if __name__ == "__main__":
    main()