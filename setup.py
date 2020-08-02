from setuptools import setup

setup(
    name="base64",
    version="1.0.0",
    entry_points={
        "console_script": [
            "b64 = main:main"
        ]
    }
)