# Ansible
- 멱등성(idempotence) 있음

## reference
https://blog.naver.com/alice_k106/221333208746
https://docs.ansible.com/ansible/latest/

## Inventory
서버목록 정의
- https://docs.ansible.com/ansible/latest/getting_started/get_started_inventory.html
- https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#intro-inventory

### hosts.ini
```ini
some-host-name ansible_host=192.168.1.100 ansible_user=ansible-alicek106
some-host-name2 ansible_host=192.168.1.102 ansible_user=ansible-alicek106

[some-group]
some-host-name2

[all_servers:vars]
ansible_ssh_private_key_file=./mykeypair.pem

[dashboard:vars]
ansible_ssh_private_key_file=./mykeypair.pem

[dashboard]
1.2.3.4 dashboard_domain=my.domain.info 
```

### inventory.yaml
```yaml
webservers:
  hosts:
    webserver01:
      ansible_host: 192.0.2.140
      http_port: 80
    webserver02:
      ansible_host: 192.0.2.150
      http_port: 443
  vars:
    ansible_user: my_server_user
```

### list hosts
```shell
# /etc/ansible/hosts
ansible all --list-hosts
```

### 서버 접속 테스트
```shell
ansible -m ping -i hosts.ini some-group # 특정 그룹만
ansible -m ping -i hosts.ini all # 전체
```

## Playbook
무엇을 할지 정의하는 파일
- https://docs.ansible.com/ansible/latest/getting_started/get_started_playbook.html
- 
### playbook.yaml
```yaml
---
- name: a playbook
  hosts: all
  
  # run with sudo
  become: true
  
  # task with modules
  tasks:
    - name: a task
      yum:
        name: nginx
        state: installed
    
    - name: debug test
      debug:
        msg: "Hello test"
  
...
```

### 실행
```shell
ansible-playbook -i hosts.ini playbook.yaml
```
