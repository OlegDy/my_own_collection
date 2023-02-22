# Ansible Collection - olegdy.my_own_collection

module: create_file

short_description: This is my test module

description: This is my longer description explaining my test module.

options:
    path:
        description: path
        required: true
        type: str
    content:
        description: content
        required: true
        type: str
        
extends_documentation_fragment:
    - olegdy.my_own_collection.create_file

author:
    - OlegDy

# Install

ansible-galaxy collection install olegdy-my_own_collection-1.0.0.tar.gz

# Example

- name: Create file 
  olegdy.my_own_collection.create_file:
    path: /tmp/test.txt
    content: 'Hello'

