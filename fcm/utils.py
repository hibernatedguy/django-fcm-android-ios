import json

import requests
from django.apps import apps
from django.core.exceptions import ImproperlyConfigured
from . import settings


def notification_push(dev_type, to, message=None, **kwargs):
    """
    Send data from your server to your users' devices.
    """
    key = {
        'ANDROID': settings.GCM_ANDROID_APIKEY,
        'IOS': settings.GCM_IOS_APIKEY
    }

    if not key[dev_type]:
        raise ImproperlyConfigured(
            "You haven't set the 'GCM_{}_APIKEY' setting yet.".format(dev_type))

    '''
    banner and notification-img : online and local file reference will work.
    required fields : title, message
    actions [
        {"icon": "emailGuests", "title": "ADD NUMBER", "callback": "app.emailGuests", "foreground": True},
        {"icon": "snooze", "title": "DISMISS", "callback": "app.snooze", "foreground": False}
    ]
    instructions {
        'content_type':
        'id':
        'notification_id':
    }

    ======== FCM PATTERN ========
    'ANDROID': {
        'to': to,
        'data': {
          "body": message.get('text'),
        },
        'notification': {
          'title': message.get('title'),
          'body': message.get('text'),
          'icon': message.get('image'),
          'sound': message.get('sound')
        }
      },
    '''
    payload = {
        'ANDROID': {
            'to': to,
            'data': {
                    'title': message.get('title'),
                    "message": message.get('body'),
                    "image": message.get('icon'),
                    'soundname': message.get('sound'),
                    "style": message.get('style'),
                    "summaryText": message.get('summary_text'),
                    "picture": message.get('banner'),
                    "actions": message.get('actions'),
                    "extra_params": message.get('extra_params'),
                    "vibrationPattern": message.get('vibration_pattern', [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]),
                    "force-start": 1,
                    "content-available": 1
                }
            },
        'IOS': {
            'to': to,
            'notification': {
                'body': message,
            },
        }
    }

    payload[dev_type].update(**kwargs)

    payload = json.dumps(payload[dev_type])

    headers = {'Authorization': 'key={}'.format(key[dev_type]), 'Content-Type': 'application/json'}

    response = requests.post(url='https://fcm.googleapis.com/fcm/send',
                             data=payload,
                             headers=headers
                             )

    if response.status_code == 200:

        response = response.json()

        if response['success']:
            return {'success': 'Message send successfully'}
        elif response['canonical_ids']:
            return {'canonical_id': response.get('results')[0].get('registration_id')}
        elif response['failure']:
            return {'error': response.get('results')[0].get('error')}

    elif 400 <= response.status_code < 500:
        return {'error': '%s Client Error: %s' % (response.status_code, response.reason)}

    elif 500 <= response.status_code < 600:
        return {'error': '%s Server Error: %s' % (response.status_code, response.reason)}


def get_device_model():
    """
    Returns the Device model that is active in this project.
    """
    try:
        return apps.get_model(settings.GCM_DEVICE_MODEL)
    except ValueError:
        raise ImproperlyConfigured("GCM_DEVICE_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            "GCM_DEVICE_MODEL refers to model '%s' that has not been installed" % settings.GCM_DEVICE_MODEL
        )
