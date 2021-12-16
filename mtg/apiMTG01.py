#1/usr/bin/env python3

#import always go at the top of your code
import requests

def main():
    """RUN TIME CODE"""

    # create resp, which is our request object
    resp = requests.get("https://api.magicthegathering.io/v1/sets")

    # Display the methods available to our new object
    print(dir(resp))

if __name__ == "__main__":
    main()
