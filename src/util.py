import pandas as pd
import os
import config


def extract_hash_tags(hash_tag_entries):
    """Return the list of hashtags if present in a tweet"""
    hash_tag_list = []
    hashtag = ""
    if len(hash_tag_entries) > 0:
        for entry in range(0, len(hash_tag_entries)):
            hashtag = hashtag + hash_tag_entries[entry]['text'] + ','
        hash_tag_list.append(hashtag)
    else:
        hash_tag_list.append("#none")

    return hash_tag_list


def extract_user_mention(user_mention_entries):
    """Return the list of user mentions if present in a tweet"""
    user_mention_list = []
    user_mention = ""
    if len(user_mention_entries) > 0:
        for entry in range(0, len(user_mention_entries)):
            user_mention = user_mention + user_mention_entries[entry]['screen_name'] + ','
        user_mention_list.append(user_mention)
    else:
        user_mention_list.append("#none")

    return user_mention_list


def write_output(tweet_data, output_dir):
    """Write the csv file into the path"""
    df = pd.DataFrame(tweet_data, columns=config.tweet_columns)
    print('Total number of tweet fetched are', len(df))
    df.to_csv(os.path.join(output_dir, config.FILE_NAME), index=False, header=True)
