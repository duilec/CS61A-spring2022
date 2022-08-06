import re

# q1 Greetings
def greetings(message):
    """
    Returns whether a string is a greeting. Greetings begin with either Hi, Hello, or
    Hey (first letter either capitalized or lowercase), and/or end with Bye (first letter 
    either capitalized or lowercase) optionally followed by an exclamation point or period.

    >>> greetings("Hi! Let's talk about our favorite submissions to the Scheme Art Contest")
    True
    >>> greetings("Hey I love Taco Bell")
    True
    >>> greetings("I'm going to watch the sun set from the top of the Campanile! Bye!")
    True
    >>> greetings("Bye Bye Birdie is one of my favorite musicals.")
    False
    >>> greetings("High in the hills of Berkeley lived a legendary creature. His name was Oski")
    False
    >>> greetings('Hi!')
    True
    >>> greetings("bye")
    True
    """
    return bool(re.search(r"^[Hh][iloey]{1,4}[\s!]+|[Bb]?ye[!\.]?$", message))
    
    #reference using ground of "()" and begin or end of "\b"
    #using
    return bool(re.search(r"(^([Hh](ey|i|ello)\b))|(\b[bB]ye[!\.]?$) ", message))

# q2 Basic URL Validation
# note: use "$" to end of URL
def match_url(text):
    """
    >>> match_url("https://cs61a.org/resources/#regular-expressions")
    True
    >>> match_url("https://pythontutor.com/composingprograms.html")
    True
    >>> match_url("https://pythontutor.com/should/not.match.this")
    False
    >>> match_url("https://link.com/nor.this/")
    False
    >>> match_url("http://insecure.net")
    True
    >>> match_url("htp://domain.org")
    False
    """
    scheme = r'^http[s]?:\/\/'
    domain = r'[\w\.]+'
    path = r'(\/([\w]+\.\w+|([\w\/])+))?'
    anchor = r'(\/\#[\w\-]+)?$'
    full_string = scheme + domain + path + anchor
    return bool(re.match(full_string, text))

    # reference solution
    # note:not just ".html" file
    # scheme = r"(https?:\/\/)?" 
    # domain = r"\w+\.\w+" 
    # path = r"(\/\w+)*(\.\w+)?" 
    # anchor = r"(\/#[\w-]+)?$" 
    # full_string = scheme + domain + path + anchor 
    # return bool(re.match(full_string, text))