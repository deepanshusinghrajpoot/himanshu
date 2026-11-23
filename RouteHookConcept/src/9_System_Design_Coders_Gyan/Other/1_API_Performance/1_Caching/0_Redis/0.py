"""



Redis Database
==============

It is Remote Directory Server


What is Redis?
 
     -> In memory data structure store that can be used as a database, cache, and message broker
     -> Redis supports various data structures such as string, hashes, lists, sets, sorted sets,
        bitmaps, hyperloglogs, and geospatial indexes.




Features of Redis

i. In-Memory Storage
      . Fast read and write operations.
      . Ideal for real time requirements


ii. Persistence
      . Provide option to dump to disk


iii. Data Structures
      . Support various string, hashset, list, bitmap etc.


iv. Replication
      . Redis support master-slave replication, allowing data to be replicated to multiple
        servers for redundancy and failover


v.  Pub/Sub Messaging
      . Redis can act as a message broker using its publish/subscribe capabilites, allowing
        for real-time messa




        

Redis Architecture
------------------



                     Request
         ------------------------------------>
[client]                                       Redis Server(Master)
         <------------------------------------
                     Response


        









"""