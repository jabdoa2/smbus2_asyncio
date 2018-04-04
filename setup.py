"""smbus2-asyncio setup.py."""
import re

from setuptools import setup

#  http://stackoverflow.com/questions/458550/standard-way-to-embed-version-into-python-package
VERSIONFILE = "smbus2_asyncio/version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(

    name='smbus2_asyncio',
    version=verstr,
    description='Asyncio support for SMBUS2',
    long_description='''I2C/SMBUS is does not provide an easy way to do
    asynchronous IO. This library wraps SMBUS2 into a thread pool and provides
    an async interface.''',

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
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
    ],

    keywords=['i2c', 'smbus', 'smbus2', 'linux'],

    install_requires=['smbus2'],

)
