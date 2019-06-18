%Esercizio_8_berrone
n=100;
i=1;
x=zeros(n,1);
z1=zeros(19,1);
z2=zeros(19,1);

for q=5:5:95
p=n-q;
A11=rand([p,p]);
A12=rand([p,q]);
A22=rand([q,q]);
A21 = zeros([q,p]);
A=[A11,A12;
   A21 ,A22 ];
b=sum(A,2);

% Metodo a:
tic
x=A\b;
z1(i) = toc;

% Metodo b:
tic
x(p+1:end)=A22\b(p+1:end);
x(1:p)=A11\(b(1:p)-A12*x(p+1:end));
z2(i) = toc;

i=i+1;
end
%alloco il vettore q
q_vett=zeros(19,1);
q_vett(1:19,1) = 5:5:95;



figure;
plot(q_vett,z1,'linewidth',2);
figure;
plot(q_vett,z2,'linewidth',2);






