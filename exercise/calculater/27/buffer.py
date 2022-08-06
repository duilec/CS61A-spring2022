""#line:1
import math #line:3
class Buffer (object ):#line:5
    ""#line:49
    def __init__ (OO0OOOO00O00OO0OO ,O00O0O00O0O0OOOOO ):#line:50
        OO0OOOO00O00OO0OO .index =0 #line:51
        OO0OOOO00O00OO0OO .lines =[]#line:52
        OO0OOOO00O00OO0OO .source =O00O0O00O0O0OOOOO #line:53
        OO0OOOO00O00OO0OO .current_line =()#line:54
        OO0OOOO00O00OO0OO .current #line:55
    def pop_first (OO0O0OO00OO0OOO00 ):#line:57
        ""#line:59
        O0OO00O00OOO000O0 =OO0O0OO00OO0OOO00 .current #line:60
        OO0O0OO00OO0OOO00 .index +=1 #line:61
        return O0OO00O00OOO000O0 #line:62
    @property #line:64
    def more_on_line (OO0OO0O000O00O0O0 ):#line:65
        return OO0OO0O000O00O0O0 .index <len (OO0OO0O000O00O0O0 .current_line )#line:66
    @property #line:68
    def current (O0O0O0OOOO00O0OO0 ):#line:69
        ""#line:70
        while not O0O0O0OOOO00O0OO0 .more_on_line :#line:71
            O0O0O0OOOO00O0OO0 .index =0 #line:72
            try :#line:73
                O0O0O0OOOO00O0OO0 .current_line =next (O0O0O0OOOO00O0OO0 .source )#line:74
                O0O0O0OOOO00O0OO0 .lines .append (O0O0O0OOOO00O0OO0 .current_line )#line:75
            except StopIteration :#line:76
                O0O0O0OOOO00O0OO0 .current_line =()#line:77
                return None #line:78
        return O0O0O0OOOO00O0OO0 .current_line [O0O0O0OOOO00O0OO0 .index ]#line:79
    def __str__ (O00O0OOO000O0OOO0 ):#line:81
        ""#line:82
        OO00000OO0OOO0000 =len (O00O0OOO000O0OOO0 .lines )#line:84
        OO0O000OO0OOO0000 ='{0:>'+str (math .floor (math .log10 (OO00000OO0OOO0000 ))+1 )+"}: "#line:85
        O0O0000O0O0OOOO0O =''#line:88
        for O0000OOOOO0000O00 in range (max (0 ,OO00000OO0OOO0000 -4 ),OO00000OO0OOO0000 -1 ):#line:89
            O0O0000O0O0OOOO0O +=OO0O000OO0OOO0000 .format (O0000OOOOO0000O00 +1 )+' '.join (map (str ,O00O0OOO000O0OOO0 .lines [O0000OOOOO0000O00 ]))+'\n'#line:90
        O0O0000O0O0OOOO0O +=OO0O000OO0OOO0000 .format (OO00000OO0OOO0000 )#line:91
        O0O0000O0O0OOOO0O +=' '.join (map (str ,O00O0OOO000O0OOO0 .current_line [:O00O0OOO000O0OOO0 .index ]))#line:92
        O0O0000O0O0OOOO0O +=' >> '#line:93
        O0O0000O0O0OOOO0O +=' '.join (map (str ,O00O0OOO000O0OOO0 .current_line [O00O0OOO000O0OOO0 .index :]))#line:94
        return O0O0000O0O0OOOO0O .strip ()#line:95
try :#line:98
    import readline #line:99
except :#line:100
    pass #line:101
class InputReader (object ):#line:103
    ""#line:104
    def __init__ (OOO00OO0000O00O0O ,OOOO000O00OO00000 ):#line:105
        OOO00OO0000O00O0O .prompt =OOOO000O00OO00000 #line:106
    def __iter__ (OOOOO0OO00OO0O0OO ):#line:108
        while True :#line:109
            yield input (OOOOO0OO00OO0O0OO .prompt )#line:110
            OOOOO0OO00OO0O0OO .prompt =' '*len (OOOOO0OO00OO0O0OO .prompt )#line:111

