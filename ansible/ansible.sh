#ansible all --list-hosts -i hosts.ini
#ansible all -m ping -i hosts.ini -u hadoop
#ansible-inventory -i inventory.yaml --list
#ansible virtualmachines -m ping -i inventory.yaml
ansible-playbook -i inventory.yaml playbook.yaml


