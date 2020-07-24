ENV=./venv
PYTHON_DEPENDENCIES_PATH=./webapp/requirements.txt
PYTHON_VERSION=3.7.6


setup:
	@echo "****Project Viral News****"
	@echo "Setting up the environment"
	conda create -p $(ENV) python=$(PYTHON_VERSION)
	conda.bat activate $(ENV)
	pip install -r $(PYTHON_DEPENDENCIES_PATH)
	@cd ui; \
	npm install
remove-env:
	conda env remove -p $(ENV)
