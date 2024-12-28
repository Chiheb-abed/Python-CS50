#include <stdio.h>
#include <cs50.h>

void printing (int a);
int main (void)
{
    int n ;
    int j = 1 ;
    do
    {
        n = get_int("Number: ");

    } while ((n < 1) || ( n > 8));



while (n>0)
{
 for (int i = 1 ; i < n ; i++)
 {
    printf(" ");
 }

 printing (j);
 printf("  ");
 printing(j);
 printf("\n");
 j++;
 n--;
}
}


void printing (int a)
{
    for (int i = 0 ; i< a; i++)
    {
        printf("#");

    }
}
