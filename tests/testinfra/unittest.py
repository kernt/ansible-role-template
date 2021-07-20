import unittest
import testinfra


class Test(unittest.TestCase):

    def setUp(self):
        self.host = testinfra.get_host("paramiko://root@host")

    def test_nginx_config(self):
        self.assertEqual(self.host.run("nginx -t").rc, 0)

    def test_nginx_service(self):
        service = self.host.service("nginx")
        self.assertTrue(service.is_running)
        self.assertTrue(service.is_enabled)


if __name__ == "__main__":
    unittest.main()