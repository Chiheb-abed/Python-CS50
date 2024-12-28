#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
int liau(string text);
int main (void){

    string text = get_string ("text: ");
    int x = liau(text);
    if (x < 0)
    printf("Before Grade 1\n");
    else if (x>16)
    printf("Grade 16+\n");
    else
    printf("Grade %i\n", x);
}

int liau(string text)
{
    int word=0;
    int sent = 0;
    int lettre=0;
  for (int i=0 , n=strlen(text) ; i < n ; i++)
    {
        if (isalpha(text[i]))
        lettre++;
        else if (text[i]==' ')
        word++;
        else if (text[i]=='.' || text[i]=='!' || text[i]=='?')
        sent++;

        }
        word++;
        float L = (float) lettre / (float) word * 100;
        float S = (float) sent / (float) word * 100;
        float index = 0.0588 * L - 0.296 * S - 15.8;
        return round(index);
}

