
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ds_toolbox",
    version="0.0.1",
    author="Nicolas Sandller",
    description="Tools for data science explorations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nicosandller/ds_toolbox",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
