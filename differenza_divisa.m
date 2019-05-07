%esercizio_8
clear all
close all
clc
format long e
%fisso h:
h=10^-7;
%scrivo la vera funzione e la sua derivata:
f=@(x) x.^3;
fder=@(x) 3.*(x.^2);
f_diffdivisa = @(x) ((x+h).^3 - x.^3)./h;

%PUNTO a:
%riscrivo la differenza finita
%usando la differenza tra cubi (si fa in carta e penna):
f_riscritta=@(x) 3.*x.^2+3.*x.*h+h.^2;

%Per x^5:
% %scrivo la vera funzione e la sua derivata:
% f=@(x) x.^5;
% fder=@(x) 5.*(x.^4);
% f_diffdivisa = @(x) ((x-h).^5 - x.^5)./h
% 
% %PUNTO a:
% %riscrivo la differenza finita
% %usando la differenza tra cubi (si fa in carta e penna):
% f_riscritta=@(x) 10.*x.^3.*h+10.*x.^2.*h^2+5.*x.*h^3+h.^4+5.*x.^4;


%PUNTO b:
x=10.^(1:4);
y_esatta = fder(x);
y_diffdivisa = f_diffdivisa(x);
y_riscritta = f_riscritta(x);

%prealloco gli errori:
err_ass_diffdiv=zeros(length(x),1);
err_rel_diffdiv=zeros(length(x),1);
err_ass_risc=zeros(length(x),1);
err_rel_risc=zeros(length(x),1);

%calcolo gli errori di y_diffdivisa
err_ass_diffdiv(1:4)=abs(y_diffdivisa(1:4) - y_esatta(1:4));
err_rel_diffdiv(1:4)=abs(y_diffdivisa(1:4) - y_esatta(1:4))./abs(y_esatta(1:4));

%calcolo gli errori di y_riscritta
err_ass_risc(1:4)=abs(y_riscritta(1:4) - y_esatta(1:4));
err_rel_risc(1:4)=abs(y_riscritta(1:4) - y_esatta(1:4))./abs(y_esatta(1:4));

%li plotto con questi formati:
%crea due figure, li visualizza una sopra l'altra quindi spostale.
%plotto riscritte:
% figure;
% semilogy(x,err_ass_risc,'-o','MarkerIndices',1:length(x),'MarkerEdgeColor','r');

%  figure;
%  semilogy(x,err_rel_risc,'b--o','MarkerIndices',1:length(x));
% 
%Plotto differenze divise:

figure;
loglog(x,err_ass_diffdiv,'b--o','MarkerIndices',1:length(x));
% 
% figure;
% semilogy(x,err_rel_diffdiv,'b--o','MarkerIndices',1:length(x));

