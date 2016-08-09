default: dist

init-py35:
	@echo Building Python 3.5 virtualenv
	test -d py35 || virtualenv py35 --no-site-packages --python=python3.5
	py35/bin/pip install -r requirements.txt
	py35/bin/python setup.py develop

init-py27:
	@echo Building Python 2.7 virtualenv
	test -d py27 || virtualenv py27 --no-site-packages --python=python2.7
	py27/bin/pip install -r requirements.txt
	py27/bin/python setup.py develop

test: init-py35
	py35/bin/tox

coverage: test
	py35/bin/coverage combine
	py35/bin/coverage xml

dist-src: init-py35
	py35/bin/python setup.py sdist

dist-rpm: init-py27
	contrib/build-rpm.sh

dist-egg: init-py35
	py35/bin/python setup.py bdist_wheel

dist-deb: dist-src
	contrib/build-deb.sh

dist: dist-src dist-egg
	@echo 'Distribution file(s) created in dist/'

install:
	pip install -U .

clean:
	rm -Rf build .coverage* htmlcov coverage.xml

distclean: clean
	rm -Rf py27 py35 __pycache__ */__pycache__ dist .tox *.egg-info

ci: test coverage dist
