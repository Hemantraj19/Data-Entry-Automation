# Web Scraping and Form Submission Script

This Python script is designed to scrape data from a Zillow clone webpage and submit the extracted information to a form. The script utilizes BeautifulSoup for web scraping and Selenium for interacting with the form.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python
- BeautifulSoup (`pip install beautifulsoup4`)
- Requests (`pip install requests`)
- Selenium (`pip install selenium`)

Additionally, make sure you have the Chrome WebDriver installed and its path configured in your system.

## Usage

1. Clone the repository or download the script file.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Configure the Chrome WebDriver path in the script if necessary.
4. Replace `"your forms link"` with the actual link to the form you want to submit data to.

## Script Explanation

- The script starts by sending a GET request to the Zillow clone webpage and extracts the HTML content.
- BeautifulSoup is used to parse the HTML and extract links, prices, and addresses from specific elements on the page.
- Selenium is then employed to automate the form submission process.
- The script iterates through the extracted data and submits it to the specified form.

## Script Customization

- If the form structure changes, you may need to update the script accordingly.
- Ensure that the Chrome WebDriver version matches your Chrome browser version.

## Running the Script

Execute the script by running the following command:

```bash
python script_name.py
```

## Note

Make sure to replace placeholders like `script_name.py` and `"your forms link"` with the actual script filename and form link.
