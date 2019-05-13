#include <stdio.h>
#include <stdlib.h>
#include<math.h>

// La fattorizzazione e' corretta.
// Ora dobbiamo implementare forward and backward substitution e quanto necessario per risolvere un sistema lineare.
// Scriviamo tutto in un unico main? O scriviamo varie funzioni per spezzare il codice?

int main()
{
    int ndim, i, j, k, ind_pivot;   // ndim -> dimensione della matrice
    double** A = NULL;              // A -> matrice da fattorizzare
    double *tmp = NULL;
    int *pivot = NULL;
    double el_pivot;

    // Leggo da standard input la dimensione della matrice

    printf("Inserire la dimensione della matrice di Hilbert:\n");
    scanf("%d", &ndim);

    // Data la dimensione alloco dinamicamente la matrice e il vettore pivot

    A = (double**)malloc(ndim*sizeof(double *));
    for(i = 0; i < ndim; i++)
    {
        A[i] = (double*)malloc(ndim*sizeof(double));
    }
    pivot = (int*)malloc((ndim - 1)*sizeof(double));

    // Stampo la matrice per verificarne la correttezza

    printf("\nLa matrice di Hilbert e':\n\n");
    for(i = 0; i < ndim; i++)
    {
        for(j = 0; j < ndim; j++)
        {
            A[i][j] = 1.0/(i+j+1);
            printf("%f ", A[i][j]);
        }
        printf("\n");
    }

    // Effettuo l'eliminazione gaussiana con pivoting parziale

    for(k = 0; k < ndim-1; k++)
    {
        // Ricerco l'elemento pivot

        el_pivot = fabs(A[k][k]);
        ind_pivot = k;
        for (i = k+1; i < ndim; i++)
            if(  fabs(A[i][k]) > el_pivot )
            {
                el_pivot = fabs(A[i][k]);
                ind_pivot = i;
            }
        pivot[k] = ind_pivot;

        // Scambio le righe se necessario

        if(pivot[k] != k)
        {
            tmp = A[k];
            A[k] = A[pivot[k]];
            A[pivot[k]] = tmp;
        }

        // Procedo con l'algoritmo di eliminazione Gaussiana

        for(i = k+1; i < ndim; i++)
            if( A[k][k] != 0.0 )
            {
                A[i][k] = A[i][k] / A[k][k];       // salvo il modificatore direttamente nella parte triangolare inferiore della matrice
                for(j = k+1; j < ndim; j++)
                    A[i][j] -= A[i][k] * A[k][j];
            }
            else
            {
                printf("\nErrore: la matrice inserita e' singolare\n");
                return -1;
            }

    }

    // Ristampo la matrice e il vettore pivot dopo la modifica

    printf("\nLa matrice modificata e':\n\n");
    for(i = 0; i < ndim; i++)
    {
        for(j = 0; j < ndim; j++)
        {
            printf("%f ", A[i][j]);
        }
        printf("\n");
    }

    printf("\nIl vettore pivot degli scambi e':\n\n");
    for(i = 0; i < ndim - 1; i++)
        printf("%d ", pivot[i]);

    return 0;
}
