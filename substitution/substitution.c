#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
bool check_key(string key);
bool check_key(string key);
bool check_exist(char ch[], char key);

int main(int argc, string argv[])
{

    if (argc != 2)
    {
        printf("Need Key\n");
        return 1;
    }
    else if (strlen(argv[1]) != 26)
    {
        printf("Invalid key\n");
        return 1;
    }
    else if (check_key(argv[1]) == false)
    {
        printf("Invalid Key\n");
        return 1;
    }
    string ptext = get_string("plaintext: ");
        printf("ciphertext: ");


    for (int i = 0, n = strlen(ptext); i < n; i++)
    {
        if (isalpha(ptext[i])&&(islower(ptext[i])))
        {
            int index = ptext[i] - 97;
            printf("%c",tolower(argv[1][index]));


        }
        else if (isalpha(ptext[i])&&(isupper(ptext[i])))
        {
            int index = ptext[i] - 65;
            printf("%c",toupper(argv[1][index]));
        }
        else
            printf("%c",ptext[i]);

    }

printf("\n");
}

bool check_key(string key)
{
    char ch[strlen(key)];
    for (int i = 0, n = strlen(key); i < n; i++)
    {
        if (isalpha(key[i]) == 0)
            return false;
        else if (check_exist(ch, key[i]) == false)
            return false;
        else
            ch[i] = key[i];
    }
    return true;
}

bool check_exist(char ch[], char key)
{
    for (int i = 0, n = strlen(ch); i < n ; i++)
    {
        if (ch[i] == key)
        {
            return false;
        }
    }
    return true;
}
