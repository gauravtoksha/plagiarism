# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 02:07:38 2018

@author: windows
"""
##work in progress

class Similarity():
    
    
    def __init__(self,searchQ,page,measure="default"):
        self.searchQ=searchQ.split(".")
        self.page=page.split(".")
        self.measure=measure
    
    def run(self):
        if self.measure=='default':
            self.default()
    
    def default(self):
        matches=[]
        for searchline in self.searchQ:
            for pageline in self.page:
                if searchline in pageline:
                    print("found one match:"+pageline)
                    matches.append(pageline)
                    break
        print(matches)
        return matches
    
    def someOtherMeasure(self):
        pass