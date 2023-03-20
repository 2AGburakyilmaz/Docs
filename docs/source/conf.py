# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Lumache'
copyright = '2021'
author = 'Graziella'

# The full version, including alpha/beta/rc tags
release = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'recommonmark',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output ----------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['css/custom.css']

# -- Options for source code -----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for Markdown -----------------------------------------------

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}

# -- Options for EPUB output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_metadata = {
    'title': 'Lumache',
    'author': 'Graziella',
    'publisher': 'Lumache',
}

epub_show_urls = 'no'
