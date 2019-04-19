#include <stdio.h>
#include <stdlib.h>
//definisco i prototipi:
int* swap(int *vett,int N);

int main(){
int N,*vett=NULL,i,tmp;
printf("Inserisci la lunghezza del vettore:\n");
scanf("%d",&N);
vett=(int*)malloc(N*sizeof(int));

//faccio il controllo se l'allocazione è andata a buon fine:
if (vett == NULL) {
  fprintf(stderr, "la malloc ha fallito\n");
  return(-1);
}

//Qui memorizzo gli elementi dinamicamente in un vettore:
printf("Inserisci ora i numeri che vuoi inserire:\n");
for(i=0;i<N;i++)
{
    printf("Numero %d\n",i);
    scanf("%d", &vett[i]);
}
printf("Il vettore che hai stampato e':\n");
for(i=0;i<N;i++) { 
    printf("v[%d]=%d\n",i,vett[i]); 
    }


//Uso la funzione SWAP
swap(vett,N);

printf("\n\nIl vettore dopo la trasformazione e':\n");
for(i=0;i<N;i++)
{
    printf("%d\n",vett[i]);
}
return 0;
}


//Qui eseguo lo swap:
//Io restituisco un puntatore a un int (un vettore di interi)
int* swap(int vett[],int N){
int i,tmp;

for(i=0;i<(N/2)-1;i++){
    tmp=vett[i];
    vett[i]=vett[N-i-1];
    vett[N-i-1]=tmp;
    }
    return vett;
}








