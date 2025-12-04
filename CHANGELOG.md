## Unreleased

### Fix

- add missing become true on privileged tasks (5b5db40)

## 2.15.1 (2025-02-12)

## 2.15.0 (2025-01-13)

### Feat

- **repo**: add deb822 repositories (dfbeaff)

## 2.14.0 (2024-06-11)

### Fix

- Avoid 'No newline at end of file' in /etc/apt/sources.list (0669185)
- Clean sources before adding new ones (e32d357)

## 2.13.0 (2023-09-07)

### Feat

- Allow to remove repository in /etc/apt/sources.list (which has certainly deistribution repositories) (5bb2ea0)

## 2.12.0 (2021-07-12)

### Feat

- add apt-mark hold and unhold capability (96483af)
- drop python 2 support, add `apt_remove_purge`, `apt_policy`, `apt_remove_suggests` Merge branch 'wolkenlos-io-master' into master (a5f4a7c)
- add  var (9796e47)
- allow package parameters (1b93444)
- remove depricated apt_remount_filesystem (7ca12fb)
- extend unattended update config Merge branch 'pbessonies-feature/update_unattended_template' (7b2c0e4)
- add bool check (1f9f71d)
- add apt timers override Merge branch 'pbessonies-feature/apt-timers' (23298c3)
- update syntax to ansible 2.8 (fa5f874)
- add apt pinning (349d5b0)
- added apt pinning (d66994d)
- add options to apt_keys and apt_repositories (f2ce4e0)
- added options (bb80fe8)
- add ability to install .deb packages (9f5c70c)
- upgrade tasks for ansible 2.4 (6e5a1ca)
- add option to alter solution cost (cfaf694)
- allow multiple file systems to be remounted (5cb5a96)
- use builtin autoremove option (87a3493)
- always get latest unattended-upgrades instead of just present (a927d6a)
- escape bare variables (96525b3)
- update to ansible 2.0 (052bc67)
- add support for proxy servers (91ae92f)
- adds variables to configure apt (3ec652b)
- only adds 50unattended-upgrades config if enabled (14742e5)
- updates travis tests (2d1873d)
- using ansible-role to generate README (3abe724)
- adds CHANGELOG (5f4c667)

### Fix

- fix lint error (65f889b)
- fix logic with apt_remove_recommends variable (eaea78e)
- ensure unattended-upgrades package installation (03740ee)
- fix deprication warning for ansible 2.7 and apt package loops (556b644)
- rename missing include to include_tasks (da051d2)
- fix proxy config conditions (27787e8)
- fixes quotation marks on 'APT::Periodic::Enable' value (bf19c90)
- fixes the usage of unattended upgrades (04f2573)

### Refactor

- add apt_remount_filesystems for backward compatibility (b18e652)
- change back to empty (c30773f)
- set empty array as default (46c3d62)
- remove 'or apt_http_pipeline_depth' check on proxy config task (2b15043)
