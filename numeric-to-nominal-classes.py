__author__ = 'Fredrik'

in_name = 'data-with-headers-tabs.txt'
out_name = 'data-with-headers-tabs-nominal.txt'

import re
p1 = re.compile('1.0$')
p0 = re.compile('0.0$')

with open(in_name) as f_in:
    with open(out_name, 'w') as f_out:
        for line in f_in.readlines():
            line = p1.sub('1', line)
            line = p0.sub('2', line)
            f_out.write(line)