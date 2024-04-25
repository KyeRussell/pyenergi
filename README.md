<h1 align="center">pyenergi</h1>
<p align="center"><em>
    Unofficial Python API client for the myenergi API.
</em></p>

<p align="center">
    <a href="https://pypi.org/project/pyenergi/"><img src="https://img.shields.io/pypi/v/pyenergi?color=%2334D058&label=PyPI%20package" alt="PyPI version"></a>
    <a href="https://github.com/KyeRussell/pyenergi/actions/workflows/release.yaml"><img src="https://github.com/KyeRussell/pyenergi/actions/workflows/release.yaml/badge.svg" alt="Release workflow status"></a>
    <a href="https://codecov.io/gh/KyeRussell/pyenergi" ><img src="https://codecov.io/gh/KyeRussell/pyenergi/graph/badge.svg?token=2XY75VWMGK"></a>
    <a href="https://pyenergi.readthedocs.io"><img src="https://readthedocs.org/projects/pyenergi/badge/" alt="Documentation on Read The Docs"></a>
</p>

---

This project is not remotely ready for anyone to look at, let alone use. It is in a very early proof-of-concept stage, focusing on iterative research and development. I have not settled on the project's architecture, and I am still exploring the problem space. As such, the quality of the code is very poor, and things are guaranteed to change.

I will not provide support, nor am I accepting PRs at this time.

---

## Developing

Clone the repository and run the following command:

```bash
uv pip install -e . -r pyproject.toml --extra=dev --extra=docs
```

This will install the project in editable mode with all development dependencies.

### Running tests

```bash
pytest
```
