#!/usr/bin/env python
import sys, datetime, math
from operator import itemgetter
def main(argv):
  for line in sys.stdin:
    # line = did, fid, f_sname, time_logged, e

    line = line.strip()
    did, fid, f_sname, time_logged, e  = line.split('\t')
    dt = datetime.datetime.strptime(time_logged, '%Y-%m-%d %H:%M:%S-%f')
    rounded_time = "%s:%s:00-00" % (dt.strftime('%Y-%m-%d %H'), 
              str(int(math.ceil(float(dt.minute) / 15)) * 15))
    print '%s\t%s\t%s\t%s' % (fid, rounded_time, f_sname, e)
  return None

if __name__=="__main__":
  main(sys.argv)

