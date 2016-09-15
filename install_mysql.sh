#!/usr/bin/env bash

export DEBIAN_FRONTEND="noninteractive"

apt-get -y install debconf-utils

sudo debconf-set-selections <<< "mysql-server mysql-server/root_password password rootpw"
sudo debconf-set-selections <<< "mysql-server mysql-server/root_password_again password rootpw"

sudo debconf-get-selections | grep mysql

sudo apt-get install -y mysql-server php5-mysql

apt-get -y install expect

sed -i 's/127\.0\.0\.1/0\.0\.0\.0/g' /etc/mysql/my.cnf
