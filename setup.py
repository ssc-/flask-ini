"""
Flask-ini
---------

Allow Flask to be configured with configparser ini files.
"""
from setuptools import setup

setup(
    name='Flask-ini',
    version='0.2.2',
    url='https://github.com/ssc-/flask-ini',
    license='BSD',
    author='Rich Daley, Sebastian Schmelzer',
    author_email='rich@richd.me, ssc@xss.nu',
    description='Allow Flask to be configured with configparser ini files',
    long_description=__doc__,
    py_modules=['flask_ini'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'configparser'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='test_flask_ini'
)
