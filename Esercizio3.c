#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct list_el
{
    int intero;
    float reale;
    char *stringa;
    struct list_el *succ;
    struct list_el *prec;
}list_el;

int in_coda(list_el **head, int intero, float reale, char *s);

int main()
{
    list_el *head=NULL, *el;
    FILE *f1, *f2;
    int a;
    float b;
    char s[7];

    f1=fopen("filelettura.txt","r");
    if(f1==NULL)
    {
        printf("Errore nell'apertura del file\n");
        exit(1);
    }

    while(fscanf(f1,"%d%f%s",&a,&b,s)!=EOF)
    {
        in_coda(&head, a, b, s);
    }

    fclose(f1);
    f2=fopen("filescrittura.txt","w");
    if(f2==NULL)
    {
        printf("Errore nell'apertura del file\n");
        exit(2);
    }

    el = head;
    while(el != NULL)
    {
        fprintf(f2,"%s %f %d \n",el -> stringa, el -> reale, el -> intero);
        el = el -> succ;
    }
    fclose(f2);

    free(head);
    free(el);

    return 0;
}

int in_coda(list_el **head, int a, float b, char *s)
{
    list_el *el, *last;

    el=malloc(sizeof(list_el));
    if(el==NULL)
        return 1;
    el -> intero=a;
    el -> reale=b;
    el -> stringa=strdup(s);
    el -> succ=NULL;
    if(*head==NULL)
    {
        *head=el;
    }
    else
    {
        last = *head;
        while (last -> succ != NULL ) last =last -> succ ;
        last -> succ = el ;
        el -> prec = last;
    }
    return 0;
}
