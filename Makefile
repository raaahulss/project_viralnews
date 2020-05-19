ENV=./venv
PYTHON_DEPENDENCIES_PATH=./webapp/requirements.txt
PYTHON_VERSION=3.7.6

.ONESHELL:
setup:
	@echo ****Project Viral News****
	@echo Setting up the environment
	cd ui ;	npm install
remove-env:
	conda env remove -p $(ENV)
