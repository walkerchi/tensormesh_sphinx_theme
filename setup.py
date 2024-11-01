import os
import os.path as osp
import re
from typing import List, Optional

from setuptools import find_packages, setup

def read_version():
    version_file = os.path.join(os.path.dirname(__file__), 'tensormesh_sphinx_theme', '_version.py')
    with open(version_file, 'r') as f:
        version_content = f.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_content, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")



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
    name='tensormesh_sphinx_theme',
    version=read_version(),
    author='walker chi',
    author_email='walker.chi.000@gmail.com',
    url='https://github.com/walkerchi/tensormesh_sphinx_theme',
    install_requires=[
        'sphinx==5.1.1',
        'sphinx_rtd_theme>=1.0',
    ],
    package_data={
        'tensormesh_sphinx_theme': [
            'theme.conf',
            *package_files('tensormesh_sphinx_theme/static',
                           ['css', 'js', 'png', 'svg']),
        ]
    },
    entry_points={
        'sphinx.html_themes': [
            'tensormesh_sphinx_theme = tensormesh_sphinx_theme',
        ]
    },
    packages=find_packages(),
    include_package_data=True,
)
