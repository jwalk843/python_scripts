#!/usr/bin/python3

class Ship:

    nautical_miles = 0

    def __init__(self, hull, beam, draft):
        self.hull = hull
        self.beam = beam
        self.draft = draft
        
    def __str__(self):
        pass

    def __repr__(self):
        pass

    def sail(self, nautical_miles):
        pass

    def play_gq(self, reason, oneMC):
        print(reason)
        return oneMC