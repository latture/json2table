from setuptools import setup

setup(
    name = "json2table",
    packages = ["json2table"],
    version = "1.1.5",
    description = "Convert JSON to an HTML table",
    long_description=open("README.rst").read(),
    author = "Ryan Latture",
    author_email = "ryan.latture@gmail.com",
    url = "https://github.com/latture/json2table",
    download_url = "https://github.com/latture/json2table/tarball/master",
    keywords = ["json", "HTML", "convert", "table"],
    license = "MIT",
    classifiers = (
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ),
)
