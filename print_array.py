#!/usr/bin/env python

from apa_mapping import APA_MAP

apa = APA_MAP()

All_sort, X_sort, V_sort, U_sort = apa.apa_femb_mapping_pd()
apa_yuv, apa_y, apa_u, apa_v = apa.apa_mapping()

#print "wire, FEMBchn, FEMBasic, ASICchn"
#print "All_sort"
#for x in All_sort:
#  print x
#print "ASIC Chn Plane"
#for x in All_sort:
#  print "{0:1} {1:2} {2:1}".format(int(x[2]),int(x[3]),x[0][0])

#print
#print "X_sort"
#for x in X_sort:
#  print x
#print
#print "V_sort"
#for x in V_sort:
#  print x
#print
#print "U_sort"
#for x in U_sort:
#  print x
#print
#print
#print
#print
#print "FEMB channel"
#print "apa_yuv"
#for x in apa_yuv:
#  print x
#print
#print "apa_y"
#for x in apa_y:
#  print x
#print
#print "apa_u"
#for x in apa_u:
#  print x
#print
#print "apa_v"
#for x in apa_v:
#  print x
#print


plane_index_dict = {
    'U': 0,
    'V': 1,
    'X': 2,
}

print
planeLetterArray = []
planeIndexArray = []
for iAsic in range(8):
    planeLetterArray.append(["?"]*16)
    planeIndexArray.append([-1]*16)
iAll=0
for iAsic in range(8):
  for iChannel in range(16):
    plane_letter = All_sort[iAll][0][0]
    plane_index = plane_index_dict[plane_letter]
    #print "{0:1} {1:2} {2:1}".format(iAsic+1,iChannel,plane_letter)
    planeLetterArray[iAsic][iChannel] = plane_letter
    planeIndexArray[iAsic][iChannel] = plane_index
    iAll += 1
print
print "Plane Letter Array"
for asic in planeLetterArray:
    print asic
print
print "Plane Index Array"
for asic in planeIndexArray:
    print asic

print "Plane Index Array C++"
for iAsic, asic in enumerate(planeIndexArray):
    rowStr = str(asic)
    rowStr = rowStr.replace('[','{')
    rowStr = rowStr.replace(']','}')
    rowStr = "  " + rowStr
    if iAsic < 7:
      rowStr += ","
    print rowStr
