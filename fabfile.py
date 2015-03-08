from fabric.api import local, run

def ls():
  local('ls /home/vagrant')

def install_mysql():
 run('sudo yum -y install mysql')

def install_jenkins():
  run('sudo wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat/jenkins.repo')
  run('sudo rpm --import http://pkg.jenkins-ci.org/redhat/jenkins-ci.org.key')
  run('sudo yum -y install jenkins')

def uninstall_mysql():
 run('sudo yum -y remove mysql')

def uninstall_jenkins():
  run('sudo yum -y remove jenkins')
