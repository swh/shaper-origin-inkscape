#!/usr/bin/env python
# coding=utf-8
#
# Copyright (C) [YEAR] [YOUR NAME], [YOUR EMAIL]
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
"""
Description of this extension
"""

import sys

import inkex

inkex.NSS["shaper"] = "http://www.shapertools.com/namespaces/shaper"

class ShaperOriginExtension(inkex.EffectExtension):
    """Please rename this class, don't keep it unnamed"""
    def add_arguments(self, pars):
        pars.add_argument("--pocketing", type=inkex.Boolean, default=False, help="Convert to pocketing cut")
        pars.add_argument("--online", type=inkex.Boolean, default=False, help="Convert to on line cut")
        pars.add_argument("--exterior", type=inkex.Boolean, default=False, help="Convert to exterior cut")
        pars.add_argument("--interior", type=inkex.Boolean, default=False, help="Convert to interior cut")
        pars.add_argument("--guide", type=inkex.Boolean, default=False, help="Convert to guide")
        pars.add_argument("--set-depth-mm", type=inkex.Boolean, default=False, help="Convert to guide")
        pars.add_argument("--depth", type=str, default="1", help="Set cut depth")

    def effect(self):
        if self.options.set_depth_mm:
            depth = str(round(float(self.options.depth), 1))+'mm'

        for elem in self.svg.selection:
            if self.options.pocketing:
                elem.style.set_color('white', 'stroke')
                elem.style['fill'] = 'grey'
                elem.style['fill-opacity'] = 1
                elem.style['opacity'] = 1
            elif self.options.online:
                elem.style.set_color('grey', 'stroke')
                elem.style['fill'] = 'white'
                elem.style['fill-opacity'] = 0
                elem.style['opacity'] = 1
            elif self.options.exterior:
                elem.style.set_color('black', 'stroke')
                elem.style['fill'] = 'black'
                elem.style['fill-opacity'] = 1
                elem.style['opacity'] = 1
            elif self.options.interior:
                elem.style.set_color('black', 'stroke')
                elem.style['fill'] = 'white'
                elem.style['fill-opacity'] = 1
                elem.style['opacity'] = 1
            elif self.options.guide:
                elem.style.set_color('blue', 'stroke')
                elem.style['fill'] = 'blue'
                elem.style['fill-opacity'] = 1
                elem.style['opacity'] = 1
            elif self.options.set_depth_mm:
                elem.set("shaper:cutDepth", depth)

if __name__ == '__main__':
    ShaperOriginExtension().run()

