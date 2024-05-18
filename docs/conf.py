from datetime import datetime

project = "pyenergi"
copyright = f"{datetime.now().year}, Kye Russell"  # noqa: A001, DTZ005
author = "Kye Russell"

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
    "sphinx.ext.intersphinx",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

autodoc_member_order = "bysource"

html_theme = "furo"

html_static_path = ["_static"]

intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_reftypes = ["*"]
