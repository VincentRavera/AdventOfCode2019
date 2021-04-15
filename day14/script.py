#!/usr/bin/env python3
# coding: utf-8
import re
from collections import defaultdict


class Recipe:
	def __init__(self, output, inputs):
		outs = re.split(' ', output)
		self.quantity = int(outs[0])
		self.type = outs[1]
		self.materials = dict()
		for i in inputs:
			input_item = re.split(' ', i)
			self.materials[input_item[1]] = int(input_item[0])


def parse_recipe(path):
	with open(path) as f:
		g = f.readlines()
	output = dict()
	for line in g:
		product = re.split(' => ', line)
		material = re.split(', ', product[0])
		recipe_of_type = Recipe(str.strip(product[1]), material)
		output[recipe_of_type.type] = recipe_of_type
	return output


def fetch_upper(recipe, counter, waste, material, quantity):
	if material == 'ORE':
		counter[material] += quantity
		return quantity
	ratio = 0
	while recipe[material].quantity * ratio < quantity - waste[material]:
		ratio += 1
	outputs = 0
	counter[material] += recipe[material].quantity * ratio
	waste[material] += recipe[material].quantity * ratio - quantity
	# print('Producing ', quantity, material, " time ", ratio)
	# for resources_type, resources_quant in recipe[material].materials.items():
	# print("Need ", resources_quant, resources_type, " times ", ratio)
	for resources_type, resources_quant in recipe[material].materials.items():
		outputs += fetch_upper(recipe, counter, waste, resources_type, resources_quant * ratio)
	return outputs


def get_ORE_for_FUEL(recipe):
	counter = defaultdict(lambda: 0)
	waste = defaultdict(lambda: 0)
	return fetch_upper(recipe, waste, counter, 'FUEL', 1)


def get_ORE_for_X_FUEL(recipe, fuel=0):
	print("\r", fuel)
	fuel -= 1
	counter = defaultdict(lambda: 0)
	waste = defaultdict(lambda: 0)
	ore = fetch_upper(recipe, waste, counter, 'FUEL', fuel)
	return ore


def dicothomy(recipe):
	final_ore = 1000000000000
	euristic = get_ORE_for_FUEL()
	init_value = final_ore/euristic




def test_p1(path, output):
	recipe = parse_recipe(path)
	if not get_ORE_for_FUEL(recipe) == output:
		print("Test p1 failed: ", path)
	else:
		print("Test p1 Successed: ", path)


def test_p2(path, output):
	recipe = parse_recipe(path)
	#if not get_FUEL_for_ORE(recipe) == output:
	#	print("Test p2 failed: ", path)


if __name__ == '__main__':
	test_p1('test_1.txt', 165)
	test_p1('test_2.txt', 13312)
	test_p2('test_2.txt', 82892753)
	test_p1('test_3.txt', 180697)
	test_p2('test_3.txt', 5586022)
	test_p1('test_4.txt', 2210736)
	test_p2('test_4.txt', 460664)
	final_recipe = parse_recipe('inputs.txt')
	print(get_ORE_for_FUEL(final_recipe))
