import unittest
from glob_utils.helpers import get_global_text


class TestEnv(unittest.TestCase):
    def test_env_var(self):
        self.assertIsNotNone(get_global_text())


if __name__ == "__main__":
    unittest.main()
    
