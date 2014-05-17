django-snowshoestamp
====================

A Django app for integrating with snowshoestamp


Installation
------------

1. python setup.py
2. pip install requirements.txt
3. add snowshoestamp to INSTALLED_APPS
4. create custom class that inherits from SnowshoeStampView
5. add path to your custom view to your apps primary urls
6. register custom url with snowsheostamp

Settings
--------


__Required__


```
SNOWSHOESTAMP_KEY : the oauth key for your app
SNOWSHOESTAMP_SECRET : the oauth secret for your app
```


__Example Implementation__

1. Setup your urls.py to use the view below as the callback reciever
2. Register the url for view below as the webhook callback at snowshoestamp

```views.py
from snowshoestamp.views import SnowshoeStampView


class MySnowshoestampWebhookRecieverView(SnowshoeStampView):
    def post(self, request, *args, **kwargs):
        print(self.stamp_serial)
        print(self.stamp_data)

        # do something amazing

        return self.render_json_response({
            'detail': 'Snowshoestamp Callback recieved',
            'stamp_data': self.stamp_data
        })
```


__Please Note__

A signal will be issued when recieving callbacks from snowshoestamp


__Signal Example Implementation__


```signals.py
from django.dispatch import receiver

from snowshoestamp.signals import snowshoestamp_event


@receiver(snowshoestamp_event)
def on_snowshoestamp_callback(sender, stamp_serial, **kwargs):
    # do something amazing with the data in the kwargs dict
    pass
```


__TODO__

1. tests
2. ~~more descriptive readme.md~~
3. improve setup.py to install from requirements
4. ~~fix broken python_sdk install cant install from pip lacks setup.py~~
