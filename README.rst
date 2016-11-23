======================
Django Firebase and iOS Messaging
======================

django-fcm-android-ios is a simple Django app to send a message using fcm HTTP connection server protocol.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Install django-fcm-android-ios::

    pip install git+https://github.com/ashish2py/django-fcm-android-ios

2. Add "fcm" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'fcm',
    )

3. Add in setting api keys like this::

    GCM_DEVICE_MODEL = "DeviceModel" # default fcm.Device
    GCM_IOS_APIKEY = "IOS_APIKEY"
    GCM_ANDROID_APIKEY = "ANDROID_APIKEY"


4. Include the fcm routers in your project urls.py like this::

    from fcm.routers import router
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
   :alt: Join the chat at https://gitter.im/ashish2py/django-fcm-android-ios
   :target: https://gitter.im/ashish2py/django-fcm-android-ios?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
