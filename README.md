django-snowshoestamp
====================

A Django app for integrating with snowshoestamp


Installation
------------

1. python setup.py
2. pip install requirements.txt
3. add snowshoestamp to INSTALLED_APPS
4. add 'sss' to urls

Settings
--------

__Required__

```
SNOWSHOESTAMP_KEY : the oauth key for your app
SNOWSHOESTAMP_SECRET : the oauth secret for your app
```


__Optional__

```
SNOWSHOESTAMP_CALLBACK_VIEW: A custom view that you can use to process callbacks
```


__Please Note__

A signal will also be issued when recieving callbacks from snowshoestamp

```
snowshoestamp_event
```


__TODO__

1. tests
2. more descriptive readme.md
3. improve setup.py to install from requirements
4. make recommendations for renaming of python_sdk to snowshoestamp.sssapi as python_sdk is VERy generic
5. make use of https://github.com/snowshoestamp/touchy_sdk and pusher for auth prompt
6. better logs