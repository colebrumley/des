init:
	test -d env || virtualenv env --no-site-packages
	. env/bin/activate
	pip install -r requirements.txt

test:
	. env/bin/activate
	python setup.py test

develop:
	. env/bin/activate
	python setup.py develop

clean:
	env/bin/python setup.py clean
	rm -Rf env
