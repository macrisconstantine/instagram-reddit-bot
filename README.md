# instagram-reddit-bot
This is a little script I made for fun to see if I could automate an Instagram meme account.
## What It Does
- This script uses a Reddit API to visit a subreddit and download the latest posted photo to the included images dir.
- It then starts up an Instagram client and logs in with specified credentials.
- It appends a random selection from a pool of GPT-generated captions, and uploads the post.
## How to Use It
- Download or clone this repo.
- To use the Reddit API, you will have to create a Reddit "app" (instructions for this can be found online--its very simple and easy).
- Once you have the necessary Reddit API credentials, replace the placeholders with your real Instagram and Reddit credentials in the `main.py` file.
- Test the script by running manually.
### Optional: 
- Use windows task scheduler or a similar tool to automate when and how often the script is run.
## WARNING
- Use at your own risk.
- Instagram may become suspicious of your account.
- I am not liable for any consequences you may face as a result of using this code.