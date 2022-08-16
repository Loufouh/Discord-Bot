OS=$(shell uname -s)

ifeq ($(OS), Darwin)
yellowCode="\033[1;33m"
whiteCode="\033[0;0m"
else
ifeq ($(OS), Linux)
yellowCode="\e[1;33m"
whiteCode="\e[0;0m"
else
yellowCode=""
whiteCode=""
endif
endif

testing:
	@echo $(yellowCode)"Testing all..."$(whiteCode)
	@export IS_TESTING=TRUE ;\
	python3 -m unittest discover

