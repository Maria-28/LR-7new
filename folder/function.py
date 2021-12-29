#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def outside(q, r):
    def inside(l):
        s = l.replace(q, r)

        return s
    return inside(l)