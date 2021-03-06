import unittest
import config
from player import Player
from map import Map
from room import Room
from item import Item

class PlayerTestCase(unittest.TestCase):
	def assert_location_equal(self, p, location):
		self.assertEqual(p.location, location)

<<<<<<< HEAD
=======
	def assert_search_string_equal(self, p, string):
		self.assertEqual(p.search(), string)

	def assert_get_item_string_equal(self, p, string):
		self.assertEqual(p.getItem('key'), string)
		
	def assert_use_item_string_equal(self, p, string):
		self.assertEqual(p.useItem('key',2), string)

>>>>>>> master
class PlayerTest(PlayerTestCase):
	def test_move_into_wall(self):
		config.map = Map()
		config.map.randomConnectedMap()
		p = Player(0)
		p.location = [0,0]
		config.pL.append(p)
		p.move(0,False)
		self.assert_location_equal(p, [0,0])

	def test_move_into_door(self):
		config.map = Map()
		config.map.randomConnectedMap()
		config.map.layout[0][0].adjacencyList = [0,0,2,0]
		config.map.addRoom(1,0,Room())
		config.map.layout[1][0].adjacencyList = [2,0,0,0]
		p = Player(0)
		p.location = [0,0]
		config.pL.append(p)
		p.move(2,False)
		self.assert_location_equal(p, [0,0])

	def test_move_into_room(self):
		config.map = Map()
		config.map.randomConnectedMap()
		config.map.layout[0][0].adjacencyList = [0,0,1,0]
		config.map.addRoom(1,0,Room())
		config.map.layout[1][0].adjacencyList = [1,0,0,0]
		p = Player(0)
		p.location = [0,0]
		config.map.layout[0][0].playerList.append(p)
		config.pL.append(p)
		p.move(2,False)
		self.assert_location_equal(p, [1,0])

	def search_empty_room(self):
		pass

	def search_room_with_item(self):
		pass

	def get_item_from_empty_room(self):
		pass

	def get_item_from_room_with_item(self):
		pass

	def use_item_with_empty_inventory(self):
		pass

	def test_use_item_on_door(self):
		config.map = Map()
		config.map.randomConnectedMap()
		config.map.layout[0][0].adjacencyList = [0,0,2,0]
		config.map.addRoom(1,0,Room())
		config.map.layout[1][0].adjacencyList = [2,0,0,0]
		p = Player(0)
		p.location = [0,0]
		config.map.layout[0][0].playerList.append(p)
		config.pL.append(p)
		key = Item(1,"key")
		p.inventory.append(key)
		p.useItem("key",2)
		p.move(2,True)
		self.assert_location_equal(p, [1,0])

	def test_use_item_on_door_without_item(self):
		config.map = Map()
		config.map.randomConnectedMap()
		config.map.layout[0][0].adjacencyList = [0,0,2,0]
		config.map.addRoom(1,0,Room())
		config.map.layout[1][0].adjacencyList = [2,0,0,0]
		p = Player(0)
		p.location = [0,0]
		config.map.layout[0][0].playerList.append(p)
		config.pL.append(p)
<<<<<<< HEAD
		p.useItem("key",2)
		p.move(2,False)
		self.assert_location_equal(p, [0,0])
=======
		self.assert_use_item_string_equal(p, "Inventory is empty")

>>>>>>> master
