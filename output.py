# open the file
file = open('output/part-00000', 'r')

# read the lines
lines = file.readlines()

def generateStateEventDict():
    # define the state event dictionary
    state_event_dict = {}
    for line in lines:
        # Split the line
        split = line.split(',')
        
        # Get the values
        state_event = split[0]
        count = split[1]

        # Split the state/event pair
        state_event_array = state_event.split('_')
        
        # Get the values
        state = state_event_array[0]
        event = state_event_array[1]

         # Check if state doesnt exists in dictionary
        if(state not in state_event_dict):
            
            # declare a new dictionary
            state_event_dict[state] = {}

        # Nest event count key-value pair under the state
        state_event_dict[state][event] = count
    return state_event_dict

def generateEventStateDict():
    # define teh event state dicstionary
    event_state_dict = {}
    for line in lines:
        # Split the line
        split = line.split(',')
        
        # Get the values
        state_event = split[0]
        count = split[1]

        # Split the state/event pair
        state_event_array = state_event.split('_')
        
        # Get the values
        state = state_event_array[0]
        event = state_event_array[1]
        
        event = str(event).replace('/', ' or ')

        if(event not in event_state_dict):
            event_state_dict[event] = {}
        event_state_dict[event][state] = count

    return event_state_dict
def generateStateFiles(state_event_dict):
    states = list(state_event_dict.keys())
    for state in states:
        event_count_dict = state_event_dict[state]
        events = list(event_count_dict.keys())
        f = open('inputs/regions/%s'%(state), 'w')
        for event in events:
            f.write("%s,%s"%(event, event_count_dict[event]))
        f.close()

def generateEventFiles(event_state_dict):
    events = list(event_state_dict.keys())
    for event in events:
        state_count_dict = event_state_dict[event]
        states = list(state_count_dict.keys())
        f = open('inputs/events/%s'%(event), 'w')
        for state in states:
            f.write('%s, %s'%(state, state_count_dict[state]))
        f.close()

def main():
    dictionary = generateStateEventDict()
    generateStateFiles(dictionary)
    dictionary = generateEventStateDict()
    generateEventFiles(dictionary)

if __name__ == '__main__':
    main()