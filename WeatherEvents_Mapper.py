#!/usr/bin/python
import sys

# Read each line
for line in sys.stdin:
    # Strip unnecessary values,
    processed_line = line.strip()
    # Split on delimiter
    line_list = processed_line.split(',')
    # Save the State
    state = line_list[0]
    state = state.replace(' ', '-')
    # Save the Event
    event = line_list[1] 
    event = event.replace(' ', '-')
    # Create concatenated key
    key = state + '_' + event
    # Emit Key Value pair
    print '%s,%i'%(key,1)
