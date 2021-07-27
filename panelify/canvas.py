import typing

import panel as pn
import pydantic

from .dashboard import Dashboard


class Config:
    arbitrary_types_allowed = True


@pydantic.dataclasses.dataclass(config=Config)
class Canvas:
    """
    A Canvas is a collection of Dashboards.
    """

    objs: typing.Dict[str, Dashboard]

    def __post_init_post_parse__(self):
        tabs = [(item, dash.view) for item, dash in self.objs.items()]
        self._canvas = pn.Tabs(*tabs, tabs_location='above')

    def show(self):
        """
        Show the canvas.
        """
        return pn.Row(self._canvas)
