import os
import subprocess


def update():
    os.system('sudo apt-get update -y')

def upgrade():
    os.system('sudo apt-get upgrade -y')

def docker():
    dependencies_package = "ca-certificates curl gnupg lsb-release"
    directory = "/etc/apt/keyrings"
    docker_package = "docker-ce docker-ce-cli containerd.io docker-compose-plugin"
    subprocess.run(["sudo", "apt", "install", "-y", dependencies_package], check=True)
    subprocess.run(["sudo", "mkdir", "-p", directory], check=True)
    os.system('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg')
    os.system('echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null')
    update()
    subprocess.run(["sudo", "apt", "install", "-y", docker_package], check=True)
    subprocess.run(["sudo", "service", "docker", "start"], check=True)

def portainer():
    subprocess.run(["sudo", "service", "docker", "start"], check=True)
    os.system('sudo docker pull portainer/portainer-ce')
    os.system('sudo docker volume create portainer_data')
    os.system('sudo docker run -d \
        -p 8000:8000 \
        -p 9443:9443 \
        --name portainer \
        --restart=always \
        -v /var/run/docker.sock:/var/run/docker.sock \
        -v portainer_data:/data \
    portainer/portainer-ce:latest')

while True:
    os.system('clear')
    u1 = input('Are you want to Install Docker? [y/n]: ')

    if u1 in ['y','Y']:
        update()
        print('')
        print('Ubuntu has been Update')
        print('')
        break
    elif u1 in ['n','N']:
        break
    else:
        print(f'{u1}:Invalid Selection!')
        continue

while True:
    d1 = input('Are you want to Upgrade Ubuntu?(Recommend to Upgrade) [y/n/skip(for skip install docker)]: ')

    if d1 in ['y','Y']:
        print('')
        print('Starting Upgrade Ubuntu')
        upgrade()
        print('')
        print('Ubuntu has been Upgraded!')
        print('')
        print('Starting Install Docker')
        docker()
        print('')
        print('Successfully installed Docker')
        print('')
        break
    elif d1 in ['n','N']:
        print('')
        print('Starting Install Docker')
        docker()
        print('')
        print('Successfully Installed Docker')
        print('')
        break
    elif d1 in ['skip']:
        break
    else:
        print(f'{d1}:Invalid Selection!')
        continue

while True:
    p1 = input('Are you want to Install Portainer? [y/n]: ')

    if p1 in ['y','Y']:
        print('Starting Install Portainer')
        portainer()
        print('')
        print('Succesfully Installed Portainer')
        print('')
        print('All Done!')
        break
    elif p1 in ['n','N']:
        print('All Done!')
        break
    else:
        print(f'{p1}:Invalid Selection!')
        continue