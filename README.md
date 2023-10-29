# How to run celeryhillel 

Step one, install dependencies:
```
 pip install -r requirements.txt
```

Step two, run broker:
```
docker run -d -p 5672:5672 rabbitmq
```

Step three, set variables:

```
Mac&Linux:
export TWILIO_ACCOUNT_SID="your sid"
export TWILIO_AUTH_TOKEN="your token"

Windows PowerShell:
$Env:TWILIO_ACCOUNT_SID="your sid"
$Env:TWILIO_AUTH_TOKEN="your token"
```

Step four, run worker:
```
celery -A celeryhillel worker -l INFO
```

Step five, run web server:
```
python manage.py runserver

OR python3 manage.py runserver
```