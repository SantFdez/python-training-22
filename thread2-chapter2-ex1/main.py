from collections import namedtuple

def get_length_units():
    # Needs to rename attributes in order no get information without errors
    Length_units = namedtuple('Length_units', ['pc', 'AU', 'km', 'mm', 'um', 'nm'])
    length_units = Length_units(
                            3.08567758149137e16,
                            149597870700,
                            10**3,
                            10**-3,
                            10**-6,
                            10**-9)
    return length_units

def get_em_labels():
    # Needs to rename attributes in order no get information without errors
    Em_labels = namedtuple('Em_labels', ['A', 'V', 'O', 'W'])
    em_labels = Em_labels('current', 'voltage', 'resistance', 'power')
    return em_labels
