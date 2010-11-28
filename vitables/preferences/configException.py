# -*- coding: utf-8 -*-
#!/usr/bin/env python

#       Copyright (C) 2005-2007 Carabos Coop. V. All rights reserved
#       Copyright (C) 2008-2010 Vicent Mas. All rights reserved
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#       Author:  Vicent Mas - vmas@vitables.org

"""
This module defines an Exception to be used when there is a problem 
reading/writting the ``ViTables`` configuration.
"""

__docformat__ = 'restructuredtext'
_context = 'ConfigFileIOException'

from PyQt4 import QtGui


def trs(source, comment=None):
    """Translate string function."""
    return unicode(QtGui.qApp.translate(_context, source, comment))


class ConfigFileIOException(Exception):
    """Exception class for IO errors in the configuration file.

    :Parameter key:
        the configuration file key that cannot be read/written
    """

    def __init__(self, key):
        """Setup the configuration error messages that will be shown to user.
        """

        Exception.__init__(self)
        # If key looks like /path/to/property=value a write exception is
        # raised. If not a read exception is raised
        if '=' in key:
            setting = key.split('=')[0]
            self.error_message = trs(\
                """\nConfiguration error: the application setting """\
                """%s cannot be saved.""",
                'A logger error message')  % setting
        else:
            self.error_message = trs(\
                """\nConfiguration warning: the application setting """\
                """%s cannot be read. Its default value will be used.""",
                'A logger error message')  % key
