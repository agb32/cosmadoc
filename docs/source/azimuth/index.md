# The Azimuth cloud portal

Azimuth is a cloud system hosted within COSMA.

Projects with accounts on Azimuth can manage their own nodes, Slurm clusters, Kubernetes clusters, etc.

# Kubernetes Access

The Azimuth Cloud Portal allow us to deploy Kubernetes clusters using `kubectl` and `k9s`.

To access a Kubernetes cluster you need access to the [Azimuth portal](https://portal.azimuth.cosma.dur.ac.uk).
If you want to have more details about Kubernetes cluster, a Kubernetes configuration file, usually called `kubeconfig`
should be download to your local machine. To be able to use this cluster `kubectl` installed on your local machine. Optional but also recommended: `k9s`

You could check if all installation is good so far by:

```bash
kubectl version --client
helm version
k9s version
```

To interact with a cluster, you sould point your terminal to the downloaded config file.

```bash
export KUBECONFIG=~/.kube/ml-intro.yaml

