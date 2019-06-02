from shutil import copyfile
import sys

src = sys.argv[1]
dest = sys.argv[2]

copyfile(src,dest)
#print(src,'\n',dest)
print('Successfully copied')
