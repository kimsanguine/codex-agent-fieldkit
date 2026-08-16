.PHONY: doctor setup demo test eval validate safety validate-report

export PYTHONDONTWRITEBYTECODE := 1

PRIMARY_KIT := $(shell python3 scripts/starter_registry.py --primary-path)

doctor:
	python3 scripts/doctor.py

setup:
	$(MAKE) -C $(PRIMARY_KIT) setup

demo:
	$(MAKE) -C $(PRIMARY_KIT) demo

test:
	$(MAKE) -C $(PRIMARY_KIT) test
	python3 -m unittest discover -s tests

eval:
	$(MAKE) -C $(PRIMARY_KIT) eval

safety:
	bash scripts/check_no_secrets.sh
	bash scripts/check_no_private_terms.sh
	bash scripts/check_no_pii.sh
	bash scripts/check_public_links.sh
	bash scripts/check_no_generated_artifacts.sh
	bash scripts/check_gitleaks.sh
	bash scripts/check_public_surface.sh

validate:
	python3 scripts/run_validation.py

validate-report:
	python3 scripts/write_validation_report.py
