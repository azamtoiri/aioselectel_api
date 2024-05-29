from setuptools import setup, find_packages

setup(
    name='selectel_async',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'aiohttp',
    ],
    test_suite='tests',
)
