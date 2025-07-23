from setuptools import setup, find_packages

setup(
    name="learning_crew",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "crewai",
        "crewai-tools",
    ],
)
