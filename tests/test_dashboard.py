import pandas as pd

from panelify import Dashboard


def test_dashboard_init(data):
    d = Dashboard(keys=['varname', 'experiment'], df=data, path_column='path')
    pd.testing.assert_frame_equal(d._raw_df, data)
