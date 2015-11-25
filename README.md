# Simpatize

[![Build
Status](https://snap-ci.com/johanngomes/simpatize/branch/master/build_image)](https://snap-ci.com/johanngomes/simpatize/branch/master)

To run the project you should:

1. Install Python 3.4.3 or higher

**We don't assure that the software will work on a higher version. We recommend the use of Python version 3.4.3.**

Here is the download link of Python 3.4.3: https://www.python.org/downloads/release/python-343/

2. Install dependencies

```
  $ pip3 install -r requirements.txt
```

3. Create the database in your machine, running the following commands:

```
  $ psql
  $ CREATE USER dev WITH password '1234';
  $ CREATE DATABASE simpatize WITH OWNER = dev;
```

3. Run the server

```
  $ python3 manage.py runserver
...
