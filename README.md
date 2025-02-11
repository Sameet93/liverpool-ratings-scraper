# Liverpool FC Player Ratings Scraper

A simple Python script that uses [Selenium](https://www.selenium.dev/) to scrape the latest Liverpool FC player ratings from a specified source (e.g., WhoScored). **Important:** Always read and comply with the target website’s Terms of Service and robots.txt before scraping.

---

## Table of Contents

1. [Features](#features)  
2. [Requirements](#requirements)  
3. [Installation](#installation)  
4. [Usage](#usage)  
5. [Customization](#customization)  
6. [Disclaimer](#disclaimer)

---

## Features

- **Selenium-based scraping**: Renders dynamic web pages that use JavaScript.  
- **Example code** to:
  1. Navigate to a Liverpool-specific page (placeholder URL).  
  2. Find the latest match link.  
  3. Extract player names and ratings.  
- **Easily extensible** for additional matches or other teams.

---

## Requirements

- Python 3.7+ (recommended)
- A compatible browser driver (e.g., [ChromeDriver](https://chromedriver.chromium.org/) for Google Chrome).
- See [`requirements.txt`](./requirements.txt) for necessary Python packages:
  ```txt
  selenium==4.8.2
  beautifulsoup4==4.11.2
  ```

---

## Installation

Follow these steps to set up and run the Liverpool FC Player Ratings Scraper:

1. **Get the Repository**  
   - Clone or download the project:
     ```bash
     git clone https://github.com/your-username/liverpool-ratings-scraper.git
     cd liverpool-ratings-scraper
     ```

2. **Install Dependencies**  
   - Use `pip` to install the required packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **Configure Your WebDriver**  
   - Download [ChromeDriver](https://chromedriver.chromium.org/downloads) (or another appropriate driver) that matches your browser version.
   - Make sure the driver executable is either on your system’s PATH or specify its exact location in the script.

---

## Usage

1. **Review the Script**  
   - Open the file (e.g., `liverpool_scraper.py`) and confirm or update:
     - The URL directing to the latest Liverpool FC matches (e.g., a WhoScored page).
     - The CSS selectors or XPaths used to locate match links and player data.

2. **Run the Script**  
   - From your terminal, navigate to the project directory, then run:
     ```bash
     python liverpool_scraper.py
     ```
   - After execution, the console should display the latest player ratings for Liverpool FC.

3. **Adapt as Needed**  
   - You can print results to the console, write them to a file, or insert them into a database. Make adjustments in the `for player in player_ratings:` loop within the script.

---

## Customization

- **Selectors**: Update your CSS or XPath selectors if the website’s HTML changes or if you switch to a different site.  
- **Multiple Matches**: Gather links for various recent matches and iterate through each.  
- **Output Format**: Save data to CSV, JSON, or a relational database—change the code snippet that processes `player_ratings` accordingly.

---

## Disclaimer

- **Educational Use**: This project demonstrates how to scrape dynamic web pages with Selenium.  
- **Website Policies**: Always consult the Terms of Service and robots.txt of the target site before scraping.  
- **Subject to Change**: Web layouts evolve frequently, so you may need to adjust your selectors or approach over time.

