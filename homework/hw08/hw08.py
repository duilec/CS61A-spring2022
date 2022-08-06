import re


def cs_classes(post):
    """
    Returns strings that look like a Berkeley CS or EE class,
    starting with "CS" or "EE", followed by a number, optionally ending with A, B, or C
    and potentially with a space between "CS" or "EE" and the number.
    Case insensitive.

    >>> cs_classes("Is it unreasonable to take CS61A, CS61B, CS70, and EE16A in the summer?")
    True
    >>> cs_classes("how do I become a TA for cs61a? that job sounds so fun")
    True
    >>> cs_classes("Can I take ECON101 as a CS major?")
    False
    >>> cs_classes("Should I do the lab lites or regular labs in EE16A?")
    True
    >>> cs_classes("thoughts on ee127?")
    True
    >>> cs_classes("Is 70 considered an EECS class?")
    False
    >>> cs_classes("What are some good CS upper division courses? I was thinking about CS 161 or CS 169a")
    True
    """
    return bool(re.search(r"([Cc][Ss]|[Ee]{2,2})[\s]?([0-9]+)[a-zA-Z]?", post))

    # reference 
    # directly using "(ee|EE|cs|CS)"
    return bool(re.search(r"(ee|EE|cs|CS)\s?\d+[a-cA-C]?", post))

import re


def match_time(text):
    """
    >>> match_time("At 07:23AM, I woke up and had some coffee.")
    True
    >>> match_time("I looked at my phone at 12:22 to check the weather.")
    True
    >>> match_time("At 05:24PM, I had sesame bagels with cream cheese.")
    True
    >>> match_time("At 23:59 I was sound asleep.")
    True
    >>> match_time("After, the clocked turned to 00:00.")
    True
    >>> match_time("Mix water in a 1:2 ratio with chicken stock.")
    False
    >>> match_time("At work, I pinged 127.0.0.1:80.")
    False
    >>> match_time("The tennis score was 40:30.")
    False
    """
    return bool(re.search(r"[0-2][0-3]:[0-5][\d]|(0[\d]|1[0-2]):[0-5][\d](am|AM|pm|PM)?", text))

    # reference:
    # note: using "\b" in begin and end
    return bool(re.search(r"\b(([01]?\d)|(2[0123])):[012345]\d([AaPp][Mm])?\b", text))
