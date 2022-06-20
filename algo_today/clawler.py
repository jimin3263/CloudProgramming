import requests, time, json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

import django
django.setup()

from algo_today.models import Problem

def crawl(page):
    url = "https://solved.ac/api/v3/search/problem"
    querystring = {"query": " ", "page": f"{page}"}

    headers = {"Content-Type": "application/json"}
    response = requests.request("GET", url, headers=headers, params=querystring)

    temp = dict()
    temp["item"] = json.loads(response.text).get("items")
    for item in temp["item"]:
        hash = int(item.get("problemId"))
        title = item.get("titleKo")
        tags = ""

        info = item.get("tags")
        length = len(info)
        for idx, tag in enumerate(info):
            temp_tag = tag.get("displayNames")
            tags += temp_tag[1].get("short")

            if idx == length - 1:
                continue
            tags += " "
        print(hash)
        #Problem.objects.create(title=title, tag=tags, number=hash)

def main():
    for i in range(1, 5):
        print(f"crawling {i} page")
        crawl(i)
        time.sleep(2)


if __name__ == "__main__":
    main()