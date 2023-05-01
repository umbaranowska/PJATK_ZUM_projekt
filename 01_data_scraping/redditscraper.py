from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
# from icecream import ic
import os

class RedditScraper(subreddit = "https://www.reddit.com/r/taskmaster/?f=flair_name%3A%22Episode%22"):

    def __init__(self, subreddit):
        self.subreddit = subreddit

    def get_thread_urls(self, save_to_txt = True):
        all_urls = []
        # opens browser
        driver = webdriver.Chrome()
        # opens subreddit
        driver.get(self.subreddit)
        time.sleep(20)
        # accepts cookies
        driver.find_element(by=By.XPATH,
                            value='/html/body/div[1]/div/div[2]/div[3]/div[1]/section/div/section[2]/section[1]/form/button').click()
        time.sleep(20)
        # scrolls down page
        for x in range(20):
            driver.execute_script('window.scrollBy(0,500)')
            time.sleep(random.randint(5, 10))
        # tries 120 xpaths (at time of scraping there were 117 episode subs)
        for x in range(120):
            try:
                xpath = f"/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[4]/div[1]/div[5]/div[{x}]/div/div/div[3]/div[2]/div[1]/a"
                url = driver.find_element(by=By.XPATH, value = xpath).get_attribute('href')
                all_urls.append(url)
                time.sleep(random.randint(5, 10))
            except:
                ic(x)
        driver.quit()
        ic(len(all_urls))
        # saves to txt
        if save_to_txt == True:
            with open('thread_urls.txt', 'w') as file:
                for url in all_urls:
                    file.write(url + '\n')

    def get_single_thread(self, replies = True, save_partial = True):
        pass

    def get_all_threads(self, **kwargs):
        pass

    def merge_threads_to_csv(self, delete_extra_files = False):
        pass





