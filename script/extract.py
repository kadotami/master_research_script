# -*- coding: utf-8 -*-
from collections import defaultdict
import datetime
import common_method as cm

#########################################
# vertical情報が入っているものだけを抽出
#########################################

if __name__ == "__main__":
  analyzeVertical = []
  allDict = {
    "all":defaultdict(lambda: 0)
  }
  deviceDict = {
    "pc": defaultdict(lambda: 0),
    "smartphone": defaultdict(lambda: 0),
    "tv": defaultdict(lambda: 0),
    "tablet": defaultdict(lambda: 0),
    "featurephone": defaultdict(lambda: 0),
  }
  generationDict = {
    "10's": defaultdict(lambda: 0),
    "20's": defaultdict(lambda: 0),
    "30's": defaultdict(lambda: 0),
    "40's": defaultdict(lambda: 0),
    "50's": defaultdict(lambda: 0),
    "60's": defaultdict(lambda: 0)
  }
  genderDict = {
    "m": defaultdict(lambda: 0),
    "f": defaultdict(lambda: 0)
  }

  outputs = {
    "device": {},
    "gender": {},
    "generation": {}
  }
  outputs["device"]["smartphone"] = open('/home/c-yukadotami/data/device/smartphone.txt', "w")
  outputs["device"]["pc"] = open('/home/c-yukadotami/data/device/pc.txt', "w")
  outputs["device"]["tablet"] = open('/home/c-yukadotami/data/device/tablet.txt', "w")
  outputs["device"]["tv"] = open('/home/c-yukadotami/data/device/tv.txt', "w")
  outputs["device"]["featurephone"] = open('/home/c-yukadotami/data/device/featurephone.txt', "w")
  outputs["gender"]["m"] = open('/home/c-yukadotami/data/gender/male.txt', "w")
  outputs["gender"]["f"] = open('/home/c-yukadotami/data/gender/female.txt', "w")
  outputs["generation"]["10's"] = open('/home/c-yukadotami/data/generation/10s.txt', "w")
  outputs["generation"]["20's"] = open('/home/c-yukadotami/data/generation/20s.txt', "w")
  outputs["generation"]["30's"] = open('/home/c-yukadotami/data/generation/30s.txt', "w")
  outputs["generation"]["40's"] = open('/home/c-yukadotami/data/generation/40s.txt', "w")
  outputs["generation"]["50's"] = open('/home/c-yukadotami/data/generation/50s.txt', "w")
  outputs["generation"]["60's"] = open('/home/c-yukadotami/data/generation/60s.txt', "w")

  other_verical_array = []
  other_device = []

  for fileNum in xrange(2,9):
    for line in open('../data/2015110'+str(fileNum)+'_all', 'r'):
      featureArray = line.split("\t")
      # if featureArray[11] != "":
      if featureArray[10] == "":
        continue
      browseId = featureArray[0]
      device = featureArray[8]
      vertical = cm.typical_vertical(featureArray[10])
      if vertical == "other" and featureArray[10] not in other_verical_array:
        other_verical_array.append(featureArray[10])
      birthYear = featureArray[2]
      gender = featureArray[1]
        # vertical = "None"
      allDict["all"]["all"] += 1
      allDict["all"][vertical] += 1

      if birthYear != "" and gender != "" and device in ["smartphone", "tablet", "pc", "tv", "featurephone"]:
        generation = cm.generation_distinction(birthYear)
        generationDict[generation]["all"] += 1
        generationDict[generation][vertical] += 1
        outputs["generation"][generation].write(line)
        genderDict[gender]["all"] += 1
        genderDict[gender][vertical] += 1
        outputs["gender"][gender].write(line)
        deviceDict[device]["all"] += 1
        deviceDict[device][vertical] += 1
        outputs["device"][device].write(line)

  cm.print_dict_content(allDict)
  cm.print_dict_content(deviceDict)
  cm.print_dict_content(generationDict)
  cm.print_dict_content(genderDict)

  print "===========other============"
  for x in other_device:
    print x