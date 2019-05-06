from setuptools import setup


setup(
    name="samplepi",
    version="1.0.0",
    entry_points={
        "console_scripts": [
            "samplepi = src.Main:main"
        ]
    }
)

