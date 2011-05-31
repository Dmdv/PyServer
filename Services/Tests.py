__author__ = 'Dmdv'

try:
    import win32pdh
    print("win32pdh imported")
except ImportError:
    print('No performance data helper installed')