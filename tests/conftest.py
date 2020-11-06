import pandas as pd
import pytest


@pytest.fixture(scope='module')
def data():
    df = pd.DataFrame(
        {
            'varname': ['O2', 'O2', 'NH4'],
            'experiment': ['RCP', 'HIST', 'RCP'],
            'path': ['file1', 'file2', 'file3'],
        }
    )
    return df
