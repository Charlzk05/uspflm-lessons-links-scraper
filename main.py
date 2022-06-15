import sys
import requests
import os
from bs4 import BeautifulSoup

error_print = "Something went wrong :/"
file_name = "Lessons list.txt"

def main(course_link, your_moodle_cookies):
    cookies = {
        'MoodleSession': f'{your_moodle_cookies}',
    }

    a_tag = "a"
    a_tag_class = "aalink"

    a_tag_listing = []

    cookies_error = "Please paste a valid moodle cookies\n"

    try:
        print("\nRequesting...")
        response = requests.get(f"{course_link}", cookies=cookies)
    except:
        os.system("cls")
        print(cookies_error)
        sys.exit()

    soup = BeautifulSoup(response.text, "html.parser")
    find_a = soup.find_all(a_tag, {"class":a_tag_class})
    get_title = soup.find("title")
    get_title = get_title.text

    for find_as in find_a:
        find_as = find_as["href"]
        a_tag_listing.append(find_as)

    with open(file_name, "w") as file:
        file.write(f"{get_title}\nLessons List:\n\n")
        for a_tag_listings in a_tag_listing:
            if "resource" in a_tag_listings:
                file.write(a_tag_listings + "\n")
            else:
                continue

    os.system("cls")
    print(f"Saved on {file_name}")

if __name__ == "__main__":
    try:
        print("USPFLM Courses Lessons Scraper by Charliezkie.\n")
        moodle_cookie = input("Insert your moodle cookie: ")
        course_link = input("Course link: ")
        main(course_link, moodle_cookie)
    except:
        print(error_print)