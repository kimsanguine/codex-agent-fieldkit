.PHONY: setup demo test eval validate

PYTHONPATH := src
export PYTHONPATH
export PYTHONDONTWRITEBYTECODE := 1

setup:
	python3 scripts/check_env.py

demo:
	python3 -m faq_agent_lite.cli demo

test:
	python3 -m unittest discover -s tests

eval:
	python3 scripts/eval.py

validate:
	python3 scripts/check_env.py
	python3 -m unittest discover -s tests
	python3 scripts/eval.py
	python3 scripts/secret_scan.py
