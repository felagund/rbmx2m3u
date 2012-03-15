#!/usr/bin/env python
# -*- coding: utf-8 -*-

# rbmx2m3u
# Version 1.O
#
# Convert Rhytmbox playlist to m3u
#
# Tomáš Hnyk <tomashnyk2gmail.com>

# Copyright (c) 2012 by Tomáš Hnyk <tomashnyk2gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import xml.etree.cElementTree as et
import urllib
import os

playlistPath = os.path.expanduser('~/.local/share/rhythmbox/playlists.xml')
#rhythmboxLibraryPath = os.path.expanduser('~/Music') 
rhythmboxLibraryPath = '/home/drew/Hudba' 
rhythmboxPlaylistName = 'Oblibene'
n900LibraryPath = '/home/user/MyDocs/Music'

rhythmboxPlaylistFile = open(playlistPath ,"r")
rhythmboxPlaylist = ''.join(rhythmboxPlaylistFile.readlines())
rhythmboxPlaylistFile.close() 
n900playlistFile = open('' + rhythmboxLibraryPath + '/' + rhythmboxPlaylistName + '.m3u' ,'w+')

tree=et.fromstring(rhythmboxPlaylist) 
for i in tree.findall('playlist'):
    if i.get('name') == rhythmboxPlaylistName:
        for j in  i.findall('location'):
            n900playlistFile.write(urllib.url2pathname(j.text)[7:].replace(rhythmboxLibraryPath, n900LibraryPath) + '\n')
n900playlistFile.close()
