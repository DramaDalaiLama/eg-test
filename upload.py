import sys
import paramiko
import tarfile
import datetime
import yaml


# path_to_logs = "."
with open('config.yml', 'r') as f:
        conf = yaml.load(f)

def write_log(message):
    logfile = open("schedule.log", "w")
    logfile.write(datetime.datetime.now().__format__('%d/%b/%Y:%H:%M:%S')+": "+message)
    logfile.close()

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
            # print path+"/"+file_name + " doesn't exist"
            write_log(path+"/"+file_name + " doesn't exist")
            pass
    tar.close()

    return {"tar_path": tar_path, "tar_name": tar_name+".tar.gz"}

def upload(user=conf['ssh_user'],password=conf['ssh_password'],private_key=None,server=conf['ssh_host'],port=conf['ssh_port'],local_path=conf['local_path'], remote_path=conf['remote_path']):
    transport = paramiko.Transport(server,port)
    transport.connect(username=user, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)

    sftp.put(local_path, remote_path)

    sftp.close()
    transport.close()

def main():
    # print "Creating archive..."
    write_log("Creating archive...")
    tar = make_tar(conf['local_path'])
    # print "\nUploading tar archive to remote host..."
    write_log("Uploading archive to remote host...")
    upload(local_path=tar['tar_path'], remote_path=conf['remote_path']+"/"+tar['tar_name'])
    # print "Upload complete\n"
    write_log("Upload complete")

if __name__ == '__main__':
    main()

