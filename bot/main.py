import requests
import json

from random import randint, choice

from faker import Faker

from config import NUMBER_OF_USERS, MAX_POSTS_PER_USER


url_register = "http://localhost:8000/api/register/"
url_login = "http://localhost:8000/api/login/"

url_posts = "http://localhost:8000/api/posts/"
url_likes = "http://localhost:8000/api/likes/"

fake = Faker()

access_tokens = []
posts = []


def create_users():
    for i in range(NUMBER_OF_USERS):
        user = {
            "username": fake.user_name(),
            "email": fake.email(),
            "password": fake.password(),
        }

        requests.post(url_register, data=user)

        data_login = {
            "username": user.get("username"),
            "password": user.get("password"),
        }

        login = requests.post(url_login, data=data_login)
        auth = json.loads(login.text)
        access_tokens.append(auth.get("access"))


def create_posts():

    for token in access_tokens:
        content = "".join(fake.texts())
        data = {"title": f"{fake.text()}", "content": f"{content}"}
        headers = {"Authorization": f"Bearer {token}"}
        for i in range(randint(1, MAX_POSTS_PER_USER)):
            post = requests.post(url_posts, data=data, headers=headers)
            post_id = json.loads(post.text).get("id")
            posts.append(post_id)


def set_likes():  # takes a function as an argument
    posts_quantity = len(posts)

    for i in range(posts_quantity):
        user_token = choice(access_tokens)
        post = choice(posts)
        headers = {"Authorization": f"Bearer {user_token}"}
        post_data = {"post": post}
        r = requests.post(url_likes, data=post_data, headers=headers)


def main():
    create_users()
    create_posts()
    set_likes()
    print("Success!")


if __name__ == "__main__":
    main()
