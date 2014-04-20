django-snowshoestamp
====================

A Django app for integrating with snowshoestamp



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

A signal will also be issued when recieving callbacks form snowshoestamp

```
snowshoestamp_event
```


__TODO__

1. tests
2. more descriptive readme.md