from setuptools import setup, find_packages

setup(
    name='stevedoretest2',
    version='1.0',

    packages=find_packages(),

    entry_points={
        'stevedoretest.formatter': [
            'fields = example2.fields:FieldList',
            'simple= example2.fields:FieldList'
        ],
    },
)