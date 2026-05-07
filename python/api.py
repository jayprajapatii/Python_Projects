import requests
import json
from datetime import datetime

BASE_URL = "https://gorest.co.in/public/v2"

HEADERS = {
    "Accept": "application/json",
    "User-Agent": "python-api-client"
}

def generate_time_columns():
    now = datetime.utcnow()

    date_id = int(now.strftime("%Y%m%d"))
    date_hour_id = int(now.strftime("%Y%m%d%H"))

    minute = now.minute
    hour = now.hour

    start15 = (minute // 15) * 15
    start30 = (minute // 30) * 30

    end15 = (start15 + 15) % 60
    end30 = (start30 + 30) % 60

    fifteen = f"{hour:02d}:{start15:02d}-{hour:02d}:{end15:02d}"
    thirty = f"{hour:02d}:{start30:02d}-{hour:02d}:{end30:02d}"

    return {
        "utc_timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
        "date_id": date_id,
        "date_hour_id": date_hour_id,
        "fifteen_min_bucket": fifteen,
        "thirty_min_bucket": thirty
    }


def get_api_data(endpoint):
    url = f"{BASE_URL}/{endpoint}?per_page=20"

    response = requests.get(url, headers=HEADERS)

    print(f"{endpoint} API Status:", response.status_code)

    if response.status_code == 200:
        return response.json()
    else:
        print("API Error:", response.text)
        return []


def process_users():
    users = get_api_data("users")

    final = []

    for user in users:
        if user["status"] == "active":
            record = {**user, **generate_time_columns()}
            final.append(record)

    with open("users_output.json", "w") as f:
        json.dump(final, f, indent=4)

    print("Users saved:", len(final))


def process_posts():
    posts = get_api_data("posts")

    final = []

    for post in posts:

        if len(post["body"]) > 150:
            post["body"] = post["body"][:150]

        record = {**post, **generate_time_columns()}
        final.append(record)

    with open("posts_output.json", "w") as f:
        json.dump(final, f, indent=4)

    print("Posts saved:", len(final))


def process_comments():
    comments = get_api_data("comments")

    final = []

    for c in comments:
        record = {**c, **generate_time_columns()}
        final.append(record)

    with open("comments_output.json", "w") as f:
        json.dump(final, f, indent=4)

    print("Comments saved:", len(final))


def main():
    print("Starting API Pipeline")

    process_users()
    process_posts()
    process_comments()

    print("Pipeline Completed")


if __name__ == "__main__":
    main()