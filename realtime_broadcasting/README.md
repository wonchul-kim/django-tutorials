## Django Channels, Celery, Redis: Real Time Broadcasting API response App (Jokes) | Django WebSockets

### 1. create project
```
django-admin startproject realtime_broadcasting
```

### 2. create app
```
python manage.py startapp joke
```

### 3. migrate 
```
python manage.py migrate 
```

### 4. make templates
```
mkdir templates && cd templates 
```
* write `index.html` to show count integers


### How to demonstrate 
```
python manage.py migrate 
celery -A realtime_broadcasting beat -l INFO
celery -A realtime_broadcasting worker -l INFO
python manage.py runserver 
```

### install celery
```
pip install 'celery[redis]'
```

### install redis
```
git clone https://github.com/redis/redis
cd redis-stable
make 
```

Need to export redis-stable directory to start the redis-server 
```
vim ~/.bashrc 
# add export PATH=$PATH:$HOME/<path to redis-stable directory>/src
source ~/.bashrc
```

Then, you can start the redis by 
```
redis-server
```

### install channels
```
pip install channels 
```

### install channels-redis
```
pip install channels-redis
```

### reference
* https://www.youtube.com/watch?v=AZNp1CfOjtE&ab_channel=RedEyedCoderClub
