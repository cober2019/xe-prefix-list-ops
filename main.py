import PrefixListOps

def menu_options(ip:str, port:int, username:str, password:str) -> None:

    selection = 0

    while selection != '6':

        selection = input('\n1. View Prefix-lists\n2. Find Prefix\n3. Check Overlapping, User Slected Prefix\n4. Check All List For Overlapping\n5. Find Prefix in RIB\n6. Back To Login\n\nSelection: \n')

        if selection == '1':
            prefix_list = PrefixListOps.get_prefix_list(ip, port, username, password)
            PrefixListOps.view_prefix_list(prefix_list)
        elif selection == '2':
            prefix_list = PrefixListOps.get_prefix_list(ip, port, username, password)
            prefix = input('\nPrefix: \n')
            PrefixListOps.find_prefix(prefix_list, prefix)
        elif selection == '3':
            prefix_list = PrefixListOps.get_prefix_list(ip, port, username, password)
            prefix = input('\nPrefix: \n')
            PrefixListOps.check_proposed_overlapping(prefix_list, prefix)
        elif selection == '4':
            prefix_list = PrefixListOps.get_prefix_list(ip, port, username, password)
            PrefixListOps.check_overlapping(prefix_list)
        elif selection == '5':
            prefix = input('\nPrefix: \n')
            PrefixListOps.find_prefix_in_rib(ip, port, username, password, prefix)
        elif selection == '6':
            main_menu()
        else:
            print('\nInvalid Selection\n')

def main_menu():

    ip = input('IP: ')
    username = input('Username: ')
    password = input('Password: ')
    port = input('Port: ')

    menu_options(ip, port, username, password)
    main_menu()


if __name__ == '__main__':

    main_menu()





