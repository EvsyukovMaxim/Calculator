* Install  Мас OS:

brew install python3


python3 -m venv ~/py3env  # create virtualenv

. ~/py3env/bin/activate  # activate virtualenv

(sudo)pip3 install -r requirements.txt


* Launch Мас OS:

pytest /tests



* Install Ubuntu:

sudo apt-get install python3

sudo apt-get install python3-venv # install virtualenv for Debian/Ubuntu systems

python3 -m venv ~/py3env  # create virtualenv

. ~/py3env/bin/activate  # activate virtualenv

sudo apt-get install python3-pip

(sudo)pip install -r requirements.txt


* Launch Ubuntu:

pytest tests/