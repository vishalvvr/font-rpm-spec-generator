# template.py
# Copyright (C) 2022 Red Hat, Inc.
#
# Authors:
#   Akira TAGOH  <tagoh@redhat.com>
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

from jinja2 import Environment, FileSystemLoader
from pathlib import Path

def get(npkgs, data):
    ptempl = Path(__file__).resolve().parents[0].with_name('template')
    env = Environment(loader=FileSystemLoader(str(ptempl)))
    template = {}

    if npkgs == 1:
        template['spec'] = env.get_template('spectemplate-fonts-simple.spec').render(data)
    else:
        template['spec'] = env.get_template('spectemplate-fonts-multi.spec').render(data)

    return template
