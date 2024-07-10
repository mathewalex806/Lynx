# Lynx

Building docker image 
```
docker build -t lynx:1.0 .
```
Run command:
```
docker run --env-file .env -p 8000:8000 -v $(pwd):/app lynx:1.0
```