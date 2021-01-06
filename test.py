from unittest import mock
from unittest.mock import Mock, patch,MagicMock
import unittest
from Api import Api

class ApiTest(unittest.TestCase):
    @patch.object("Api.MyClass")
    def test_failed_data(self,mock_class):
        mc = mock_class.return_value

def main():
    # Create the test suite from the cases above.
    suite = unittest.TestLoader().loadTestsFromTestCase(ApiTest)
    # This will run the test suite.
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()