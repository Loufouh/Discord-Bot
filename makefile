testing_no_req:
	export SKIP_REQUEST_TESTS=TRUE ;\
	python3 -m unittest test/*.py test/*/*.py test/*/*/*.py test/*/*/*/*.py test/*/*/*/*/*.py

testing:
	python3 -m unittest test/*.py test/*/*.py test/*/*/*.py test/*/*/*/*.py test/*/*/*/*/*.py


