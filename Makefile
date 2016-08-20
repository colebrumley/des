default: dist

test:
	tox -r

coverage: test
	coverage combine
	coverage xml

dist-rpm:
	contrib/build-rpm.sh

dist:
	python setup.py sdist
	python setup.py bdist_egg
	@echo 'Distribution file(s) created in dist/'

pip:
	python setup.py sdist upload

install:
	pip install -U .

clean:
	rm -Rf .cache .eggs build .coverage* htmlcov coverage.xml __pycache__ */__pycache__ dist .tox *.egg-info

ci: test coverage dist
