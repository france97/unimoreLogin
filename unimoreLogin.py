import sys
import yaml
import requests

if __name__ == '__main__':
    settings_file = "config.yaml"

    try:
        with open(settings_file, "r") as file:
            settings = yaml.safe_load(file)
            file.close()
    except FileNotFoundError:
        print(f"ERROR: config file {settings_file} not found.", file=sys.stderr)
        sys.exit(1)

    with requests.Session() as session:
        uri = "https://c1.wifi.unimo.it/upload/custom/UNIMORE_cppm_prof/portal_login.html"
        response = session.get(uri)

        if response.status_code != 200:
            print(f"ERROR: first response status code: {response.status_code}", file=sys.stderr)
            sys.exit(2)

        uri = "https://portal.wifi.unimore.it/cgi-bin/login"

        app_settings = settings.get("APP")

        if app_settings is None:
            print(f"ERROR: settings not found.", file=sys.stderr)
            sys.exit(3)

        user = app_settings.get("USER")
        password = app_settings.get("PASSWORD")

        if not user or not password:
            print(f"ERROR: first response status code: {response.status_code}", file=sys.stderr)
            sys.exit(4)

        data = {
            "user": user,
            "password": password,
            "cmd": "authenticate",
            "Login": "Log+In"
        }

        response = session.post(url=uri, data=data, allow_redirects=True)

        if response.status_code != 200:
            print(f"ERROR: second response status code: {response.status_code}", file=sys.stderr)
            sys.exit(5)

        sys.exit(0)
