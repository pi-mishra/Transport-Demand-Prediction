from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return a list of requirements.
    """
    requirements = []

    with open(file_path) as file_object:
        requirements = file_object.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

    return requirements

setup(
    name="Nairobi demand prediction",
    version="0.0.1",
    author="Piyush",
    author_email="piyushmishra898@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
