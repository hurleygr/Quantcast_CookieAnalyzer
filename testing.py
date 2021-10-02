import sys
import io
import unittest
import most_active_cookie


class UnitTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.analyzer_no_matching_date = most_active_cookie.CookieAnalyzer("quantcast.csv", "2018-12-06")
        cls.analyzer_matching_date = most_active_cookie.CookieAnalyzer("quantcast.csv", "2018-12-07")
        cls.test_data = [  'AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00\n',
                            'SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00\n',
                            '5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00\n',
                            'AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00\n',
                            'SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00\n',
                            '4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00\n',
                            'fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00\n',
                            '4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00']

    def test_get_date(self):
        test_date = "2018-12-07T23:30:00+00:00"
        self.analyzer = most_active_cookie.CookieAnalyzer("quantcast.csv", "2018-12-06")
        self.assertEqual(self.analyzer.get_date(test_date), "2018-12-07")

    def test_invalid_number_of_arguments(self):
        with self.assertRaises(most_active_cookie.InvalidArgumentsException):
            most_active_cookie.main()

    def test_with_no_matching_date(self):
        test_output = io.StringIO()
        sys.stdout = test_output
        self.analyzer_no_matching_date.read_file()
        self.assertEqual(self.test_data, self.analyzer_no_matching_date.file_data)
        self.analyzer_no_matching_date.parse_data()
        self.assertEqual({}, self.analyzer_no_matching_date.cookie_count)
        self.assertEqual(0, self.analyzer_no_matching_date.max_frequency)
        self.analyzer_no_matching_date.analyze_data()
        self.assertEqual(test_output.getvalue(), "")
        sys.stdout = sys.__stdout__

    def test_with_matching_date(self):
        test_output = io.StringIO()
        sys.stdout = test_output
        self.analyzer_matching_date.read_file()
        self.assertEqual(self.test_data, self.analyzer_matching_date.file_data)
        self.analyzer_matching_date.parse_data()
        self.assertEqual({"4sMM2LxV07bPJzwf" : 1}, self.analyzer_matching_date.cookie_count)
        self.assertEqual(1, self.analyzer_matching_date.max_frequency)
        self.analyzer_matching_date.analyze_data()
        self.assertEqual(test_output.getvalue(), "4sMM2LxV07bPJzwf\n")
        sys.stdout = sys.__stdout__


if __name__ == "__main__":
    unittest.main()