#include <stdio.h>
#include <stdlib.h>
#define maxl 6 //lunghezza massima di ogni parola

/*
non so quante parole sono da leggere
quindi creo una funzione che me lo
dica.
*/

struct Dati
{
    char parola[6]; //può avere massimo 6 caratteri
    float reale;
    int  intero;
};


int main(){
    FILE *fp, *fp1;
    int n,i,j, intero;
    char parola[6];
    float reale;
    struct Dati *dati;
/*
printf("Inserisci il nome del file:\n");
nomefile=gets();
*/
    fp=fopen("file.txt","r");

    if(fp==NULL){
        printf("Il file non e' stato aperto correttamente");
        return 1;
    }
    j=0;
    i=0;
    n=1;
    //puntatore a una struttura
    dati=(struct Dati *)malloc(n*sizeof(struct Dati));
    /*feof(fp) restituisce un booleano vero se trova l'EOF, noi lo neghiamo: */
    do{

        fscanf(fp," %d",dati[i].intero)  ;
        printf("DAWSAD");
        fscanf(fp," %f",dati[i].reale)  ;
        fscanf(fp," %s",dati[i].parola) ;
        if (i>0){
        if(!feof(fp))
            {
            struct Dati *B =(struct Dati *)realloc(dati,i*n*sizeof(struct Dati));

                            }}
        i++;

    }while(!feof(fp));
    printf("%d",dati[1].intero);



    fclose(fp);

    fp1=fopen("file1.txt","w");
//Ora stampo al contrario:
    for(int j=i;j>0;j--){

        fprintf(fp1," %d",dati[j].intero)   ;
        fprintf(fp1," %f",dati[j].reale)  ;
        fprintf(fp1," %s",dati[j].parola) ;
        fprintf(fp1,"\n");
    }


    fclose(fp1);


    return 0;
}
