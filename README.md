# Twitter Unfollow Detector

Get notified when someone unfollows you on Twitter

## Install

* Setup `virtualenv` and install dependencies:

```bash
virtualenv venv && ./venv/bin/pip install -r requirements.txt
```

* Make your own `settings.py`

```bash
cp settings-example.py settings.py
```

* Create an app at https://apps.twitter.com
* Find the app's Consumer Key and Secret, paste in `settings.py`
* Create an Access Token and Secret, paste in `settings.py`
* Setup your server's `EMAIL_FROM` and `EMAIL_TO`
* Run script every now and then `crontab -e`:

```bash
30 * * * * /path/to/venv/bin/python /path/to/unfollow_detector.py > /dev/null 2>&1
```


