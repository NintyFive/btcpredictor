from .reporter import *
from .database import *
from .helpers  import *
from .logger   import *
import apscheduler
import requests

from apscheduler.triggers.base import BaseTrigger
from datetime import timedelta, datetime

class NewsLogger(AbstractLogger):

    INTERVAL = 5   # Minimum number of minutes that must pass to retrieve news
    ARTICLES = 5   # Number of articles to gather every INTERVAL minutes between [1, 50]
    base_url = 'https://cloud.iexapis.com/stable/{}'
    sand_url = 'https://sandbox.iexapis.com/stable/{}'
    api_pkey = '?token=' + 'pk_18221745178442aa83406f8a3f877c2e'
    api_skey = '?token=' + 'sk_a82b032b40ff4f3bb7824074dc9243d5'
    logrname = 'News'
    curr_url = base_url
    progress = True

    def _purl(endpoint):
        url = NewsLogger.curr_url.format(endpoint)
        return url + NewsLogger.api_pkey
    def _surl(endpoint):
        url = NewsLogger.curr_url.format(endpoint)
        return url + NewsLogger.api_skey

    @staticmethod
    def store():
        this = NewsLogger
        super(this, this).store(this.logrname, this.progress)

    @staticmethod
    def log():
        try:
            ltime = localtime(fmt=True)
            reqst = requests.get(NewsLogger._purl('stock/btcusd/news/last/{}/'.format(NewsLogger.ARTICLES)))
            items = json.loads(reqst.content)
            items = { "LAtime" : ltime, "articles" : items }
            items = Database.rt.child(NewsLogger.logrname).push(items)
            if NewsLogger.progress: print("Logged {} data: {}".format(NewsLogger.logrname, items))
        except Exception as e:
            Reporter.send_urgent(NewsLogger.logrname, "logging", repr(e))
