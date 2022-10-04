The dataset used is ```Final_Trans.csv```

.To run all the jobs, run the ```Run.sh``` file on the Command Line or Ubuntu Terminal.

(Before running it, the input and output paths must be modified in the Run.sh file).
Make sure Hadoop is installed on the system and all the services (DFS and YARN) are running.
```
$ bash Run.sh
```
This will run all the jobs and the output will be generated in the working directory. 

The K-Means Clustering Algorithm is divided into 3 MapReduce Jobs.

- First MapReduce Job - 
The First Mapreduce job creates the initial centroids for the data passed to it.
Since muliple mappers and nodes generate different initial centroids, the best 
set of initial centroids are chosen in this job 

- Second MapReduce Job- 
The second MapReduce job is responsible of creating clusters using the initial 
centroids. 
Since this is a multiple iteration process, the final cluster is formed either 
after the max. number of iterations has completed, or if the convergence 
criteria is satisfied

- Third MapReduce Job - 
After finding the final cluster, the Third MapReduce job finds all the points 
associated to that cluster. 

The following are the output files generated - 
- Final Clusters - ```Fincluster.txt```
- Final Centroids - ```fincent.txt```

The Fincluster.csv and fincent.csv are generated after running it on jupyter 
notebook for visualisations

However, only the clusters file is required for visualisations
Both visualisation and cleaning were done on the jupyter notebook.
The files for visualisation and cleaning are provided aswell.
