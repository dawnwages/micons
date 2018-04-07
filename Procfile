#web: gunicorn micons.wsgi --log-file -
web: uwsgi --http :$PORT --module micons.heroku_wsgi --master --processes 2 --static-map /media/=/app/media/ --offload-threads 1