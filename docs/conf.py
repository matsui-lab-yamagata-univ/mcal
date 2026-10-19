import os
import re
import sys


sys.path.insert(0, os.path.abspath("../src"))

def _get_version() -> str:
    init_path = os.path.join(os.path.dirname(__file__), "../src/mcal/__init__.py")
    with open(init_path) as f:
        match = re.search(r'^__version__\s*=\s*["\']([^"\']+)["\']', f.read(), re.MULTILINE)
    if match:
        return match.group(1)
    raise RuntimeError("Unable to find __version__ in mcal/__init__.py")

project = "mcal"
copyright = "2025, Hiroyuki Matsui, Koki Ozawa"
author = "Hiroyuki Matsui, Koki Ozawa"
version = _get_version()
release = version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinxcontrib.autodoc_pydantic",
    "sphinx_new_tab_link",
]

# Optional dependencies not installed in the docs build environment
autodoc_mock_imports = ["pyscf", "gpu4pyscf", "opi"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = []
