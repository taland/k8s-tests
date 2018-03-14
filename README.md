# K8s Playground

## Kubectl

Kubectl is a command line utility (CLI) for running commands against Kubernetes clusters. You need kubectl to interact with your local Kubernetese cluster (i.e. Minikube) as well as remote clusters.

On Mac, you can install Kubectl using one of the following methods,

- Using the Google Cloud SDK: `gcloud components install kubectl`
- Using Homebrew package manager: `brew install kubectl`

For other operating systems please see detailed documentation on [how to install](https://kubernetes.io/docs/tasks/tools/install-kubectl/) kubectl.


## Kubectl Basics

Using kubectl you can interact with various Kubernetes clusters by setting an appropriate context. Typically a kubeconfig file is used to configure access to one or more clusters and include details required for a context. On Mac, this can be found at `~/.kube/config`.

For more details please review [this page](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/) on how to configure access to multiple clusters by using configuration files.

```console
kubectl cluster-info
kubectl config --kubeconfig=config view
kubectl config use-context minikube
kubectl config --kubeconfig=config set-context minikube --cluster=minikube
kubectl config --help
```

Using kubectl you can interact with namespaces. Namespaces are virtual clusters and typically used to isolate projects deployed on Kubernetes cluster.

```console
kubectl get namespace
kubectl create namespace dev
```

When interacting with different namespaces, you can set namespace temporary,

```console
kubectl -n dev get pods
```

Or permanently for all subsequent kubectl commands in that context,

```console
kubectl config set-context $(kubectl config current-context) --namespace=dev
kubectl get pods
```

You can also list and edit pods, deployments, services, ingress, and nodes.

```console
kubectl get pods
kubectl get deployments
kubectl get services
kubectl get ingress
kubectl get nodes
```

## Minikube Basics

Starting the Minikube will create a single-node Kubernetes cluster inside a VM. Minikube start command also creates minikube context and set it as default.

```console
minikube start [--vm-driver=xhyve]
minikube status
```

Kubernetes dashboard is a web-based user interface. You can create and modify individual Kubernetes resources from this UI. It also provides information on the state of Kubernetes resources in your cluster.

By default, Minikube comes with dashboard add-on enabled, and we can access the Kubernetes dashboard in the browser by typing following command.

```console
minikube dashboard [--url]
```

Another way to access dashboard is to use kubectl. Run the following command in your terminal:

```console
kubectl proxy
```

kubectl will handle authentication with API server and make Dashboard available at http://localhost:8001/ui.

You can always stop or delete minikube cluster,

```console
minikube stop
minikube delete
```

In addition, Minikube provides a range of Kubernetes versions to run. You can print a list of available versions to use,

```console
minikube get-k8s-versions
```

Then start Minikube by passing a specific version,

```console
minikube start --kubernetes-version v1.7.0
```

In addition, you can run Minikube with more customised configurations such as you can specify a different network plugin than default or use a different virtual machine driver rather than VirtualBox. You can also change default allocation of memory and CPU.

```console
minikube start --kubernetes-version v1.7.0 \
 --extra-config=proxy.IPTables.SyncPeriod.Duration=5000000000 \
 --extra-config=proxy.IPTables.MinSyncPeriod.Duration=3000000000
 ```

These additional start options can be viewed by running,

```console
minikube start --help
```

## Manage Minikube Add Ons

Minikube provides a set of built-in add-ons and some of them such as dashboard is enabled by default. These add-ons that can be enabled, disabled, or opened inside of the local Kubernetes environment.

```console
minikube addons list
```

For development purpose, I highly recommend enabling heapster add-on. Heapster enables multi-level monitoring and performance analysis including pods, nodes, and cluster.

Under the hood, it is using InfluxDB as the storage backend for metric data and Grafana as visualization UI.

```console
minikube addons enable heapster
minikube addons open heapster
```

Once enabled we can open Grafana UI (to interact with Heapster) in the browser.

I also highly recommend enabling Ingress functionality for your Minikube,

```console
minikube addons enable ingress
```
