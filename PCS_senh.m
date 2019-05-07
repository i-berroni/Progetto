%esercizio_6_con_esercizio_7_aritmetica_finita
clear all
close all
clc
format long e

x=10.^(-(0:12));
x=x';
%seno iperbolico 1
y1 = senh1(x);
%seno iperbolico 2
y2=zeros(length(x),1);
for i=1:length(x)
y2(i) = senh2(x(i));
end
%valore implementato in matlab del seno iperbolico:
y_matlab=sinh(x);
%preallocazioni degli errori:
err1 = zeros(length(x),1);
err2 = zeros(length(x),1);
%errori relativi:
err1(1:13)=abs(y1(1:13)-y_matlab(1:13))./abs(y_matlab(1:13));
err2(1:13)=abs(y2(1:13)-y_matlab(1:13))./abs(y_matlab(1:13));


figure;
loglog(x,err1,'-o','MarkerIndices',1:length(x));
figure;
loglog(x,err2,'-o','MarkerIndices',1:length(x));



%errori assoluti:
err1abs(1:13)=abs(y1(1:13)-y_matlab(1:13));
err2abs(1:13)=abs(y2(1:13)-y_matlab(1:13));

figure;
loglog(x,err1abs,'-o','MarkerIndices',1:length(x));
figure;
loglog(x,err2abs,'-o','MarkerIndices',1:length(x));







