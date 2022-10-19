#!/usr/bin/env python

import argparse
import csv
import sys
import time
import os
import twitter
from dateutil.parser import parse

__author__ = "Roni Bandini, based on Koen Rouwhorst original code"
__version__ = "0.1"

def delete(api, date, r):
    with open("tweets.csv") as file:
        count = 0

        for row in csv.DictReader(file):
            tweet_id = int(row["id"])
            tweet_date = parse(row["created_at"], ignoretz=True).date()

            if date != "" and tweet_date >= parse(date).date():
                continue

            if (r == "retweet" and row["retweeted_status_id"] == "" or
                    r == "reply" and row["in_reply_to_status_id"] == ""):
                continue

            try:
                print("Borrando tweet #{0} ({1})".format(tweet_id, tweet_date))

                api.DestroyStatus(tweet_id)
                count += 1
                time.sleep(0.5)

            except twitter.TwitterError:
                print("Error: %s\n" )

    print("Cantidad de tweets borrados: %s\n" % count)

def error(msg, exit_code=1):
    sys.stderr.write("Error: %s\n" % msg)
    exit(exit_code)

def main():
    parser = argparse.ArgumentParser(description="Delete old tweets.")
    parser.add_argument("-d", dest="date", required=True,
                        help="Borrar tweets hasta la fecha")
    parser.add_argument("-r", dest="restrict", choices=["reply", "retweet"],
                        help="Restringir respuestas y retweets")

    args = parser.parse_args()

    api = twitter.Api(consumer_key="123456",
                      consumer_secret="123456",
                      access_token_key="123456",
                      access_token_secret="123456")

    delete(api, args.date, args.restrict)


if __name__ == "__main__":
    main()
