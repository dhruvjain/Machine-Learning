
X = load('./breast_cancer_x.dat');

X = [ones(rows(X), 1) X];

X(:,2) = log(X(:,2));

y = load('./breast_cancer_y.dat');

for i = 1:size(y,1)
	if y(i,1) == 2
		y(i,1) = 0
	else
		y(i,1) = 1
	end
endfor		

n = length(y); 

d = size(X, 2);

max_iter = 1e4;

sigm = @(X, w) 1./(1+exp(-(X*w)));

w = zeros(d, max_iter);

w(:, 1) = zeros(d, 1);

alpha = 0.001;

for k=1:max_iter
	random_number = randi(n)

	temp = (alpha*(y(random_number, 1) - sigm(X(random_number, :), w(:, k))))*X(random_number, :);

	w(:,k+1) = w(:,k) + temp';

    fprintf('iter: %d, ||w_{k+1}-w_{k}||= %.6f\n', k, norm(w(:,k+1)-w(:,k),2));
    
    if (norm(w(:,k+1)-w(:,k),2) < 1e-6), break; 
    endif

endfor

no_of_iterations = k;
obj = zeros(no_of_iterations, 1);

for i=1:no_of_iterations
    term = sum(y.*log(sigm(X, w(:, i))) + (1-y).*log(1-sigm(X, w(:, i))));
        obj(i, 1) = term;
endfor

figure; legendInfo={};
axis([1, no_of_iterations]);

plot(1:no_of_iterations,obj(1:no_of_iterations, 1),'color',rand(1,3),'linewidth',2.0); hold on; grid on;

xlabel('iterations'); ylabel('Likelihood'); legend(legendInfo);

title('Likelihood vs iterations for Stochastic Gradient Descent Logistic Regression');

