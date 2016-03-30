import sys
import paramiko
import tarfile
import datetime


path_to_logs = "."

# Archive logs before uploading them to remote server
def make_tar(path):
    tar_name = "1995_07_28"
    # tar_name = datetime.datetime.now().__format__("%Y_%m_%d")
    tar_path = path+"/"+tar_name+".tar.gz"

    tar = tarfile.open(path+"/"+tar_name+".tar.gz", "w:gz")
    for hour in xrange(18,22):
        file_name = tar_name+"_"+str(hour)+".log"
        try:
            tar.add(path+"/"+file_name)
        except OSError:
            print path+"/"+file_name + " doesn't exist"
            pass
    tar.close()

    return tar_path

make_tar(path_to_logs)
