import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='vnaddress',
    version='0.9.6',
    scripts=['vnas'],
    author="vantrong291",
    author_email="vantrong291@gmail.com",
    description="A package for parsing Vietnamese address",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vantrong291/vn_address_standardizer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'nltk', 'joblib', 'sklearn_crfsuite', 'fuzzywuzzy', 'python-Levenshtein'
    ],
    include_package_data=True,
)
