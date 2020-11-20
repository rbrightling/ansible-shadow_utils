import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_shadow_utils_installed(host):
    shadow_utils_package_name = _get_distro_package_name(host.system_info.distribution)
    for package_name in shadow_utils_package_name:
        shadow_utils_package = host.package(package_name)
        assert shadow_utils_package.is_installed


def test_login_defs_file(host):
    login_defs_config = host.file("/etc/login.defs")
    assert login_defs_config.exists
    assert login_defs_config.user == "root"
    assert login_defs_config.group == "root"
    assert login_defs_config.mode == 0o644


def test_useradd_default_file(host):
    useradd_default_config = host.file("/etc/default/useradd")
    assert useradd_default_config.exists
    assert useradd_default_config.user == "root"
    assert useradd_default_config.group == "root"
    assert useradd_default_config.mode == 0o644


def _get_distro_package_name(host_distro):
    return {
        "centos": ["shadow-utils"],
        "debian": ["login", "passwd"]
    }.get(host_distro, ["shadow-utils"])
