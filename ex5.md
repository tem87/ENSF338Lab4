### Question 1:
 The first approach is used when we want to execute a given code a specified number of times and is used when we want a single measurement of how long it takes. By repeating the execution multiple times, it accounts for factors like loading, caching and other external factors that might alter the results of a single run. 

The second approach which uses repeat is used when we care about having consistent performances over numerous runs. It is often sued to check for outliers. 

In summary, if you only care about the time it takes for a function to run and do not care about the consistency or variance between runs, you would use the first approach. However if you are more interested in analyzing the distribution of timings, you would use the second approach. 


### Question 2:
The appropriate statistic to apply to timeit.timeit() would be average. This is because it returns the total time taken for the specified number of runs so the average is easily computed by dividing by the total number of runs. 

The appropriate statistics to apply to timeit.repeat would be minimum and maximum times. Since it returns a list of times taken for each repetition, this allows us to compute the minimum and maximum times taken. The minimum time tells us the fastest time we might hypothetically expect in a run, and the maximum time tells us the slowest time we might expect for a hypothetical run. 

