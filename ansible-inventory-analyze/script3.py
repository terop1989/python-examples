#!/usr/bin/env python

from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager

data_loader = DataLoader()
inv_file = 'inv.txt'

def inv(inventory_file_path):
    inventory = InventoryManager(loader = data_loader, sources=[inventory_file_path])
    return inventory

def hosts_in_group(group_name):
    hosts = inv(inv_file).get_groups_dict()[group_name]
    return hosts

def get_group_var(group_name, var_name):
    host0 = inv(inv_file).get_host(hosts_in_group(group_name)[0])
    var_man = VariableManager(loader=data_loader, inventory= inv(inv_file))
    v2 = var_man.get_vars(host=host0)
    group_var = str(v2[var_name])
    return group_var


inv_my = inv(inv_file)
variable_manager = VariableManager(loader=data_loader, inventory= inv(inv_file))

print("")
print("For all hosts in inventory:")
hostnames = []
for host in inv_my.get_hosts():
    hostnames.append(variable_manager.get_vars(host=host))

for host in hostnames:
    print(str(host['version']))
print("")

print("For hosts in group 'servers':")
servers_group = hosts_in_group('servers')
hostnames2 = []
for hhh in servers_group:
    h1 = inv_my.get_host(hhh)
    v = variable_manager.get_vars(host=h1)
    hostnames2.append(variable_manager.get_vars(host=h1))

for host2 in hostnames2:
    print(str(host2['version']))
print("")


group = 'servers'
var = 'version'
vvv = get_group_var(group, var)
print("For Group '" + group + "' Value of Variable '" + var + "' = " + vvv)
print("")
