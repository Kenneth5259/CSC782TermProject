# This script was used to reset files for execution and quickly run mapreduce tests 
# Remove output and old versions of the mapper and reducer
hdfs dfs -rm -r -f WeatherEvents/output
hdfs dfs -rm /user/hadoop/WeatherEvents/WeatherEvents_Reducer.py
hdfs dfs -rm /user/hadoop/WeatherEvents/WeatherEvents_Mapper.py
# Pass updated mapper and reducer scripts to hdfs
hdfs dfs -copyFromLocal WeatherEvents_Reducer.py WeatherEvents/
hdfs dfs -copyFromLocal WeatherEvents_Mapper.py WeatherEvents/
# Provide the dataset if not there
hdfs dfs -copyFromLocal stormdata_2012_STATE_WEATHER WeatherEvents/
# mapreduce command for execution
mapred streaming \
-files WeatherEvents_Mapper.py,WeatherEvents_Reducer.py,stormdata_2012_STATE_WEATHER \
-mapper WeatherEvents_Mapper.py \
-reducer WeatherEvents_Reducer.py \
-input WeatherEvents/stormdata_2012_STATE_WEATHER \
-output /user/hadoop/WeatherEvents/output
# Cat out the output file
hdfs dfs -copyToLocal /user/hadoop/WeatherEvents/output/part-00000 output/