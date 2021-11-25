#!/usr/bin/python
import sys

# state dictionary
state_event_records = {}

def main():

    # read the line
    for line in sys.stdin:
        # extract values
        (key, value) = line.strip().split(',')
        # Increment existing Key
        if key in state_event_records:
            state_event_records[key] = state_event_records[key] + int(value)
        # Add New Key
        else:
            state_event_records[key] = int(value)
    # Iterate over each Key
    for key in state_event_records:
        # Output the value
        print '%s,%i'%(key, state_event_records[key])

if __name__ == "__main__":
    main()  

