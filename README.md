# Image Scraper

A developer tool used to aid in the procurement of large amounts of images for machine learning algorithms or other use cases

## Description

In the past I have looked to train machine learning models to tell the difference between to different objects.
This requires the procurement of a large number of images.
Doing so is very difficult and time consuming manually, so I decided to create this tool which speeds up the process.
The images retrieved by this web scraper aren't always perfect, and so require third party intervention before they are fed into any machine learning algorithms.
The tool uses three different types of user inputs to build a broad but direct set of google image search terms. 
These inputs are known as nouns, adjectives, and describers.
Nouns are what you are looking for, adjectives are basic descriptors of what you are looking for, describers are more unique adjectives.
If a user wanted to retrieve images of trees possible nouns could include:
* jungle
* forest
* woodlands

Possible adjectives could include:
* big
* small
* dense

Possible describers could include:
* african
* mountainous
* coastal

These inputs would create searches such as "small coastal forest" or "dense mountainous woodlands". 
Inputs are entered, when prompted, individually.
For example, when entering nouns the user would type jungle then hit enter, then type forest then hit enter, then type woodlands then hit enter. 
The same is done for adjectives and describers. 
This tool is not designed to be user friendly, high proficiency of python is required, and reading both the readme and the code is highly recommended before using. 

## Getting Started

### Dependencies

* Built using Python 3.8.5, should work on Python 3 and above
* Built on Linux, should also run on windows and macOS

### Libraries/Modules

* urllib3 1.25.8
* requests 2.22.0
* bs4 0.0.1

### Installing

* Download the repository 
* Unzip the repository into the desired location

### Executing Program

* cd into the folders location
* cd into Image-Scraper
* Run the Command:
```
python imgScrape.py
```

## Authors

Jack Sanderson
[@JackASanderson](https://twitter.com/JackASanderson)


## Acknowledgments

Inspiration, code snippets, etc.
* [freecodecamp.org](https://www.freecodecamp.org/news/web-scraping-python-tutorial-how-to-scrape-data-from-a-website/)
* [dataquest.io](https://www.dataquest.io/blog/web-scraping-python-using-beautiful-soup/)
* [urllib](https://docs.python.org/3/library/urllib.html)
* [requests](https://docs.python-requests.org/en/master/)
* [beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)