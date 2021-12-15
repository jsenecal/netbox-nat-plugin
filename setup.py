from setuptools import find_packages, setup

from os import path
top_level_directory = path.abspath(path.dirname(__file__))
with open(path.join(top_level_directory, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='netbox-nat-plugin',
    version='0.0.0',
    url='https://github.com/jsenecal/netbox-nat-plugin',
    # download_url='https://github.com/jsenecal/netbox-nat-plugin/archive/v0.0.0.tar.gz',
    description='A NetBox plugin to document NAT related things.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Jonathan Senecal',
    author_email='contact@jonathansenecal.com',
    install_requires=[],
    packages=find_packages(),
    license='Apache 2.0',
    include_package_data=True,
    keywords=['netbox', 'netbox-plugin', 'plugin'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    zip_safe=False
)