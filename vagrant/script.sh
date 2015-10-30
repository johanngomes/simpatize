echo "Installing dependencies... (if required)"

sudo apt-get update
sudo locale-gen UTF-8
sudo ln -s /usr/bin/nodejs /usr/bin/node
sudo apt-get install --yes python3-pip
sudo pip3 install Django==1.8.5
sudo apt-get install --yes postgresql postgresql-contrib
sudo locale-gen UTF-8

sudo locale-gen en_US en_US.UTF-8 
sudo dpkg-reconfigure locales

sudo apt-get install --yes libpq-dev python-dev
sudo apt-get install --yes python-psycopg2
sudo apt-get install --yes libpq-dev

sudo pip3 install psycopg2
sudo pip3 install selenium==2.48.0
sudo apt-get install --yes firefox

echo "Done!"