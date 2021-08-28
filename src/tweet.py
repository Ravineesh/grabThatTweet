import argparse
import os
import config
import tweepy
import datetime
import time

# Creating an OAuthHandler instance.
auth = tweepy.OAuthHandler(os.environ["API_KEY"], os.environ["API_SECRET_KEY"])
# Setting the access token provided by the Twitter
auth.set_access_token(os.environ["ACCESS_TOKEN"], os.environ["ACCESS_TOKEN_SECRET"])

# The API class is used to provide access to entire twitter RESTFul API methods
api = tweepy.API(auth)


def fetch_tweets(twitter_handle, tweet_limit, output_dir):
    tweets = tweepy.Cursor(api.user_timeline, id=twitter_handle, tweet_mode='extended').items(tweet_limit)
    startDate = datetime.datetime(2012, 1, 1, 0, 0, 0)
    endDate = datetime.datetime(2021, 9, 24, 0, 0, 0)

    for tweet in tweets:
        hashtag_str = ""
        user_mention_str = ""
        if (tweet.created_at > startDate) & (tweet.created_at < endDate):
            config.user_name.append(tweet.user.name)
            config.user_id.append(tweet.user.id_str)
            config.user_screen_name.append(tweet.user.screen_name)
            config.source.append(tweet._json["source"])
            config.language.append(tweet._json["lang"])
            config.tweet_text.append(tweet.full_text)
            config.tweet_creation_date.append(tweet.created_at)
            config.retweets_count.append(tweet._json["retweet_count"])
            config.like_count.append(tweet._json["favorite_count"])

            # If tweet contains hashtags
            config.hashtag.append(util.extract_hash_tags(tweet._json["entities"]["hashtags"]))

            # If tweet contains user_mentions
            config.user_mention.append(util.extract_user_mention(tweet._json["entities"]["user_mentions"]))

    tweet_data = zip(config.user_name, config.user_id, config.user_screen_name, config.source,
                     config.language, config.tweet_text, config.tweet_creation_date,
                     config.retweets_count, config.like_count, config.hashtag, config.user_mention)
    util.write_output(tweet_data, output_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--twitter_handle",
        type=str
    )
    parser.add_argument(
        "--tweet_limit",
        type=int,
    )
    parser.add_argument(
        "--output_dir",
        type=str,
    )

    args = parser.parse_args()

    fetch_tweets(
        twitter_handle=args.twitter_handle,
        tweet_limit=args.tweet_limit,
        output_dir=args.output_dir
    )
