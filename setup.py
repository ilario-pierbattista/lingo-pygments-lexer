import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
        name="lingo-pygments-lexer",
        version="0.0.2",
        author="Ilario Pierbattista",
        author_email="pierbattista.ilario@gmail.com",
        description="A LINGO modelling language lexer for pygments",
        license="BSD",
        keywords="Lingo lexer pygments",
        packages=find_packages(),
        install_requires=[
            "pygments"
        ],
        entry_points="""[pygments.lexers]
                        lingo=lingo_pygments_lexer:LingoLexer"""
)
