# The Azimuth cloud portal

Azimuth is a cloud system hosted within COSMA.

Projects with accounts on Azimuth can manage their own nodes, Slurm clusters, Kubernetes clusters, etc.

# Kubernetes Access

The Azimuth Cloud Portal allow us to deploy Kubernetes clusters using `kubectl` and `k9s`.

To access a Kubernetes cluster you need access to the [Azimuth portal](https://portal.azimuth.cosma.dur.ac.uk).
If you want to have more details about Kubernetes cluster, a Kubernetes configuration file, usually called `kubeconfig`
should be download to your local machine. To be able to use this cluster `kubectl` installed on your local machine. Optional but also recommended: `k9s`

You can check if all installation is good so far by:

```bash
kubectl version --client
helm version
k9s version
```

To interact with a cluster, you sould point your terminal to the downloaded config file.

```bash
export KUBECONFIG=~/.kube/ml-intro.yaml

You can check that access works:

```bash
kubectl cluster-info
kubectl get nodes
```

Example output:

```text
NAME                                  STATUS   ROLES           VERSION   INTERNAL-IP
ml-intro-control-plane-65mpf          Ready    control-plane   v1.34.6   x.x.x.x
ml-intro-control-plane-l4rv2          Ready    control-plane   v1.34.6   x.x.x.x
ml-intro-control-plane-ntm9r          Ready    control-plane   v1.34.6   x.x.x.x
ml-intro-ml-intro-69ngd-ckrhh         Ready    worker          v1.34.6   x.x.x.x
```

---

## Using K9s

`k9s` is a terminal user interface for Kubernetes. It is can be useful for checking pods, logs, deployments, services, config maps, and secrets.

```bash
k9s
```
## Checking the Current Context

Kubernetes commands are run against the current context in your kubeconfig.

```bash
kubectl config current-context
```

List all available contexts:

```bash
kubectl config get-contexts
```

Switch context:

```bash
kubectl config use-context <context-name>
```

Example:

```bash
kubectl config use-context ml-intro-admin@ml-intro
```

## Multiple Kubernetes Clusters

Users may have access to more than one Kubernetes cluster, for example a GPU cluster,ML cluster etc. Kubernetes uses a file called a `kubeconfig` to store cluster connection details, users, namespaces, and contexts.

Kubernetes can merge multiple kubeconfig files using the KUBECONFIG environment variable:

```bash
export KUBECONFIG=$HOME/.kube/config:$HOME/ml-intro.yaml:$HOME//test-cluster.yaml
```

## JupyterHub Configurations

Jupyter notebooks runs as a Kubernetes pod inside the JupyterHub namespaces.  In those namespaces, diffrent reproducible deployments can be created via Helm charts. To maintaine and extend user resoruces, it could build unlike Docker images such as, GPU-enabled notebook, CPU-based notebook, C/C++ notebook etc. For more details please check [here](https://z2jh.jupyter.org/en/stable/resources/reference.html)


