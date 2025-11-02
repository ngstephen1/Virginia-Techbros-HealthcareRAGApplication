.PHONY: venv install-lite index query eval clean
venv:
	python3 -m venv .venv
install-lite: venv
	. .venv/bin/activate; python -m pip install --upgrade pip
	. .venv/bin/activate; pip install -r server/requirements.txt
	. .venv/bin/activate; pip install requests
index:
	. .venv/bin/activate; python scripts/build_index.py
query:
	. .venv/bin/activate; python scripts/offline_query.py "$(Q)"
eval:
	. .venv/bin/activate; python eval/run_eval.py
clean:
	rm -rf .venv data/index
