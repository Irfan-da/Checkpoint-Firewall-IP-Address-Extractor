import json

# open the json file containing members of group
with open('FILENAME.json', 'r') as f:
    content = json.load(f)

# loop for number of members
for numbers in range(0, len(content['members'])):
    try:
        # for members having Subnet mask other than /32 mask
        ip_sub = content['members'][numbers]['subnet4']
        subnet = content['members'][numbers]['subnet-mask']
        print(f"{ip_sub} {subnet}")

    except KeyError as subnet_error:
        if subnet_error.args[0] == 'subnet4':
            try:
                # for members having /32 mask
                ip_4 = content['members'][numbers]['ipv4-address']
                subnet = '255.255.255.255'
                print(f"{ip_4} {subnet}")

            except KeyError as address_range_error:
                # for members having range mask
                if address_range_error.args[0] == 'ipv4-address':
                    ip_1 = content['members'][numbers]['ipv4-address-first']
                    ip_2 = content['members'][numbers]['ipv4-address-last']
                    print(f"{ip_1} {ip_2}")
