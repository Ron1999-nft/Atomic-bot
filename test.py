from unittest import mock
from unittest.mock import Mock, patch,MagicMock
import unittest
from Api import Api

class ApiTest(unittest.TestCase):
    @mock.patch("Api.Api")
    def test_failed_data(self,mock_class):
        mock_class.return_value.get_data.return_value = {"success": False,"message": "string"}
        test = mock_class(100,"haha")
        print(test.get_data())

    def test_failed_data_2(self):
        api = Api(100,"haha")

def main():
    # Create the test suite from the cases above.
    suite = unittest.TestLoader().loadTestsFromTestCase(ApiTest)
    # This will run the test suite.
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()