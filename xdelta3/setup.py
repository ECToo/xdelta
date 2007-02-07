# xdelta 3 - delta compression tools and library
# Copyright (C) 2004, 2007.  Joshua P. MacDonald
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#
from distutils.core import setup, Extension
from distutils.util import get_platform

# External compression support works on Windows/Cygwin, but not from
# within the Python module. It's something to do with fork() and
# exec() support.
platform  = get_platform()
is_cygwin = platform.startswith('cygwin')
extcomp   = 1

if is_cygwin:
    print 'Note: not compiling external compression support for Python/Cygwin'
    extcomp = 0
#end

xdelta3_ext = Extension('xdelta3main',
                        ['xdelta3.c'],
                        define_macros = [
                                         ('PYTHON_MODULE',1),
                                         ('SECONDARY_DJW',1),
                                         ('VCDIFF_TOOLS',1),
                                         ('XD3_POSIX',1),
                                         ('XD3_USE_LARGEFILE64',1),

                                         ('EXTERNAL_COMPRESSION',extcomp),

                                         ('REGRESSION_TEST',0),
                                         ('SECONDARY_FGK',0),
                                         ('XD3_DEBUG',0),
                                         ],
                        extra_compile_args = [ '-O3',
                                               '-g',
                                               '-funroll-loops',
                                               ])

# $Format: "REL='$Xdelta3Version$'" $
REL='0n'

# This provides xdelta3.main(), which calls the xdelta3 command-line main()
# from python.
setup(name='xdelta3main',
      version=REL,
      ext_modules=[xdelta3_ext])