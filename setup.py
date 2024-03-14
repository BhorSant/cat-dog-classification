import os
import setuptools 

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="cat_dog_classification",
    version="0.1.0",
    author="Santosh Bhor",
    author_email="santoshbhor2001@gmail.com",
    description="A small package for Cat and Dog classification with CNN",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SantBhor/Cat-Dog-Classification",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
