def GetAdditionalFlags():
    flags = []
    return flags

# Return a list of ignored flags. Alternatively, return a function that checks
# whether a flag is ignored.
def GetIgnoredFlags():
    flags = ['-Werror']
    return flags
