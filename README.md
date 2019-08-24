* Install Мас OS:

brew install python3


python3 -m venv ~/py3env  # create virtualenv

. ~/py3env/bin/activate  # activate virtualenv

(sudo)pip3 install -r requirements.txt


* Launch Мас OS:

pytest /tests



* Install Linux:

sudo apt-get install python3


sudo apt-get install python3-venv # install virtualenv for Debian/Linux systems

python3 -m venv ~/py3env  # create virtualenv

. ~/py3env/bin/activate  # activate virtualenv

sudo apt-get install python3-pip

(sudo)pip install -r requirements.txt


* Launch Linux:

pytest tests/



* Install Windows:

[Download latest version of Python](https://www.python.org/downloads/)


python -m venv venv/py3env  # create virtualenv

`<venv>`/Sripts/activate  # activate virtualenv, where `<venv>` is full path to your Project

pip install -r requirements.txt
 

* Launch Windows:

pytest tests