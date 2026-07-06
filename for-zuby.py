# import random
# random.seed("JESUS")
# # names = ["Ayomide", "Emmanuel", "Stephen", "Lekan", "Mayowa", "Temi"]
# # names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
# # teams = []
# # for i in range(3):
# #     selection = random.choice(names)
# #     names.remove(selection)
# #     second = random.choice(names)
# #     names.remove(second)
# #     teams.append((selection, second))
# # print(teams)
#
# people = ["Ayomide", "Emmanuel", "Stephen", "Lekan", "Mayowa", "Temi"]
#
# random.shuffle(people)
#
# teams = [people[i:i+2] for i in range(0, len(people), 2)]
#
# for n, team in enumerate(teams, start=1):
#     print(f"Team {n}: {team}")

import browser_cookie3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import shutil

# from datetime import datetime


class CrdownloadChecker:
    def __init__(self, folder_path):
        if not os.path.isdir(folder_path):
            raise ValueError(f"The path '{folder_path}' is not a valid directory.")
        self.folder_path = folder_path

    def count_crdownload_files(self):
        """Count the number of .crdownload files in the folder."""
        return sum(
            1 for file in os.listdir(self.folder_path)
            if file.endswith('.crdownload') and os.path.isfile(os.path.join(self.folder_path, file))
        )

    def get_crdownload_filenames(self):
        """Return a list of .crdownload file names in the folder."""
        return [
            file for file in os.listdir(self.folder_path)
            if file.endswith('.crdownload') and os.path.isfile(os.path.join(self.folder_path, file))
        ]

    def get_file_size(self, filename):
        """Return the size of a specific file in bytes. Raises error if file doesn't exist."""
        file_path = os.path.join(self.folder_path, filename)
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file '{filename}' does not exist in the folder.")
        return os.path.getsize(file_path)

    def find_file(self, filename):
        """Check if a certain file exists."""
        file_path = os.path.join(self.folder_path, filename)
        return True if os.path.isfile(file_path) else False

    def move_crdownload_files_to_stay_there(self):
        """Move all .crdownload files into a 'stay_there' folder, creating it if needed."""
        stay_there_path = os.path.join(self.folder_path, 'stay_there')
        os.makedirs(stay_there_path, exist_ok=True)

        for file in os.listdir(self.folder_path):
            full_file_path = os.path.join(self.folder_path, file)
            if file.endswith('.crdownload') and os.path.isfile(full_file_path):
                shutil.move(full_file_path, os.path.join(stay_there_path, file))


# base_url = "https://animepahe.ru/anime/d58fc9f8-582e-fdf0-3618-112cd54ed5ab"
# base_url = "https://animepahe.ru/anime/98a7ea7c-3ba2-de14-7e4c-d4999b259083" # For haikyu
base_url = "https://animepahe.pw/anime/f237db4d-bb0d-5e95-cd22-b2cc4ef76f9e" # For Shippuden
start_page = 1
# page_last_ep = 291
# start_episode = 212
start_episodes = [i for i in range(107, 201)]
# start_episodes = [i for i in range(2, 3)]# For haikyu
exceptions = [110, 111, 119, 150]
go_back_one = False


download_folder = "/home/manuel7tin/Downloads/SavedAnime"
os.makedirs(download_folder, exist_ok=True)
# download_folder = "C:/Users/PC/Downloads/"

chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_folder,
    "download.prompt_for_download": False,
    "directory_upgrade": True,
    "safebrowsing.enabled": True,  # Enables safe downloads
}
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_options)
checker = CrdownloadChecker(download_folder)

retry_limit = 3  # Max retries per episode
retry_counts = {}
last_size = 0

j = 0
while j < len(start_episodes):
    # print(j, start_episodes)
    if start_episodes[j] in exceptions:
        j += 1
        continue
    start_episode = start_episodes[j]
    if checker.get_crdownload_filenames():
        checker.move_crdownload_files_to_stay_there()
    for k in range(3):
        try:
            driver.get(f"{base_url}?page={start_page}")
            #To bypass ReCaptcha
            cookies = browser_cookie3.chrome(domain_name=base_url[8:].split("/")[0])

            for cookie in cookies:
                selenium_cookie = {
                    "name": cookie.name,
                    "value": cookie.value,
                    "path": cookie.path,
                }

                if cookie.domain:
                    selenium_cookie["domain"] = cookie.domain

                driver.add_cookie(selenium_cookie)

            driver.refresh()
             # driver.get(base_url)  # For haikyu
        except Exception as e:
            time.sleep(4)
        else:
            break
    time.sleep(10)
    print(f"Trying episode {start_episode} in page {start_page}")
    try:
        episodes = driver.find_elements(By.CLASS_NAME, value="episode-wrap")
    # print(episodes)
    # print(driver.find_element(By.TAG_NAME, "a"))
        link_text = [i.find_element(By.TAG_NAME, value="a").text for i in episodes]
        links = [i.find_element(By.TAG_NAME, value="a").get_attribute("href") for i in episodes]
    # try:
    #     max_page_ep = int(link_text[0].split()[2])
        max_page_ep = int(link_text[-1].split()[2]) # For haikyu
    # except Exception as e:
    #     go_back_one = True
        # driver.refresh()
        # continue
        ep_position = (max_page_ep - start_episode)
        print("---", ep_position, max_page_ep, start_page, "---")
        print(link_text)
        # ep_position = -1 * (max_page_ep - start_episode + 1) # For haikyu

        if ep_position <= 0:
        # if ep_position >= 0: # For haikyu
            start_page += 1
            # page_last_ep += 30
            print(f"🚫 It appears the last episode on page {start_page - 1} has been surpassed. Ep_Position is {ep_position}")
            # print(f"📈 Moving to page {start_page}, the last ep has now become {page_last_ep} from {page_last_ep - 30}")
            if ep_position < 0:
            # if ep_position > 0: # For haikyu
                print("Start page is even before where it should be.")
                continue
        elif ep_position >= 30:
            start_page -= 1
            # page_last_ep -= 30
            print(f"🎯 It appears the first episode on page {start_page + 1} hasn't been reached. Ep_Position is {ep_position}")
#             print(f"📈 Moving to page {start_page}, the last ep has now become {page_last_ep} from {page_last_ep + 30}")

        print("EP_POSITION", ep_position)
        print(links)
        driver.get(links[29 - ep_position])
        for i in range(3):
            time.sleep(1)
            download_btn = driver.find_element(By.ID, value="downloadMenu")
            try:
                driver.execute_script("arguments[0].click();", download_btn)
                # download_btn.click()
            except Exception as e:
                print(f"INterc3eption: {e}")
                driver.refresh()
            else:
               break
        try:
            download_link = driver.find_element(By.PARTIAL_LINK_TEXT, value="HorribleSubs · 1080p")
        except Exception as e:
            try:
                download_link = driver.find_element(By.PARTIAL_LINK_TEXT, value="HorribleSubs · 1072p")
            except Exception as e:
                raise ValueError()
        # download_link = driver.find_element(By.PARTIAL_LINK_TEXT, value="sam · 720p") # For haikyu

        driver.get(download_link.get_attribute("href"))
        time.sleep(4)
        "pl-5e665a97aec27d3d9d2ec573a80ea0bf__close"
        for i in range(3):
            try:
                continue_btn = driver.find_element(By.LINK_TEXT, value="Continue")
                # continue_btn.click()
                final_link = continue_btn.get_attribute("href")
                driver.get(final_link)
            except Exception as e:
                print("error in clickin continue bnt", str(e)[:70])
                time.sleep(2)
                print(driver.find_element(By.TAG_NAME, value="h1"))
                # print(f"Error: {e}")
            else:
                time.sleep(3)
                break
        for i in range(3):
            try:
                print("Initializing cookie integration")
                cookies = browser_cookie3.chrome(domain_name="kwik.cx")
                for cookie in cookies:
                    selenium_cookie = {
                        "name": cookie.name,
                        "value": cookie.value,
                        "path": cookie.path,
                    }

                    if cookie.domain:
                        selenium_cookie["domain"] = cookie.domain

                    driver.add_cookie(selenium_cookie)
                driver.refresh()
                print("done with integration, refreshing")
                final_btn = driver.find_element(By.XPATH, value='//*[@title="Sorry for the ads, we really need them to pay server bills and to keep the site up!"]')
                if i == 2:
                    print("using JS")
                    driver.execute_script("arguments[0].click();", final_btn)
                else:
                    final_btn.click()
            except Exception as e:
                print(i, "exception in clickin download button", str(e)[:70])
                time.sleep(2)
            else:
                break
    except ZeroDivisionError as e:
        print(f"❌ Error downloading episode {start_episode}: {e}")
        retry_counts[start_episode] = retry_counts.get(start_episode, 0) + 1

        if retry_counts[start_episode] >= retry_limit:
            print(f"⚠️ Skipping episode {start_episode} after {retry_limit} failed attempts.")
            j += 1  # Give up on it
        else:
            print(f"🔁 Will retry episode {start_episode}")
            # i stays the same — this episode will be retried
    else:
        downloaded = True
        print(f"⌛ Downloading episode {start_episode}")
        while True:
            # print("in while")
            time.sleep(10)
            try:
                filename = checker.get_crdownload_filenames()[0]
            except IndexError:
                # if not checker.find_file(f"AnimePahe_One_Piece_-_{start_episode}_720p_HorribleSubs.mp4"):
                if not checker.find_file(f"AnimePahe_Naruto_-_Shippuuden_-_{start_episode}_1072p_HorribleSubs.mp4"):
                # if not checker.find_file(f"AnimePahe_Haikyuu_-_0{start_episode}_BD_720p_sam") and checker.find_file(f"AnimePahe_Haikyuu_-_{start_episode}_BD_720p_sam"): # For haikyu
                    print(f"☠️ Bot claims episode {start_episode} is downloaded but it can't be found.")
                    print("It will be retried")
                    downloaded = False
                    j -= 1
                break
            size = checker.get_file_size(filename)
            if last_size == size:
                time.sleep(15)
                if last_size == checker.get_file_size(filename):
                    print(f"❌ Error downloading episode {start_episode}: Download seems it has stopped")
                    print(f"📝 last_size: {last_size} | size: {size}")
                    downloaded = False
                    j -= 1
                    break
            else:
                # print(f"📝Just Checked: last_size: {last_size} | size: {size}")
                last_size = size
        last_size = 0
        j += 1
        if downloaded:
            print(f"✅ Downloaded episode {start_episode}")


# for i in link_text:
print(retry_counts)
# for j in links:
#     print(j)
# print([max_page_ep, ep_position])