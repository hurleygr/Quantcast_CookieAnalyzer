# Quantcast_CookieAnalyzer

CookieAnalyzer parses cookie logs for a specific date and returns the most frequent cookies.

It can be ran from terminal with the following command:
python3 most_active_cookie.py something.csv -d YYYY-MM-DD
where something.csv is a csv file containing cookie logs
and YYY-MM-DD is a valid date formatted as such.

The unit tests can be ran from terminal with the following command:
python3 testing.py
