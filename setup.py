from setuptools import setup, find_packages

import json
import os

if __name__ == '__main__':
    setup(
        name='show',
        version=os.getenv('PACKAGE_VERSION', '0.0.1'),
        package_dir={"": "package"},  # Optional
        packages=find_packages('package'),
        description='A package',
        install_requires=[],
        entry_points={
            'console_scripts': ['show=show:show_main']
        }
    )
