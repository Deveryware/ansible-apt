# ansible-apt

Configures apt and installs/updates packages

## Table of contents

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [apt_aptitude_solution_cost](#apt_aptitude_solution_cost)
  - [apt_auto_clean_interval](#apt_auto_clean_interval)
  - [apt_autoclean](#apt_autoclean)
  - [apt_autoremove](#apt_autoremove)
  - [apt_cache_update](#apt_cache_update)
  - [apt_cache_valid_time](#apt_cache_valid_time)
  - [apt_clean_sources_list](#apt_clean_sources_list)
  - [apt_deb822_repositories](#apt_deb822_repositories)
  - [apt_deb_packages](#apt_deb_packages)
  - [apt_dependencies](#apt_dependencies)
  - [apt_download_upgradeable_packages](#apt_download_upgradeable_packages)
  - [apt_install_recommends](#apt_install_recommends)
  - [apt_install_suggests](#apt_install_suggests)
  - [apt_keys](#apt_keys)
  - [apt_mails](#apt_mails)
  - [apt_package_state](#apt_package_state)
  - [apt_packages](#apt_packages)
  - [apt_periodic](#apt_periodic)
  - [apt_policy](#apt_policy)
  - [apt_preferences](#apt_preferences)
  - [apt_remount_filesystems](#apt_remount_filesystems)
  - [apt_remove_purge](#apt_remove_purge)
  - [apt_remove_recommends](#apt_remove_recommends)
  - [apt_remove_suggests](#apt_remove_suggests)
  - [apt_repositories](#apt_repositories)
  - [apt_unattended_upgrades](#apt_unattended_upgrades)
  - [apt_unattended_upgrades_allowed](#apt_unattended_upgrades_allowed)
  - [apt_unattended_upgrades_automatic_reboot](#apt_unattended_upgrades_automatic_reboot)
  - [apt_unattended_upgrades_automatic_reboot_time](#apt_unattended_upgrades_automatic_reboot_time)
  - [apt_unattended_upgrades_automatic_reboot_with_users](#apt_unattended_upgrades_automatic_reboot_with_users)
  - [apt_unattended_upgrades_autoremove](#apt_unattended_upgrades_autoremove)
  - [apt_unattended_upgrades_blacklist](#apt_unattended_upgrades_blacklist)
  - [apt_unattended_upgrades_download_timer_override](#apt_unattended_upgrades_download_timer_override)
  - [apt_unattended_upgrades_minimal_steps](#apt_unattended_upgrades_minimal_steps)
  - [apt_unattended_upgrades_notify_error_only](#apt_unattended_upgrades_notify_error_only)
  - [apt_unattended_upgrades_origins](#apt_unattended_upgrades_origins)
  - [apt_unattended_upgrades_syslog_enable](#apt_unattended_upgrades_syslog_enable)
  - [apt_unattended_upgrades_syslog_facility](#apt_unattended_upgrades_syslog_facility)
  - [apt_unattended_upgrades_upgrade_timer_override](#apt_unattended_upgrades_upgrade_timer_override)
  - [apt_update_package_lists](#apt_update_package_lists)
  - [apt_upgrade](#apt_upgrade)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.4`

## Default Variables

### apt_aptitude_solution_cost

Change Aptitudes solution costs, default is not to change anything. Mirror https://lists.debian.org/543FF3BD.1020609@zen.co.uk


**_Type:_** list<br />

#### Default value

```YAML
apt_aptitude_solution_cost: []
```

### apt_auto_clean_interval

Do "apt-get autoclean" every n-days (0=disable)

**_Type:_** int<br />

#### Default value

```YAML
apt_auto_clean_interval: 0
```

### apt_autoclean

remove .deb files for packages no longer on your system

**_Type:_** bool<br />

#### Default value

```YAML
apt_autoclean: yes
```

### apt_autoremove

remove packages that are no longer needed for dependencies

**_Type:_** bool<br />

#### Default value

```YAML
apt_autoremove: yes
```

### apt_cache_update

Run apt-get update before installing/upgrading a package

**_Type:_** bool<br />

#### Default value

```YAML
apt_cache_update: yes
```

### apt_cache_valid_time

sets the amount of time the cache is valid

**_Type:_** int<br />

#### Default value

```YAML
apt_cache_valid_time: 3600
```

### apt_clean_sources_list

Clean /etc/apt/sources.list

**_Type:_** bool<br />

#### Default value

```YAML
apt_clean_sources_list: false
```

### apt_deb822_repositories

deb822 repositories configuration

**_Type:_** list<br />

#### Default value

```YAML
apt_deb822_repositories: []
```

### apt_deb_packages

.deb packages to install

**_Type:_** list<br />

#### Default value

```YAML
apt_deb_packages: []
```

### apt_dependencies

depenencies packages

**_Type:_** list<br />

#### Default value

```YAML
apt_dependencies:
  - aptitude
  - python3-apt
  - python3-pycurl
  - python3-debian
```

### apt_download_upgradeable_packages

Do "apt-get upgrade -download-only" every n-days (0=disable)

**_Type:_** int<br />

#### Default value

```YAML
apt_download_upgradeable_packages: 0
```

### apt_install_recommends

do not install Recommended packages by default

**_Type:_** bool<br />

#### Default value

```YAML
apt_install_recommends: no
```

### apt_install_suggests

whether or not suggested packages should be installed.

**_Type:_** bool<br />

#### Default value

```YAML
apt_install_suggests: no
```

### apt_keys

gpg keys for external repositories

**_Type:_** list<br />

#### Default value

```YAML
apt_keys: []
```

### apt_mails

List of apt mails items

**_Type:_** list<br />

#### Default value

```YAML
apt_mails: []
```

### apt_package_state

default package state

**_Type:_** str<br />

#### Default value

```YAML
apt_package_state: present
```

### apt_packages

packages to ensure

**_Type:_** list<br />

#### Default value

```YAML
apt_packages: []
```

### apt_periodic

Enable the update/upgrade script

**_Type:_** bool<br />

#### Default value

```YAML
apt_periodic: yes
```

### apt_policy

https://people.debian.org/~hmh/invokerc.d-policyrc.d-specification.txt

**_Type:_** int<br />

#### Default value

```YAML
apt_policy: 101
```

### apt_preferences

List of preferences options

**_Type:_** list<br />

#### Default value

```YAML
apt_preferences: []
```

### apt_remount_filesystems

remount file system: supported options are rootfs and tmpfs

**_Type:_** list<br />

#### Default value

```YAML
apt_remount_filesystems: []
```

### apt_remove_purge

purge configuration when removing packages

**_Type:_** bool<br />

#### Default value

```YAML
apt_remove_purge: no
```

### apt_remove_recommends

allow 'apt-get autoremove' to remove recommended packages

**_Type:_** bool<br />

#### Default value

```YAML
apt_remove_recommends: no
```

### apt_remove_suggests

allow 'apt-get autoremove' to remove suggested packages

**_Type:_** bool<br />

#### Default value

```YAML
apt_remove_suggests: no
```

### apt_repositories

repositories to register

**_Type:_** list<br />

#### Default value

```YAML
apt_repositories: []
```

### apt_unattended_upgrades

enable unattended-upgrades

**_Type:_** bool<br />

#### Default value

```YAML
apt_unattended_upgrades: yes
```

### apt_unattended_upgrades_allowed

List of allowed-origins

**_Type:_** list<br />

#### Default value

```YAML
apt_unattended_upgrades_allowed:
  - ${distro_id}:${distro_codename}-security
```

### apt_unattended_upgrades_automatic_reboot

Automatically reboot if the file /var/run/reboot-required is found after the upgrade

**_Type:_** bool<br />

#### Default value

```YAML
apt_unattended_upgrades_automatic_reboot: no
```

### apt_unattended_upgrades_automatic_reboot_time

If automatic reboot is enabled and needed, reboot at the specific time instead of immediately

**_Type:_** str<br />

#### Default value

```YAML
apt_unattended_upgrades_automatic_reboot_time: now
```

### apt_unattended_upgrades_automatic_reboot_with_users

Automatically reboot even if there are users currently logged in

**_Type:_** bool<br />

#### Default value

```YAML
apt_unattended_upgrades_automatic_reboot_with_users: no
```

### apt_unattended_upgrades_autoremove

Do automatic removal of new unused dependencies after the upgrade

**_Type:_** bool<br />

#### Default value

```YAML
apt_unattended_upgrades_autoremove: yes
```

### apt_unattended_upgrades_blacklist

Upgrades blacklist ackages

**_Type:_** list<br />

#### Default value

```YAML
apt_unattended_upgrades_blacklist: []
```

### apt_unattended_upgrades_download_timer_override

Override download timer

**_Type:_** dict<br />

#### Default value

```YAML
apt_unattended_upgrades_download_timer_override:
```

### apt_unattended_upgrades_minimal_steps

Split the upgrade into the smallest possible chunks so that
they can be interrupted with SIGUSR1. This makes the upgrade
a bit slower but it has the benefit that shutdown while a upgrade
is running is possible (with a small delay)


**_Type:_** bool<br />

#### Default value

```YAML
apt_unattended_upgrades_minimal_steps: no
```

### apt_unattended_upgrades_notify_error_only

Set this value to "true" to get emails only on errors. Default
is to always send a mail if Unattended-Upgrade::Mail is set


**_Type:_** bool<br />

#### Default value

```YAML
apt_unattended_upgrades_notify_error_only: yes
```

### apt_unattended_upgrades_origins

list of origins patterns to control which packages are upgraded
replaces allowed-origins, kept for compatibility


**_Type:_** list<br />

#### Default value

```YAML
apt_unattended_upgrades_origins: []
```

### apt_unattended_upgrades_syslog_enable

Enable logging to syslog

**_Type:_** bool<br />

#### Default value

```YAML
apt_unattended_upgrades_syslog_enable: no
```

### apt_unattended_upgrades_syslog_facility

Specify syslog facility

**_Type:_** str<br />

#### Default value

```YAML
apt_unattended_upgrades_syslog_facility: daemon
```

### apt_unattended_upgrades_upgrade_timer_override

Override upgrade timer

**_Type:_** dict<br />

#### Default value

```YAML
apt_unattended_upgrades_upgrade_timer_override:
```

### apt_update_package_lists

Do "apt-get update" automatically every n-days (0=disable)

**_Type:_** int<br />

#### Default value

```YAML
apt_update_package_lists: 1
```

### apt_upgrade

upgrade system

**_Type:_** str<br />

#### Default value

```YAML
apt_upgrade: no
```

## Discovered Tags

**_apt_**

**_apt-config_**

**_apt-install_**

**_apt-manage_**

**_config_**

**_install_**

**_manage_**

**_system_**

## Dependencies

None.

## License

MIT

## Author

franklin
