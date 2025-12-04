<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: ansible-apt
Configures apt and installs/updates packages

Tags: system, apt

## Requirements

| Platform | Versions |
| -------- | -------- |
| Ubuntu | all |
| Debian | all |

## Role Arguments


### Entrypoint: main

Configure apt

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| apt_aptitude_solution_cost | Change Aptitudes solution costs, default is not to change anything. Mirror https://lists.debian.org/543FF3BD.1020609@zen.co.uk | list of 'str' | no | [] |
| apt_auto_clean_interval | Do "apt-get autoclean" every n-days (0=disable) | int | no | 0 |
| apt_autoclean | remove .deb files for packages no longer on your system | bool | no | True |
| apt_autoremove | remove packages that are no longer needed for dependencies | bool | no | True |
| apt_cache_update | Run apt-get update before installing/upgrading a package | bool | no | True |
| apt_cache_valid_time | sets the amount of time the cache is valid | int | no | 3600 |
| apt_clean_sources_list | Clean /etc/apt/sources.list | bool | no | False |
| apt_deb822_repositories | deb822 repositories configuration | list of 'dict' | no | [] |
| apt_deb_packages | .deb packages to install | list of 'str' | no | [] |
| apt_dependencies | depenencies packages | list of 'str' | no | ['aptitude', 'python3-apt', 'python3-pycurl', 'python3-debian'] |
| apt_download_upgradeable_packages | Do "apt-get upgrade -download-only" every n-days (0=disable) | int | no | 0 |
| apt_install_recommends | do not install Recommended packages by default | bool | no | False |
| apt_install_suggests | whether or not suggested packages should be installed. | bool | no | False |
| apt_keys | gpg keys for external repositories | list of 'str' | no | [] |
| apt_mails | List of apt mails items | list of 'str' | no | [] |
| apt_package_state | default package state | str | no | present |
| apt_packages | packages to ensure | list of 'str' | no | [] |
| apt_periodic | Enable the update/upgrade script | bool | no | True |
| apt_policy | https://people.debian.org/~hmh/invokerc.d-policyrc.d-specification.txt | int | no | 101 |
| apt_preferences | List of preferences options | list of 'dict' | no | [] |
| apt_remount_filesystems | remount file system: supported options are rootfs and tmpfs | list of 'str' | no | [] |
| apt_remove_purge | purge configuration when removing packages | bool | no | False |
| apt_remove_recommends | allow 'apt-get autoremove' to remove recommended packages | bool | no | False |
| apt_remove_suggests | allow 'apt-get autoremove' to remove suggested packages | bool | no | False |
| apt_repositories | repositories to register | list of 'dict' | no | [] |
| apt_unattended_upgrades | enable unattended-upgrades | bool | no | True |
| apt_unattended_upgrades_allowed | List of allowed-origins | list of 'str' | no | ['${distro_id}:${distro_codename}-security'] |
| apt_unattended_upgrades_automatic_reboot | Automatically reboot if the file /var/run/reboot-required is found after the upgrade | bool | no | False |
| apt_unattended_upgrades_automatic_reboot_time | If automatic reboot is enabled and needed, reboot at the specific time instead of immediately | str | no | now |
| apt_unattended_upgrades_automatic_reboot_with_users | Automatically reboot even if there are users currently logged in | bool | no | False |
| apt_unattended_upgrades_autoremove | Do automatic removal of new unused dependencies after the upgrade | bool | no | True |
| apt_unattended_upgrades_blacklist | Upgrades blacklist ackages | list of 'str' | no | [] |
| apt_unattended_upgrades_download_timer_override | Override download timer | dict | no |  |
| apt_unattended_upgrades_minimal_steps | Split the upgrade into the smallest possible chunks so that they can be interrupted with SIGUSR1. This makes the upgrade a bit slower but it has the benefit that shutdown while a upgrade is running is possible (with a small delay) | bool | no | False |
| apt_unattended_upgrades_notify_error_only | Set this value to "true" to get emails only on errors. Default is to always send a mail if Unattended-Upgrade::Mail is set | bool | no | True |
| apt_unattended_upgrades_origins | list of origins patterns to control which packages are upgraded replaces allowed-origins, kept for compatibility | list of 'str' | no | [] |
| apt_unattended_upgrades_syslog_enable | Enable logging to syslog | bool | no | False |
| apt_unattended_upgrades_syslog_facility | Specify syslog facility | str | no | daemon |
| apt_unattended_upgrades_upgrade_timer_override | Override upgrade timer | dict | no |  |
| apt_update_package_lists | Do "apt-get update" automatically every n-days (0=disable) | int | no | 1 |
| apt_upgrade | upgrade system | str | no | no |

#### Choices for main > apt_upgrade

|Choice|
|---|
| no |
| safe |
| full |
| dist |



## Dependencies
None.

## Example Playbook

```
- hosts: all
  tasks:
    - name: Importing role: ansible-apt
      ansible.builtin.import_role:
        name: ansible-apt
      vars:
```

## License

MIT

## Author and Project Information
franklin @ We Are Interactive

<!-- END_ANSIBLE_DOCS -->
