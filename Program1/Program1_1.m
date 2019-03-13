x = 1;
x = single(x);
for i=1:10
    x = x/8;
    fprintf("x:%.12e ",x);
    fx = sqrt(x^2+4)-2;
    fprintf("f(x):%.12e  ",fx);
    gx = x^2/(sqrt(x^2+4)+2);
    fprintf("g(x):%.12e\n",gx);
end
