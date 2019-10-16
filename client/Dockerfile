FROM node:6.9
RUN npm install webpack@1.13.2 -g
ADD . /client
WORKDIR /client
ENTRYPOINT ["bash", "build.sh"]
