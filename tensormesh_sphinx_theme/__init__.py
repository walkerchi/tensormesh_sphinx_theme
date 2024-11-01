import os.path as osp
from ._version import __version__

def setup(app):
    app.add_html_theme('tensormesh_sphinx_theme', osp.abspath(osp.dirname(__file__)))