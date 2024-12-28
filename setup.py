from setuptools import setup, find_packages
import os

# Read the contents of README file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

# Read requirements.txt
with open('requirements.txt') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="pymerdoc",
    version="0.1.0",
    author="Scott Peterman",
    author_email="scottpeterman@example.com",  # Replace with actual email
    description="A tool for creating and managing Mermaid diagrams with modern UI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/scottpeterman/pymerdoc",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'pymerdoc=pymerdoc.main:main',
            'pymerdoc-gm=pymerdoc.gm:main',
            'pymerdoc-mc=pymerdoc.mc:main',
        ],
    },
    include_package_data=True,
    package_data={
        'pymerdoc': [
            'docs/*',
            'docs/*.png',
            'docs/*.svg',
            'docs/*.mermaid',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/scottpeterman/pymerdoc/issues',
        'Source': 'https://github.com/scottpeterman/pymerdoc',
    },
    test_suite='tests',
)