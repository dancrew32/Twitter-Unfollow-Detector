import settings
import tweepy
import json
import sys
import smtplib


def lazyprop(fn):
    attr_name = '_lazy_' + fn.__name__
    @property
    def _lazyprop(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)
    return _lazyprop


class UnfollowDetector(object):

    def __init__(self):
        self.api = self.auth()

    def auth(self):
        auth = tweepy.OAuthHandler(consumer_key=settings.CONSUMER_KEY,
                                   consumer_secret=settings.CONSUMER_SECRET)
        auth.set_access_token(key=settings.ACCESS_TOKEN_KEY,
                              secret=settings.ACCESS_TOKEN_SECRET)
        return tweepy.API(auth)

    @lazyprop
    def current_followers(self):
        return self.api.followers_ids()

    def save_current_followers(self):
        with open(settings.CACHE_FILE, 'w') as f:
            f.write(json.dumps(self.current_followers))

    @lazyprop
    def previous_followers(self):
        try:
            with open(settings.CACHE_FILE, 'r') as f:
                return json.loads(f.read())
        except IOError:
            return []

    @property
    def difference(self):
        return list(set(self.previous_followers) - set(self.current_followers))

    def end(self):
        self.save_current_followers()
        sys.exit()

    def mail(self, out):
        from email.mime.text import MIMEText
        msg = MIMEText("\n".join(out))

        msg['Subject'] = 'New Twitter Unfollowers'
        msg['From'] = settings.EMAIL_FROM
        msg['To'] = settings.EMAIL_TO

        s = smtplib.SMTP('localhost')
        s.sendmail(settings.EMAIL_FROM, [settings.EMAIL_TO], msg.as_string())
        s.quit()

    @classmethod
    def main(cls):
        detector = cls()
        out = []
        for user_id in detector.difference:
            u = detector.api.get_user(user_id=user_id)
            if u.id not in detector.current_followers:
                out.append("%s is no longer your follower: %s" % (u.screen_name, u.url))

        if out:
            detector.mail(out)
        detector.end()

        

if __name__ == "__main__":
    UnfollowDetector.main()






