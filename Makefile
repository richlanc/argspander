name = argspander
venv_name = $(name)_venv
venv_sh = $(venv_name)/bin/activate

test: $(venv_name) $(venv_name).egg-info
	. $(venv_sh); py.test tests

$(venv_name):
	virtualenv -p python3 $(venv_name)

$(venv_name).egg-info:
	. $(venv_sh); python setup.py develop

install:
	python setup.py install

clean:
	rm -rf $(venv_name) $(name).egg-info __pycache__
