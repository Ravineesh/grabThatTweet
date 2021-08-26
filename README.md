# grabThatTweet

A command line utility to fetch the tweets of user.

# Installation instruction
After cloning this repository.

``` 
git clone  https://github.com/Ravineesh/grabThatTweet.git 
cd grabThatTweet/src 
```

Before running the utlity you have export the `API_KEY`, `API_SECRET_KEY`, `ACCESS_TOKEN`, `ACCESS_TOKEN_SECRET` in your command line. These keys can be generated from your Twitter Developer account.

 `` $export  API_KEY='your_api_key' ``
 `` $export  API_SECRET_KEY='your_api_secret_key' ``
 `` $export  ACCESS_TOKEN='your_access_token' ``
 `` $export  ACCESS_TOKEN_SECRET='your_access_token_secret' ``
 


Run the following command.

 `` python tweet.py --twitter_handle @ --tweet_limit 2000 --output_dir '/home/' ``
 
 The parameters required:
- `--twitter_handle` : The twitter username.
- `--tweet_limit` : The maximum limit of tweets to be fetched.
- `--output_dir`: The path of csv file which contains tweets of user
 
