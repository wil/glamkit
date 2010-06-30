from django.db import models
from blogtools.models import *

# Uncomment lines to add functionality

class MyBlogPost(
        EntryBase,                      # The base class for all GLAMkit-blogtool blog entries - required
        # FeaturableEntryMixin,         # Allows for featured, 'sticky' posts
        # StatusableEntryMixin,         # Allows for draft, live, and hidden posts
        # TaggableEntryMixin,           # Posts with tags
        # HTMLFormattableEntryMixin,    # Use markup on the body field
    ):
    # EntryBase provides author, title, pub_date, slug, and enable_comments fields
    # define your own additional fields here
