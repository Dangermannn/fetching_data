import json
import sys
import urllib.request
import haversine as hs

POSTS_URL = "https://jsonplaceholder.typicode.com/posts"
USERS_URL = "https://jsonplaceholder.typicode.com/users"


def get_data_as_json(url: str):
    data = None
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    return data


def get_users_with_posts(users, posts):
    for user in users:
        user_posts = []
        for post in posts:
            if post["userId"] == user["id"]:
                user_posts.append(post)
        user['posts'] = user_posts

    return users


def print_users_number_of_posts(users):
    for user in users:
        print(f'{user["username"]} napistał(a) {len(user["posts"])} postów')


def get_not_unique_titles(posts):
    sorted_posts = sorted(posts, key=lambda x: x["title"].lower())
    not_unique_titles = []
    for i in range(0, len(sorted_posts) - 1):
        if sorted_posts[i + 1]["title"] is sorted_posts[i]["title"]:
            repeats = False
            for post in not_unique_titles:
                if post["title"] == sorted_posts[i]["title"]:
                    repeats = True
            if not repeats:
                not_unique_titles.append(sorted_posts[i])
    return not_unique_titles


def calculate_distance_between_geolocations(geo1, geo2):
    return hs.haversine((float(geo1["lat"]), float(geo1["lng"])), (float(geo2["lat"]), float(geo2["lng"])))


def get_distance_between_users(users):
    msgs_to_return = []
    if len(users) < 2:
        return ["there are not enough users to compare"]

    for i in range(0, len(users)):
        distance = sys.maxsize
        index = -1
        for j in range(0, len(users) - 1):
            if i == j:
                continue
            d = float(calculate_distance_between_geolocations(users[i]["address"]["geo"], users[j]["address"]["geo"]))
            if d < distance:
                distance = d
                index = j
        msgs_to_return.append(f"The closest user to {users[i]['username']} lives {users[index]['username']}")
    return msgs_to_return

def main():
    data = get_users_with_posts(get_data_as_json(USERS_URL), get_data_as_json(POSTS_URL))
    print_users_number_of_posts(data)
    print(json.dumps(data))

    p = get_not_unique_titles(get_data_as_json(POSTS_URL))
    print(p)

    print_users_number_of_posts(data)
    print(get_distance_between_users(users))


if __name__ == '__main__':
    main()
