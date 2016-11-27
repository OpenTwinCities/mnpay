FROM node:6.9
RUN npm install webpack -g
ADD . /client
WORKDIR /client
ENTRYPOINT ["bash", "build.sh"]
