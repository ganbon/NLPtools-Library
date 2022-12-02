from setuptools import setup, find_packages
install_requires = [
       "mecab-python3", 
        "ipadic",
        "pandas"
]

setup(
    name = 'nlptoolsjp',
    version = '0.3',
    author = 'ganbon', 
    install_requires=install_requires,
    packages = find_packages()
)