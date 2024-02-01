from setuptools import setup, find_packages

version = os.environ.get('VERSION', '0.0.0').split('.')
VERSION_STR = '.'.join(str(v) for v in version.split('.'))

install_requires = [
    'polib',
]

extras_require = {
    'test': ['pytest'],
}

setup(
    name='poxx',
    version=VERSION_STR,
    author='Ned Batchelder, Package by Jacob Burch, Forked by CloudBolt Software, Inc.',
    author_email='dmenedez@cloudbolt.io',
    url='https://github.com/cloudboltsoftware/poxx',
    description='Faked translations',
    long_description=__doc__,
    packages=find_packages(),
    zip_safe=False,
    install_requires=install_requires,
    extras_require=extras_require,  # Use extras_require for test dependencies
    license='BSD',
    include_package_data=True,
    scripts=['poxx.py'],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',  # Specify your Python compatibility
)

