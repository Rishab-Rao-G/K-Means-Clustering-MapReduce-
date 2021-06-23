The dataset used is Final_Trans.csv
To run all the jobs, run the "Run.sh"
(Before running it, the input and output paths must be modified)

>> bash Run.sh

The K-Means Clustering Algorithm is divided into 3 MapReduce Jobs.

i)First MapReduce Job - 
The First Mapreduce job creates the initial centroids for the data passed to it.
Since muliple mappers and nodes generate different initial centroids, the best 
set of initial centroids are chosen in this job 

ii)Second MapReduce Job- 
The second MapReduce job is responsible of creating clusters using the initial 
centroids. 
Since this is a multiple iteration process, the final cluster is formed either 
after the max. number of iterations has completed, or if the convergence 
criteria is satisfied

iii) Third MapReduce Job - 
After finding the final cluster, the Third MapReduce job finds all the points 
associated to that cluster. 

The following are the output files generated - 
i) Final Clusters - Fincluster.txt
ii) Final Centroids - fincent.txt

The Fincluster.csv and fincent.csv are generated after running it on jupyter 
notebook for visualisations

However, only the clusters file is required for visualisations
Both visualisation and cleaning were done on the jupyter notebook.
The files for visualisation and cleaning are provided aswell.