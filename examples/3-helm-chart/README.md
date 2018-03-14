## Prerequisites

- Kubernetes 1.9+ with Beta APIs enabled
- PV provisioner support in the underlying infrastructure

## Lint the Chart

```console
helm lint .
```

## Installing the Chart

```console
helm install --name <chart-name> .
```

If overriding of some parameters are needed:

```console
helm install -f myvalues.yaml --name <chart-name> .
```

This option might be useful for CI/CD.

## Uninstalling the Chart

To uninstall/delete the chart deployment:

```console
helm del [--purge] <chart-name>
```

## Configuration

The following tables lists the configurable parameters of the chart and their default values.

| Parameter        | Description                  | Default |
| ---              | ---                          | --- |
| app.replicaCount | Number of ReplicaSets        | 1 |
