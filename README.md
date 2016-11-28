# MN Pay #
## Getting started ##
### Dependencies ###
Your system needs the following installed:

- Docker - DigitalOcean has a [great tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04) to do this on ubuntu 16.04.
- Docker-compose - If you have pip installed this can be installed with `pip install docker-compose`

### One-time setup ###
First start up all of our services
```
$ source ./dev_env.sh
$ docker-compose up
```
leave this terminal open.

Initialize the database and load in some sample data
```
$ docker-compose run oneoff python manage.py migrate
$ docker-compose run oneoff python manage.py loadwages ./raw_data/sample_data.csv
```

#### Optional ####
If you would like to add a super user you can run
```
docker-compose run oneoff python manage.py createsuperuser
```
after initializing the database. It will prompt you to enter a username and
password. You can then sign in to the admin console at
[localhost/admin](http://localhost/admin).


### Running ###
To launch your server run
```
$ source ./dev_env.sh
$ docker-compose up
```
You can then direct your browser to [localhost:80](http://localhost/) to see the site.

If you are working on the server, restart the server container to see changes.
Do this by hitting `ctrl+c` in the terminal you ran `docker-compose up` in,
then run `docker-compose up` again.

### Adding server dependencies ###
If you add a dependency to the server you need to rebuild the docker containers
in order for it to get picked up. This would be the case if you ran
`pip install [anything]`. Add the requirement to `server/requirements.txt`
and then run
```
$ docker-compose build oneoff
$ docker-compose build web
```
