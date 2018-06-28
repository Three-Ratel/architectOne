
# import shutil
# shutil.make_archive('/code/m1/day07/准备阶段/x1',format='zip',root_dir='/code/m1/day07/准备阶段/m1')
#

import zipfile

obj=zipfile.ZipFile('/code/m1/day07/准备阶段/x1.zip',mode='r')
obj.extractall('/code/m1/day07/准备阶段/m1')
obj.close()