"""smbus2-asyncio setup.py."""
import re

from setuptools import setup

#  http://stackoverflow.com/questions/458550/standard-way-to-embed-version-into-python-package
VERSIONFILE = "smbus2_asyncio/version.py"
exec(open(VERSIONFILE).read())

setup(

    name='smbus2_asyncio',
    packages=["smbus2_asyncio"],
    # Use `__version__` as defined in the `VERSIONFILE`.
    version=__version__, # pylint: disable=undefined-variable
    description='Asyncio support for SMBUS2',
    long_description='''I2C/SMBUS does not provide an easy way to perform asynchronous IO.

This library wraps SMBUS2 into an executor and provides an asyncio interface.''',

    url='http://github.com/jabdoa2/smbus2_asyncio',
    author='Jan Kantert',
    author_email='jan-smbus2-asyncio@kantert.net',
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
    ],

    keywords=['i2c', 'smbus', 'smbus2', 'linux'],

    install_requires=['smbus2'],

)
