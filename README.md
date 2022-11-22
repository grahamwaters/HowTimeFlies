# HowTimeFlies



Using requests and google images to show how a query visually changes given a time parameter when searching google images.

**Version 1.0.0**

**Created by Graham Waters**
<div align='center'>
<!-- add badges for the issues, release, latest updates, and stars/forks -->

[![GitHub issues](https://img.shields.io/github/issues/grahamwaters/HowTimeFlies)](https://img.shields.io/github/issues/grahamwaters/HowTimeFlies)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/grahamwaters/HowTimeFlies)](https://img.shields.io/github/v/release/grahamwaters/HowTimeFlies)
[![GitHub last commit](https://img.shields.io/github/last-commit/grahamwaters/HowTimeFlies)](https://img.shields.io/github/last-commit/grahamwaters/HowTimeFlies)
[![GitHub stars](https://img.shields.io/github/stars/grahamwaters/HowTimeFlies)](https://img.shields.io/github/stars/grahamwaters/HowTimeFlies)
[![GitHub forks](https://img.shields.io/github/forks/grahamwaters/HowTimeFlies)](https://img.shields.io/github/forks/grahamwaters/HowTimeFlies)
<!-- add view count to the repo -->
![ViewCount](https://views.whatilearened.today/views/github/grahamwaters/HowTimeFlies.svg)

</div>

## How to use
1. Clone the repo
2. Install the requirements
3. Run `python3 howitschanged.py`


## Process

The program prompts the user to give several inputs:

`What are you looking for?` you type: `London, England`

`from what year at the earliest?` you type: `1920`

`to what year at the latest?` you type: `1980`

`How many images do you want? (80 is limit per page)` you type: `20`

`what MUST be included in the search?` you type: `England`

`what would you like to leave out of the search?` you type: `(blank)`

```
retrieving 60 years worth of photos related to London, England`
dataline:London, England "in the year  (years go here) "" England "-
this is 1200 images in 60 folders.
```
Then you should see something like this:
```bash
 "London, England" in "the year 1974" "England" imagesize:500x500
searching...
Downloading 20 images...
Running total of collected images:40
 52%|████████▋       | 31/60 [01:09<00:04,  1.05it/s]
```






## How it works
1. The user inputs a query
2. The program uses the `requests` library to get the html of the google images page, and uses `BeautifulSoup` to parse the html.
