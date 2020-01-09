#!/usr/bin/env python3

# Copied basically from DotWatch-Website project (older)

import sys

#sys.path.insert(0, '/home/siteuser/DotWatch')

from . import create_app # from __init__.py

if __name__ == '__main__':
	application = create_app()
	
	application.run()