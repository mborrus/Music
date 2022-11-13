from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller as chromedriver
path = chromedriver.install()
import time

print('how many times to run?')
number_of_times_to_run = input()

for runs in number_of_times_to_run:
    #This mutes the windows we're going to open
    chrome_options = Options()
    chrome_options.add_argument("--mute-audio")

    #This makes a web-driver - aka a virtual online session
    driver = webdriver.Chrome(path,chrome_options=chrome_options)

    #This opens up the widget (rather than the website), and the second step clicks the html element for the play button
    driver.get("https://www.mixcloud.com/widget/iframe/?hide_cover=1&feed=%2FDj_Soup9%2Fdj-soup-fresh-start-dj-contest%2F")
    driver.find_element_by_class_name('widget-play-button').click()

    #pause for 5 seconds so it can load before switching tabs
    pause_length = random.randint(5,3*60);
    time.sleep(pause_length)
    # time.sleep(10)

    #Open a new tab and switch to it
    driver.execute_script("window.open('about:blank','secondtab');")
    driver.switch_to.window("secondtab")

    #repeat above
    driver.get("https://www.mixcloud.com/widget/iframe/?hide_cover=1&feed=%2FDj_Soup9%2Fdj-soup-fresh-start-dj-contest%2F")
    driver.find_element_by_class_name('widget-play-button').click()

    play_length = random.randint(5*60,25*60)
    time.sleep(play_length)
    # time.sleep(10)

    driver.close();
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
