build:
	python3 src/py/build.py

transcript:
	python3 src/py/transcript.py $e

article:
	python3 src/py/article.py refugee-health

test:
	cd web && python3 test.py
