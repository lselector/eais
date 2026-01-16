"""MyBunch class - dict-like container by Lev Selector, 2012-2024."""

import os
import sys
import re

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
os.environ["PYTHONUNBUFFERED"] = "1"
import pandas as pd

# --------------------------------------------------------------
class MyBunch(dict):
    """Dict-like class with attribute access (obj.key and obj['key'])."""

    # ----------------------------------------------------------
    def __init__(self, **kw):
        """Initialize MyBunch with optional keyword arguments."""
        dict.__init__(self, kw)
        self.__dict__ = self

    # ----------------------------------------------------------
    def __getstate__(self):
        """Return state for pickle protocol."""
        return self

    # ----------------------------------------------------------
    def __setstate__(self, state):
        """Restore state from pickle protocol."""
        self.update(state)
        self.__dict__ = self

    # ----------------------------------------------------------
    def __repr__(self):
        """String representation for interactive use."""
        ks = sorted([x for x in self.keys()])
        if len(ks) <= 0:
            return ""
        ss = "\n"
        len_n_elems = 100
        len_list_str = 50
        mytab = max(len(w) for w in ks)
        for kk in ks:
            aa = self[kk]
            if callable(aa):
                ss += "%s()\n" % kk
                continue
            format_str = "%-" + str(mytab) + "s = "
            ss += format_str % kk
            ss += self._format_value(aa, len_n_elems, len_list_str)
        return ss

    # ----------------------------------------------------------
    def _format_value(self, aa, len_n_elems, len_list_str):
        """Format a single value for repr output."""
        if type(aa) == pd.DataFrame:
            return "(df - %d rows)\n" % (len(aa))
        elif type(aa).__name__ == 'MyBunch':
            return "(MyBunch - %d elems)\n" % (len(aa))
        elif type(aa) in [set, list, dict, tuple]:
            return self._format_collection(aa, len_n_elems, len_list_str)
        elif type(aa) in [str]:
            return self._format_string(aa)
        elif hasattr(aa, "__str4bag__") and callable(aa.__str4bag__):
            return aa.__str4bag__() + "\n"
        else:
            return str(aa) + "\n"

    # ----------------------------------------------------------
    def _format_collection(self, aa, len_n_elems, len_list_str):
        """Format collection types (list, dict, set, tuple)."""
        mylen = len(aa)
        if type(aa) == list:
            mystr = str(aa[:len_n_elems])
            word = 'list'
        elif type(aa) == tuple:
            mystr = str(aa[:len_n_elems])
            word = 'tuple'
        elif type(aa) == dict:
            mydict = dict(list(aa.items())[:len_n_elems])
            mystr = str(mydict)
            word = 'dict'
        elif type(aa) == set:
            mystr = str(list(aa)[:len_n_elems])
            word = 'set'
        if len(mystr) >= (len_list_str + 4):
            mystr = mystr[:len_list_str] + " ..."
        return "%s %d elems: %s\n" % (word, mylen, mystr)

    # ----------------------------------------------------------
    def _format_string(self, aa):
        """Format string values with truncation if needed."""
        tmp = aa
        nnn = len(tmp)
        if nnn > 75:
            tmp = tmp[:75] + " ... " + " (len(str) = %d)" % nnn
        return "%r\n" % (tmp)

    # ----------------------------------------------------------
    def __str__(self):
        """Provide a list of members."""
        return self.__repr__()

# --------------------------------------------------------------
def test_avail(container, mem_str):
    """Recursive procedure to test if bunch members exist."""
    mem_str = mem_str.strip()
    if not len(mem_str):
        return False
    elems = mem_str.split('.')
    first_elem = elems.pop(0)
    if first_elem not in container:
        return False
    elif len(elems) >= 1:
        return test_avail(container[first_elem], '.'.join(elems))
    else:
        return True