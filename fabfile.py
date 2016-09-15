from fabric.api import *
from fabric.contrib.files import exists
import os
import pprint

@task
def apache2Install():
    run("sudo apt-get update")
    run("sudo apt-get upgrade -y --force-yes")
    run("sudo apt-get install -y apache2 --force-yes")

@task 
def mysqlInstall(PASSWORD):
    put("./install_mysql.sh","/home/ubuntu/")
    run("chmod +x /home/ubuntu/install_mysql.sh")
    run("sudo /home/ubuntu/install_mysql.sh")
    put("./secure_db.exp", "/home/ubuntu")
    run("chmod +x /home/ubuntu/secure_db.exp")
    run("sudo /home/ubuntu/secure_db.exp " + PASSWORD)

@task
def mysqlRemove():
    run("sudo apt-get remove mysql-server  php5-mysql expect -y --force-yes && sudo apt-get autoremove -y --force-yes")

@task
def phpInstall():
    run("sudo apt-get update")
    run("sudo apt-get install -y php5 libapache2-mod-php5 php5-mcrypt --force-yes")
    put("./dir.conf", "/etc/apache2/mods-enabled/dir.conf", use_sudo=True)
    run("sudo apt-get install -y --force-yes  php5-gd  php5-ldap ")
    apache2Restart()
 
@task
def zabbixInstallDebFile():
    run("wget http://repo.zabbix.com/zabbix/3.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_3.0-1+trusty_all.deb")
    run("sudo dpkg -i zabbix-release_3.0-1+trusty_all.deb")
    run("sudo apt-get update")

@task
def zabbixInstallServerPackages():
    run("sudo apt-get install -y zabbix-server-mysql zabbix-frontend-php --force-yes")
    run("sudo service apache2 reload")

@task
def zabbixInstallClientPackages():
    run("sudo apt-get install -y zabbix-agent --force-yes")


@task
def apache2Stop():
    run("sudo service apache2 stop")

@task
def apache2Start():
    run("sudo service apache2 start")

@task
def apache2Restart():
    apache2Stop()
    apache2Start()

@task
def zabbixINSTALL(PASSWORD):
    apache2Install()
    mysqlInstall(PASSWORD)
    phpInstall()
    zabbixInstallDebFile()
    zabbixInstallServerPackages()
    zabbixInstallClientPackages()



