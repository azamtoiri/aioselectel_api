from setuptools import setup, find_packages

setup(
    name='selectel_async',
    version='0.1.4',
    packages=find_packages(),
    author="Azam Toiri",
    author_email="<azamtoiri@gmail.com>",
    keywords=['selectel', 'async', 'aiohttp'],
    install_requires=[
        'aiohttp',
    ],
    test_suite='tests',
)
