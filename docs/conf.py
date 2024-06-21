# -- Project information -----------------------------------------------------

repository = 'documentation'
project = 'System Level Documentation'
copyright = '2024, Analog Devices, Inc.'
author = 'Analog Devices, Inc.'

# -- General configuration ---------------------------------------------------

extensions = [
    "adi_doctools",
    "myst_parser",
    "sphinxcontrib.mermaid",
    "sphinxcontrib_d2",
]

needs_extensions = {
    'adi_doctools': '0.3.17'
}

myst_enable_extensions = [
    "colon_fence",
]

d2_config = {
    "d2_args": ["--pad 0", "-l elk"],
}

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = ['.rst', '.md']

# -- External docs configuration ----------------------------------------------

interref_repos = ['doctools']

# -- Options for HTML output --------------------------------------------------

html_theme = 'cosmic'
