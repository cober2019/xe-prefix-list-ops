XE Prefix-List Ops
==================

This is a collections of functions that allow you to view, and check prefix-lists:

- View prefix-lists
- Find a prefix in the device prefix-list
- Find a prefix in the routing table
- Propose a prefix and check it against the current list
- Find overlapping prefix in all prefix-lists


Functions:
-----------
- get_prefix_list(ip, port, username, password)
- view_prefix_list(prefix_lists)
- find_prefix(prefix_lists, prefix)
- check_proposed_overlapping(prefix_lists, proposed_prefix, ge, le)
- check_overlapping(prefix_lists)
- find_prefix_in_rib(ip, port, username, password, prefix)
