from collections import namedtuple

LENGTH_UNITS = type('LENGTH_UNITS', (object,), {})
LENGTH_UNITS.pc = 3.08567758149137e16
LENGTH_UNITS.AU = 149597870700
LENGTH_UNITS.km = 10**3
LENGTH_UNITS.mm = 10**-3
LENGTH_UNITS.µm = 10**-6
LENGTH_UNITS.nm = 10**-9

# Needs to rename attributes in order no get information without errors
Length_units = namedtuple('Length_units', ['pc', 'AU', 'km', 'mm', 'um', 'nm'])
length_units = Length_units(
                        3.08567758149137e16,
                        149597870700,
                        10**3,
                        10**-3,
                        10**-6,
                        10**-9)

print(length_units.um)
print(LENGTH_UNITS.µm)

EM_LABELS = type('EM_LABELS', (object,), {})
EM_LABELS.A = 'current'
EM_LABELS.V = 'voltage'
EM_LABELS.Ω = 'resistance'
EM_LABELS.W = 'power'

# Needs to rename attributes in order no get information without errors
Em_labels = namedtuple('Em_labels', ['A', 'V', 'O', 'W'])
em_labels = Em_labels('current', 'voltage', 'resistance', 'power')

print(em_labels.O)
print(EM_LABELS.Ω)
