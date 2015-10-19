# Part of the PsychoPy library
# Copyright (C) 2015 Jonathan Peirce
# Distributed under the terms of the GNU General Public License (GPL).

#--------------------------------------------------------------------------
#This file is automatically generated during build (do not edit directly).
#--------------------------------------------------------------------------

import os, sys

#version info for PsychoPy
__version__='1.83.01'
__license__='GNU GPLv3 (or more recent equivalent)'
__author__='Jonathan Peirce'
__author_email__='jon@peirce.org.uk'
__maintainer_email__='psychopy-dev@googlegroups.com'
__users_email__='psychopy-users@googlegroups.com'
__url__='http://www.psychopy.org'
__downloadUrl__='https://github.com/psychopy/psychopy/releases/'
__git_sha__='n/a'
__build_platform__='n/a'

__all__ = ["gui", "misc", "visual", "core", "event", "data", "filters", "sound"]

#for developers the following allows access to the current git sha from their repository
if __git_sha__=='n/a':
    import subprocess
    #see if we're in a git repo and fetch from there
    try:
        thisFileLoc = os.path.split(__file__)[0]
        output = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'],
                                         cwd=thisFileLoc, stderr=subprocess.PIPE)
    except:
        output=False
    if output:
        __git_sha__ = output.strip()#remove final linefeed

#update preferences and the user paths
from psychopy.preferences import prefs
import sys
for pathName in prefs.general['paths']:
    sys.path.append(pathName)

from psychopy.tools.versionchooser import useVersion

