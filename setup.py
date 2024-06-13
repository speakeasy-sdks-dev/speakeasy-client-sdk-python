"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import setuptools
import re

try:
    with open('README.md', 'r') as fh:
        long_description = fh.read()
        GITHUB_URL = 'https://github.com/speakeasy-api/speakeasy-client-sdk-python.git'
        GITHUB_URL = GITHUB_URL[: -len('.git')] if GITHUB_URL.endswith('.git') else GITHUB_URL
        # links on PyPI should have absolute URLs
        long_description = re.sub(
            r'(\[[^\]]+\]\()((?!https?:)[^\)]+)(\))',
            lambda m: m.group(1) + GITHUB_URL + '/blob/master/' + m.group(2) + m.group(3),
            long_description,
        )
except FileNotFoundError:
    long_description = ''

setuptools.setup(
    name='speakeasy-client-sdk-python',
    version='5.9.11',
    author='Speakeasy',
    description='Speakeasy API Client SDK for Python',
    url='https://github.com/speakeasy-api/speakeasy-client-sdk-python.git',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(where='src'),
    install_requires=[
        "certifi>=2023.7.22",
        "charset-normalizer>=3.2.0",
        "dataclasses-json>=0.6.4",
        "idna>=3.4",
        "jsonpath-python>=1.0.6",
        "marshmallow>=3.19.0",
        "mypy-extensions>=1.0.0",
        "packaging>=23.1",
        "python-dateutil>=2.8.2",
        "requests>=2.31.0",
        "six>=1.16.0",
        "typing-inspect>=0.9.0",
        "typing_extensions>=4.7.1",
        "urllib3>=1.26.18",
    ],
    extras_require={
        "dev": [
            "pylint==3.1.0",
        ],
    },
    package_dir={'': 'src'},
    python_requires='>=3.8',
    package_data={
        'speakeasy-client-sdk-python': ['py.typed']
    },
)
