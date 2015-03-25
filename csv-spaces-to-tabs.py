__author__ = 'Fredrik'

in_name = 'data-with-headers.txt'
out_name = 'data-with-headers-tabs.txt'

import re, os
pattern = re.compile('\s+')
def spaces_to_tabs(line):
    line = line.rstrip('\n')
    line = line.strip(' ')
    return pattern.sub('\t', line)


# print(spaces_to_tabs(' test  b 1.0'))

with open(in_name) as f_in:
    with open(out_name, 'w') as f_out:
        for line in f_in.readlines():
            f_out.write(spaces_to_tabs(line) + '\n')