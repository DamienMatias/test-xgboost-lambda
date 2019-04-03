# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='test_xgboost_lambda',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    zip_safe=False,
    install_requires=['colorama==0.4.0',
                      'dotmap==1.3.3',
                      'numpy>=1.15.4',
                      'pandas>=0.24.2',
                      'scikit-learn==0.20.0',
                      'scipy==1.1.0',
                      'boto3',
                      's3fs',
                      'watchtower >=0.5.5',
                      'cloudpickle==0.8.0',
                      'dask >=1.1.4',
                      'xgboost==0.81'],
    author='dmatias',
    description='Test Xgboost lambda',
)
