#!/usr/bin/python

# Copyright: (c) 2023 OlegDy
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
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
'''

EXAMPLES = r'''
# Pass in a message
- name: Test 
  olegdy.my_own_collection.create_file:
    path: /tmp/test.txt
    content: 'Hello'

'''

RETURN = r'''

'''

from ansible.module_utils.basic import AnsibleModule


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=False, default='empty')
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=True,
        original_message='',
        message=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    result['original_message'] = module.params['path']
    result['message'] = '{},{}!'.format(module.params['path'], module.params['content'])

    try:
        file = open(module.params['path'], "w")
        file.write(module.params['content'])
        file.close()
    except FileNotFoundError as error:
        module.fail_json(msg='No such directory', **result)

    # during the execution of the module, if there is an exception or a
    # conditional state that effectively causes a failure, run
    # AnsibleModule.fail_json() to pass in the message and the result
    if module.params['path'] == 'fail me':
        module.fail_json(msg='You requested this to fail', **result)

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()





