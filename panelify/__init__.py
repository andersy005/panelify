#!/usr/bin/env python
# flake8: noqa
"""Top-level module for panelify ."""
from pkg_resources import DistributionNotFound, get_distribution

from .canvas import Canvas  # pragma: no cover
from .dashboard import Dashboard, create_dashboard  # pragma: no cover

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:  # pragma: no cover
    # package is not installed
    _version__ = '0.0.0'  # pragma: no cover
