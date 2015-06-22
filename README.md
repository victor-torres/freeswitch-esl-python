# FreeSWITCH ESL Python

This is a python package to distribute the ESL.py module generated by FreeSWITCH. It's an auto-generated swig module and the idea is make it easy to use FreeSWITCH Event Socket Library without having it installed in the same box. So you can have different servers, one running FreeSWITCH and another one running your business logic.

## Installing

```shell
$ pip install FreeSWITCH-ESL-Python
```

## Checking version

```shell
$ pip freeze | grep ESL
```

Should return something like `FreeSWITCH-ESL-Python==1.0`.

## Using

```python
from freeswitchESL import ESL
```

## Redundancy

```python
try:
    import ESL
except ImportError:
    from freeswitchESL import ESL
```

Redundancy could be helpful when you have FreeSWITCH running with your system in production environments, so you can just import ESL, but you also have a test environment (E.g. Codeship) without a FreeSWITCH installation.

## Building

```shell
$ cd swig
$ swig -module ESL -classic -python -c++ -DMULTIPLICITY -threads -I../include -o esl_wrap.cpp ESL.i
$ mv ESL.py ../freeswitchESL/ESL.py
```

## Resources

- Original repository by [gurteshwar](https://github.com/gurteshwar/freeswitch-esl-python)
- FreeSWITCH docs: [ESL](http://wiki.freeswitch.org/wiki/Esl)
- FreeSWICTH docs [Python ESL](http://wiki.freeswitch.org/wiki/Python_ESL)
