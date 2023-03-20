# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose


class GildedRoseNormalItemsTest(unittest.TestCase):
    def test_foo(self):
        item = [GildedRose.order("foo", 0, 0)]
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual("foo", item[0].name)

    def test_item_sell_in_decreased(self):
        item = [GildedRose.order("Healing Potion", 10, 10)]
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(9, item[0].sell_in)

    def test_normal_item_quality_before_sell_date(self):
        item = [GildedRose.order("Bread", 10, 10)]
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(9, item[0].quality)
        self.assertEqual(9, item[0].sell_in)

    def test_normal_item_quality_after_sell_date(self):
        item = [GildedRose.order("Ale", 0, 10)]
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(8, item[0].quality)

    def test_quality_not_negative(self):
        item = [GildedRose.order("Cheddar", 0, 0)]
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(0, item[0].quality)


class GildedRoseSpecialItemsTest(unittest.TestCase):
    def test_aged_brie(self):
        item = [GildedRose.order("Aged Brie", 10, 10)]
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(11, item[0].quality)

    def test_sulfuras(self):
        item = [GildedRose.order("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(80, item[0].quality)

    def test_backstage_pass_sell_in_more_ten_days(self):
        item = [GildedRose.order("Backstage passes to a TAFKAL80ETC concert", 15, 10)]  # noqa E501
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(11, item[0].quality)

    def test_backstage_pass_sell_in_ten_days(self):
        item = [GildedRose.order("Backstage passes to a TAFKAL80ETC concert", 10, 10)]  # noqa E501
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(12, item[0].quality)

    def test_backstage_pass_sell_in_six_days(self):
        item = [GildedRose.order("Backstage passes to a TAFKAL80ETC concert", 6, 10)]  # noqa E501
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(12, item[0].quality)

    def test_backstage_pass_sell_in_five_days(self):
        item = [GildedRose.order("Backstage passes to a TAFKAL80ETC concert", 5, 10)]  # noqa E501
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(13, item[0].quality)

    def test_backstage_pass_sell_in_one_day(self):
        item = [GildedRose.order("Backstage passes to a TAFKAL80ETC concert", 1, 10)]  # noqa E501
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(13, item[0].quality)

    def test_backstage_pass_sell_in_zero(self):
        item = [GildedRose.order("Backstage passes to a TAFKAL80ETC concert", 0, 10)]  # noqa E501
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(0, item[0].quality)

    def test_conjured_items_before_sell_in(self):
        item = [GildedRose.order("Conjured Mana Cake", 10, 10)]
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(8, item[0].quality)

    def test_conjured_items_after_sell_in(self):
        item = [GildedRose.order("Conjured Mana Cake", 0, 10)]
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(6, item[0].quality)


if __name__ == '__main__':
    unittest.main()
