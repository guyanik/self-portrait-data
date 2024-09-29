# WikiArt Self-Portrait Image Scraper

This repository contains a set of Python scripts for scraping and processing self-portrait images from WikiArt.

## Scripts

### 1. url_scraper.py

This script is responsible for scraping image URLs and titles from WikiArt.

Key features:
- Reads links from `clean-links.txt`
- Scrapes image URLs and titles using BeautifulSoup
- Writes the results to `urls-and-titles.txt`

### 2. image_scraper.py

This script downloads images using the URLs scraped by `url_scraper.py`.

Key features:
- Reads URLs and titles from `urls-and-titles.txt`
- Downloads images and saves them in the `images/` directory
- Uses the `titlecase` library to format image titles

### 3. rename.py

This script renames and organizes the downloaded images.

Key features:
- Reads from `urls-and-titles.txt`
- Renames files based on their content and URL structure
- Handles file name conflicts by adding numbering
- Separates JPEG and PNG files into lists

## Usage

1. Run `url_scraper.py` to gather image URLs and titles.
2. Run `image_scraper.py` to download the images.
3. Run `rename.py` to organize and rename the downloaded images.

## Dependencies

- `requests`
- `beautifulsoup4`
- `titlecase`

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Notes

- The `links.txt` file should contain the initial list of WikiArt pages to scrape.
- Downloaded images are stored in the `images/` directory.
- The `jpeg-and-png/` directory is present to separate JPEG and PNG files.

## Disclaimer

Please ensure you have the right to scrape and use images from WikiArt. Always respect copyright laws and the website's terms of service.