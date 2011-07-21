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
    return '''
            <span class="social_icons">
            <g:plusone>
            '''+ url_for(post) + '''%s</g:plusone>
            </span>
        '''

def insert_header_js(metadata):
    metadata.append(
            '''<script type="text/javascript" src="https://apis.google.com/js/plusone.js">
            {lang: 'fr'}
            </script> ''')

def setup(app, plugin):
    """This function is called by Zine in the application initialization
    phase. Here we connect to the events and register our template paths,
    url rules, views etc.
    """

    app.connect_event('before-metadata-assembled', insert_header_js)
    app.connect_event('after-entry-rendered', add_social_banner)
