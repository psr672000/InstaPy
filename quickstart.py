""" Quickstart script for InstaPy usage """

# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace


# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

headless_browser=True

# get an InstaPy session!
session = InstaPy()

with smart_run(session):
    # activity
    session.like_by_tags(["natgeo"], amount=10)
