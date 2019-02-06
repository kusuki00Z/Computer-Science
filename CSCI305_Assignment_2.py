#  part one
def sumList(list):
	if len(list) == 0:
		return 0
	if len(list) == 1:
		return list[0]
	else:
		return list[0] + sumList(list[1:])



# part tw
def consecSum(list):
	x = 0
	temp = 0
	result = 0
	while x <= len(list) - 3:
		if result >= temp:
			temp = list[x] + list[x+1] + list[x+2]
			x += 1
		else:
			result = temp

	return result



# part three






def main():
	list = [-2, 4, 5, -6, 3, 6, 1]
	total = sumList(list)
	print(total)

	result = consecSum(list)
	print(result)



if __name__ == "__main__":
	main()