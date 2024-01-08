# Kubernetes

1. Install 6 nodes
   1. https://www.youtube.com/watch?v=CbkEWcUZ7zM&t=3s
   2. https://technotim.live/posts/k3s-etcd-ansible/
   3. https://github.com/techno-tim/k3s-ansible
2. Install Rancher
   1. https://www.youtube.com/watch?v=hT2_O2Yd_wE&t=11s
   2. https://ranchermanager.docs.rancher.com/pages-for-subheaders/install-upgrade-on-a-kubernetes-cluster
   3. https://github.com/JamesTurland/JimsGarage/tree/main/Kubernetes/Rancher-Deployment

    Settings I set
    ```shell
    helm install rancher rancher-stable/rancher \
     --namespace cattle-system \
     --set hostname=rancher.nicholasjbaron.com \
     --set bootstrapPassword=admin
    ```

    ```
    kubectl expose deployment rancher --name=rancher-lb --port=443 --type=LoadBalancer -n cattle-system
    ```
3. Install Longhorn
   1. https://longhorn.io/docs/1.5.3/deploy/install/install-with-helm/
   2. https://longhorn.io/docs/1.5.3/deploy/accessing-the-ui/
   3. https://www.youtube.com/watch?v=eKBBHc0t7bc
4. 