#!/usr/bin/env python
import sys
def main(argv):
  fid = "-1"
  dids = []
  did = "-1"
  f_sName = "\N"
  try:
    for line in sys.stdin:
      # line = (fid, f_sName, did)
      line = line.strip()
      values = line.split('\t')
      if (fid == "-1"):
        fid = values[0]

      # This only works if hadoop has done the sorting
      if (fid != values[0]):
        for did in dids:
          print "%s\t%s\t%s" % (fid, f_sName, did)
        dids = []
        fid = values[0]
      
      # group by fid
      if (values[2] == "-1"):
        # this row is of the facility relation as did has no value
        if (values[1] != ""):
          f_sName = values[1]
      if (values[1] == "-1"):
        #this row is of the device relation as f_sName has no value
        dids.append(values[2])
  except:
    pass
  # End of the file, print the last fid
  for did in dids:
    print "%s\t%s\t%s" % (fid, f_sName, did)
if __name__ == "__main__":
  main(sys.argv)
