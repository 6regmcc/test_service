docker run -d -p 3000:8080 test_service
docker build -t servicenew .
docker tag servicenew 6regmcc/servicenew:28
docker push 6regmcc/servicenew:28