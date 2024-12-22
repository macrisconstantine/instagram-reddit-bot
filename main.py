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
    "When the group chat turns into a war zone and you’re just here for the memes.",
    "Me: 'This is fine.' Also me: *screams internally*.",
    "Somewhere out there, my last two brain cells are playing tag.",
    "POV: You forgot to hit 'save' before the game crashed.",
    "Nothing like a fresh existential crisis to start the day.",
    "They said it gets better, but 'it' was apparently on vacation.",
    "How to fail successfully: a memoir by me.",
    "Me staring at the fridge hoping for a snack that doesn’t exist.",
    "Friend: 'Why are you so quiet?' Me: *Internally narrating my imaginary comeback from five years ago.*",
    "When you're the meme in a world of stock photos.",
    "Some mistakes were made. Mainly by me, but let’s not point fingers.",
    "When life gives you lemons, it also steals your wallet for the juicer.",
    "Me: 'I’ll sleep early tonight.' Also me at 3am: *Researching the migration patterns of geese.*",
    "The internet: a place where sarcasm and bad decisions go to thrive.",
    "Trying to adult, but my inner child keeps calling for backup.",
    "Me: *Looks productive*. Reality: *Just hitting 'refresh' on life.*",
    "I told myself I'd stop procrastinating tomorrow. That was three months ago.",
    "Every day I wake up with a new excuse to not go outside.",
    "When you run out of storage, but your brain still downloads bad ideas.",
    "Me: 'This year will be different!' Life: *Uno reverse card.*",
    "Nobody: Literally nobody: My brain: 'You should rewatch that show from 2006.'",
    "When you lose an argument in the shower against an imaginary opponent.",
    "Shoutout to gravity for keeping it real and me on the floor.",
    "Just here to vibe, overthink, and misinterpret social cues.",
    "That awkward moment when the Wi-Fi goes down, and you have to be a person again.",
    "When life hands you lemons, it's probably a scam. Demand pizza instead.",
    "The world: 'Be yourself!' Me: *Wishes I were a taco.*",
    "It’s not a phase, Mom. It’s a full-blown personality crisis.",
    "If sarcasm burned calories, I’d be a fitness influencer by now.",
    "When the 'low battery' alert hits harder than your will to live.",
    "Some people train for marathons. I train to carry all the groceries in one trip.",
    "My toxic trait is thinking I can fix everything with snacks.",
    "Me: *Tries to blend in.* Also me: *Trips over my own existence.*",
    "Can’t come to the phone right now. I’m too busy spiraling.",
    "Why make plans when you can just panic instead?",
    "When the meme hits so hard, you temporarily forget the pain of existence.",
    "Me: *Laughs at meme*. Brain: 'Save it to laugh at when you’re sad later.'",
    "When you're the 'funny friend' but dead inside is your default setting.",
    "The Wi-Fi went out, so now I’m here, questioning reality.",
    "Pro tip: If you can’t handle the heat, uninstall the app.",
    "In my defense, the instructions were in Comic Sans.",
    "I’d like to file a complaint with the universe, but the line’s too long.",
    "When you realize the plot twist is that you’re the problem.",
    "Can someone pause life for a minute? I need a snack break.",
    "When the meme perfectly describes your entire personality in two panels.",
    "I aspire to be the person my dog thinks I am.",
    "The struggle was real. And then it got a sequel.",
    "Not all heroes wear capes. Some just scroll Reddit at 3am.",
    "My autobiography: 'Still Buffering After All These Years.'"
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


