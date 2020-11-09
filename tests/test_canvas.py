import panel as pn

from panelify import Canvas, create_dashboard


def test_canvas(data):
    d = create_dashboard(keys=['varname', 'experiment'], df=data, path_column='path')
    canvas = Canvas({'test': d.view})
    assert isinstance(canvas.show(), pn.layout.base.Row)
