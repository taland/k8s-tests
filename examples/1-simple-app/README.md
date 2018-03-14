## Build local Docker images and deploy them to Minikube

A. Build Docker image message-api against the minikube

```
eval $(minikube docker-env)
docker build -t message-api:v1 .
```

Please note that eval $(minikube docker-env) enables us to interact and build against docker daemon inside the minikube VM.

B. Create a deployment message-api

```
kubectl run hello-python --image=message-api:v1 --port=5000
```

C. Expose deployment message-api as service

```
kubectl expose deployment hello-python --type=NodePort
kubectl get services
```

As you can see, everytime you make changes in your code you still have to repeat few things: build a new Docker images (Step-A) and then update our deployment to use updated Docker image (Step-D).

D. Update the deployment to use updated Docker image

```
kubectl set image deployment/message-api *=message-api:v1
```

To avoid this repetition we are going to add a Makefile in our project folder. In this Makefile we will add an update command which basically allows us to automate step-A and step-D.

```
.PHONY: update
update:  
    @eval $$(minikube docker-env) ;\
    docker image build -t message-api:v1 -f Dockerfile .
    kubectl set image deployment/message-api *=message-api:v1
```

Now all we need is to run `make update` command after every code change and we will see update results in Minikube.