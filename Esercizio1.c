#include <stdio.h>
#include <stdlib.h>
//definisco i prototipi:
char* swap(char *vett,int N);

int main(){
int N,i;
char *vett=NULL;
printf("Inserisci la lunghezza del vettore:\n");
scanf("%d",&N);
vett=(char*)malloc(N*sizeof(char));

//faccio il controllo se l'allocazione è andata a buon fine:
if (vett == NULL) {
  fprintf(stderr, "la malloc ha fallito\n");
  return(-1);
}

//Qui memorizzo gli elementi dinamicamente in un vettore:
printf("Inserisci ora i numeri che vuoi inserire:\n");
for(i=0;i<N;i++)
{
    
    scanf(" %c", &vett[i]);
}
printf("Il vettore che hai stampato e':\n");
for(i=0;i<N;i++) { 
    printf("v[%d]=%c\n",i,vett[i]); 
    }


//Uso la funzione SWAP
swap(vett,N);

printf("\n\nIl vettore dopo la trasformazione e':\n");
for(i=0;i<N;i++)
{
    printf("%c",vett[i]);
}
return 0;
}


//Qui eseguo lo swap:
//Io restituisco un puntatore a un int (un vettore di interi)
char* swap(char vett[],int N){
int i;
char tmp;

for(i=0;i<(N/2);i++){
    tmp=vett[i];
    vett[i]=vett[N-i-1];
    vett[N-i-1]=tmp;
    }
    return vett;
}


