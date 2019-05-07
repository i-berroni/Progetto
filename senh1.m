function [senh]=senh1(x)
f=@(x) (exp(x)-exp(-x))./2;
senh=f(x);
end
