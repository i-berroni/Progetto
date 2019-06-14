#include <stdio.h>
#include <stdlib.h>
#define N 2

struct riga
{
    int intero;
    float reale;
    char stringa[7];
};

int main()
{
    struct riga *v=NULL;
    int i,n=N,dim=0;
    FILE *fp1,*fp2;

    v=malloc(n*sizeof(struct riga));
    fp1=fopen("filelettura.txt","r");
    if(fp1==NULL)
    {
        printf("Errore nell'apertura del file in lettura\n");
        exit(1);
    }
    for(i=0;fscanf(fp1, "%d%f%s",&v[i].intero,&v[i].reale,v[i].stringa)!=EOF;i++)
    {
        if(i==n-1)
        {
            v=realloc(v,2*n*sizeof(struct riga));
            n=2*n;
        }
        dim=i+1;
    }
    fclose(fp1);
    fp2=fopen("filescrittura.txt","w");
    if(fp2==NULL)
    {
        printf("Errore nell'apertura del file in scrittura\n");
        exit(2);
    }
    for(i=0;i<dim;i++)
        fprintf(fp2,"%s %f %d \n",v[i].stringa,v[i].reale,v[i].intero);

    fclose(fp2);
    free(v);
    return 0;
}
