import os
import os.path as osp
import re
from typing import List, Optional

from setuptools import find_packages, setup

__version__ = '0.1.0'


def package_files(
    root: str,
    whitelist: Optional[List[str]] = None,
) -> List[str]:
    pattern = f'.({"|".join(whitelist or [])})$'

    paths: List[str] = []
    for path, _, names in os.walk(root):
        for name in names:
            if whitelist is not None and not re.search(pattern, name):
                continue
            paths.append(osp.join('..', path, name))
    return paths


setup(
    name='torch_fem_sphinx_theme',
    version=__version__,
    author='walker chi',
    author_email='walker.chi.000@gmail.com',
    url='https://github.com/walkerchi/torch_fem_sphinx_theme',
    install_requires=[
        'sphinx==5.1.1',
        'sphinx_rtd_theme>=1.0',
    ],
    package_data={
        'torch_fem_sphinx_theme': [
            'theme.conf',
            *package_files('torch_fem_sphinx_theme/static',
                           ['css', 'js', 'png', 'svg']),
        ]
    },
    entry_points={
        'sphinx.html_themes': [
            'torch_fem_sphinx_theme = torch_fem_sphinx_theme',
        ]
    },
    packages=find_packages(),
    include_package_data=True,
)
