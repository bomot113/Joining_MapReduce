#!/usr/bin/env python
import sys
def main(argv):
  try:
    for line in sys.stdin:
      #initialize variable 
      fid = "-1"
      did = "-1"
      f_name = "\N"
      time_logged = "\N"
      e = "0"

      # parsing lines
      line = line.strip()
      values = line.split('\t')
      if (len(values) == 3):
        # this must be a row in fid_did file
        fid = values[0]
        f_name = values[1]
        did = values[2]
      else:
        # this must be a row in work_log file
        fid = "-1"
        did = values[1]
        time_logged = values[2]
        e = values[4]  
      print "%s\t%s\t%s\t%s\t%s" % (did, fid, f_name, time_logged, e)
  except:
    pass
if __name__=="__main__":
  main(sys.argv)
