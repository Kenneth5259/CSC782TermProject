# CSC782TermProject
# Kenneth Carroll, Samuel Christopher 
### Preface
Various versions and filetypes are used due to minor issues and bugs between alternating between linux virtual machines, a macbook, and a windows laptop. 

Due to difficulties in access provisioning all code commits were pushed from Kenneth Carroll's account but the code, structure, troubleshooting, and final report were an equal collaborative effort.

### MAPREDUCE - Requires Python 2.7
There is a script, run_mapred.sh that will execute the map reduce functionality. File names are hard coded and would need to be updated if the Mapper, Reducer or input file names are changed. It will pull the output into a local output folder. A smaller test file is included alongside the main processed file and the original csv.

### Data Preprocessing - Requires Python 3.8
There is a preprocessing script that converts the csv file into a formatted output. This also fixes troublesome characters and is needed to run before the mapred job

Once the output is created, run the output.py script which will break the output file into smaller digestible files either by region or event. This allows for easier manipulation of data and allows focus on specific areas of interes

### Graphing - Requires Python 3.8
the graphs.py script can be run by specifying which input folder i.e. regions or events, then the file name. It will generate a pie graph for the distribution of the values. To create groups of graphs, a run_graphs.bat file is used to loop through the folders and call the script for each file. This was unable to be done within the main graphs.py due to an issue where the legend colors become offset from the graph when ran under multiple iterations. Update the bat file with the correct absolute path to enable usage.

