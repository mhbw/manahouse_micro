from setuptools import setup, find_packages

setup(
    name="mana-house",
    version="0.1.0",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        "click",
        "pydantic>=2.0",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "mana-house=mana_house.cli:cli"
        ]
    },
    python_requires='>=3.9',
)
