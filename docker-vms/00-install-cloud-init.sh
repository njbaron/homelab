#!/bin/bash
# https://technotim.live/posts/cloud-init-cloud-image/
UBUNTU_CLOUD_INIT_IMAGE_PATH=$1
VI_ID=9000
DEFAULT_MEMEORY_MB=2048
DEFAULT_CORES=2
PVE_STORAGE_TARGET=pve-nvme0
CONTAINER_NAME=ubuntu-2204-cloud

set -e
set -x

qm create $VI_ID --memory $DEFAULT_MEMEORY_MB --core $DEFAULT_CORES --name $CONTAINER_NAME --net0 virtio,bridge=vmbr0
created_storage=`qm importdisk $VI_ID $UBUNTU_CLOUD_INIT_IMAGE_PATH $PVE_STORAGE_TARGET | grep "Successfully imported disk as" | tr -d "'" | awk '{print $NF}'`
created_storage="${created_storage/'unused0:'/''}"
qm set $VI_ID --scsihw virtio-scsi-pci --scsi0 $created_storage
qm set $VI_ID --ide2 $PVE_STORAGE_TARGET:cloudinit
qm set $VI_ID --boot c --bootdisk scsi0
qm set $VI_ID --serial0 socket --vga serial0