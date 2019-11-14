import pathlib
from distutils.core import setup

setup(
    name="ChainTranslator",
    packages=["ChainTranslator"],
    version="1.0.4",
    license="MIT",
    description="a package to mess up text via google translate",
    author="Benjamin Hinchliff",
    author_email="benjamin.hinchliff@gmail.com",
    url="https://github.com/SuniTheFish/ChainTranslator",
    keywords=["google", "translator", "useless", "stupid", "random", "chain", "translator", "ChainTranslator"],
    install_requires=[
        'googletrans'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Text Processing',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    entry_points={
        "console_scripts": [
            "chaintranslator=ChainTranslator.__main__:main"
        ]
    }
)