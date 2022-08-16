testing:
	@echo "\033[1;33mTesting all...\033[0;0m"
	@export IS_TESTING=TRUE ;\
	python3 -m unittest discover

