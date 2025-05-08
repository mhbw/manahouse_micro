from setuptools import setup, find_packages

setup(
    name="mana-house",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click",
        "pydantic",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "mana-house=cli:cli"
        ]
    },
    python_requires='>=3.9',
)
