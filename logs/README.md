# 25/04

## Additional dependencies:
pip install redis  
pip install pymongo  

## Explanation:

The middleware extracts the relevant log info from the request and stores it in a dict. 
Then it calls dump_json_logs on a separate thread (hence non blocking), which adds this 
dict to a redis queue named 'tasks'. 

To consume the items from the queue, another python script (monitor_queue.py) is kept
running. The script repeatedly checks for items in the 'tasks' queue of redis, extracts 
an item if the queue is not empty and stores them in MongoDB.

This setup has been tested locally.

# Other approaches

Tried to use asyncio 
To speed up the consumer, we can consider using multiprocessing to run multiple consumers
parallely.

# 27/04

### Additional dependencies:
pip install celery

The Django project has been setup to use a Celery task processing queue, with Redis as  
the message broker between the Django application and Celery.  

Next steps would be to possibly create a result backend, store celery logs, optimize worker  
performance, set task failure behaviour, etc.  

# 28/04

#### Running a celery instance

Ensure that the redis server is running  

> celery -A spoken worker -l INFO -f celery.logs  

-A - appname  
-l - loglevel  
-f - log file path. If no logfile is specified, stderr is used.  

- Added generic exception handling
- Ignore backend results to improve performance

#### Mongo validation design (in progress)

path pattern: "^(/(.)*)*/$" - matches /.../.../
event pattern - matches event. anything

#### Merged logs branch into my branch

#### GeoIP2

Using Geolite2 databases (free)  
Downloaded the binaries and saved in geodb/. Total size ~ 30mb  
Todo: cron job to update the db everyweek - https://mauteam.org/mautic/mautic-admins/solved-maxmind-geolite2-database-not-updating/

License  
The GeoLite2 end-user license agreement, which incorporates components of the Creative Commons   Attribution-ShareAlike 4.0 International License can be found here. The attribution requirement may be met by   including the following in all advertising and documentation mentioning features of or use of this database:  

This product includes GeoLite2 data created by MaxMind, available from  
<a href="https://www.maxmind.com">https://www.maxmind.com</a>.  



