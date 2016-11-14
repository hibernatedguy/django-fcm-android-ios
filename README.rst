======================
Django Firebase and iOS Messaging
======================

django-fcm-android-ios is a simple Django app to send a message using GCM HTTP connection server protocol.

Detailed documentation is in the "docs" directory.

.. image:: https://travis-ci.org/hugobrilhante/django-fcm-android-ios.svg
  :target: https://travis-ci.org/hugobrilhante/django-fcm-android-ios

.. image:: https://coveralls.io/repos/hugobrilhante/django-fcm-android-ios/badge.svg?branch=master&service=github
  :target: https://coveralls.io/github/hugobrilhante/django-fcm-android-ios?branch=master

.. image:: https://readthedocs.org/projects/django-fcm-android-ios/badge/?version=latest
   :target: http://django-fcm-android-ios.readthedocs.org/en/latest/
   :alt: Documentation Status

.. image:: https://img.shields.io/pypi/status/django-fcm-android-ios.svg
   :target: https://pypi.python.org/pypi/django-fcm-android-ios

.. image:: https://img.shields.io/pypi/dm/django-fcm-android-ios.svg
   :target: https://pypi.python.org/pypi/django-fcm-android-ios/1.0.0#downloads

.. image:: https://img.shields.io/pypi/l/django-fcm-android-ios.svg
   :target: https://github.com/hugobrilhante/django-fcm-android-ios/blob/master/LICENSE

.. image:: https://img.shields.io/github/release/hugobrilhante/django-fcm-android-ios.svg
   :target: https://github.com/hugobrilhante/django-fcm-android-ios/releases/tag/1.0.0

.. image:: https://img.shields.io/pypi/pyversions/django-fcm-android-ios.svg
   :target: https://pypi.python.org/pypi/django-fcm-android-ios



Quick start
-----------

1. Install django-fcm-android-ios::

    pip install git+https://github.com/ashish2py/django-fcm-android-ios

2. Add "gcm" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'gcm',
    )

3. Add in setting api keys like this::

    GCM_DEVICE_MODEL = "DeviceModel" # default gcm.Device
    GCM_IOS_APIKEY = "IOS_APIKEY"
    GCM_ANDROID_APIKEY = "ANDROID_APIKEY"


4. Include the gcm routers in your project urls.py like this::

    from gcm.routers import router
    url(r'api/', include(router.urls))

5. Run `python manage.py migrate` to create the device models


6. To register device::

    curl -X POST -H "Content-Type: application/json" -H "Authorization: "
     -d '{
        "dev_id": "Device id",
        "dev_type": "ANDROID or IOS",
        "reg_id": "Register id"
       }' 'http://localhost:8001/api/devices'

7. To unregister device::

    curl -X DELETE -H "Content-Type: application/json" -H "Authorization: "  
    'http://localhost:8001/api/devices/id_device'


.. image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/hugobrilhante/django-fcm-android-ios
   :target: https://gitter.im/hugobrilhante/django-fcm-android-ios?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge