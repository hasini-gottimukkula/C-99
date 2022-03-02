import os
import shutil

source = "/Users/hasinigottimukkula/Downloads/"
print(os.listdir(source))

destination = "/Users/hasinigottimukkula/Documents/"

filelist = os.listdir(source)

print(filelist)
for file in filelist :
    shutil.copy((source+file),destination)
