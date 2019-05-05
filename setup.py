from setuptools import setup

setup(
    name="sample.pi",
    version="1.0.0",
    install_requires=[],
    extras_require={
        "develop":[]
    },
    entry_points={
        "console_scripts":[
            "samplepi=src.Main.main"
        ]
    }
)