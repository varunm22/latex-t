#!/bin/bash
# You start with an array of 0's and 1's. Using this, we want to output the ranges of each block of 1's in 
#horizontally sorted order. For the basic level, this is sufficient. 

#This means floodfilling for every 1 block, and then getting the upper, lower, horizontal, and vertical
from argparse import ArgumentParser
import numpy as np
import Queue

MIN_CHARACTER_SIZE = 120

if __name__ == "__main__":
	arr_shape = arr.shape
	image_height=arr_shape[0]
	image_width=arr_shape[1]
	
	visited = np.zeros(shape=(image_height,image_width),dtype=bool)

	characters = []
	for i in xrange(image_width):
		for j in xrange(image_height):
			if visited[i,j] is 0:
				chartuple = floodfill(i,j,visited,arr)
				if (chartuple[2]-chartuple[0])*(chartuple[3]-chartuple[1]) >= MIN_CHARACTER_SIZE:
					characters.append(chartuple)
	return characters
	

def floodfill(i,j,visited,arr):
	dfs = Queue()
	dfs.put((i,j))
	visited[i,j] = 1

	max_x=0
	max_y=0
	min_x=arr_shape[0]
        min_y=arr_shape[1]

	character_size = 0

	while dfs.empty() is False:
		current = dfs.get()
		character_size += 1

		if (arr[i+1,j] is 1) and (visited[i+1,j] is 0):
			dfs.put((i+1,j))
			visited[i+1,j] = 1	
		if (arr[i-1,j] is 1) and (visited[i-1,j] is 0):
			dfs.put((i,j+1))
			visited[i
		if (arr[i,j+1] is 1) and (visited[i,j+1] is 0):
			dfs.put((i-1,j))
		if (arr[i,j-1] is 1) and (visited[i,j-1] is 0):
			dfs.put((i,j-1))
		

		max_x=max(max_x,current[0])
		max_y=max(max_y,current[1])
		min_x=min(min_x,current[0])
		min_y=min(min_y,current[1])
	
	return (min_x, min_y, max_x, max_y)
				
		
		
	
			
	
