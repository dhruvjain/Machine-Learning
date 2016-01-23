import math
import numpy as np
import random
from numpy.linalg import inv
import sys
from numpy import linalg as LA
import csv


# calculating sinx from -pi to pi and storing in a list A

def y(x,w):
	ans=w[9].item(0)

	for i in range(1,10):
		ans= ans*x + w[9-i].item(0)
	return ans

def calc_error(var,a):
	
	t_points=[]
	for i in range(0,len(x_points)):
		t_points.append(math.sin(x_points[i])+a*random.gauss(0,1))
 
	xdata_train=x_points[:int(math.floor(len(x_points)*0.8))]
	tdata_train=t_points[:int(math.floor(len(t_points)*0.8))]

	#print len(xdata_train), len(tdata_train)

	xdata_test=x_points[int(math.floor(len(x_points)*0.8)):]
	tdata_test=t_points[int(math.floor(len(t_points)*0.8)):]



	A=[]

	for x in xdata_train:
		A_coeff=[1]
		for i in range(1,10):
			A_coeff.append(A_coeff[i-1]*x)
		A.append(A_coeff)

	A_mat=np.matrix(A)
	I_mat=np.identity(10)
	w=(inv(var*I_mat+A_mat.transpose()*A_mat))*(A_mat.transpose())*(np.matrix(tdata_train).transpose())

	ans_test=0
	for i in range(0,len(xdata_test)):
		temp=y(xdata_test[i],w)-tdata_test[i]
		temp=temp*temp;
		ans_test += temp
	ans_test=ans_test/2;

	# w=np.array(w);
	ans_test=ans_test+var*LA.norm(w)/2
	ans_test=math.sqrt(2*ans_test/len(xdata_test))

	ans_train=0
	for i in range(0,len(xdata_train)):
		temp=y(xdata_train[i],w)-tdata_train[i]
		temp=temp*temp;
		ans_train += temp
	ans_train=ans_train/2;

	# w=np.array(w);
	ans_train=ans_train+var*LA.norm(w)/2
	ans_train=math.sqrt(2*ans_train/len(xdata_train))
	return ans_test,ans_train

if __name__=="__main__":

	Values=[]
	start=-1*math.pi
	end=math.pi
	i=start
	while (i<=end):
		Values.append(math.sin(i))
		# print i,math.sin(i)
		i+=0.1

	x_points=[]
	i=start

	while (i<=end):
		x_points.append(i)
		i+=0.1
	x_points=x_points*10

	
	random.shuffle(x_points)
	lambdas = [0.001,0.01,0.1,1,10,100,1000]
	all_a = [0.1,0.5,1,2,10]

	error_train = [[0 for x in range(5)] for x in range(7)]

	error_test = [[0 for x in range(5)] for x in range(7)] 

	
	c = csv.writer(open("results8_7.csv", "wb"))
	c.writerow(['lambda','a','root_mean square test error','root_mean square training error'])
	for i in range(0,len(lambdas)):
		for j in range(0,len(all_a)):
			error_test[i][j],error_train[i][j] = calc_error(lambdas[i],all_a[j]);
			print lambdas[i],'  ',all_a[j],'  ',error_test[i][j],'  ',error_train[i][j]
			c.writerow([str(lambdas[i]),str(all_a[j]),str(error_test[i][j]),str(error_train[i][j])])
			# sys.stdout.write(str(error_train[i][j])+'  '+str(error_test[i][j])+' ****  ')			
		print '\n'
	