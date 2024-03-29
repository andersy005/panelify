# Panelify

---
⚠️ Warning

This project is no longer being actively maintained and there are no plans to update it in the future. As such, I cannot guarantee that the code and resources contained in this repository are up-to-date or secure.

I strongly advise you to exercise caution if you decide to continue using or building upon the work that has been done here. You should carefully review and test any code that you plan to use, and you should be aware that there may be security vulnerabilities or other issues that could impact your project.

--- 

- [Panelify](#panelify)
  - [Badges](#badges)
  - [Overview](#overview)
    - [Why use Panelify?](#why-use-panelify)
  - [Installation (COMING SOON)](#installation-coming-soon)

## Badges

| CI          | [![GitHub Workflow Status][github-ci-badge]][github-ci-link] [![GitHub Workflow Status][github-lint-badge]][github-lint-link] [![Code Coverage Status][codecov-badge]][codecov-link] |
| :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| **Docs**    |                                                                    [![Documentation Status][rtd-badge]][rtd-link]                                                                    |
| **Package** |                                                         [![Conda][conda-badge]][conda-link] [![PyPI][pypi-badge]][pypi-link]                                                         |
| **License** |                                                                        [![License][license-badge]][repo-link]                                                                        |

## Overview

Panelify is a Python library that makes it easy to create dashboards from **static images/plots/charts** via the [Panel](https://panel.holoviz.org/) and [Pandas](https://pandas.pydata.org/) libraries.

### Why use Panelify?

- **Simple API**: We've attempted to make the API as intuitive and easy to learn as possible.
- **Flexibity**: Panelify is built on top of [Panel](https://panel.holoviz.org/), so if you need more control, you can always fall back on Panel's API.

## Installation (COMING SOON)

Panelify can be installed from PyPI with pip:

```bash
python -m pip install panelify
```

Panelify will also be available from conda-forge for conda installations:

```bash
conda install -c conda-forge panelify
```

See [documentation](https://panelify.readthedocs.io) for more information.

[github-ci-badge]: https://img.shields.io/github/workflow/status/andersy005/panelify/CI?label=CI&logo=github&style=for-the-badge
[github-lint-badge]: https://img.shields.io/github/workflow/status/andersy005/panelify/linting?label=linting&logo=github&style=for-the-badge
[github-ci-link]: https://github.com/andersy005/panelify/actions?query=workflow%3ACI
[github-lint-link]: https://github.com/andersy005/panelify/actions?query=workflow%3Alinting
[codecov-badge]: https://img.shields.io/codecov/c/github/andersy005/panelify.svg?logo=codecov&style=for-the-badge
[codecov-link]: https://codecov.io/gh/andersy005/panelify
[rtd-badge]: https://img.shields.io/readthedocs/panelify/latest.svg?style=for-the-badge
[rtd-link]: https://panelify.readthedocs.io/en/latest/?badge=latest
[pypi-badge]: https://img.shields.io/pypi/v/panelify?logo=pypi&style=for-the-badge
[pypi-link]: https://pypi.org/project/panelify
[conda-badge]: https://img.shields.io/conda/vn/conda-forge/panelify?logo=anaconda&style=for-the-badge
[conda-link]: https://anaconda.org/conda-forge/panelify
[license-badge]: https://img.shields.io/github/license/andersy005/panelify?style=for-the-badge
[repo-link]: https://github.com/andersy005/panelify
