import os
import os.path
import pytest
import pprint

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture(scope='module')
def ansible_variables(host):
    return host.ansible.get_variables()


# Assert requuested packages are present
def test_package_installed(host):
    assert host.package("vim").is_installed
    assert host.package("tree").is_installed


# Assert removed packages are absent
def test_package_removed(host):
    assert host.package("zsh").is_installed is False


# Assert apt key is present
def test_apt_key_present(host, ansible_variables):
    apt_key = ansible_variables.get('apt_keys', None)
    assert apt_key is not None
    assert len(apt_key) > 0
    apt_key = apt_key[0]
    assert host.file(apt_key['keyring']).exists


# Assert apt pin for package is present
def test_apt_pin_present(host, ansible_variables):
    apt_pin = ansible_variables.get('apt_preferences', None)
    assert apt_pin is not None
    assert len(apt_pin) > 0
    apt_pin = apt_pin[0]
    pin_file = f"/etc/apt/preferences.d/{apt_pin['file']}"
    f = host.file(pin_file)
    assert f.exists
    assert f.contains(f"Package: {apt_pin['package']}")
    assert f.contains(f"Pin: {apt_pin['pin']}")
    assert f.contains(f"Pin-Priority: {apt_pin['priority']}")
