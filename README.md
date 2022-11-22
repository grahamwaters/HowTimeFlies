# HowItsChanged
Using requests and google images to show how a query visually changes given a time parameter when searching google images.



## How to use
1. Clone the repo
2. Install the requirements
3. Run `python3 howitschanged.py`

## How it works
1. The user inputs a query
2. The program uses the `requests` library to get the html of the google images page, and uses `BeautifulSoup` to parse the html.
