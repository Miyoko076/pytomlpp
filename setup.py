#!/usr/bin/env python3

import os
import glob
import platform
from setuptools import setup, Extension

dir_path = os.path.dirname(os.path.realpath(__file__))

class PyBind11Include:
    def __str__(self):
        import pybind11
        return pybind11.get_include()


extra_compile_args = []
if platform.system() == "Windows":
    extra_compile_args.append('/std:c++17')
    extra_compile_args.append('/DTOML_ENABLE_UNRELEASED_FEATURES=1')
else:
    extra_compile_args.append('-std=c++17')
    extra_compile_args.append('-DTOML_ENABLE_UNRELEASED_FEATURES=1')


setup(
    ext_modules=[
        Extension(
            'pytomlpp._impl',
            ['src/pytomlpp.cpp', 'src/type_casters.cpp', 'src/encoding_decoding.cpp'],
            include_dirs=[
                dir_path + '/include',
                dir_path + '/third_party',
                PyBind11Include(),
            ],
            extra_compile_args=extra_compile_args,
            language='c++',
        ),
    ],
)
