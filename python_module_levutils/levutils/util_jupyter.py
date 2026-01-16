"""Helper functions for jupyter notebook by Lev Selector, 2019."""

import sys
import os
import pandas as pd
import numpy as np
import time
import glob
import re
import pickle
import gc
import datetime as dt
from IPython import get_ipython
from IPython.display import display, Image

# --------------------------------------------------------------
def is_jupyter():
    """Check if running in Jupyter notebook."""
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True
        elif shell == 'TerminalInteractiveShell':
            return False
        else:
            return False
    except NameError:
        return False

# --------------------------------------------------------------
def is_ipython():
    """Check if running in IPython terminal."""
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'TerminalInteractiveShell':
            return True
        else:
            return False
    except NameError:
        return False

# --------------------------------------------------------------
def sdf(df, detail=1, label=""):
    """Display DataFrame info: Nrows, Ncols, and more by detail."""
    Nrows = len(df)
    Ncols = len(df.columns)
    if len(label) >= 1:
        print(label, " : ", end="")
    print(f"rows = {Nrows:2,d}, cols = {Ncols:2,d}, {list(df.columns)}")
    if detail >= 1:
        print("HEAD:")
        display(df.head(3))
        print("TAIL:")
        display(df.tail(3))
        print('-' * 50)
    if detail >= 2:
        print('SUMMARY :')
        display(df.describe(include='all'))
        print('*' * 50)

# --------------------------------------------------------------
def date_time():
    """Return string YYYY-MM-DD HH:MM:SS."""
    now_str = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return now_str

# --------------------------------------------------------------
def date_time_for_fname():
    """Return string YYYYMMDD_HHMMSS."""
    now_str = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    return now_str

# --------------------------------------------------------------
def print_date_time(label="date_time"):
    """Print current date and time."""
    now_str = date_time()
    print(label, " : ", now_str)

# --------------------------------------------------------------
def sec_to_hms(secs):
    """Convert seconds into string in format Hh Mm Ss."""
    m, s = divmod(secs, 60)
    h, m = divmod(m, 60)
    h_str = "%d" % int(h)
    m_str = "%02d" % int(m)
    s_str = "%02.2f" % round(s, 2)
    s_str = re.sub(r'\.00$', '', s_str)
    return "%sh %sm %ss" % (h_str, m_str, s_str)

# --------------------------------------------------------------
def read_df_from_extract(fname=None):
    """Read file and return DataFrame."""
    print("reading", fname)
    df = pd.read_csv(fname, low_memory=False)
    df.index = range(len(df))
    df.columns = [x.lower() for x in list(df.columns)]
    print(" " * 20 + "%d cols, %d rows" % (len(df.columns), len(df)))
    return df

# --------------------------------------------------------------
def today_yyyymmdd():
    """Return string for today in format YYYYMMDD."""
    yyyy, mm, dd = str(dt.date.today()).split('-')
    return "%s%s%s" % (yyyy, mm, dd)

# --------------------------------------------------------------
def delete_dataframes():
    """Delete all DataFrames from memory."""
    myvars = globals()
    for vv in sorted(myvars):
        if 'DataFrame' in str(type(eval(vv))):
            del globals()[vv]
    gc.collect()

# --------------------------------------------------------------
def df_memory(df):
    """Return memory usage of pandas DataFrame in MB."""
    return df.memory_usage(deep=True).sum() / 1024.0 / 1024.0

# --------------------------------------------------------------
def shout_error(ss, rep=10):
    """Print error message multiple times and exit."""
    for ii in range(rep):
        print("ERROR, ", ss)

    try:
        run_step
    except NameError:
        run_step = -1
    run_step -= 1

    try:
        ok_flag
    except NameError:
        ok_flag = False
    ok_flag = False

    sys.exit(1)

# --------------------------------------------------------------
def ddd(nrows=10):
    """Return a simple pandas DataFrame for quick tests."""
    n_aa = 10
    nn = int(nrows / n_aa)
    if nn < 1:
        nn = 1
    aa = _create_test_dataframe(nn)
    aa = aa[[
        'ii', 'i1', 'i2', 'ff', 'f1', 'f2',
        'ss', 's1', 's2', 'bb', 'b1', 'xx', 'yy'
    ]].copy()
    aa.index = range(len(aa))
    if 1 <= nrows < 10:
        aa = aa[:nrows + 1]
    return aa

# --------------------------------------------------------------
def _create_test_dataframe(nn):
    """Create test DataFrame with sample data."""
    return pd.DataFrame({
        'ii': nn * [0, 1, 2, 3, 4, 5, np.nan, 7, 8, 9],
        'i1': nn * [6, 5, 4, 3, 2, 1, 0, -1, -2, -3],
        'i2': nn * [6, 5, 4, 4, 1, 1, 0, -1, -2, -3],
        'ff': nn * [0.0, 1.0, 2.0, np.NaN, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0],
        'f1': nn * [0.0, 1.01, 2.002, 3.0003, 4.00004,
                    5.000005, 6.0000006, 7.0, 8.0, 9.0],
        'f2': nn * [1.11, 2.22, 3.33, 4.44, 5.55,
                    7.77, 9.99, 0.01, -0.01, -1.11],
        'ss': nn * ['s0', 's1', '狗', '汽车', np.nan,
                    's5', 's6', 's7', 's8', 's9'],
        's1': nn * list(np.array(
            ['s0', 's1', 's2', 's2', np.nan,
             's5', 's6', 's7', 's8', 's9'], dtype=np.str_)),
        's2': nn * ['1.11', '2.22', '3.33', '4.44', '5.55',
                    '7.77', '9.99', '0.01', '-0.01', '-1.11'],
        'bb': nn * [True, False, True, False, np.nan,
                    False, True, np.nan, False, True],
        'b1': nn * [True, False, True, False, True,
                    False, True, True, False, True],
        'xx': nn * list(range(10)),
        'yy': nn * [x * 50 + 60 + np.random.randn() for x in range(10)]
    })

# --------------------------------------------------------------
def cell_width(width_pct=95):
    """Set width of jupyter cells (in percentage of window)."""
    from IPython.core.display import display, HTML
    ss = """<style>
              .container {width:__CHANGE_ME__ !important;}
            </style>
         """
    ss = ss.replace("__CHANGE_ME__", str(width_pct) + "%")
    display(HTML(ss))
    return HTML(ss)

# --------------------------------------------------------------
def commify(n, show_cents=False):
    """Add commas to money amount."""
    if n is None:
        return None
    if n < 0:
        return '-' + commify(-n, show_cents)
    n = round(n, 2)
    dollars = int(n)
    cents = round((n - dollars) * 100)
    dollars = '%d' % dollars
    cents = '%02d' % cents
    groups = []
    while dollars and dollars[-1].isdigit():
        groups.append(dollars[-3:])
        dollars = dollars[:-3]
    ss = dollars + ','.join(reversed(groups))
    if show_cents:
        ss = ss + '.' + cents
    return ss

# --------------------------------------------------------------
def commify2(n):
    """Add commas to money amount and show cents."""
    return commify(n, True)

# --------------------------------------------------------------
def commify2_dollar(n):
    """Add commas, show cents, prepend dollar sign."""
    return "$" + commify2(n)