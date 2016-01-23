
import math
from collections import defaultdict

def split_data(x, y, k):

	size_of_split = int(math.ceil(float(len(y))/k))

	for i in range(k):
		x_train = []
		y_train = []
		for j in range(k):
			index = j*size_of_split
			if j == i:
				x_test = x[index:index+size_of_split-1]
				y_test = y[index:index+size_of_split-1]
			else:
				x_train += x[index:index+size_of_split-1]
				y_train += y[index:index+size_of_split-1]

		count_features, count_class = naive_bayes(x_train, y_train)
		error = test_error(x_test, y_test, count_features, count_class)

		print error


def parse_data(path):							
	
	y = []
	x = []
	with open(path, 'r') as f:
		for line in f:
			
			elements_list = line.split(" ")
			y.append(elements_list[0])
			x.append(elements_list[1:])			
		
	return (x, y)



def test_error(x, y, count_features, count_class):					
	
	no_of_incorrect_labellings = 0
	for i, elt_list in enumerate(x):
		
		p = {}

		for key in count_class:
			p[key] = count_class[key]
	
		for j, elt in enumerate(elt_list):
			for key in count_class:
				if key in count_features[j] and elt in count_features[j][key]:
					p[key] *= (count_features[j][key][elt]/count_class[key])
				else:
					p[key] = 0

		flag = 0
		for key in count_class:
			if p[key] != 0:
				flag = 1

		if flag == 1:
			no_of_incorrect_labellings += math.fabs(float(max(p, key = p.get))-float(y[i]))/2


	fraction_of_incorrect_labellings = no_of_incorrect_labellings/len(y)

	return fraction_of_incorrect_labellings

def naive_bayes(x, y):							
	
	count_features = []
	for i, elt in enumerate(x[0]):
		count_features.append(defaultdict(dict))

	for i, elt_list in enumerate(x):					
		for j, elt in enumerate(elt_list):
			if y[i] in count_features[j] and elt in count_features[j][y[i]]:
				count_features[j][y[i]][elt] += 1.0
			else:
				count_features[j][y[i]][elt] = 1.0

	count_class = {}
	for elt in y:
		if elt in count_class:
			count_class[elt] += 1.0
		else:
			count_class[elt] = 1.0

	return (count_features, count_class)


def main():

	path = "./breast_cancer_dataset.txt"

	x, y = parse_data(path)
	split_data(x, y, 3)
	split_data(x, y, 5)
	split_data(x, y, 10)

if __name__ == '__main__':
	main()


		


