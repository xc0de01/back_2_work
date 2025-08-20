#DAY 1/100

import os
import django


def day_1(name: str):
    try:
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        return f"Welcome {name}, to 100 Days of Django Development!"
    except Exception as e:
        return f"Error: {e}"


def env_det():
    print(f"Django version: {django.get_version()}")
    print("Django applications include:")
    apps = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.sessions",

    ]
    for app in apps:
        print(f"- {app}")


if __name__ == "__main__":
    print(day_1("Simon"))
    env_det()


#DAY 2/100
