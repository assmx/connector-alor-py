from setuptools import setup, find_packages

setup(
    name="connector-alor-py",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pytz",
        "requests",
        "pyjwt",
        "urllib3",
        "websockets",
        "pandas",
    ],
)
