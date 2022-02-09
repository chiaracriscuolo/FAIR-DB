FROM ubuntu

RUN apt-get update
RUN apt-get install -y nodejs
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends tzdata
RUN apt-get install -y npm
RUN apt-get install -y pip

COPY . /home/app

WORKDIR /home/app
EXPOSE 80

RUN pip install pipenv
WORKDIR /home/app/nodePythonApp
RUN pipenv install
WORKDIR /home/app

RUN npm ci

RUN npm run build

CMD ["npm", "start"]
