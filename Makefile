up:
	pip install -r requirements.txt

ab-sanic:
	 ab -n 1000 -c 50 http://localhost:8080/url-parser\?target\=https://www.nytimes.com/2018/10/01/opinion/justice-kavanaugh-recuse-himself.html

ab-japronoto:
	 ab -n 1000 -c 50 http://localhost:8000/url-parser\?target\=https://www.nytimes.com/2018/10/01/opinion/justice-kavanaugh-recuse-himself.html

# Setup venv locally (no docker)
venv:
	virtualenv -p python3 venv

# Install dependencies locally (no docker)
requrirements:
	source venv/bin/activate
	pip install -r app/requirements.txt
