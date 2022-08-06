import re

def match_gme(tweet):
    """
    >>> match_gme('GME')
    True
    >>> match_gme('yooo buy GME right now!')
    True
    >>> match_gme('#HUGME')
    False
    >>> match_gme('#HUGMEHARDER')
    False
    """
    return bool(re.search(r'^GME|[^#HU]+GME[^#HARDER]+', tweet))