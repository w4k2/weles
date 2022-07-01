.PHONY: all clean test

clean:
	find . -name "*.so" -o -name "*.pyc" -o -name "*.md5" -o -name "*.pyd" -o -name "*~" | xargs rm -f
	find . -name "*.pyx" -exec ./tools/rm_pyx_c_file.sh {} \;
	rm -rf coverage
	rm -rf dist
	rm -rf build
	rm -rf doc/_build
	rm -rf doc/auto_examples
	rm -rf doc/generated
	rm -rf doc/modules
	rm -rf examples/.ipynb_checkpoints

docs: clean install
	cd doc && make html

test-code:
	py.test weles

test-coverage:
	rm -rf coverage .coverage
	py.test --cov-report term-missing:skip-covered --cov-report xml:coverage.xml --cov=weles weles

test: clean test-coverage

code-analysis:
	flake8 weles | grep -v __init__
	pylint -E weles/ -d E1103,E0611,E1101

upload:
	python setup.py sdist bdist_wheel
	twine upload dist/*
	pip3 install --upgrade weles

install: clean
	python setup.py clean
	python setup.py develop
