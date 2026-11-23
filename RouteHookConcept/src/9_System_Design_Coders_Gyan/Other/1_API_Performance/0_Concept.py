"""



7 Ways to 10x your API Performance
==================================

1. Caching

   [client] <---------> [Redis] <-------------> [Database]


2. Connection Pool

   [] ----------> |--------------|
                  |              |
   [] ----------> | Connection   |--------> [Database]
                  | Pool         |
   [] ----------> |--------------|


3. Avoid N+1 Problem

   [] ----------> |--------------|
                  |              |
   [] ----------> | Database     |
                  |              |
   [] ----------> |--------------|


4. Pagination
        
           Request
        --------------->
[client]                [services]
        <---------------

                       [][][]... result
Page[1] <--------------| | |
Page[2] <----------------| | 
Page[3] <------------------|


     
5. JSON Serializers

   [] ----------> |--------------|
                  |              |
   [] ----------> | JSON         |
                  |              |
   [] ----------> |--------------|


6. Payload Compression

    Request(compress payload)
        --------------->
[client]                [services]
        <---------------
    (copress payload)Response


  For compression we use algorithum : Brotli


7. Asynchronous Logging
 
          ------------------>
   [logs] ------------------> [Buffer] ----------> Flush -------> Disk
          ------------------>



                    

          





"""