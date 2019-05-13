#include <stdio.h>
#include <stdlib.h>

/* IL CODICE E' SBAGLIATO, POSSIBILI ERRORI:
   1. scambio delle righe e memorizzazzione di 'pivot'
   2. allocazione della matrice e gestione dei puntatori
   3. errori generici nell'algoritmo
*/

// La funzione 'fabs' per il valore assoluto di numeri reali mi dà warning

int main()
{
    // Definisco le variabili e tutte le quantita' di cui ho bisogno

    int ndim;
    double *A = NULL;
    double *tmp = NULL;
    int *pivot = NULL;
    double el_pivot;
    int i,j,k;
    int ind_pivot;

    // Leggo da standard input la dimensione della matrice

    printf("Inserire la dimensione della matrice di Hilbert:\n");
    scanf("%d", &ndim);     // e' necessario fare un controllo sulla lettura di ndim?

    // Data la dimensione alloco dinamicamente la matrice, ne definisco le entrate e la stampo per verificarne la correttezza

    // Il fatto che richieda che A sia un vettore colonna di puntatori e' solo concettuale o devo effettivamente salvarla come matrice ndim x 1 ?

    // Potrei richiedere un booleano in input per decidere se stampare la matrice o meno; per grandi dimensioni non ha senso stamparla

    A = malloc(ndim*sizeof(double[ndim]));
    pivot = malloc((ndim - 1)*sizeof(double));

    printf("\nLa matrice di Hilbert e':\n\n");
    for(i = 0; i < ndim; i++)
    {
        for(j = 0; j < ndim; j++)
        {
            (&A[i])[j] = 1.0/(i+j+1);
            printf("%f ", (&A[i])[j]);
        }
        printf("\n");
    }

    // Effettuo l'eliminazione gaussiana con pivoting parziale

    for(k = 0; k < ndim-1; k++)
    {
        // Ricerco l'elemento pivot

        el_pivot = fabs((&A[k])[k]);
        ind_pivot = k;
        for (i = k+1; i < ndim; i++)
            if(  fabs((&A[i])[k]) > el_pivot )
            {
                el_pivot = fabs((&A[i])[k]);
                ind_pivot = i;
            }
        pivot[k] = ind_pivot;

        // Scambio le righe se necessario

        if(pivot[k] != k)
        {
            // Non so se lo scambio e' eseguito correttamente
            tmp = (&A[k]);
            A[k] = A[pivot[k]];
            A[pivot[k]] = *tmp;
        }

        // Procedo con l'algoritmo di eliminazione Gaussiana

        for(i = k+1; i < ndim; i++)
            if( (&A[k])[k] != 0.0 )
            {
                (&A[i])[k] = (&A[i])[k] / (&A[k])[k];       // salvo il modificatore direttamente nella parte triangolare inferiore della matrice
                for(j = k+1; j < ndim; j++)
                    (&A[i])[j] -= (&A[i])[k] * (&A[k])[j];
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
            printf("%f ", (&A[i])[j]);
        }
        printf("\n");
    }

    printf("\nIl vettore pivot degli scambi e':\n\n");
    for(i = 0; i < ndim - 1; i++)
        printf("%d ", pivot[i]);



    return 0;
}
