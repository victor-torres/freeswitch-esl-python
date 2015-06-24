from distutils.core import setup, Extension
import os

setup_path = __file__.split('/')
pkg_dir = '/'.join(setup_path[:-1]) + '/'

setup (name = 'FreeSWITCH-ESL-Python',
       version = '1.2',
       ext_modules=[Extension('_ESL',
       sources=[
              'swig/esl_wrap.cpp',
              'src/esl.c',
              'src/esl_json.c',
              'src/esl_event.c',
              'src/esl_threadmutex.c',
              'src/esl_config.c',
              'src/esl_oop.cpp',
              'src/esl_buffer.c'])],
       include_dirs=[os.path.join(pkg_dir, 'include/')],
       packages = ['freeswitchESL'],
       pymodules = ['ESL'],
       description = 'Standalone FreeSWITCH ESL Python module.',)

