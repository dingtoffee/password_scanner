import os
import datetime
from itertools import chain
import shutil

# put your path here 
# Network SMB path you want to search 
root_dir = ("xxxxxx", "etc.")
# location where you want to put the result 
stored_dir = 'xxxxxxxxx'
# exception you want to filter
exception_path = ["snapshot"]
counter = 0
part = 0
date2 = datetime.datetime.now()
date = date2.strftime("%Y-%m-%d")

# identify any file in the directory
if os.listdir(stored_dir):
    print("there is file")
    for filename in os.listdir(stored_dir):
        filepath = os.path.join(stored_dir, filename)
        try:
            shutil.rmtree(filepath)
        except:
            os.remove(filepath)
        else:
            print ("proceed with directory discovery.")

# listing directory
for path, subdirs, files in chain.from_iterable(os.walk(root_dirs)for root_dirs in root_dir):
    
    if any( x in path for x in exception_path):
        pass
    for name in files:
        if any(x in os.path.join(path,name) for x in exception_path)is False:
            counter = counter + 1
            if counter <=10000:
                part = str(part)
                with open(stored_dir + date + '-'+ part,'a+', encoding='utf=8') as f:
                    f.write(os.path.join(path,name)+'\n')
                    f.close()
            else:
                part = int(part)
                part += 1
                counter = 0
        else:
            pass
