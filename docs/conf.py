import os
import sys
sys.path.insert(0, os.path.abspath('..'))
from main import * 
from api import *

project = 'OSC-API'
copyright = '2022, Siddhesh Zantye'
author = 'Siddhesh Zantye'

release = '1.0.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',

]
templates_path = ['_templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']