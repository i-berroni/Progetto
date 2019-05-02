
#include <stdio.h>
#include <stdlib.h>

int main(){
int N,i;
char *vett=NULL,tmp;

printf("Inserisci la lunghezza del vettore:\n");
scanf("%d",&N);
vett=(char*)malloc(N*sizeof(char));

//faccio il controllo se l'allocazione è andata a buon fine:
if (vett == NULL) {
  fprintf(stderr, "la malloc ha fallito\n");
  return(-1);
}


printf("Inserisci ora i caratteri che vuoi inserire:\n");
for(i=0;i<N;i++)
{
    scanf(" %c", &vett[i]);
    
}
printf("Il vettore che hai stampato e':\n");
for(i=0;i<N;i++) { 
    printf("v[%d]=%c\n",i,vett[i]); 
    }

for(i=0;i<(N/2);i++){
    tmp=vett[i];
    vett[i]=vett[N-i-1];
    vett[N-i-1]=tmp;
}
printf("\n\nIl vettore dopo la trasformazione e':\n");
for(i=0;i<N;i++)
{
    printf("%c",vett[i]);
}
return 0;


}








