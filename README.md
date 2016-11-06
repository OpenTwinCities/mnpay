# MN Wages #
## Getting started ##
### Dependencies ###
Your system needs the following installed:

- Docker - DigitalOcean has a [great tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04) to do this on ubuntu 16.04.
- Docker-compose - If you have pip installed this can be installed with `pip install docker-compose`
- nodejs - I suggest using NVM. Once again, [DigitalOcean has you covered](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-16-04).

### One-time setup ###
Setup our python dependencies
```
$ cd <project_repo>
$ pip install -r requirements
```
Initialize the database and load in some sample data
```
$ python db_create.py
$ python load_in_csv.py sample_data.csv
```

Setup our node dependencies
```
$ npm install
```
Install webpack globally so we can use the `webpack` command.
```
$ npm install -g webpack
```


### Running ###
To launch your server run
```
docker-compose up -d
```
You can then direct your browser to [localhost:80](http://localhost/) to see the site.

If you are working on the client, start webpack in watch mode.
```
$ cd <project_repo>
$ webpack -w
```
This way everytime that you make a change to client code it will rebuild it and
put it were our nginx docker container can see it.
