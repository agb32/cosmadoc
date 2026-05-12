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

