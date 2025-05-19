SCENE ?= CompareSpectraScene
FLAGS ?=
OUTPUT_DIR ?= videos

.PHONY: setup env clean test

setup: envrc python-version venv install-deps 

envrc:
	echo 'source ./venv/bin/activate' > .envrc
	direnv allow

python-version:
	echo "3.10.13" > .python-version

venv:
	pyenv install --skip-existing 3.10.13
	pyenv local 3.10.13
	python -m venv venv

install-manimgl:
	. ./venv/bin/activate && pip install --upgrade pip && pip install manimgl

test:
	. ./venv/bin/activate && manimgl manim/scenes/test_scene.py HelloWorld

clean:
	rm -rf venv .envrc .python-version __pycache__ .direnv

install-deps:
	. ./venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt


# Show live preview (default)
# make run-scene SCENE=VibratingGraphScene
run-scene:
	. ./venv/bin/activate && manimgl --clear-cache --full_screen -c "#008080" $(FLAGS) manim/scenes/sagt.py $(SCENE)

# Render to file (no window)
# make render-scene SCENE=VibratingGraphScene
render-scene:
	. ./venv/bin/activate && manimgl --clear-cache -w --hd --full_screen --finder -c "#008080" $(FLAGS) manim/scenes/sagt.py $(SCENE)

