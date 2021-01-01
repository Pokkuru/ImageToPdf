#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import re
import datetime

args = sys.argv
targetDir = "./" + str(args[1]) + "/"
files = os.listdir(targetDir)
i = 0
sa = []
dt = []
for file in files:
  stat = os.stat(targetDir + file)
  last_modified = stat.st_mtime
  t = datetime.datetime.fromtimestamp(last_modified)
  dt.append(last_modified)
sa = dt
sa = sorted(sa, key = float)
sortedFilePath = [0 for i in range(len(files))]
for dtt in dt:
  for sat in sa:
    if dtt == sat:
      sortedFilePath[int(sa.index(sat))] = targetDir + str(files[dt.index(dtt)])

extension = ""
re_jpg = re.compile("jpg")
re_png = re.compile("png")
re_bmp = re.compile("bmp")
if re_jpg.search(sortedFilePath[0]):
  extension = ".jpg"
elif re_png.search(sortedFilePath[0]):
  extension = ".png"
elif re_bmp.search(sortedFilePath[0]):
  extension = ".bmp"
else:
  exit()

i = 1
for file in sortedFilePath:
  os.rename(file, str(targetDir+"%06d"+extension) %(i))
  i += 1

os.system('convert {0}/*.jpg {1}.pdf'.format(args[1], args[1]))