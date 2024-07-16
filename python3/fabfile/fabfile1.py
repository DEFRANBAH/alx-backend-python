# fabfile for testing fabric

from fabric.api import *

# Define the host list

env.hosts = ['localhost' , 'localhost']
env.user = 'root'
env.password = 'root'

# Define the tasks
def update():
    run('apt-get update')
    run('apt-get upgrade -y')

# install the defauly os packages manager

def apdt():
    run('apt-get install aptitude -y')
    run('aptitude update')
    run('aptitude upgrade -y')

#install memcached from aptitude
def install_memcached():
    run('aptitude install memcached -y')
    run('service memcached start')  

#recurse the process to be reversed and not interfre with the process
def install-upgrade():
    update()
    apdt()
    install_memcached()
    run('service memcached status')
