#! /usr/bin/env python3

from immutables import Map

ORIENTATION_MAPPING = {
  '^': 0,
  '>': 1,
  'v': 2,
  '<': 3,
}


def read_file(file_name):
  with open(file_name, 'r') as f:
    cart_file = f.read()
  return cart_file


def get_coordinates_of_first_collision(cart_file):
  """Return the x,y coordinates of the first cart collision as a tuple."""
  initial_cart_map = load_cart_file(cart_file)
  carts = get_carts_from_cart_map(initial_cart_map)
  map_with_carts_removed = get_cart_map(initial_cart_map)
  collision_coords = run_ticks_until_collision(carts, map_with_carts_removed)
  return collision_coords


def get_coordinates_of_last_cart(cart_file):
  initial_cart_map = load_cart_file(cart_file)
  carts = get_carts_from_cart_map(initial_cart_map)
  map_with_carts_removed = get_cart_map(initial_cart_map)



def load_cart_file(cart_file):
  """Return cart file divided into list of lists"""
  return tuple([create_list_of_cart_tracks(row) for row in cart_file.splitlines()])


def create_list_of_cart_tracks(row):
  """Convert all spaces to None."""
  return tuple([char if char != ' ' else None for char in row])


def get_carts_from_cart_map(cart_map):
  """Return a list of dictionaries that describe the carts found in the map file."""
  unmoved_carts = ()
  for y_coord, row in enumerate(cart_map):
    for x_coord, item in enumerate(row):
      if item in ORIENTATION_MAPPING.keys():
        unmoved_cart = Map({
          "coords": (x_coord, y_coord),
          "orientation": ORIENTATION_MAPPING[item],
          "turn_choice": -1,
        })
        unmoved_carts = (*unmoved_carts, unmoved_cart)
  return unmoved_carts


def get_cart_map(unformatted_cart_map):
  """Return the cart map with the missing track symbols added.

  The initial cart map has cart symbols obfuscating some of the tracks.
  This replaces the unknown tracks with needed symbols."""
  new = tuple([
    tuple([
      replace_cart_with_track_symbol(unformatted_cart_map, (x, y))
      if element in ORIENTATION_MAPPING.keys() else element
      for x, element in enumerate(row)])
      for y, row in enumerate(unformatted_cart_map)
  ])
  return new



def replace_cart_with_track_symbol(cart_map, coords):
  """Return the appropriate track symbol to replace the cart symbol."""
  if intersection(cart_map, coords):
    return "+"
  if vertical(cart_map, coords):
    return "|"
  if horizontal(cart_map, coords):
    return "-"
  if right_angle(cart_map, coords):
    return "/"
  if left_angle(cart_map, coords):
    return '\\'


def intersection(cart_map, coords):
  """Mystery item should be "+" """
  return item_above(cart_map, coords) and \
         item_below(cart_map, coords) and \
         item_right(cart_map, coords) and \
         item_left(cart_map, coords)


def vertical(cart_map, coords):
  """Mystery item should be "|" """
  return item_above(cart_map, coords) and \
         item_below(cart_map, coords)


def horizontal(cart_map, coords):
  """Mystery item should be "-" """
  return item_right(cart_map, coords) and \
         item_left(cart_map, coords)


def right_angle(cart_map, coords):
  """Mystery item should be "/" """
  return (item_above(cart_map, coords) and
         item_left(cart_map, coords)) or \
         (item_below(cart_map, coords) and
         item_right(cart_map, coords))


def left_angle(cart_map, coords):
  r"""Mystery item should be "\" """
  return (item_above(cart_map, coords) and
         item_right(cart_map, coords)) or \
         (item_below(cart_map, coords) and
         item_left(cart_map, coords))


def item_above(cart_map, coords):
  return retrieve_by_coordinates(cart_map, coords_above(coords))


def item_below(cart_map, coords):
  return retrieve_by_coordinates(cart_map, coords_below(coords))


def item_right(cart_map, coords):
  return retrieve_by_coordinates(cart_map, coords_right(coords))


def item_left(cart_map, coords):
  return retrieve_by_coordinates(cart_map, coords_left(coords))


def retrieve_by_coordinates(xymap, coordinates):
  """Return character located at coordinates, or False if something is wrong.

  coordinates come in as x,y tuple. Rows of xymap are considered the y axis,
  and each element in each row are considered the X axis"""
  column, row = coordinates
  try:
    return xymap[row][column]
  except:
    return False


def coords_above(coords):
  x, y = coords
  return x, y + 1

def coords_below(coords):
  x, y = coords
  return x, y - 1

def coords_right(coords):
  x, y = coords
  return x + 1, y

def coords_left(coords):
  x, y = coords
  return x - 1, y


def run_ticks_until_collision(carts, cart_map):
  """Run until a collision happens, then return the coordinates as tuple."""
  try:
    recursively_call_ticks(carts, cart_map)
  except CartCollision as collision:
    return collision.coordinates


def recursively_call_ticks(carts, cart_map):
  """"""
  carts = do_tick(carts, cart_map)
  sorted_unmoved_carts = sorted(
    carts,
    key=lambda x: (x["coords"][0], x["coords"][1]),
  )
  recursively_call_ticks(sorted_unmoved_carts, cart_map)


def do_tick(carts, cart_map):
  """Move each cart, and return their new positions unless a collision happens."""
  moved_carts = []
  collision_points = [cart["coords"] for cart in carts]
  for cart in carts:
    moved_cart = move(cart, cart_map)
    if moved_cart["coords"] in collision_points:
      raise CartCollision(moved_cart["coords"])
    moved_carts.append(moved_cart)
    collision_points.remove(cart["coords"])
    collision_points.append(moved_cart["coords"])
  return moved_carts


def move(cart, cart_map):
  """Return dictionary of updated cart after moving."""
  coordinates = get_updated_coordinates(cart["orientation"], cart["coords"])

  next_symbol = retrieve_by_coordinates(cart_map, coordinates)

  orientation, turn_choice = get_updated_orientation(cart, next_symbol)

  return Map({
    "coords": coordinates,
    "orientation": orientation,
    "turn_choice": turn_choice,
  })


class CartCollision(Exception):
  """Raised when two carts collide"""
  def __init__(self, coordinates):
    self.coordinates = coordinates


def get_updated_coordinates(orientation, coords):
  if orientation == 0:
    return coords_below(coords)
  if orientation == 1:
    return coords_right(coords)
  if orientation == 2:
    return coords_above(coords)
  if orientation == 3:
    return coords_left(coords)


def get_updated_orientation(cart, next_symbol):
  new_orientation = None
  turn_choice = cart["turn_choice"]
  if next_symbol == '/':
    if cart["orientation"] % 2 == 0:
      new_orientation = (cart["orientation"] + 1) % 4
    else:
      new_orientation = (cart["orientation"] - 1) % 4

  elif next_symbol == "\\":
    if cart["orientation"] % 2 == 0:
      new_orientation = (cart["orientation"] - 1) % 4
    else:
      new_orientation = (cart["orientation"] + 1) % 4

  elif next_symbol == '+':
    new_orientation = (cart["orientation"] + turn_choice) % 4
    turn_choice = ((turn_choice + 2) % 3) - 1

  elif next_symbol in ('-', '|'):
    new_orientation = cart["orientation"]

  else:
    print('something went terribly wrong')
    print(next_symbol)

  return new_orientation, turn_choice



if __name__ == '__main__':
  cart_file = read_file('test_data_real.txt')
  import timeit
  collision_coords = get_coordinates_of_first_collision(cart_file)
  # 74,87
  last_cart_coords = get_coordinates_of_last_cart(cart_file)
  print(collision_coords)

  print(
    timeit.timeit("get_coordinates_of_first_collision(cart_file)",
    setup="""from __main__ import get_coordinates_of_first_collision, read_file
cart_file = read_file('test_data_real.txt')""", number=1000))