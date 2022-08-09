testing_no_req:
	@echo "\e[1;33mTesting all...\e[0;35m (skipping HTTP requests)\e[0;0m"
	@export IS_TESTING=TRUE ;\
	python3 -m unittest discover

testing:
	@echo "\e[1;33mTesting all...\e[0;0m"
	python3 -m unittest test/*.py test/*/*.py test/*/*/*.py test/*/*/*/*.py test/*/*/*/*/*.py

