from math import sqrt
from csv import reader


def read_csv_file(input_path: str) -> list[list[str]]:
	try:
		file = open(input_path, "r")
		return list(reader(file))
	finally:
		file.close()

def write_list_file(output_path: str, groups: list[list[int]]) -> None:
	try:
		file = open(output_path, "w")
		for group in groups:
			file.write(", ".join(map(str, sorted(group))))
			file.write("\n")
	finally:
		file.close()

def read_points(input_path: str) -> dict[int, list[float]]:
	points: dict[int, list[float]] = {}
	csv_data = read_csv_file(input_path)

	for point_id, row in enumerate(csv_data, start=1):
			dimensions = [float(coord) for coord in row]
			points[point_id] = dimensions

	return points

def euclidean_distance(p1: list[float], p2: list[float]) -> float:
	if len(p1) != len(p2):
		raise ValueError("Os pontos devem ter o mesmo número de dimensões.")
	dimensions_distance = [((x - y) ** 2) for x, y in zip(p1, p2)]
	return sqrt(sum(dimensions_distance))

def find_closest_point(current_point: int, points: dict[int, list[float]], used_points: set) -> tuple[int, float]:
	infinity = float('inf')
	min_distance: float = infinity
	closest_point: int = -1

	for point_id, dimensions in points.items():
		if point_id not in used_points:
			distance = euclidean_distance(points[current_point], dimensions)
			is_closer_distance: bool = distance < min_distance
			is_same_distance_and_closer_id: bool = distance == min_distance and point_id < closest_point
			if is_closer_distance or is_same_distance_and_closer_id:
				min_distance = distance
				closest_point = point_id

	return closest_point, min_distance

def build_links(points: dict[int, list[float]]) -> list[tuple[int, int, float]]:
	links: list[tuple[int, int, float]] = []
	current_point: int = 1
	used_points: set[int] = {1}

	while len(used_points) < len(points):
		next_point, distance = find_closest_point(current_point, points, used_points)
		links.append((current_point, next_point, distance))
		used_points.add(next_point)
		current_point = next_point

	return links

def dfs(visited: set[int], adjacency: dict[int, list], node: int, current_group: list[int]):
	visited.add(node)
	current_group.append(node)
	for neighbor in adjacency[node]:
		if neighbor not in visited:
			dfs(visited, adjacency, neighbor, current_group)

def split_groups(links: list[tuple[int, int, float]], k: int) -> list[list[int]]:
	# caso K seja menor ou igual a 1, retorna todos os pontos em um único grupo
	if k <= 1:
		all_points_set = set()
		for link in links:
			all_points_set.add(link[0])
			all_points_set.add(link[1])
		return [list(all_points_set)]
	# caso K seja maior ou igual ao número de links + 1, retorna cada ponto em um grupo separado
	if k >= len(links) + 1:
		single_point_set = set()
		for link in links:
			single_point_set.add(link[0])
			single_point_set.add(link[1])
		return [[point] for point in sorted(single_point_set)]

	# ordena os links pela distância (x[2]) em ordem decrescente
	dist_sorted_links = sorted(links, key=lambda x: x[2], reverse=True)
	# seleciona os K-1 links mais proximos
	links_to_keep = dist_sorted_links[k-1:]

	adjacency: dict[int, list[int]] = {}
	all_points: set[int] = set()

	for link in links:
		all_points.add(link[0])
		all_points.add(link[1])

	for point in all_points:
		adjacency[point] = []
	for link in links_to_keep:
		adjacency[link[0]].append(link[1])
		adjacency[link[1]].append(link[0])

	visited: set[int] = set()
	groups: list[list[int]] = []

	for point in sorted(all_points):
		if point not in visited:
			current_group: list[int] = []
			dfs(visited, adjacency, point, current_group)
			groups.append(current_group)

	return groups

def main(input_file: str, output_file: str, k: int) -> None:
	points = read_points(input_file)
	links = build_links(points)
	groups = split_groups(links, k)

	print("Agrupamentos:")
	for group in groups:
		print(", ".join(map(str, sorted(group))))
	write_list_file(output_file, groups)

if __name__ == "__main__":
	input_file: str = input("Forneca o nome do arquivo de entrada: ")
	output_file: str = input("Forneca o nome do arquivo de saida: ")
	group_size: str = input("Forneca o número de grupos (K): ")
	main(input_file, output_file, int(group_size))
