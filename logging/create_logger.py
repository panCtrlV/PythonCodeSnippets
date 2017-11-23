# -*- coding: utf-8 -*-
# @Author: panc25
# @Date:   2017-11-23 13:03:04
# @Last Modified by:   Pan Chao
# @Last Modified time: 2017-11-23 13:03:23

import logging

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('sh_fzb.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)