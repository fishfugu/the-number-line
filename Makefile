SCENE ?= CompareSpectraScene
FLAGS ?=

# run `make install` or `make` to create a virtual environment and install dependencies
# then run `make run-scene` or `make render-scene` to run/render a scene

# This Makefile is for managing the installation and rendering of scenes using ManimGL.
# It includes targets for creating a virtual environment, installing dependencies, and rendering scenes.
# The default target is to run a scene with the specified SCENE variable.

# .PHONY: setup env clean test

# setup: envrc python-version venv install-deps 

# envrc:
# 	echo 'source ./venv/bin/activate' > .envrc
# 	direnv allow

# python-version:
# 	echo "3.10.13" > .python-version

# venv:
# 	pyenv install --skip-existing 3.10.13
# 	pyenv local 3.10.13
# 	python -m venv venv

# install-manimgl:
# 	. ./venv/bin/activate && pip install --upgrade pip && pip install manimgl

# test:
# 	. ./venv/bin/activate && manimgl manim/scenes/test_scene.py HelloWorld

clean:
	rm -rf venv .envrc .python-version __pycache__ .direnv

# install-deps:
# 	. ./venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

# Create virtual environment if missing
venv/bin/activate:
	@echo "Creating virtual environment..."
	/opt/homebrew/bin/python3.11 -m venv venv
	@echo "Virtual environment created."

# Install packages (runs after venv is created)
install: clean venv/bin/activate
	@echo "Brew Installing requirements..."
	brew update && brew upgrade
	brew cleanup
	brew install ffmpeg
	@echo "Upgrading pip..."
	venv/bin/pip install --upgrade pip
	@echo "Installing packages..."
	venv/bin/pip install -r requirements.txt
	@echo "Installation complete."

# Deploy with git commit and push
deploy-git:
	git commit -a -m "Build site into docs folder for GitHub Pages"
	git push
	@echo "Site deployed to GitHub Pages"
	@echo "Visit https://fishfugu.github.io/creativearts to see the site"

# Convenience shortcut: make all
all: install


# Show live preview (default)
# make run-scene SCENE=VibratingGraphScene
run-scene:
	. ./venv/bin/activate && manimgl --clear-cache --full_screen -c "#008080" $(FLAGS) manim/scenes/ch1_groups_fields.py $(SCENE)

# Render to file (no window)
# make render-scene SCENE=VibratingGraphScene
render-scene:
	. ./venv/bin/activate && manimgl --clear-cache -w --hd --full_screen --finder -c "#008080" $(FLAGS) manim/scenes/ch1_groups_fields.py $(SCENE)

