LENGTH_UNITS = type('LENGTH_UNITS', (object,), {})
LENGTH_UNITS.pc = 3.08567758149137e16
LENGTH_UNITS.AU = 149597870700
LENGTH_UNITS.km = 10**3
LENGTH_UNITS.mm = 10**-3
LENGTH_UNITS.µm = 10**-6
LENGTH_UNITS.nm = 10**-9

EM_LABELS = type('EM_LABELS', (object,), {})
EM_LABELS.A = 'current'
EM_LABELS.V = 'voltage'
EM_LABELS.Ω = 'resistance'
EM_LABELS.W = 'power'