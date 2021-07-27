import uuid
from collections import OrderedDict

import fsspec
import matplotlib.image as img
import matplotlib.pyplot as plt
import pandas as pd
import panel as pn
import param

_DEFAULT_WIDGETS = {'discrete_slider': pn.widgets.DiscreteSlider}


class Dashboard(param.Parameterized):
    def __init__(
        self, keys, df, path_column, storage_options=None, column_widget_types=None, **params
    ):
        super().__init__(**params)
        self.keys = sorted(keys)
        self.path_column = path_column
        self._raw_df = df.copy()
        uniques = self._uniques(self._raw_df)
        self._set_index(self._raw_df)
        self.widgets = {}
        column_widget_types = column_widget_types or {}
        for column in self.keys:
            self.param._add_parameter(
                column, param.ObjectSelector(objects=uniques[column], default=uniques[column][0])
            )
            if column in column_widget_types:
                value = column_widget_types[column]
                try:
                    self.widgets[column] = _DEFAULT_WIDGETS[value]
                except KeyError:
                    raise KeyError(
                        f'{value} is not a valid value. Valid values are: {list(_DEFAULT_WIDGETS.keys())}'
                    )

        self.storage_options = storage_options or {}

    def _get_item(self):
        values = OrderedDict()
        for k in self.keys:
            values[k] = getattr(self, k)

        return self.df.xs(key=list(values.values()), level=list(values.keys()))

    def _get_image_path(self):
        item = self._get_item()
        if not item.empty:
            return item.iloc[0][self.path_column]
        return None

    def imread(self):
        nrows, ncols = 1, 1
        fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(8.5, 6.5), squeeze=True)
        image = self._get_image_path()
        if image:
            with fsspec.open(image, **self.storage_options) as fobj:
                data = img.imread(fobj)
            ax.imshow(data)
        ax.axis('off')
        plt.tight_layout()
        plt.close(fig)
        return fig

    def view(self):
        return pn.Column(
            pn.WidgetBox(pn.panel(self.param, widgets=self.widgets), pn.Row(self.imread))
        )

    def _set_index(self, data):
        self.df = data[self.keys + [self.path_column]].set_index(self.keys)

    def _uniques(self, data):
        return data.apply(pd.unique)[self.keys].map(sorted)


def create_dashboard(
    keys: list,
    df: pd.DataFrame,
    path_column: str,
    storage_options: dict = None,
    column_widget_types: dict = None,
    **params,
) -> Dashboard:
    """
    Lets you define dashboard class dynamically. We must use this function
    to create dashboard instances because `.param` attribute defined in Dashboard class
    is a class attribute and not an instance attribute.

    Parameters
    ----------
    keys: list
        List of column names.
    df: pandas.DataFrame
        DataFrame containing data.
    path_column: str
        Name of column containing path to image.
    storage_options: dict
        Keyword arguments to pass to fsspec.open.
    column_widget_types: dict
        Dictionary mapping column names to widget types.
    params: dict
        Dictionary of parameters to pass to Dashboard class.
    """
    _id = f"Dashboard{str(uuid.uuid4()).split('-')[0]}"
    _class = type(_id, (Dashboard,), {})
    return _class(
        keys,
        df,
        path_column,
        storage_options=storage_options,
        column_widget_types=column_widget_types,
        **params,
    )
