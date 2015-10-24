echo "Installing dependencies... (if required)"

sudo apt-get update
sudo apt-get install --yes nodejs
sudo apt-get install --yes npm
sudo npm install -g stubby
sudo locale-gen UTF-8
sudo ln -s /usr/bin/nodejs /usr/bin/node
sudo apt-get install python3-pip
sudo pip3 install Django==1.8.5
sudo apt-get install postgresql postgresql-contrib

sudo locale-gen en_US en_US.UTF-8 
sudo dpkg-reconfigure locales

sudo -i -u postgres
psql  
CREATE DATABASE simpatize;
\q
exit

sudo apt-get install libpq-dev python-dev
sudo pip3 install psycopg2

echo "Done!"