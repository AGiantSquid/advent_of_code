def power_level(x, y, serial_number=1955):
  rack_id = x + 10
  power_level_start = rack_id * y
  power_level_plus_serial = power_level_start + serial_number
  power_level_multiplied_by_rack_id = power_level_plus_serial * rack_id
  hundreds_level_of_power_id = power_level_multiplied_by_rack_id // 100 % 10
  final_power = hundreds_level_of_power_id - 5
  return final_power

assert power_level(3, 5, 8) == 4
assert power_level(217,196, 39) == 0
assert power_level(122, 79, 57) == -5
assert power_level(101, 153, 71) == 4


GRID_SIZE = 300


def get_upper_left_coords_of_max_power(serial_number, grid_size=3):
  power_dict = {
    (x, y): power_level(x, y, serial_number)
    for x in range(1, GRID_SIZE + 1) for y in range(1, GRID_SIZE + 1)
  }
  # print(power_dict)

  three_by_three = {
    (x, y): sum([
        power_dict[(x + i, y + j)]
        for i in range(grid_size) for j in range(grid_size)
      ])
      for x, y in power_dict
      if x + 2 <= GRID_SIZE and y + 2 <= GRID_SIZE
  }
  # print(three_by_three)

  result = max(three_by_three, key=three_by_three.get)
  return '{},{}'.format(result[0], result[1])


assert get_upper_left_coords_of_max_power(18) == '33,45'
assert get_upper_left_coords_of_max_power(42) == '21,61'

print(get_upper_left_coords_of_max_power(1955))
