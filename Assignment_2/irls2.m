
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

w(:,1)=zeros(d,1);

max_num_iter=1e2; w=zeros(d,max_num_iter);

lambda=1e-4; v = lambda*eye(d);

sigm = @(X, w) 1./(1+exp(-(X*w)));

for k=1:max_num_iter
    
    mu_k = sigm(X,y,w(:,k));

    Sk = diag(mu_k.*(1-mu_k) + eps);

    z_k = X*w(:,k)-inv(Sk)*(mu_k - y);     
    
    w(:,k+1)=inv(X'*Sk*X + v)*(X'*Sk*z_k); %w update
    
    fprintf('iter: %d, ||w_{k+1}-w_{k}||= %.6f\n', k, norm(w(:,k+1)-w(:,k),2));

    if (norm(w(:,k+1)-w(:,k),2) < 1e-6), break; 
    endif

endfor

w=w(:,1:k);


no_of_iterations = k;
obj = zeros(no_of_iterations, 1);

for i=1:no_of_iterations
    term = sum(y.*log(sigm(X, y, w(:, i))) + (1-y).*log(1-sigm(X, y, w(:, i))));
        obj(i, 1) = term;
endfor

figure; legendInfo={};
plot(1:no_of_iterations,obj(1:no_of_iterations, 1),'color',rand(1,3),'linewidth',2.0); hold on; grid on;

xlabel('iterations'); ylabel('Likelihood'); legend(legendInfo);

title('Likelihood vs iterations for IRLS Logistic Regression');


