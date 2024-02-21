from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

requirements = [
    'base58==2.1.1',
    'ed25519==1.5',
    'x25519==0.0.2',
    'PyNaCl==1.5.0',
    'cryptography==42.0.4',
    'requests==2.31.0',
    'pickleDB==0.9.2',
    'grpcio==1.59.0',
    'grpcio-tools==1.59.0',
    'tcabci-read-client'
]

setup(
    name="transferchain-python-sdk",
    version="0.2.1",
    author="TransferChain",
    author_email="info@transferchain.io",
    description="TransferChain Python SDK",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TransferChain/transferchain-python-sdk",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
