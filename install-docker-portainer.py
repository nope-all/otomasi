import os
import subprocess


def update():
    os.system('sudo apt-get update -y')

def upgrade():
    os.system('sudo apt-get upgrade -y')

def docker():
#    dependencies_package = "ca-certificates curl gnupg lsb-release"
#    docker_package = "docker-ce docker-ce-cli containerd.io docker-compose-plugin"
    directory = "/etc/apt/keyrings"
    os.system('sudo apt install -y ca-certificates curl gnupg lsb-release')
#    subprocess.run(["sudo", "apt", "install", "-y", dependencies_package], check=True)
    subprocess.run(["sudo", "mkdir", "-p", directory], check=True)
    os.system('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg')
    os.system('echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null')
    update()
    os.system('sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin')
#    subprocess.run(["sudo", "apt", "install", "-y", docker_package], check=True)
    subprocess.run(["sudo", "service", "docker", "start"], check=True)

def portainer():
    subprocess.run(["sudo", "service", "docker", "restart"], check=True)
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
    u1 = input('Are you want to Install Docker? [y/N]: ')

    if u1 in ['y','Y']:
        update()
        print('')
        print('Ubuntu has been Update')
        print('')
        while True:
            u2 = input('Are you want to Upgrade Ubuntu?(Recommend to Upgrade) [y/N]: ')

            if u2 in ['y','Y']:
                print('Starting Upgrade Ubuntu')
                print('')
                upgrade()
                print('')
                print('Ubuntu has been Upgraded!')
                print('')
                print('Starting Install Docker')
                print('')
                docker()
                print('')
                print('Succesfully Installed Docker')
                while True:
                    print('')
                    p1 = input('Are you want to Install Portainer? [y/N]: ')
                    
                    if p1 in ['y','Y']:
                        print('Starting Install Portainer')
                        portainer()
                        print('')
                        print('Succesfully Installed Portainer')
                        break
                    elif p1 in ['n','N']:
                        break
                    else:
                        print(f'{p1}:Invalid Selection!')
                        continue
            elif u2 in ['n','N']:
                print('Starting Install Docker')
                docker()
                print('')
                print('Succesfully Installed Docker')
                while True:
                    print('')
                    p2 = input('Are you want to Install Portainer? [y/N]: ')

                    if p2 in ['y','Y']:
                        print('Starting Install Portainer')
                        portainer()
                        print('')
                        print('Succesfully Installed Portainer')
                        break
                    elif p2 in ['n','N']:
                        break
                    else:
                        print(f'{p2}:Invalid Selection!')
                        continue
                break
            else:
                print(f'{u2}:Invalid Selection!')
                continue
        break
    elif u1 in ['n','N']:
        while True:
            p3 = input('Are you want to Install Portainer? [y/N]: ')

            if p3 in ['y','Y']:
                print('Starting Install Portainer')
                print('')
                portainer()
                print('')
                print('Succesfully Installed Portainer')
                break
            elif p3 in ['n','N']:
                print('')
                print('Aborted to Install Docker and Portainer')
                break
            else:
                print(f'{p3}:Invalid Selection!')
                continue
        break
    else:
        print(f'{u1}:Invalid Selection!')
        continue