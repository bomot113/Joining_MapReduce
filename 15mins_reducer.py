#!/usr/bin/env python

import sys
from operator import itemgetter
def main(argv):
    total_e = 0
    fid = "-1"
    f_name = None
    e = "-1"
    time = ""
    current_time = None    
    current_fid = None
    for line in sys.stdin:
          # remove leading and trailing whitespace
          line = line.strip()
          # parse the input we got from mapper.py
          fid, time, f_name, e_str = line.split('\t', 3)
          
          # convert e (currently a string) to int
          try:
              e = int(e_str)
          except ValueError:
              # count was not a number, so silently
              # ignore/discard this line
              continue
          
          # first line reading
          if current_time == None:
            current_time = time
            current_fid = fid
            count_e = 1
            

          # this IF-switch only works because Hadoop sorts map output
          # by key (here: fid, time) before it is passed to the reducer
          if (fid != current_fid) | (current_time != time):
              print '%s\t%s\t%s\t%.2f' % (fid, f_name, current_time, total_e)
              current_time = time
              current_fid  = fid
              total_e = e

          # aggregate function grouped by time
          total_e += e
    # do not forget to output the last word!
    if (current_time != None):
      print '%s\t%s\t%s\t%.2f' % (fid, f_name, current_time, total_e)
if __name__ == "__main__":
    main(sys.argv)

