echo "Installing dependencies... (if required)"

sudo apt-get update
sudo apt-get install --yes nodejs
sudo apt-get install --yes npm
sudo npm install -g stubby
sudo locale-gen UTF-8
sudo ln -s /usr/bin/nodejs /usr/bin/node

echo "Done!"