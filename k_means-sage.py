from random import sample as rand
from math import sqrt


def init_centroids(L, K):
	centroids = rand(L, K)
	return centroids

def calculate_distance(p, c):
	distance = sqrt((p[0] - c[0]) ** 2 + (p[1] - c[1]) ** 2)
	return distance

def group_points(L, C):
	setList = []
	for _ in range(len(C)):
		setList.append([])
	for p in L:
		min_dist = 999999
		set = []
		for i in range(len(C)):
			dist = calculate_distance(p, C[i])
			if dist < min_dist:
				min_dist = dist
				set = setList[i]
		set.append(p)
	return setList

def calculate_centroids(S):
		new_centroids = []
		for s in S:
				s_len = float(len(s))
				if s:
						mean_x = sum(point[0] for point in s) / s_len
						mean_y = sum(point[1] for point in s) / s_len
						new_centroids.append((mean_x, mean_y))
				else:
						new_centroids.append((0, 0))
		return new_centroids

def k_means(L, K):
	if K < 0 or K > len(L):
		print("Invalid K value")
		exit(1)
	S = []
	finish = False
	C = init_centroids(L, K)
	while finish == False:
		S = group_points(L, C)
		NC = calculate_centroids(S)
		if NC == C:
			finish = True
		C = NC
	return S


K = 2
L = [(0, 0),(3, 2),(1, 2.5),(2, 2),(5, 1),(1, 1)]

S = k_means(L, K)
print("Sets:")
for s in S:
	print(s)
