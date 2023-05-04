from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from icecream import ic
import os
import pandas as pd

class RedditScraper:

    def __init__(self, subreddit = "https://www.reddit.com/r/taskmaster/?f=flair_name%3A%22Episode%22",
                 run_all = False):
        self.subreddit = subreddit
        if run_all == True:
            print("Running all with default arguments")
            self.run_all()
        else:
            print("Scraper created, not running")

    def run_all(self):
        self.get_thread_urls()
        self.get_all_threads()
        self.merge_threads_to_csv()

    def get_thread_urls(self, save_to_txt = True):
        print(F"GETTING THREAD URLS FROM {self.subreddit}")
        all_urls = []
        # opens browser
        print("Opening browser")
        driver = webdriver.Chrome()
        # opens subreddit
        driver.get(self.subreddit)
        time.sleep(20)
        # accepts cookies
        print("Accepting cookies")
        driver.find_element(by=By.XPATH,
                            value='/html/body/div[1]/div/div[2]/div[3]/div[1]/section/div/section[2]/section[1]/form/button').click()
        time.sleep(20)
        # scrolls down page
        for x in range(20):
            print(f"Scrolling {x+1}/20")
            driver.execute_script('window.scrollBy(0,1000)')
            time.sleep(random.randint(5, 10))
        # tries 120 xpaths (at time of scraping there were about 120 episodes)
        num_threads = 120
        for x in range(num_threads):
            print(f"Trying {x+1}/{num_threads}")
            try:
                xpath = f"/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[4]/div[1]/div[4]/div[{x}]/div/div/div[3]/div[2]/div[1]/a"
                url = driver.find_element(by=By.XPATH, value = xpath).get_attribute('href')
                print(url)
                all_urls.append(url)
                time.sleep(random.randint(5, 10))
            except:
                print("FAILED")
        driver.quit()
        ic(len(all_urls))
        # saves to txt
        if save_to_txt == True:
            print("Saving to .txt")
            with open('thread_urls.txt', 'w') as file:
                for url in all_urls:
                    file.write(url + '\n')
        print("Finished")

    def get_single_thread(self, url):
        print(f"GETTING SINGLE THREAD FROM {url}")
        # gets thread id from url
        thread_id = url.split('/')[6]
        print(f"Thread id: {thread_id}")
        # opens browser
        print("Opening browser")
        driver = webdriver.Chrome()
        # opens url
        driver.get(url)
        time.sleep(20)
        # gets total number of comments in this thread
        number_of_comments = driver.find_element(by=By.XPATH,
                                                 value = "/html/body/shreddit-app/div/div[2]/shreddit-async-loader/comment-body-header/div/span[2]/faceplate-number").text
        if number_of_comments.find("K") == -1:
            number_of_comments = int(number_of_comments)
        else:
            number_of_comments = int(float(number_of_comments.replace("K", "")) * 1000)
        print(f"Total number of comments in this thread: {number_of_comments}")
        # scrolls down page and clicks "view more comments"
        for x in range(20):
            print(f"Scrolling {x+1}/20")
            driver.execute_script('window.scrollBy(0,5000)')
            print("Loading")
            time.sleep(random.randint(20, 30))
            try:
                driver.find_element(by=By.XPATH,
                                    value='//*[@id="comment-tree"]/faceplate-partial/div[1]/button').click()
                time.sleep(random.randint(10, 20))
                driver.execute_script('window.scrollBy(0,100000)')
                print("OK")
            except:
                print("did not find load more comments button")
                break
        # creates directory for the data if necessary
        if not os.path.exists("single_thread_data"):
            os.mkdir("single_thread_data")
        # gets all comments without replies
        comments_dict = {}
        for i in range(1, number_of_comments+1):
            comment_id = f"{thread_id}_{str(i).zfill(5)}"
            print(f"Getting comment {comment_id} out of total: {number_of_comments}")
            try:
                comment_text = driver.find_element(by=By.XPATH,
                                                   value = f"/html/body/shreddit-app/div/div[2]/faceplate-batch/faceplate-tracker/shreddit-comment-tree/shreddit-comment[{i}]/div[2]/div").text
                comment_text = comment_text.replace("\n", " ")
                comments_dict.update({comment_id : comment_text})
                time.sleep(random.randint(10,20))
            except:
                print("finished getting commments")
                break
        # changes comments into pandas dataframe and saves to .csv
        comments_dict_to_dataframe = {"comment_id": list(comments_dict.keys()),
                                      "comment_text": list(comments_dict.values())}
        comments_dataframe = pd.DataFrame.from_dict(comments_dict_to_dataframe)
        print("Saving to .csv")
        comments_dataframe.to_csv(f"single_thread_data/{thread_id}.csv")
        driver.quit()
        print("Finished")

    def get_all_threads(self, url_list = "thread_urls.txt"):
        with open(url_list, "r") as file:
            for line in file:
                self.get_single_thread(url = line)

    def merge_threads_to_csv(self, delete_extra_files = False):
        data_list = [pd.read_csv(f"single_thread_data/{file}") for file in os.listdir("single_thread_data")]
        data_frame = pd.concat(data_list)[["comment_id", "comment_text"]]
        data_frame.to_csv("all_scraped_data.csv")
        print(data_frame.shape)
        if delete_extra_files == True:
            os.remove("single_thread_data")