* Install  Мас OS:

brew install python3


python3 -m venv ~/py3env  # create virtualenv
. ~/py3env/bin/activate  # activate virtualenv

(sudo)pip3 install -r requirements.txt

* Launch
pytest /tests
pytest --html=report.html /tests # for creating report file


* Install Ubuntu

sudo apt-get install python3


sudo apt-get install python3-venv # install virtualenv for Debian/Ubuntu systems
python3 -m venv ~/py3env  # create virtualenv
. ~/py3env/bin/activate  # activate virtualenv

sudo apt-get install python3-pip
(sudo)pip install -r requirements.txt

* Launch
pytest tests/
pytest --html=report.html tests/ # for creating report file