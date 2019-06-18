% Esercizi 6 e 7 Aritmetica finita
clear all
close all
clc
format long e

x=10.^(-(0:12));
x=x';

% Seno iperbolico 1
y1 = senh1(x);

% Seno iperbolico 2
y2=zeros(length(x),1);
for i=1:length(x)
    y2(i) = senh2(x(i));
end

% Valore implementato in matlab del seno iperbolico:
y_matlab=sinh(x);

% Preallocazioni degli errori:
err1 = zeros(length(x),1);
err2 = zeros(length(x),1);
err1abs = zeros(length(x),1);
err2abs = zeros(length(x),1);

% Errori relativi:
err1(1:13)=abs(y1(1:13)-y_matlab(1:13))./abs(y_matlab(1:13));
err2(1:13)=abs(y2(1:13)-y_matlab(1:13))./abs(y_matlab(1:13));

figure(1);
loglog(x,err1,'-o','MarkerIndices',1:length(x));
legend('Errore relativo di senh1')
figure(2);
loglog(x,err2,'-o','MarkerIndices',1:length(x));
legend('Errore relativo di senh2')

% Errori assoluti:
err1abs(1:13)=abs(y1(1:13)-y_matlab(1:13));
err2abs(1:13)=abs(y2(1:13)-y_matlab(1:13));

figure(3);
loglog(x,err1abs,'-o','MarkerIndices',1:length(x));
legend('Errore assoluto di senh1')
figure(4);
loglog(x,err2abs,'-o','MarkerIndices',1:length(x));
legend('Errore assoluto di senh2')





