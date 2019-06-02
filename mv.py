from shutil import copyfile
import sys, os

src = sys.argv[1]
dest = sys.argv[2]

copyfile(src,dest)
os.remove(src)
print('Successfully Moved')
