import pandas as pd

from panelify import Dashboard, create_dashboard


def test_dashboard_init(data):
    d = Dashboard(keys=['varname', 'experiment'], df=data, path_column='path')
    pd.testing.assert_frame_equal(d._raw_df, data)


def test_create_dashboard(data):
    d = create_dashboard(keys=['varname', 'experiment'], df=data, path_column='path')
    pd.testing.assert_frame_equal(d._raw_df, data)
