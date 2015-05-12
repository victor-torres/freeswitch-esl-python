from distutils.core import setup, Extension

setup (name = 'FreeSWITCH-ESL-Python',
       version = '1.0',
       ext_modules=[Extension('_ESL',sources=['swig/esl_wrap.cpp',
                                              'src/esl.c',
                                              'src/esl_json.c',
                                              'src/esl_event.c',
                                              'src/esl_threadmutex.c',
                                              'src/esl_config.c',
                                              'src/esl_oop.cpp',
                                              'src/esl_buffer.c'],
       include_dirs=['include/'])],
       packages = ['freeswitchESL'],
       pymodules = ['ESL'],
       description = 'Standalone FreeSWITCH ESL Python module.',)

