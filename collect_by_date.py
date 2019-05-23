import got
import codecs


try:
    tweetCriteria = got.manager.TweetCriteria()
    outputFileName = "output_got_greve.csv"

    outputFile = codecs.open(outputFileName, "w+", "utf-8")
    outputFile.write(
        'username;date;retweets;favorites;text;geo;mentions;hashtags;id;permalink')

    print('Searching...\n')

    def receiveBuffer(tweets):
        for t in tweets:
            outputFile.write(('\n%s;%s;%d;%d;"%s";%s;%s;%s;"%s";%s' % (t.username, t.date.strftime(
                "%Y-%m-%d %H:%M"), t.retweets, t.favorites, t.text, t.geo, t.mentions, t.hashtags, t.id, t.permalink)))
        outputFile.flush()
        print('More %d saved on file...\n' % len(tweets))

    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(
        'greve').setSince("2019-05-14").setUntil("2019-05-16").setMaxTweets(5)

    got.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer)
finally:
    outputFile.close()
    print('Done. Output file generated "%s".' % outputFileName)
# print got.manager.TweetManager.getTweets(tweetCriteria)

# for tweet in got.manager.TweetManager.getTweets(tweetCriteria):
#    print tweet._json
#tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
# print tweet.text
