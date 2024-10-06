# English with Elegance

This repository contains scripts and Ansible configuration for server management. It hosts the WordPress-based website [englishwithelegance.com](www.englishwithelegance.com).

## Requirements

`ansible-galaxy install nginxinc.nginx`

## Deploy

`ansible-playbook -i inventory.ini provision.yml`

## Vault

`ansible-vault create vault.yml` and `ansible-vault edit vault.yml  --ask-vault-pass`.
