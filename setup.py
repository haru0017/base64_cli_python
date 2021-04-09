from setuptools import setup

setup(
    name="multiple-base64",
    version="1.0.0",
    entry_points={
        "console_scripts": [
            "mbase64 = main:main"
        ]
    }
)
