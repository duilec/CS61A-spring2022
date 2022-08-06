import numbers
import builtins

from ucb import main, trace, interact
from scheme_tokens import tokenize_lines, DELIMITERS

from buffer import Buffer, InputReader, LineReader
from pair import Pair, nil
# Buffer(iter([['(', '+'], [15], [], [12, ')']]))
read_tail(Buffer(tokenize_lines(['1 2 3)'])))
Pair(1, Pair(2, Pair(3, nil)))

read_tail(Buffer(tokenize_lines(['2 (3 4))'])))
Pair(Pair(3, Pair(4, nil)), nil)
Pair(2)
Pair(2, Pair(Pair(3, Pair(4, nil)), nil))