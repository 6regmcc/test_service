docker run -d -p 3000:8080 test_service
docker build -t test_service .
docker tag test_service 6regmcc/test-service
docker push 6regmcc/test-service   