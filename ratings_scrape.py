import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_latest_liverpool_ratings():
    """
    Scrapes the WhoScored Liverpool page for the most recent match,
    then gathers player ratings from that match.
    
    Returns:
        A list of dicts, each with {'name': player_name, 'rating': rating}.
    """
    
    # 1. Set up Selenium (Chrome in this example)
    #    Make sure you have ChromeDriver installed and either on your PATH
    #    or provide the explicit path: Service("path/to/chromedriver")
    service = Service()  # Uses the default chromedriver on your system PATH
    driver = webdriver.Chrome(service=service)
    
    try:
        # 2. Go to Liverpool’s WhoScored page
        liverpool_url = "https://www.whoscored.com/Teams/26"
        driver.get(liverpool_url)

        # 3. Wait briefly (or use WebDriverWait) to let the JS render the matches
        time.sleep(5)  # Adjust as needed, or use an explicit wait.

        # 4. Find the link to the latest match
        #    By inspecting the site’s HTML, you’ll see a list of fixtures/results.
        #    Let's assume the most recent match link has a particular CSS selector or XPATH.
        #    Below is a placeholder selector—adjust to match actual site structure.
        #    
        #    Example (pseudo-structure):
        #       <a class="match-link" href="/Matches/xxxx/MatchReport/TeamName-TeamName" ... >
        #
        match_link = driver.find_element(By.CSS_SELECTOR, "a.match-link")
        match_url = match_link.get_attribute("href")
        
        # 5. Navigate to the match page
        driver.get(match_url)
        
        # 6. Wait for the match center data to load
        time.sleep(5)  # Or use WebDriverWait to wait for a specific element

        # 7. Identify elements that contain player ratings
        #    Typically, you’ll see tables or divs for each player. 
        #    In WhoScored’s DOM, you might look for something like:
        #    <td class="player">... player name ...</td>
        #    <td class="rating">... rating ...</td>
        #
        #    This can vary. The best approach is to open DevTools (F12),
        #    inspect the HTML, and find unique class names or data attributes.
        #
        #    Below is a hypothetical example:
        player_rows = driver.find_elements(By.CSS_SELECTOR, "tr.player-tr")

        # 8. Loop through each row and gather the name/rating
        results = []
        for row in player_rows:
            try:
                # Find name and rating by looking for specific td elements
                name_el = row.find_element(By.CSS_SELECTOR, "td.player-name")
                rating_el = row.find_element(By.CSS_SELECTOR, "td.player-rating")
                
                name = name_el.text.strip()
                rating = rating_el.text.strip()

                results.append({"name": name, "rating": rating})
            except Exception:
                # If an element is missing or doesn't match the pattern, skip it
                continue

        return results

    finally:
        # Always close the browser
        driver.quit()


if __name__ == "__main__":
    try:
        player_ratings = scrape_latest_liverpool_ratings()
        print("Latest Liverpool Player Ratings:")
        for player in player_ratings:
            print(f"  {player['name']}: {player['rating']}")
    except Exception as e:
        print("Error scraping data:", e)

