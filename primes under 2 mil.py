#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 08:47:05 2017

@author: Pranavtadepalli
"""
import primesieve
primes = primesieve.generate_primes(2000000)
print(sum(primes))