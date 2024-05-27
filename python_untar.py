# importing the "tarfile" module
import tarfile

import os
import sys

walk_dir = "/Users/bharathdevaraju/Documents/GitHub/cloud-pak/repo/case"

print('walk_dir = ' + walk_dir)
i=0
f = open("/tmp/directory.txt", "w")


for (root, subdirs, files) in os.walk(walk_dir):
    #f.write(root+"\n")
    i=i+1
    for name in files:
        #print(name[-3:]+"\n")
        if name[-3:]=="tgz":
            filepath=os.path.join(root,name)
            f.write(filepath+"\n")
            #print(filepath)
            input_tar=tarfile.open(filepath)
            #print(root+"/\n")
            input_tar.extractall(root+"/")
            input_tar.close()
            #break

    #print(subdirs)

print(i)

f.close()

