#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 18:04:39 2017

@author: Pranavtadepalli
"""

class say:
    def this(text_to_say):
        import os
        os.system("say "+text_to_say)
say=say()
say.this("IT WORKED")