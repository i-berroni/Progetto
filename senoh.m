%esercizio_6
function []=senoh()
clear all
close all
clc
format long e


x=10.^(-(0:12));
f=@(x) (exp(x)-exp(-x))./2;
%la funzione valutata con la relazione:
y=f(x);
%la funzione valutata con la funzione nativa su matlab:
y1=sinh(x);
%ora calcolo l'errore:
for n=1:13

    err(n)=abs(y1(n)-y(n))/abs(y1(n));

end
%stampo gli indici
loglog(x,err,'-o','MarkerIndices',1:length(x));
err
end