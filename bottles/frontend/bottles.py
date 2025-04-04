#!@PYTHON@

# bottles.in
#
# Copyright 2020 brombinmirko <send@mirko.pm>
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

import os
import sys
import signal
import gettext

APP_VERSION = "@APP_VERSION@"
pkgdatadir = "@pkgdatadir@"
localedir = "@localedir@"
# noinspection DuplicatedCode
data_gresource_path = f"{pkgdatadir}/data.gresource"
bottles_gresource_path = f"{pkgdatadir}/bottles.gresource"
sys.path.insert(1, pkgdatadir)

# Remove GTK_THEME variable to prevent breakages
# REF: https://github.com/bottlesdevs/Bottles/pull/2886
os.unsetenv("GTK_THEME")

signal.signal(signal.SIGINT, signal.SIG_DFL)
gettext.install("bottles", localedir)

if __name__ == "__main__":
    from gi.repository import Gio

    data_resource = Gio.Resource.load(data_gresource_path)
    bottles_resource = Gio.Resource.load(bottles_gresource_path)
    # noinspection PyProtectedMember
    data_resource._register()
    bottles_resource._register()

    from bottles.frontend import main

    sys.exit(main.main(APP_VERSION))
