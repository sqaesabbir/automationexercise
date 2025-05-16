from setuptools import setup, find_packages

setup(
    name="automation-exercise",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "playwright>=1.42.0",
        "pytest>=8.0.2",
        "pytest-playwright>=0.4.4",
        "python-dotenv>=1.0.1",
        "pytest-html>=4.1.1",
        "allure-pytest>=2.13.2",
        "pytest-rerunfailures>=13.0"
    ],
) 