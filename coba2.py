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
    print('What Should I Do: ')
    print('')
    print('Select An Options:')
    print(' 1) Update Ubuntu')
    print(' 2) Upgrade Ubuntu')
    print(' 3) Install Docker')
    print(' 4) Install Portainer')
    print(' 5) Exit')
    o1 = input('Option: ')


    if o1 in ['1']:
        update()
        print('')
        print('Ubuntu has been Update')
        break
    
    elif o1 in ['2']:
        print('Starting Upgrade Ubuntu')
        print('')
        upgrade()
        print('')
        print('Successfully Upgrade Ubuuntu')
        break

    elif o1 in ['3']:
        print('Starting Install Docker')
        print('')
        docker()
        print('')
        print('Successfully Install Docker')
        break

    elif o1 in ['4']:
        print('Starting Install Portainer')
        print('')
        portainer()
        print('')
        print('Successfully Install Portainer')
        break

    elif o1 in ['5']:
        print('Thank You! Bye Bye!')
        break

    else:
        print(f'{o1}:Invalid Selection!')
        continue