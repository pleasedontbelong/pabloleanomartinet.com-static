# Requirements

- Python 2.7
- NodeJS 0.10


# Installation

```
sudo apt-get install python-virtualenv
cd /path/to/botify-website/
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
sudo apt-get install npm
npm install
sudo apt-get install curl
curl -sL https://deb.nodesource.com/setup | sudo bash -
sudo apt-get install -y nodejs
sudo npm -g install yuglify
sudo ln -s /usr/bin/nodejs /usr/bin/node # needed to fix error "pipeline.exceptions.CompressorError: /usr/bin/env: node: No such file or directory" on `make generate-dev`
```

# Launch server


```
python manage.py runserver
```

Then go to http://localhost:8000


# Push on Staging


```
git pull origin master
make generate-dev
```


# Push on Production



```
git pull origin master
make generate-prod
```
