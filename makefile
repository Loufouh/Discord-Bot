testing_no_req:
	@echo "\e[1;33mTesting all...\e[0;35m (skipping HTTP requests)\e[0;0m"
	@export SKIP_REQUEST_TESTS=TRUE ;\
	python3 -m unittest test/*.py test/*/*.py test/*/*/*.py test/*/*/*/*.py test/*/*/*/*/*.py

testing:
	@echo "\e[1;33mTesting all...\e[0;0m"
	@python3 -m unittest test/*.py test/*/*.py test/*/*/*.py test/*/*/*/*.py test/*/*/*/*/*.py

