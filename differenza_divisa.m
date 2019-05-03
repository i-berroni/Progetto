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
%scivo la sua differenza divisa
fd=@(x) (f(x+h)-f(x))./h;
%Il valore della differenza divisa
%nel punto x0 è dato da fd=fd(x0);


%PUNTO a:
%riscrivo la differenza finita
%usando la differenza tra cubi (si fa in carta e penna):
f_riscritta=h^2;

%PUNTO b:
x=10.^(1:4);
for i=x
%valori effettivi della funzione(facoltativo)
y=f(i);
%valori della differenza divisa non semplificata
yd=fd(i);
end




%calcolo l'errore assoluto:
err_ass=zeros(length(x));
i=1;
for j=x
    err_ass(i)=abs(fd(j)-fder(j));
    i=i+1;
end

%calcolo l'errore relativo:
err_rel=zeros(length(x));
i=1;
for j=x
    err_rel(i)=abs(fd(j)-fder(j))/abs(fder(j));
    i=i+1;
end

%li plotto con questi formati:
%crea due figure, li visualizza una sopra l'altra quindi spostale.
figure;
loglog(x,err_ass,'-o','MarkerIndices',1:length(x),'MarkerEdgeColor','r');
figure;
loglog(x,err_ass,'b--o','MarkerIndices',1:length(x));

%% RIPETO CON LA FUNZIONE y=x.^5

%esercizio_8
clear all
close all
clc
format long e
%fisso h:
h=10^-7;
%scrivo la vera funzione e la sua derivata:
f=@(x) x.^5;
fder=@(x) 5.*(x.^4);
%scivo la sua differenza divisa
fd=@(x) (f(x+h)-f(x))./h;
%Il valore della differenza divisa
%nel punto x0 è dato da fd=fd(x0);


%PUNTO a:
%riscrivo la differenza finita (si fa in carta e penna)
% x5 - a5 = (x-a) (x4 +ax3 +a2x2 +a3x +a4) :
f_riscritta=%calcolala a mano facendo i conti, mi secca haha;

%PUNTO b:
x=10.^(1:4);
for i=x
%valori effettivi della funzione(facoltativo)
y=f(i);
%valori della differenza divisa non semplificata
yd=fd(i);
end




%calcolo l'errore assoluto:
err_ass=zeros(length(x));
i=1;
for j=x
    err_ass(i)=abs(fd(j)-fder(j));
    i=i+1;
end

%calcolo l'errore relativo:
err_rel=zeros(length(x));
i=1;
for j=x
    err_rel(i)=abs(fd(j)-fder(j))/abs(fder(j));
    i=i+1;
end

%li plotto con questi formati:
%crea due figure, li visualizza una sopra l'altra quindi spostale.
figure;
loglog(x,err_ass,'-o','MarkerIndices',1:length(x),'MarkerEdgeColor','r');
figure;
loglog(x,err_ass,'b--o','MarkerIndices',1:length(x));
