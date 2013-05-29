#!/usr/bin/env python
import sys
def main(argv):
  try:
    for line in sys.stdin:
      # initialize all variables
      fid = "-1"
      did = "-1"
      f_sName = "-1"

      #parsing lines
      line = line.strip()
      values = line.split('\t')
      if (len(values) == 3):
        # this is a row in file device.txt
        did = values[0]
        fid = values[1]
      else:
        # This must be a ro in file facility.txt
        fid = values[0]
        f_sName = values[2]       
      if (fid != "\N"):
        print "%s\t%s\t%s" % (fid, f_sName, did)
  except:
    pass

if __name__=="__main__":
  main(sys.argv)
