import testinfra

def test_os_release(host):
    assert host.file("/etc/os-release").contains("Fedora")

def test_sshd_inactive(host):
    assert host.service("sshd").is_running is False

def check_httpd_service(host):
    """Check that the httpd service is running on the host"""
    assert host.service("httpd").is_running

def check_ansible_play(host):
    """
    Verify that a package is installed using Ansible
    package module
    """
    assert not host.ansible("package", "name=httpd state=present")["changed"]