from redditscraper import *

RedditScraper = RedditScraper()
# RedditScraper.run_all()
# RedditScraper.get_all_threads()
RedditScraper.get_single_thread(url = "https://www.reddit.com/r/taskmaster/comments/137osj0/taskmaster_s15e06_its_my_milk_now_discussion/")
RedditScraper.get_single_thread(url = "https://www.reddit.com/r/taskmaster/comments/13epy1e/taskmaster_s15e07_schrodingers_egg_discussion/")
RedditScraper.merge_threads_to_csv()
