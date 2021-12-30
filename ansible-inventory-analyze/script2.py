#!/usr/bin/env python

from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager

def get_groups(inventory_file_path):

    inv_file = open(inventory_file_path, 'r')
    group_list = []

    for line in inv_file :
        if ( line[0] == '['  ) :
            line = line.lstrip('[').split(']')[0]

            if ( not ((':children' ) in line)  ):
                group_list.append(line)
                print(line)
    inv_file.close()

    if ( 'all' in group_list  ):
        group_list.remove('all')
    group_list.sort()

    return group_list


def inv(inventory_file_path):

    data_loader = DataLoader()
    inventory = InventoryManager(loader = data_loader, sources=[inventory_file_path])
    return inventory


if __name__ == '__main__':

    inventory_file_path = 'inv.txt'

    inv_my = inv(inventory_file_path)
    group_list = get_groups(inventory_file_path)
    hosts_list = list(inv_my.get_hosts())


    for current_host in hosts_list:
        current_host = str(current_host)
        print( "Groups for Host : " + current_host)
        current_host_groups_list = []
        for current_group in group_list:

           hosts_in_current_group = inv_my.get_groups_dict()[current_group]

           if (str(current_host) in hosts_in_current_group):
               print(current_host + ":  " + current_group)
               current_host_groups_list.append(current_group)

        print('')
