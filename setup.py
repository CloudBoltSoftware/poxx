from setuptools import setup, find_packages

version = (1, 1, 1)
VERSION_STR = '.'.join(str(v) for v in version)  # Use version tuple here

install_requires = [
    'polib',
]

extras_require = {
    'test': ['pytest'],
}

setup(
    name='poxx',
    version=VERSION_STR,
    author='Ned Batchelder, Package by Jacob Burch',
    author_email='jacobburch@revsys.com',
    url='http://github.com/jacobb/poxx',
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

