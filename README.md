How to install?
===============

```
$ mkdir priceminister.com
$ cd priceminister.com
$ git --recursive clone git@github.com:mahendrakalkura/priceminister.com.git .
$ cp --archive settings.py.sample settings.py
$ mkvirtualenv priceminister.com
$ pip install -r requirements.txt
```

How to run?
===========

```
$ cd priceminister.com
$ workon priceminister.com
$ python manage.py
```
