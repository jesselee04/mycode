#!/usr/bin/env python3

import requests

# Define our base API
API = "https://api.magicthegathering.io/v1/"

def main():
    """RUN time code"""

    # create resp, which is our request object
    resp = requests.get(f"{API}sets")

    # display the methods available to our new object
    print (dir(resp))

if __name__ == "__main__":
    main()
