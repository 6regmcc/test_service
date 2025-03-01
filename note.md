docker run -d -p 3000:8080 servicenew 
docker build -t servicenew .
docker tag servicenew 6regmcc/servicenew:42
docker push 6regmcc/servicenew:42
kubectl rollout restart deployment testservicea



minikube tunnel
minikube addons enable ingress