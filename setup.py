import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    dependencies = list(map(lambda x: x.strip(), fh.readlines()))

setuptools.setup(
    name="databuri",
    version="0.0.3-dev",
    packages=setuptools.find_packages(),
    author="Pattarawat Chormai and friends",
    author_email="author@example.com",
    install_requires=dependencies,
    # @todo #1 add description
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codeforthailand/databuri",
    classifiers=[
        "Programming Language :: Python :: 3",
        # @todo #1 add license
        # "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # @todo #1 add keywords
    # keywords=[...]
)