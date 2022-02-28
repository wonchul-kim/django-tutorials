## Count the number in realtime using Django-channels 

### 1. create project
```
django-admin startproject realtime_count
```

### 2. create app
```
python manage.py startapp integers
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
python manage.py runserver 
```

### reference:
* https://www.youtube.com/watch?v=R4-XRK6NqMA



