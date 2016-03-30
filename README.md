# eg-test

pip install paramiko PyYAML schedule ansible


Create config.yml in the same directory with upload.py
```yaml
ssh_user: "user"
ssh_password: "user"
ssh_host: "123.123.123.123"
ssh_port: "22"
local_path: "."
remote_path: "/home/user"
```

Write down remote server ip as "testserver" in `/etc/hosts` for ansible usage

Download sample app from here
```
https://tomcat.apache.org/tomcat-6.0-doc/appdev/sample/sample.war
```