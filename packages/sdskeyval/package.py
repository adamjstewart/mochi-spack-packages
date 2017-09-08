##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Sdskeyval(AutotoolsPackage):
    """a library that provides a Margo-based keyval service"""

    homepage = "https://xgitlab.cels.anl.gov/sds/sds-keyval"

    version('master', git='https://xgitlab.cels.anl.gov/sds/sds-keyval.git')

    depends_on('margo', type=("build", "link", "run"))
    depends_on('mercury', type=("build", "link", "run"))
    depends_on('argobots')
    depends_on('abtsnoozer')
    depends_on('libev')
    depends_on('autoconf@2.65:')
    depends_on('automake@1.15:')
    depends_on('libtool', type=("build"))

    # requires c++11
    conflicts('%gcc@:4.8.0')
    # clang fullly implemented C++11 in 3
    # intel implemented c++11 in 13.0
    # but neither clang nor intel compile the BwTree data structure
    conflicts('%clang')
    conflicts('%intel')