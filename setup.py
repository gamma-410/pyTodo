from setuptools import setup

setup(
    name="todo",
    version="1.0.0",
    install_requires=["pandas"],
    entry_points={
        "console_scripts": [
            "todo = main:main"
        ]
    }
)
