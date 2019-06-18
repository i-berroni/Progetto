% Esercizio 8 Aritmetica Finita
clear all
close all
clc
format long e

h=1.0e-7;

f=@(x) x.^3;
fder=@(x) 3.*(x.^2);
f_diffdivisa = @(x) ((x+h).^3 - x.^3)./h;

% PUNTO a:
% Si riscrive la differenza finita evitando la cancellazione numerica
f_riscritta=@(x) 3.*x.^2+3.*x.*h+h.^2;

% Per x^5:
%
% f=@(x) x.^5;
% fder=@(x) 5.*(x.^4);
% f_diffdivisa = @(x) ((x-h).^5 - x.^5)./h
% 
% %PUNTO a:
% % Si riscrive la differenza finita evitando la cancellazione numerica
% f_riscritta=@(x) 10.*x.^3.*h+10.*x.^2.*h^2+5.*x.*h^3+h.^4+5.*x.^4;

% PUNTO b:
x=10.^(1:4);
y_esatta = fder(x);
y_diffdivisa = f_diffdivisa(x);
y_riscritta = f_riscritta(x);

% Si preallocano gli errori:
err_ass_diffdiv=zeros(length(x),1);
err_rel_diffdiv=zeros(length(x),1);
err_ass_risc=zeros(length(x),1);
err_rel_risc=zeros(length(x),1);

% Si calcolano gli errori di y_diffdivisa
err_ass_diffdiv(1:4)=abs(y_diffdivisa(1:4) - y_esatta(1:4));
err_rel_diffdiv(1:4)=abs(y_diffdivisa(1:4) - y_esatta(1:4))./abs(y_esatta(1:4));

% Si calcolano gli errori di y_riscritta
err_ass_risc(1:4)=abs(y_riscritta(1:4) - y_esatta(1:4));
err_rel_risc(1:4)=abs(y_riscritta(1:4) - y_esatta(1:4))./abs(y_esatta(1:4));

figure(1);
loglog(x,err_ass_risc,'-o','MarkerIndices',1:length(x),'MarkerEdgeColor','r');
legend('Errore assoluto y riscritta')

figure(2);
loglog(x,err_rel_risc,'b--o','MarkerIndices',1:length(x));
legend('Errore relativo y riscritta')

figure(3);
loglog(x,err_ass_diffdiv,'b--o','MarkerIndices',1:length(x));
legend('Errore assoluto y diffdiv')

figure(4);
loglog(x,err_rel_diffdiv,'b--o','MarkerIndices',1:length(x));
legend('Errore relativo y diffdiv')

