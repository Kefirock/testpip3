import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="testpip3",
    version="0.0.1",
    author="Someone",
    author_email="id.justevolution@gmail.com",
    description="testpip3 package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kefirock/testpip3",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
