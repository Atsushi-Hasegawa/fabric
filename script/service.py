from fabric.api import run

def service_start():
  run('service jenkins start')
  run('service mysql start')
