#!/usr/bin/env python
import sys
def main(argv):
  #initialize variables
  did = "-1"
  fid = "-1"
  f_name = "\N"
  time_logs = []
  time_log = []
  try:
    for line in sys.stdin:
      # line = (did, fid, f_name, time_logged, e)
      line = line.strip()
      values = line.split('\t')
      # make sure right rows is being processed
      if (len(values) != 5):
        continue
      # firt line is reached   
      if (did == "-1"):
        did = values[0]

      # this only works after hadoop's sorting
      if (did != values[0]):
        # the line reaches to the new did
        # it's time to emit pairs
        if (fid != "-1"):
          for time_log in time_logs:
            print "%s\t%s\t%s\t%s\t%s" % (did, fid, 
            f_name, time_log[0], time_log[1])
        # reset values
        time_logs = []
        did = values[0]

      # group by did
      if (values[1] == "-1"):
        # this row is of the work_log relation as fid has no value
        time_logs.append([values[3], values[4]])
      if (values[3] == "\N"):
        # this row is of the did_fid relation as time_logged has no value
        f_name = values[2]
        fid = values[1]
  except:
    pass
  # End of the file, print the last did    
  if (fid != "-1"): 
    for time_log in time_logs:
      print "%s\t%s\t%s\t%s\t%s" % (did, fid, 
      f_name, time_log[0], time_log[1])
if __name__ == "__main__":
  main(sys.argv)
