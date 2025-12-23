#!/bin/bash

# From: https://centos.org/keys/

sigs=("Extras" "AltImages" "Atomic" "Automotive" "Cloud" "ConfigManagement" "Core" "HyperScale" "Infra" "ISA" "Kmods" "Messaging" "NFV" "OpsTools" "PaaS" "Proposed-Updates" "SCLo" "Storage" "Virtualization")

for sig in ${sigs[@]}; do
	curl https://centos.org/keys/RPM-GPG-KEY-CentOS-SIG-${sig} > keys/centos/RPM-GPG-KEY-CentOS-SIG-${sig}
done
