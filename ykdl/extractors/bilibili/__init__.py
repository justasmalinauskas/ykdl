#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ykdl.util.html import get_location, fake_headers
from ykdl.util.match import match1, matchall

import re

def get_extractor(url):
    fake_headers.pop('Accept-Language', None)

    if 'live.bilibili' in url:
        from . import live as s
        return s.site, url
    elif 'vc.bilibili' in url:
        from . import vc as s
        return s.site, url
    elif '/bangumi/' in url:
        from . import bangumi as s
        return s.site, url

    av_id = match1(url, '(?:/av|aid=)(\d+)')
    page_index = match1(url, '(?:page|\?p)=(\d+)', 'index_(\d+)\.') or '1'
    if page_index == '1':
        url = 'https://www.bilibili.com/av{}/'.format(av_id)
    else:
        url = 'https://www.bilibili.com/av{}/?p={}'.format(av_id, page_index)
    url = get_location(url)

    if '/bangumi/' in url:
        from . import bangumi as s
    else:
        from . import video as s

    return s.site, url
