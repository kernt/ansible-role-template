# BAD: If the test fails on nginx, python is not tested
def test_packages(host):
    for name, version in (
        ("nginx", "1.6"),
        ("python", "2.7"),
    ):
        pkg = host.package(name)
        assert pkg.is_installed
        assert pkg.version.startswith(version)


# GOOD: Each package is tested
# $ py.test -v test.py
# [...]
# test.py::test_package[local-nginx-1.6] PASSED
# test.py::test_package[local-python-2.7] PASSED
# [...]
import pytest

@pytest.mark.parametrize("name,version", [
    ("nginx", "1.6"),
    ("python", "2.7"),
])
def test_packages(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed
    assert pkg.version.startswith(version)