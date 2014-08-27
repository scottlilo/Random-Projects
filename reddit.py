import praw
r = praw.Reddit(user_agent='test_application by scottlilo')

file = 'logsgeorgesucks.txt'

rawfile = open(file,"w")

sub = raw_input("What subreddit should we load? ----> ")


submissions = r.get_subreddit(sub)
for post in submissions.get_hot(limit=10):
	
	print post
	print post.author
	print post.id + '\n'
	
	rawfile.write(str(post.score) + ' -- ' + post.title + '\n')
	rawfile.write(str(post.author)  + '\n')
	rawfile.write(str(post.selftext)+'\n')
	rawfile.write(str(post.comments[0]) + '\n')
	rawfile.write('*'*140 + '\n \n')



rawfile.close()
