from git import Repo
import os

path = './.poster'
try:
    os.makedirs(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)

cloned_repo = Repo.clone_from('https://github.com/sunyu912/cm2-admin-automation.git', path)
print('repo cloned')
