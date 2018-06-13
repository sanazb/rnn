
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup



requirements = [
    'cachetools==2.0.1'
    'scipy==1.0.0'
    'numpy==1.13.1'
    'nltk==3.2.4'
    'tqdm==4.19.4'
    'ekphrasis==0.4.10'
    'Keras==2.2.0'
    'keras_utilities==0.5.0'
    'frozendict==1.2'
]

test_requirements = [
    'pandas',
    'scipy',
    'scikit-learn>=0.18',
    'numpy'
]

setup(
    name='rnn',
    version='1.0.0',
    description="",
    author="",
    author_email='',
    url='https://github.com/sanazb/datastories-semeval2017-task4/new/master',
    packages=[
        'rnn'
    ],
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='rnn',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
