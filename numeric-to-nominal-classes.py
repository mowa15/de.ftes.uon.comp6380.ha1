__author__ = 'Fredrik'

in_name = 'data-with-headers-tabs.txt'
out_name = 'data-with-headers-tabs-nominal.txt'


with open(in_name) as f_in:
    with open(out_name, 'w') as f_out:
        for line in f_in.readlines():
            line = line.replace('\t1.0', '\t1')
            line = line.replace('\t0.0', '\t2')
            f_out.write(line)