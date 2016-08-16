init:
	pip install -r requirement.txt

test:
	nosetests 

package: 
	python setup.py bdist_wheel

register:
	python setup.py register
