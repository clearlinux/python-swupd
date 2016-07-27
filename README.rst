Python swupd bindings
=====================

Module Description
``````````````````

swupd.py is an API module intended for developers that want to add swupd
functionality (install, remove, update) into their codes.

Prerequisites
-------------
- swupd: https://clearlinux.org/features/software-update


Functions
----------
get_latest_version
    :Description: Gets the latest Clear Linux version as stated at:
        https://download.clearlinux.org/update/version/formatstaging/latest
    :Arguments: None
    :Returns: latest Clear Linux Version as string
get_bundle_list
    :Description: Gets the names of all the available bundles for a given Clear Linux version
    :Arguments: Clear Linux version number as string
    :Returns: List of bundles as list
get_installed_bundles
    :Description: Gets the names of the bundles installed in the system
    :Arguments: None
    :Returns: List of bundles as list
install_bundles
    :Description: Install one or more bundles in the system
    :Arguments: List of bundles as list
                F: Format, optional as string
                url: URL, optional as string
    :Returns: stdout as string, stderr as string, exit status as int
remove_bundles
    :Description: Removes one or more bundles from the system
    :Arguments: List of bundles as list
    :Returns: stdout as string, stderr as string, exit status as int
update
    :Description: Performs a full update of the system
    :Arguments: None
    :Returns: stdout as string, stderr as string, exit status as int

Examples
````````

>>> Python 2.7.11 (default, May  1 2016, 00:18:30)
[GCC 6.1.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import swupd

>>> swupd.get_latest_version()
'9400'

>>> swupd.get_bundle_list('9400')
['sysadmin', 'os-cloudguest-cci', 'openstack-all-in-one', 'devtools-extras', 'kernel-embedded', ... , 'opencontainers-dev', 'machine-learning-basic', 'go-basic', 'dev-utils', 'bootloader']

>>> swupd.get_installed_bundles()
['R-extras', 'pxe-server', 'network-proxy-client', 'R-basic', 'koji', ... , 'mail-utils', 'openstack-python-clients', 'sysadmin-hostmgmt', 'os-utils-gui', 'go-extras']

>>> swupd.install_bundles(['games','rust-basic'])
('swupd-client bundle adder 3.5.5\n   Copyright (C) 2012-2016 Intel Corporation\n\nDownloading required packs...\nAttempting to download version string to memory\nInstalling bundle(s) files...\nCalling post-update helper scripts.\nNo kernel update needed, skipping helper call out.\nNo bootloader update needed, skipping helper call out.\nBundle(s) installation done.\nswupd-client bundle adder 3.5.5\n   Copyright (C) 2012-2016 Intel Corporation\n\nDownloading required packs...\nAttempting to download version string to memory\nInstalling bundle(s) files...\nCalling post-update helper scripts.\nNo kernel update needed, skipping helper call out.\nNo bootloader update needed, skipping helper call out.\nBundle(s) installation done.\n', '', 0)

>>> swupd.remove_bundles(['games','rust-basic'])
('swupd-client bundle remover 3.5.5\n   Copyright (C) 2012-2016 Intel Corporation\n\nDeleting bundle files...\nTotal deleted files: 23\nUntracking bundle from system...\nSuccess: Bundle removed\nswupd-client bundle remover 3.5.5\n   Copyright (C) 2012-2016 Intel Corporation\n\nDeleting bundle files...\nTotal deleted files: 43\nUntracking bundle from system...\nSuccess: Bundle removed\n', '', 0)
