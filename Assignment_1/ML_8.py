import math
import numpy as np
import random
from numpy.linalg import inv
import sys
from numpy import linalg as LA



def split_list(a_list, number_of_splits):
    step = len(a_list) / number_of_splits + (1 if len(a_list) % number_of_splits else 0)
    return [a_list[i*step:(i+1)*step] for i in range(number_of_splits)]

if __name__ == '__main__':

	A=[]
	mean=5
	variance=2

	for i in range(0,1000):
		A.append(random.gauss(mean,variance))
	a=np.array(A)
	mean_1000=a.mean()
	variance_1000=a.var()
	# mean_1000=sum(A) / float(len(A))
	# print mean_1000

	bias_mean=abs(mean_1000-mean)
	bias_variance=abs(variance_1000- variance)
	print 'bias mean='+ str(bias_mean) +' bias_variance=  '+ str(bias_variance)


	subsets=split_list(A,100)

	variance_mean=0
	variance_var=0
	for i in range(len(subsets)):
		l=subsets[i]
		a=np.array(l)
		mean_l=a.mean()
		var_l=a.var()
		temp1=mean_1000- mean_l
		temp1=temp1*temp1
		variance_mean+=temp1

		temp2=variance_1000- var_l
		temp2=temp2*temp2
		variance_var+=temp2

	variance_mean=variance_mean/100
	variance_var/=100
	print 'variance_mean= '+ str(variance_mean) +' variance_var '+ str(variance_var)



# bias mean=0.0678354723432 bias_variance=  2.29195935562
# variance_mean= 0.447809797847 variance_var 3.57720342985
