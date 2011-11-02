#Friendlog
I am curious how fast and when I gain facebook friends. I created this script to get some data, later I might analyse it.

Some classmates are interested so I thought i'd post it on github.

## Instalation
The following steps should get you up and running:

    $ git clone git@github.com:highriseo/friendlog.git
    $ pip install requests simplejson
    
###You'll need to add some values yourself:

- In scrape.py you need to add where you want your log files to go. (I have mine under log/)
- In `apikey.py` you need to add your facebook api key. 

### Get a facebook access_token
The easiest way to get yourself an api key is to use facebook's graph explorer application. Click on the Get Access Token button. When it asks for which permissions you want, click on the extended permissions tab and check "offline_access". Insert that value into `apikey.py`.

### Add a cronjob
Add a cronjob to check at a regular frequency for any changes. Here is mine:

03       *       *       *       *       /usr/bin/python /PATH/TO/scrape.py

This makes the script execute every 3rd minute of every hour.

Goodluck, feel free to contact me if you have questions.