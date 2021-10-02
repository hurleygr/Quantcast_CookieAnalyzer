"""
This module takes in a log file containing cookies and timestamps, and a date.
It outputs the most frequently encountered cookies on the specified date.

Usage:
This file can be run from the command line as follows (assuming you are in the same directory as most_active_cookie.py):

python most_active_cookie.py cookie_log_file.csv -d YYYY-MM-DD where:

cookie_log_file.csv is a path to the cookie log file and YYYY-MM-DD is a date formatted as such.
"""

import sys


class InvalidArgumentsException(Exception):
    """Exception that is raised when command line arguments are too few"""
    def __init__(self, message="Arguments must include a .csv file, and a -d followed by a date in YYYY-MM-DD format"):
        self.message = message

    def __str__(self):
        return self.message


class CookieAnalyzer:
    """
    Initializes CookieAnalyzer class with command line arguments

    Parameters:
        cookie_log_file (String): File path to csv file containing cookie logs

        target_date (String): Date (in YYYY-MM-DD format) for which most frequent cookies should be determined
    """
    def __init__(self, cookie_log_file, target_date):
        self.cookie_log_file = cookie_log_file
        self.target_date = target_date
        self.cookie_count = {}
        self.max_frequency = 0
        self.results = []
        self.file_data = []

    @staticmethod
    def get_date(date_time):
        """"
        Parses date-time and returns YYYY-MM-DD portion

        Parameters:
            date_time (String): Date-Time in YYYY-MM-DDThh:mm:ssTZD format

        Returns:
            date (String): Date in YYYY-MM-DD format
        """
        date, time = date_time.split("T")
        return date

    def read_file(self):
        """Reads log file into list variable and strips quotes"""
        with open(self.cookie_log_file) as cookie_file:
            line_count = 0
            for line in cookie_file:
                line = line.replace('"', '')
                if line_count == 0:
                    line_count += 1
                    continue
                line_count += 1
                self.file_data.append(line)

    def parse_data(self):
        """Parses log file to determine most frequent cookies during specified date"""
        for line in self.file_data:
            cookie, date_time = line.split(",")
            date = self.get_date(date_time)
            if date == self.target_date:
                self.cookie_count[cookie] = self.cookie_count.get(cookie, 0) + 1
                self.max_frequency = max(self.max_frequency, self.cookie_count[cookie])

    def analyze_data(self):
        """
        Prints each cookie that occurred with maximum frequency on that date
        """
        for cookie, frequency in self.cookie_count.items():
            if frequency == self.max_frequency:
                self.results.append(cookie)
                print(cookie)


def main():
    """Initializes CookieAnalyzer class and runs its methods in response to command line call"""
    if len(sys.argv) < 4:
        raise InvalidArgumentsException

    analyzer = CookieAnalyzer(sys.argv[1], sys.argv[3])
    analyzer.read_file()
    analyzer.parse_data()
    analyzer.analyze_data()


if __name__ == "__main__":
    main()
