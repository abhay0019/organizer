#!/usr/bin/python

import os
import sys
import subprocess as s
import magic
import re
if len(sys.argv)!=2:
  print "usage : ./organizer.py path_of_directory_to_organize"
  sys.exit()

def organizer(dest):
  if os.path.isdir(dest):
    root,directories,filenames =next(os.walk(dest))
    if not len(filenames):
      s.call(["notify-send",'Directory Already Organized ;) !!',''])
    for filename in filenames:
      type_of_file=magic.from_file(os.path.join(root,filename),mime=True)
      gp=re.search('[^/]*',type_of_file)
      type_of_file=gp.group()
      if not os.path.isdir(os.path.join(root,type_of_file)):
        os.mkdir(os.path.join(root,type_of_file))
      src=os.path.join(root,filename)
      dest=os.path.join(os.path.join(root,type_of_file),filename)  
      s.call(["mv",src,dest])
    s.call(["notify-send",'Updated Directory !!',''])    
  else:
    s.call(["notify-send",'Directory not present !!',''])
if __name__=='__main__':
  organizer(sys.argv[1])     
