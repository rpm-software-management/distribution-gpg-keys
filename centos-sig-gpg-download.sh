#!/bin/bash

# From: https://centos.org/keys/

sigs=("Extras" "Atomic" "Automotive" "Cloud" "ConfigManagement" "Core" "HyperScale" "Infra" "Kmods" "Infra" "NFV" "OpsTools" "PaaS" "SCLo" "Storage" "Virtualization")

for sig in ${sigs[@]}; do
	curl https://centos.org/keys/RPM-GPG-KEY-CentOS-SIG-${sig} > keys/centos/RPM-GPG-KEY-CentOS-SIG-${sig}
done
