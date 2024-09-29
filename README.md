# English with Elegance

This repository contains scripts and Ansible configuration for server management. It hosts the WordPress-based website [www.englishwithelegance.com](englishwithelegance.com).

## Requirements

`ansible-galaxy install nginxinc.nginx`

## Deploy

`ansible-playbook -i inventory.ini provision.yml`
