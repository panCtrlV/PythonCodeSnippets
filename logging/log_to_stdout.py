# -*- coding: utf-8 -*-
# @Author: Pan Chao
# @Date:   2018-05-11 22:27:19
# @Last Modified by:   Pan Chao
# @Last Modified time: 2018-05-11 22:27:53

'''Creating a python logger to stdout

Ref: https://coderwall.com/p/_fg97w/creating-a-python-logger-to-stdout
'''

import logging
import sys
log = logging.getLogger(__name__)
out_hdlr = logging.StreamHandler(sys.stdout)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
out_hdlr.setLevel(logging.INFO)
log.addHandler(out_hdlr)
log.setLevel(logging.INFO)

# Then you can do:

log.debug("NO")
log.error("THIS IS AN ERROR")