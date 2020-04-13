sudo docker-compose down

sudo docker swarm leave --force

sudo docker rmi $(docker images -qa)