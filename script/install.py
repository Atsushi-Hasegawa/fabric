from fabric.api import run, task

def install_mysql():
 run('sudo yum -y install mysql')

def install_jenkins():
  run('sudo wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat/jenkins.repo')
  run('sudo rpm --import http://pkg.jenkins-ci.org/redhat/jenkins-ci.org.key')
  run('sudo yum -y install jenkins')

def install_git():
 run('sudo yum -y install git')

def uninstall_mysql():
 run('sudo yum -y remove mysql')

def uninstall_jenkins():
  run('sudo yum -y remove jenkins')

def uninstall_git():
 run('sudo yum -y remove git')

