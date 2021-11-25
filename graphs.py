import matplotlib.pyplot as plt
import sys

def getKeysAndPortions(file, inputType):
    # Open the file
    f = open('inputs/%s/%s'%(inputType, file), 'r')
    # Read the lines
    lines = f.readlines()

    #array for keys and values
    keys = []
    values = []

    # read each line and grab values
    for line in lines:
        key_value = line.split(',')
        key = key_value[0]
        value = key_value[1]
        keys.append(key)
        values.append(value)
    #define a total
    total=0

    # sum to total
    for value in values:
        total = total + int(value)
    
    portions = []
    # get portions
    for value in values:
        portion = float(value) / float(total) * 100
        portions.append(portion)
    
    # create tuple
    key_portion_tuples = []
    for (key, portion) in zip(keys, portions):
        key_portion_tuples.append((key, portion))
    key_portion_tuples.sort(key=lambda x:x[1], reverse=True)
    k = []
    p = []
    for tup in key_portion_tuples:
        k.append(tup[0])
        p.append(tup[1])
    return (k, p)

def createPieChart(keys, portions, file, fileType, save):
    # create appropriate title
    if fileType == 'events':
        plt.title("%s Regional Distribution"%(file), loc='center')
    else:
        plt.title("%s Weather Event Distribution"%(file), loc='center')
    
    # add the portions
    plt.pie(portions, shadow=True, startangle=90)

    # create the labels
    labels=[]
    for key, portion in zip(keys, portions):
        label = "%s - %.2f%%"%(key, portion)
        labels.append(label)

    # Determine number of legend columns
    numberOfColumns = int(len(keys) / 15)
    if(len(keys) % 15 > 0):
        numberOfColumns = numberOfColumns + 1
    # Include a Legend
    plt.legend(portions, labels=labels, loc='lower center', bbox_to_anchor=(0.5,-0.7), ncol=numberOfColumns)
    # Save or Show chart based on input
    if save:
        plt.savefig('charts/%s/%s.png'%(fileType, file), bbox_inches='tight')
    else:
        plt.show()

# Main Method
def main():
    # Name of File under observation
    fileName = sys.argv[2]
    # Name of folder containing File
    folder = sys.argv[1]
    # Get the keys and correspontion proportions
    (k, p) = getKeysAndPortions(fileName, folder)
    # Create the corresponding pie chart and save to charts/foldername/filename.png
    # Final value determines if chart is saved or shown (True is save, false is show)
    createPieChart(k, p, fileName, folder, True)
    

if __name__ == '__main__':
    main()