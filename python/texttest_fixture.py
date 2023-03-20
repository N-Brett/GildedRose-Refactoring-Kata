# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import GildedRose

if __name__ == "__main__":
    print("OMGHAI!")
    items = [
            GildedRose.order(name="+5 Dexterity Vest", sell_in=10, quality=20),
            GildedRose.order(name="Aged Brie", sell_in=2, quality=0),
            GildedRose.order(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),  # noqa E501
            GildedRose.order(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),  # noqa E501
            GildedRose.order(name="Elixir of the Mongoose", sell_in=5, quality=7),  # noqa E501
            GildedRose.order(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),  # noqa E501
            GildedRose.order(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),  # noqa E501
            GildedRose.order(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),  # noqa E501
            GildedRose.order(name="Conjured Mana Cake", sell_in=3, quality=6),  # noqa E501
            ]

    days = 2
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_quality()
