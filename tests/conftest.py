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


@pytest.fixture(scope='module')
def cesm_data():
    df = pd.DataFrame(
        [
            {
                'casename': 'g.e22.G1850ECO_JRA_HR.TL319_t13.004',
                'depth_level': -9999.0,
                'log_10': True,
                'time': '0005-01-16 12:00:00',
                'varname': 'CaCO3_FLUX_100m',
                'path': 's3://ncar-cesm-pop-test/images/g.e22.G1850ECO_JRA_HR.TL319_t13.004/timestep-global-map/CaCO3_FLUX_100m+0005-01-16 12:00:00+log_10@True.png',
            },
            {
                'casename': 'g.e22.G1850ECO_JRA_HR.TL319_t13.004',
                'depth_level': -9999.0,
                'log_10': True,
                'time': '0003-01-16 12:00:00',
                'varname': 'photoC_sp_zint',
                'path': 's3://ncar-cesm-pop-test/images/g.e22.G1850ECO_JRA_HR.TL319_t13.004/timestep-global-map/photoC_sp_zint+0003-01-16 12:00:00+log_10@True.png',
            },
            {
                'casename': 'g.e22.G1850ECO_JRA_HR.TL319_t13.003',
                'depth_level': 500.0,
                'log_10': True,
                'time': '0001-08-16 12:00:00',
                'varname': 'SiO3',
                'path': 's3://ncar-cesm-pop-test/images/g.e22.G1850ECO_JRA_HR.TL319_t13.003/timestep-global-map/SiO3+0001-08-16 12:00:00+log_10@True+z_t@500.0.png',
            },
            {
                'casename': 'g.e22.G1850ECO_JRA_HR.TL319_t13.003',
                'depth_level': 500.0,
                'log_10': True,
                'time': '0004-11-16 00:00:00',
                'varname': 'coccoChl',
                'path': 's3://ncar-cesm-pop-test/images/g.e22.G1850ECO_JRA_HR.TL319_t13.003/timestep-global-map/coccoChl+0004-11-16 00:00:00+log_10@True+z_t_150m@500.0.png',
            },
            {
                'casename': 'g.e22.G1850ECO_JRA_HR.TL319_t13.004',
                'depth_level': -9999.0,
                'log_10': True,
                'time': '0002-06-16 00:00:00',
                'varname': 'photoC_diaz_zint',
                'path': 's3://ncar-cesm-pop-test/images/g.e22.G1850ECO_JRA_HR.TL319_t13.004/timestep-global-map/photoC_diaz_zint+0002-06-16 00:00:00+log_10@True.png',
            },
        ]
    )

    return df
