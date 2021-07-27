import typing

import panel as pn
import pydantic

from .dashboard import Dashboard


@pydantic.dataclasses.dataclass
class Canvas:
    """
    A Canvas is a collection of Dashboards.
    """

    objs: typing.Dict[str, Dashboard]

    def __post_init_post_parse__(self):
        tabs = [(item, dash) for item, dash in self.objs.items()]
        self._canvas = pn.Tabs(*tabs, tabs_location='above')

    def show(self):
        """
        Show the canvas.
        """
        return pn.Row(self._canvas)
