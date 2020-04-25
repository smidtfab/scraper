import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scraper-smidtfab", # Replace with your own username
    version="0.0.1",
    author="Fabian",
    author_email="imp.fsch@gmail.com",
    description="A package to scrape articles from various sources including newspapers and social media",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/smidtfab/scraper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)