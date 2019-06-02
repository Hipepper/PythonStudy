from setuptools import setup

setup(
    name='TestFirstApp',
    version='0.0.1',
    packages=['myapp'],
    entry_points={
        "console_scripts":[
            "foobard = myapp.server:main",
            "foobar = myapp.client:main"
        ]
    }
)
