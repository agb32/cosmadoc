# The Azimuth cloud portal

Azimuth is a cloud system hosted within COSMA.

Projects with accounts on Azimuth can manage their own nodes, Slurm clusters, Kubernetes clusters, etc.

# Kubernetes 

The Azimuth Cloud Portal allow us to deploy Kubernetes clusters using `kubectl` and `k9s`.

To interact with a cluster, you sould point your terminal to the downloaded config file.

```bash
export KUBECONFIG=~/.kube/ml-intro.yaml