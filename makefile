testing:
	@echo "\e[1;33mTesting all...\e[0;0m"
	@export IS_TESTING=TRUE ;\
	python3 -m unittest discover

