% Esercizi 8/9/10 Vettori, matrici e sistemi lineari
clear all
close all
clc
format short e

n = 10000;
i = 1;
x = zeros(n,1);
t_a = zeros(19,1);
t_b = zeros(19,1);

for q = 500:500:9500
   p = n-q;
   A11 = rand(p,p);
   A12 = rand(p,q);
   A22 = rand(q,q);
   A21 = zeros(q,p);
   A = [A11, A12;
        A21, A22];
   b = sum(A,2);

   % Metodo a:
   tic
   x = A\b;
   t_a(i) = toc;

   % Metodo b:
   tic
   x(p+1:end) = A22\b(p+1:end);
   x(1:p) = A11\(b(1:p)-A12*x(p+1:end));
   t_b(i) = toc;

   i=i+1;
end

costo_a = n^3/3 + n^2/2;
costo_b = @(q) n^3/3 + n^2/2 + n*q.^2 - n^2*q;

q_vett = 500:500:9500;
z = linspace(500, 9500, 1000);

% Si rappresentano graficamente i tempi di esecuzione per ambo i metodi
% e le rispettive curve teoriche, opportunamente scalate per poterle
% sovrapporre ai dati sperimentali in uno stesso grafico

plot(q_vett, t_a, 'b*', q_vett, t_b, 'r*', z, ones(1000,1)*costo_a/(2.5*1.0e10), 'b', z, costo_b(z)/(2.5*1.0e10), 'r');
legend('Tempo esecuzione metodo a', 'Tempo esecuzione metodo b','Costo teorico metodo a', 'Costo teorico metodo b')
xlabel('q')


