"""
'xxxx' # optimal endcase


'yyyyy' # suboptimal endcase

# If I always destroy the most common elements, assume that this does not
# always give me the optimal endcase.

# Thus, there will be a case where the above occurs.

'xxxx...a'
'yyyyyy...b'

N is number of times optimal had to go back to reach suboptimal as it went
backwards.
"""

import sys
import math

caseN = int(sys.stdin.readline())
for i in range(caseN):
    length = int(sys.stdin.readline())
    cutoff = int(math.ceil(length / 2.0))

    counter = dict()
    max_freq = 0
    for num in sys.stdin.readline().split():
        n = int(num)
        counter[n] = counter.get(n, 0) + 1
        max_freq = max(max_freq, counter[n])

    print cutoff if max_freq <= cutoff else max_freq
