"""Entry poing for prefix-list ops. Function for main menu"""

import PrefixListOps

def ge_le() -> tuple:
    """Get ge and le for prefix statement"""

    ge = input('ge: ')
    le = input('le: ')
    print('\n')

    if ge == '':
        ge = None
    if le == '':
        le = None

    return ge, le

def menu_options(ip:str, port:int, username:str, password:str) -> None:
    """Menu options"""
    
    #Use while loop so the user doesn't have to endter credentials unless using option 6
    selection = 0
    
    while selection != '6':

        selection = input('\n1. View Prefix-lists\n2. Find Prefix\n3. Check Overlapping, User Selected Prefix\n4. Check All List For Overlapping\n5. Find Prefix in RIB\n6. Back To Login\n\nSelection: ')

        if selection == '1':
            prefix_list = PrefixListOps.get_prefix_list(ip, port, username, password)
            PrefixListOps.view_prefix_list(prefix_list)
        elif selection == '2':
            prefix_list = PrefixListOps.get_prefix_list(ip, port, username, password)
            prefix = input('\nPrefix: ')
            PrefixListOps.find_prefix(prefix_list, prefix)
        elif selection == '3':
            prefix_list = PrefixListOps.get_prefix_list(ip, port, username, password)
            prefix = input('\nPrefix: ')
            is_ge_and_le = ge_le()
            PrefixListOps.check_proposed_overlapping(prefix_list, prefix, is_ge_and_le[0], is_ge_and_le[1])
        elif selection == '4':
            prefix_list = PrefixListOps.get_prefix_list(ip, port, username, password)
            PrefixListOps.check_overlapping(prefix_list)
        elif selection == '5':
            prefix = input('\nPrefix: ')
            PrefixListOps.find_prefix_in_rib(ip, port, username, password, prefix)
        elif selection == '6':
            main_menu()
        else:
            print('\nInvalid Selection\n')

def main_menu():
    """Get device credentials"""
    
    print('\nPrefix-List-Ops\n------------------\n')
    
    ip = input('IP: ')
    username = input('Username: ')
    password = input('Password: ')
    port = input('Port: ')

    menu_options(ip, port, username, password)
    main_menu()


if __name__ == '__main__':

    try:
        main_menu()
    except BaseException as e:
        print(f'Something Went Wrong: {e}')
        main_menu()





