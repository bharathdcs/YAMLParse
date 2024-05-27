

import yaml
import os
import sys
from yaml.loader import SafeLoader


class ImageDigest:
    appVersion = ""
    displayName = ""
    displayDescription = ""
    image = ""
    tag = ""
    digest = ""

walk_dir = "/Users/bharathdevaraju/Documents/CPD-CaseRepo/cloud-pak-master/repo/case"


#walk_dir = "/Users/bharathdevaraju/Documents/CPD-CaseRepo/zen-digests-vnext-dev"

print('walk_dir = ' + walk_dir)
i = 0
output = open("/tmp/cpd_director.csv", "w")


for (root, subdirs, files) in os.walk(walk_dir):
    # f.write(root+"\n")
    i = i+1
    for name in files:
        if name[-4:] == "yaml" and os.path.islink(os.path.join(root, name)) != True:
            with open(os.path.join(root, name), 'r') as f:
                try:
                    data = yaml.load(f, Loader=SafeLoader)
                except yaml.scanner.ScannerError:
                    print("Skipping the file:"+os.path.join(root, name))
                    break
                ImageDigest.appVersion = root[-5:]
                if ImageDigest.appVersion=='chive':
                    break
                ImageDigest.displayName = 'ZenService'
                ImageDigest.tag=''
                digests = data['image_digests']
                for digest in digests.keys():
                    ImageDigest.digest = data['image_digests'][digest]
                    if ImageDigest.digest is None:
                        break
                    ImageDigest.image=digest
                    output.write("'"+ImageDigest.appVersion+"','"+ImageDigest.displayName+"','" +
                                     ImageDigest.image+"','"+ImageDigest.tag+"','"+ImageDigest.digest+"'\n")
#f.close()
