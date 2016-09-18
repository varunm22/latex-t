#!/bin/bash
# You start with an array of 0's and 1's. Using this, we want to output the ranges of each block of 1's in 
#horizontally sorted order. For the basic level, this is sufficient. 

#This means floodfilling for every 1 block, and then getting the upper, lower, horizontal, and vertical
from argparse import ArgumentParser
import numpy as np
import Queue
import scipy.misc
import os

MIN_CHARACTER_SIZE = 200
MAX_HEIGHT = 720
MAX_WIDTH = 960

#counter = 0
visited = np.zeros(shape=(MAX_HEIGHT,MAX_WIDTH),dtype=int)

def floodfill(arr):
	arr_shape = arr.shape
	image_height=arr_shape[0]
	image_width=arr_shape[1]
	
	os.system('rm -r outputimages')
	os.system('rmdir outputimages')
	os.system('mkdir outputimages')
	
	
	characters = []
	count = 1
	for i in xrange(image_height):
		for j in xrange(image_width):
			#print visited[i,j]
			if ((visited[i,j]==0) and (arr[i,j]==1)):
				chartuple = DFS(i,j,count,arr)
				characters.append(chartuple)
				count +=1
			visited[i,j]=1
				

	print len(characters)
	return characters
	

#Yes, I know this is a BFS. 

def DFS(i,j,counter,arr):
	#print i,j

	block = []

	dfs = Queue.Queue()
	dfs.put((i,j))
	visited[i,j] = 1

	max_x=0
	max_y=0
	min_x=arr.shape[1]
        min_y=arr.shape[0]

	character_size = 0
	
	while dfs.empty() is False:
		current = dfs.get()
		#print current
		character_size += 1
	
		if ((arr[current[0]+1,current[1]]==1) and (visited[current[0]+1,current[1]]==0)):
			dfs.put((current[0]+1,current[1]))
			visited[current[0]+1,current[1]] = 1
			block.append((current[0]+1,current[1]))	
		if ((arr[current[0]-1,current[1]]==1) and (visited[current[0]-1,current[1]]==0)):
			dfs.put((current[0]-1,current[1]))
			visited[current[0]-1,current[1]] = 1
			block.append((current[0]-1,current[1]))
		if ((arr[current[0],current[1]+1]==1) and (visited[current[0],current[1]+1]==0)):
			dfs.put((current[0],current[1]+1))
			visited[current[0],current[1]+1] = 1
			block.append((current[0],current[1]+1))
		if ((arr[current[0],current[1]-1]==1) and (visited[current[0],current[1]-1]==0)):
			dfs.put((current[0],current[1]-1))
			visited[current[0],current[1]-1] = 1
			block.append((current[0],current[1]-1))
		
		max_x=max(max_x,current[0])
		max_y=max(max_y,current[1])
		min_x=min(min_x,current[0])
		min_y=min(min_y,current[1])


	if character_size>=MIN_CHARACTER_SIZE:
		out_array = np.ones(shape=(max_x-min_x+1,max_y-min_y+1),dtype=int)
		for k in xrange(len(block)):
			out_array[block[k][0]-min_x,block[k][1]-min_y]=0
		outstring = 'outputimages/outfile'+str(counter)+'.png'
		scipy.misc.imsave(outstring, out_array)
	print character_size
	bottom_corner = (min_x,min_y)
	top_corner = (max_x,max_y)
	return (bottom_corner,top_corner)

		
		
	
			
	
