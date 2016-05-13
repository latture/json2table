from setuptools import setup

setup(
    name = 'json_to_table',
    packages = ['json_to_table'],
    version = '1.0',
    description = 'Convert JSON to an HTML table',
    long_description=open('README.md').read(),
    author = 'Ryan Latture',
    author_email = 'ryan.latture@gmail.com',
    url = 'https://github.com/latture/json_to_table',
    download_url = 'https://github.com/latture/json_to_table/zipball/master',
    keywords = ['json', 'HTML', 'convert', 'table'],
    license = 'MIT',
    classifiers = (
        "Programming Language :: Python",
    ),
)