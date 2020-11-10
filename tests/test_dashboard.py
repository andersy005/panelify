import matplotlib
import pandas as pd

from panelify import Dashboard, create_dashboard


def test_create_dashboard(data):
    d = create_dashboard(keys=['varname', 'experiment'], df=data, path_column='path')
    pd.testing.assert_frame_equal(d._raw_df, data)
    assert isinstance(d, Dashboard)


def test_dashboard_imread(cesm_data):
    d = create_dashboard(
        keys=['casename', 'varname', 'depth_level', 'time', 'log_10'],
        df=cesm_data,
        path_column='path',
        column_widget_types={'time': 'discrete_slider'},
    )
    fig = d.imread()
    assert isinstance(fig, matplotlib.figure.Figure)
