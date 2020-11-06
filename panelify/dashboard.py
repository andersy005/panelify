from collections import OrderedDict

import pandas as pd
import param


class Dashboard(param.Parameterized):
    def __init__(self, keys, df, path_column, **params):
        super().__init__(**params)
        self.keys = sorted(keys)
        self.path_column = path_column
        self._raw_df = df
        uniques = self._uniques(self._raw_df)
        self._set_index(self._raw_df)
        for column in self.keys:
            self.param._add_parameter(
                column, param.ObjectSelector(objects=uniques[column], default=uniques[column][0])
            )

    def _get_item(self):
        values = OrderedDict()
        for k in self.keys:
            values[k] = getattr(self, k)

        return self.df.xs(key=list(values.values()), level=list(values.keys()))

    def _get_image_path(self):
        item = self._get_item()
        if not item.empty:
            return item.iloc[0][self.path_column]
        return 'No image'

    def _set_index(self, data):
        self.df = data[self.keys + [self.path_column]].set_index(self.keys)

    def _uniques(self, data):
        uniques = data.apply(pd.unique)[self.keys].map(sorted)
        return uniques
