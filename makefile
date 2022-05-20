build:
	python3 src/py/build.py

transcript:
	python3 src/py/transcript.py $e

test:
	cd web && python3 test.py
