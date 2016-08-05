init:
	test -d env || virtualenv env --no-site-packages
	env/bin/pip install -r requirements.txt

test:
	env/bin/tox
	env/bin/coverage combine 
	env/bin/coverage xml --include=*

develop:
	env/bin/python setup.py develop

dist: init test
	env/bin/python setup.py sdist bdist_wheel
	@echo 'Distribution tarball(s) created in dist/'

install: init test
	env/bin/python setup.py install

clean:
	rm -Rf \
		env \
		dist \
		build \
		*.egg-info \
		.tox \
		.coverage* \
		coverage.xml

all: init install dist