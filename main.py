from instagrapi import Client
import time
import random
import praw
import requests
import os


# Set up Reddit API credentials
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="image_downloader"
)

# Specify the subreddit to download images from
subreddit_name = "SUBREDDIT_OF_CHOICE"  # e.g., "wallpapers"

# Create a folder to store images
output_folder = "images"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to download an image
def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {url}")

# Initialize the Instagram client
client = Client()

# List of some random starter captions
captions = [
    "When you realize you’re the ‘before’ picture.",
    "Adulting: it’s like folding a fitted sheet.",
    "Plot twist: I wasn’t prepared for this either.",
    "Is this the new ‘normal’ they warned us about?",
    "When life hands you lemons, throw them back.",
    "Instructions unclear. Ended up in another timeline.",
    "Can we go back to the good old 'buffering' days?",
    "Error 404: motivation not found.",
    "I need six months of vacation, twice a year.",
    "That moment when caffeine fails you.",
    "Running out of reasons to act normal.",
    "Let’s pretend I had something witty to say.",
    "A little sass never hurt anybody... or did it?",
    "If it’s wrong, it’s probably my favorite.",
    "My bed is a magical place. I suddenly remember everything I forgot to do.",
    "The 'no worries' lifestyle is so underrated.",
    "I need a user manual for this whole life thing.",
    "Still loading… any day now.",
    "I can’t adult today. Please don’t make me.",
    "Living on a diet of pizza and bad decisions.",
    "This wasn’t on my vision board.",
    "Password: 12345… again.",
    "It’s all fun and games until your coffee wears off.",
    "When in doubt, nap it out.",
    "I’ve upgraded from procrastination to full-on 'ignore mode.'",
    "I didn’t sign up for this level of responsibility.",
    "The struggle is real, but the nap is worth it.",
    "Just winging it: life, eyeliner, everything.",
    "How do I delete yesterday?",
    "Oops, I adulted… won’t happen again."
]

# Randomly select a caption
caption = random.choice(captions)

# Input your Instagram credentials
username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"
client.login(username, password)

def upload_post(image_path, caption):
    try:
        client.photo_upload(image_path, caption)
        print("Post uploaded successfully!")
    except Exception as e:
        print(f"Error uploading post: {e}")

# Input the path to the image you want to upload
image_path = "images/image.jpeg"



# Fetch the most recent post in the subreddit
subreddit = reddit.subreddit(subreddit_name)
latest_post = next(subreddit.new(limit=1))  # Get the most recent post

# Check if the post has an image URL
if latest_post.url.endswith((".jpg", ".png", ".jpeg")):
    filename = os.path.join(output_folder, "image.jpeg")
    download_image(latest_post.url, filename)
else:
    print("The most recent post does not contain an image.")

print("Download complete!")

# # Pseudorandom posting activity
# delay_minutes = random.randint(5, 10)
# print(f"Waiting for {delay_minutes} minutes before uploading post...")
# time.sleep(delay_minutes * 60) 

upload_post(image_path, caption)


