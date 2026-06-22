.PHONY: setup demo test eval validate safety

export PYTHONDONTWRITEBYTECODE := 1

setup:
	$(MAKE) -C starter-kits/faq-agent-lite setup

demo:
	$(MAKE) -C starter-kits/faq-agent-lite demo

test:
	$(MAKE) -C starter-kits/faq-agent-lite test
	python3 -m unittest discover -s tests

eval:
	$(MAKE) -C starter-kits/faq-agent-lite eval

safety:
	bash scripts/check_no_secrets.sh
	bash scripts/check_no_private_terms.sh
	bash scripts/check_no_pii.sh
	bash scripts/check_public_links.sh
	bash scripts/check_no_generated_artifacts.sh
	bash scripts/check_gitleaks.sh

validate:
	$(MAKE) -C starter-kits/faq-agent-lite validate
	python3 -m unittest discover -s tests
	bash scripts/check_no_secrets.sh
	bash scripts/check_no_private_terms.sh
	bash scripts/check_no_pii.sh
	bash scripts/check_public_links.sh
	bash scripts/check_no_generated_artifacts.sh
	bash scripts/check_gitleaks.sh
