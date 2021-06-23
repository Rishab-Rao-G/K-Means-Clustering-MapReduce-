#!/bin/bash

#loading the data to hdfs

hdfs dfs -copyFromLocal Final_Trans.csv /user/hduser/rishab-in/inp



# first map reduce job
mapred streaming -files  ./firstmapper.py,./firstreducer.py \
                 -mapper firstmapper.py \
                 -reducer firstreducer.py \
                 -input /user/hduser/rishab-in/inp \
                 -output /user/hduser/rishab-out/oup1

#get the centroids from hdfs
hdfs dfs -get /user/hduser/rishab-out/oup1/part-00000 initcent.txt

#removes the output directory
hdfs dfs -rm -r /user/hduser/rishab-out/oup1

#iteration for second map reduce job
for (( i=1; i<=5; i++ ))
do
	mapred streaming -files ./initcent.txt,./secondmapper.py,./secondcombiner.py,./secondreducer.py \
                         -mapper secondmapper.py \
                         -combiner secondcombiner.py \
                         -reducer secondreducer.py \
                         -input /user/hduser/rishab-in/inp \
                         -output /user/hduser/rishab-out/oup2
        #get the new centroids
        hdfs dfs -get /user/hduser/rishab-out/oup2/part-00000 newcent$i.txt
        #removes the output directory
        hdfs dfs -rm -r /user/hduser/rishab-out/oup2
        #compare the size of new centroids and initial centroids
        #if they are equal then our initial centroids will be replaced with the new centroids file
	if [ "$(wc -l < newcent$i.txt)" -eq "$(wc -l < initcent.txt)" ];
        then

            cp newcent$i.txt initcent.txt
        else
            mv newcent$((i-2)).txt initcent.txt
            break
        fi

        rm -f newcent.txt
done

mv initcent.txt fincent.txt

#third map reduce job

mapred streaming -files ./fincent.txt,./thirdmapper.py,./thirdreducer.py \
                         -mapper thirdmapper.py \
                         -reducer thirdreducer.py \
                         -input /user/hduser/rishab-in/inp \
                         -output /user/hduser/rishab-out/oup3

#Final cluster with cluster ID and points associated with them

hdfs dfs -get /user/hduser/rishab-out/oup3/part-00000 Fincluster.txt

hdfs dfs -rm -r  /user/hduser/rishab-out/oup3
