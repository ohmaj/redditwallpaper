import time
import praw
user_agent = "get popular wallpapers 1.0 by ohmaj4699@gmail.com"
r = praw.Reddit(user_agent=user_agent)
r.login()

def downloadImage(imageUrl, localFileName):
    response = requests.get(imageUrl)
    if response.status_code == 200:
        print('Downloading %s...' % (localFileName))
        with open(localFileName, 'wb') as fo:
            for chunk in response.iter_content(4096):
                fo.write(chunk)
already_done = []                
while True:
    subreddit = r.get_subreddit('wallpapers')
    for submission in subreddit.get_hot(limit=10):
        if submission.id not in already_done:
            localFileName = 'reddit_%s_%s_album_None_imgur_%s' % (submission.id, imageFile)
            downloadImage(imageUrl, localFileName)    
            already_done.append(submission.id)
    time.sleep(1800)
