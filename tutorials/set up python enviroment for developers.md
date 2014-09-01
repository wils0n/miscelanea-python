##Set up python enviroment for django developers and more

	sudo apt-get install python-pip
	sudo pip install virtualenvwrapper
	mkdir .envs
	export WORKON_HOME=~/.envs
	mkdir -p $WORKON_HOME
	source /usr/local/bin/virtualenvwrapper.sh

list, ready for use pip and virtualenv

	mkvirtualenv env