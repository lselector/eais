"""Simple utilities module."""

import os
import sys
import pickle
import re
import json
import time
import subprocess
import datetime as dt
import unidecode as ud
from mybag import *
from util_jupyter import *

# --------------------------------------------------------------
def date_valid(date_str=None, fmt='%Y-%m-%d'):
    """Check if date_str is a valid date (default: YYYY-MM-DD)."""
    try:
        dt.datetime.strptime(date_str, fmt)
        return True
    except:
        return False

# --------------------------------------------------------------
def days_start_to_end(bag):
    """Return number of days between bag.date1 and bag.date2."""
    dt1 = dt.datetime.strptime(bag.date1, '%Y-%m-%d')
    dt2 = dt.datetime.strptime(bag.date2, '%Y-%m-%d')
    return (dt2 - dt1).days

# --------------------------------------------------------------
def get_date_shifted_by_days(start_date, num_days):
    """Return date shifted by num_days (YYYY-MM-DD format)."""
    shifted = dt.datetime.strptime(start_date, '%Y-%m-%d')
    shifted += dt.timedelta(num_days)
    return shifted.strftime('%Y-%m-%d')

# --------------------------------------------------------------
def today_yyyymmdd():
    """Return string for today in format YYYYMMDD."""
    yyyy, mm, dd = str(dt.date.today()).split('-')
    return "%s%s%s" % (yyyy, mm, dd)

# --------------------------------------------------------------
def today_yyyy_mm_dd():
    """Return string for today in format YYYY-MM-DD."""
    yyyy, mm, dd = str(dt.date.today()).split('-')
    return "%s-%s-%s" % (yyyy, mm, dd)

# --------------------------------------------------------------
def now_str():
    """Return current date-time as YYYY-MM-DD HH:MM:SS."""
    return dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# --------------------------------------------------------------
def sec_to_hms(secs):
    """Convert seconds into string in format HH:MM:SS."""
    m, s = divmod(secs, 60)
    h, m = divmod(m, 60)
    h_str = "%d" % int(h)
    m_str = "%02d" % int(m)
    s_str = "%02.2f" % round(s, 2)
    s_str = re.sub(r'\.00$', '', s_str)
    return ':'.join([h_str, m_str, s_str])

# --------------------------------------------------------------
def elapsed_time(bag, t1=None):
    """Return time elapsed from script start in seconds."""
    if t1 is None:
        t1 = bag.script_start_time
    t2 = time.time()
    return round(t2 - t1, 2)

# --------------------------------------------------------------
def elapsed_time_hms(bag, t1=None):
    """Return time elapsed from script start as HH:MM:SS."""
    return sec_to_hms(elapsed_time(bag, t1))

# --------------------------------------------------------------
def print_elapsed_time(bag, t1=None):
    """Print current date/time and elapsed time from script start."""
    time_now = now_str()
    if not t1:
        t1 = bag.script_start_time
    elapsed = elapsed_time_hms(bag, t1)
    script_cmd = bag.script_cmd
    print(f"{time_now} FINISHED ( {script_cmd} ), elapsed: {elapsed}")

# --------------------------------------------------------------
def write_bag_to_pk(bag, fname):
    """Write bag to pickle file."""
    print(f"writing bag to pickle file {fname}")
    with open(fname, 'wb') as fh:
        pickle.dump(bag, fh, protocol=pickle.HIGHEST_PROTOCOL)

# --------------------------------------------------------------
def read_pk_to_bag(fname):
    """Read pickle file into the bag variable."""
    print(f"reading file {fname} into the bag variable")
    with open(fname, 'rb') as fh:
        bag = pickle.load(fh)
    return bag

# --------------------------------------------------------------
def replace_multiple_underscores(fname):
    """Replace multiple underscores with single underscore."""
    ss = re.sub(r'_+', '_', fname)
    return ss

# --------------------------------------------------------------
def title_to_alphanum(title):
    """Convert title into alphanumeric string with underscores."""
    ascii_title = ud.unidecode(title)
    alphanum = ''.join(c if c.isalnum() else '_' for c in ascii_title)
    alphanum = replace_multiple_underscores(alphanum)
    return alphanum

# --------------------------------------------------------------
def myrun(cmd):
    """Run shell command and return output as string."""
    try:
        txt = subprocess.check_output(
            cmd, shell=True, stderr=subprocess.STDOUT
        )
    except Exception as e:
        txt = e.output
    txt = txt.decode().strip()
    return txt

# --------------------------------------------------------------
def convert_to_json(bag):
    """Write scraped data into JSON file."""
    mydict = {
        "title": bag.title,
        "text": bag.content,
        "date": bag.date,
        "date_run": bag.date_run,
        "link": bag.url
    }

    os.makedirs(bag.directory_path, exist_ok=True)
    fpath = bag.directory_path + bag.file_name + ".json"
    with open(fpath, "w", encoding="utf-8") as fh:
        json.dump(mydict, fh, indent=4)