apt-get update -y
apt-get install python3.7 python3.7-distutils
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 1
!echo "3" | sudo update-alternatives --config python3
apt-get install python3-pip
python3 -m pip install --upgrade pip --user