# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def order(name, sell_in, quality):
        if name == "Aged Brie":
            return AgedBrie(name, sell_in, quality)
        if name == "Sulfuras, Hand of Ragnaros":
            return Sulfuras(name, sell_in, quality)
        if name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePasses(name, sell_in, quality)
        # if name == "Conjured":
        #     return Conjured(name, sell_in, quality) # TODO implement conjured class
        else:
            return Item(name, sell_in, quality)

    def update_quality(self):
        for item in self.items:
            item.day()

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    
    def day(self):
        self.sell_in -= 1 # should this be at the end?
        if 50 > self.quality > 0:
            if self.sell_in <= 0:
                self.quality -= 2
            else:
                self.quality -= 1


class AgedBrie(Item):
    def day(self):
        self.sell_in -= 1
        if 50 > self.quality > 0:
            self.quality += 1


class Sulfuras(Item):
    def day(self):
        return


class BackstagePasses(Item):
    def day(self):
        self.sell_in -= 1
        if 50 > self.quality:
            if self.sell_in <= 0:
                self.quality == 0
            elif 5 >= self.sell_in > 0:
                self.quality += 3
            elif 10 >= self.sell_in > 5:
                self.quality += 2
            else:
                self.quality += 1
