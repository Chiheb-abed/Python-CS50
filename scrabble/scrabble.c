#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
int game (string input, int points[]);
int main (void){


    int ponts[]= {1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10};
    string player1 = get_string("Player 1: ");
    string player2 = get_string("Player 2: ");

    int score1 = game(player1 ,ponts);
    int score2 =game (player2 , ponts);

    if (score1 > score2)
    printf("Player 1 wins!\n");
    else if (score2> score1)
    printf("Player 2 wins!\n");
    else
    printf("Tie!\n");


}

int game (string input, int points[]){
    int score = 0;
    for (int i=0 , n=strlen(input) ; i < n ; i++)
    {
        if ((toupper(input[i]) >= 'A') && (toupper(input[i]) <= 'Z'))
        {
            score = score + points[toupper(input[i])-65] ;
        }
        }
    return score ;
}
