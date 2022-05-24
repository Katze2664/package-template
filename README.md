# Package Template

A simple python package template allowing testing with either pytest or tox.

## Usage

To run, clone the repo and do the following:

Tox (slow but more consistent)
 - run `tox .` from inside package-template
   
pytest
 - Set up a venv
 - run pip install -e path/to/package
 - run `pytest`

There are some TODOs, notably renaming things to your liking, and adding dependencies in setup.cfg.

## Future

Best to turn this into a cookiecutter template.
