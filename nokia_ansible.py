A sample ansible config for Nokia SROS device. 

  GNU nano 4.8                                     nokia_config.yaml                                               ---
- hosts: nokia_classic
  vars:
    - ansible_network_os: nokia.sros.classic
  vars_prompt:
    - name: ansible_user
      prompt: "Username"
      private: no
    - name: ansible_password
      prompt: "Password"
  connection: network_cli
  gather_facts: No

  collections:
  - nokia.sros

  tasks:
  - name: do some config
    cli_config:
      config: |
        configure system
        contact baris
        location istanbul
        exit all
...
