'''



What is Spark?
Why need of Spark?


data -----------------------> machine ---------------------> DataWarehouse/DataLack
          Extract            Transform         Load          



We know that when our organisation had limited size. then that data we can handle using one machine.
As time when organisation data grow we can't handle using one machine. So, we required multiple machine to hable large size of data.

To handle this kind of situation we use distributed machine.

this goups of machine connected trough network known as clustered.




And these groups of machine handle by master machine.

                  |------------------> Worker(Machine)
                  |
Master -----------|
(Machine)         |-------------------> Worker(Machine)
                  |
                  |
                  |-------------------> Worker(Machine)


                  
In word of spark master machine known as driver machine.
And each worker has a executor.

We know that each ETL pipeline don't use all resourse.

User tells to driver we need only two executor.

And this drive don't know which machine are available and which are busy.

And then resourse manager come in picture which is intermediate between driver and executor.
This resourse manager know which executors are available and which are busy.



                  |------------------> Worker(Machine)
                  |
Master -----------|
(Machine)         |-------------------> Worker(Machine)
   |              |
   |              |
   |              |-------------------> Worker(Machine)
   |
   |
Resourse Manager



                               (In Memory)
() ------------------------> (Spark Cluster) -----------------------> ()



We know that spark is a in memory processing engine. that mean it doesn't store any data.
It read data from some where. It will take data into memory and process it in distributed maner 
and write back in some where.

Spark read data in form of partition and those partition will be process parallel.
Driver create tasks to process each partition.

These all task don't run paralle its depend on how many number of core available.
and we know each core run one task at time.


By default each partition has size 128MB



'''