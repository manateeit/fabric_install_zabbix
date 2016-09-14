from fabric.api import *
from fabric.contrib.files import exists
import os
import pprint

@task
def apache2Install():
    run("sudo apt-get udpate")
    run("sudo apt-get install -y apache2 --force-yes")

@task 
def mysqlInstall():
    run("sudo apt-get udpate")
    run("sudo apt-get install -y mysql-server php5-mysql --force-yes")
    run("sudo mysql_install_db")
    run("sudo mysql_secure_installation")

@task
def phpInstall():
    run("sudo apt-get udpate")
    run("sudo apt-get install -y php5 libapache2-mod-php5 php5-mcrypt --force-yes")
    put("./dif.conf", "/etc/apache2/mods-enabled/dir.conf", use_sudo=True)
    apache2Restart()

@task
def phpInstallExtentions():
    run("sudo apt-get update")
    run("sudo apt-get install php-gd")
    run("sudo apt-get install php-libXML")
    run("sudo apt-get install php-xmlreader")
    run("sudo apt-get install php-xmlwriter")
    run("sudo apt-get install php-session")
    run("sudo apt-get install php-mbstring")
    run("sudo apt-get install php-gettext")
    run("sudo apt-get install php-ldap")
    run("sudo apt-get install php-mysqli")
 
@task
def zabbixInstallDebFile():
    run("wget http://repo.zabbix.com/zabbix/3.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_3.0-1+trusty_all.deb")
    run("dpkg -i zabbix-release_3.0-1+trusty_all.deb")
    run("sudo apt-get update")

@task
def zabbixInstallServerPackages():
    run("sudo apt-get install -y zabbix-server-mysql zabbix-frontend-php --force-yes")

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




# wget http://repo.zabbix.com/zabbix/3.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_3.0-1+trusty_all.deb
# dpkg -i zabbix-release_3.0-1+trusty_all.deb
# apt-get update

