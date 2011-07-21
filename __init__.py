# -*- coding: utf-8 -*-
"""
    zine.plugins.social
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2011 by gabriel pettier
    :license: GPL, see LICENSE for more details.
"""
from zine.api import *
from zine.views.admin import render_admin_response

def add_social_banner(post):
    url = url_for(post)
    return '''
            <div class="social_icons">
            <g:plusone href="'''+ url +'''"></g:plusone>

            <a href="http://twitter.com/share" class="twitter-share-button"
            data-url="'''+ url +'''" data-count="none">Tweet</a>

            <span id="fb-root"></span>
            <fb:like href="'''+ url +'''" send="true" layout="button_count"
            width="450" show_faces="true" font=""></fb:like>
            </div>
        '''

def insert_header_js(metadata):
    metadata.append(
            '''
            <script type="text/javascript" src="https://apis.google.com/js/plusone.js">
            {lang: 'fr'}
            </script>

           <script
            type="text/javascript" src="http://platform.twitter.com/widgets.js">
            </script>

            <script src="http://connect.facebook.net/en_US/all.js#xfbml=1"></script>
            ''')

def setup(app, plugin):
    """This function is called by Zine in the application initialization
    phase. Here we connect to the events and register our template paths,
    url rules, views etc.
    """

    app.connect_event('before-metadata-assembled', insert_header_js)
    app.connect_event('after-entry-rendered', add_social_banner)
