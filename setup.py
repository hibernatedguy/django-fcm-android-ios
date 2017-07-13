from setuptools import setup

import fcm

version = fcm.VERSION

requires = [
    'Django==1.10.5',
    'djangorestframework>=3.3.1',
    'mock==1.0.1',
    'pytz==2015.4',
    'requests==2.7.0',
]

setup(name='django-fcm-android-ios',
    version=version,
    author='Ashish and Sunit',
    author_email='developerbyweekend@gmail.com',
    description='Send a message using FCM HTTP connection server protocol',
    long_description=open('docs/index.rst').read(),
    url='https://github.com/ashish2py/django-fcm-android-ios',
    license='MIT',
    packages=[ "fcm","fcm/migrations"],
    zip_safe=False,
    include_package_data=True,
    install_requires=requires,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
)
