#include <stdio.h>
#include <stdlib.h>

#define VERBOSITY 2

char* swap(char *vett, int N);

int main(){
    int N, i;
    char *vett = NULL;

    printf("Inserisci la lunghezza del vettore:\n");
    scanf("%d", &N);
    vett = (char*)malloc(N*sizeof(char));

    if (vett == NULL)
    {
      fprintf(stderr, "\nLa malloc ha fallito\n");
      return(-1);
    }

    printf("\nInserisci ora i caratteri:\n");
    for(i=0; i<N; i++)
    {
        scanf(" %c", &vett[i]);
    }

    #if VERBOSITY >= 1
    printf("\nCaratteri inseriti: \n");
    for(i=0; i<N; i++)
    {
        printf("%c", vett[i]);
    }
    printf("\n");
    #endif

    swap(vett,N);

    printf("\n\nIl vettore dopo la trasformazione e':\n");
    for(i=0;i<N;i++)
    {
        printf("%c",vett[i]);
    }
    return 0;
}

char* swap(char vett[],int N){

    int i;
    char tmp;

    for(i=0;i<(N/2);i++)
        {
            tmp = vett[i];
            vett[i] = vett[N-i-1];
            vett[N-i-1] = tmp;
            #if VERBOSITY >= 2
            printf("\nScambiati i caratteri: %c %c", vett[N-i-1], vett[i]);
            #endif
        }

    return vett;
}
