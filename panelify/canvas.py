import dataclasses
import typing

import panel as pn

from .dashboard import Dashboard


@dataclasses.dataclass
class Canvas:
    objs: typing.Dict[str, Dashboard]

    def __post_init__(self):
        tabs = []
        for item, dash in self.objs.items():
            tabs.append((item, dash))

        self._canvas = pn.Tabs(*tabs, tabs_location='above')

    def show(self):
        return pn.Row(self._canvas)
