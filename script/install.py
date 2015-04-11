from fabric.api import run, task, sudo

def install_mysql():
  response = sudo('yum -y install mysql-server')
  if response.failed:
    uninstall_mysql()
    abort("mysql install failed!")

def install_jenkins():
  response1 = sudo('wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat/jenkins.repo')
  response2 = sudo('rpm --import http://pkg.jenkins-ci.org/redhat/jenkins-ci.org.key')
  response3 = sudo('yum -y install jenkins')
  if response1.failed and response2.failed and response3.failed:
      uninstall_jenkins()
      abort("jenkins install failed")

def install_git():
  response = sudo('yum -y install git')
  if response.failed:
      uninstall_git()
      abort("git install failed")

def install_redis():
  response = sudo('yum -y install redis')
  if response.failed:
      uninstall_redis()
      abort("redis install failed")

def install_npm_nodejs():
  response1 = sudo('rpm -ivh --force http://ftp.riken.jp/Linux/fedora/epel/6/x86_64/epel-release-6-8.noarch.rpm')
  response2 = sudo('yum -y install npm nodejs --enablerepo=epel')
  if response1.failed and response2.failed:
      uninstall_npm()
      abort("npm nodejs install failed")

def uninstall_mysql():
    sudo('yum -y remove mysql-server')

def uninstall_jenkins():
    sudo('yum -y remove jenkins')

def uninstall_git():
    sudo('yum -y remove git')

def uninstall_redis():
    sudo('yum -y remove redis')

def uninstall_npm_nodejs():
    sudo('yum -y remove npm nodejs')
