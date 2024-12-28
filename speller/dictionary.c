// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>


#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

int word_count = 0;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

char* turn_upper(const char *word)
{
    int n=strlen(word);
    char *ch = malloc(strlen(word)+1);
    for (int i=0  ; i<n; i++)
    {
        ch[i]=toupper(word[i]);
    }
    ch[n] = '\0';
    return ch;
}

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    char *ch1 = turn_upper(word);
    // TODO
    int pos = hash(word);
    if ( table[pos] == NULL)
    return false;
    node *n = table[pos];
    while (n != NULL){
        char *ch =turn_upper(n->word);
        if(strcmp(ch,ch1) == 0){
        free(ch);
        free(ch1);
        return true;
        }
        else{
        free(ch);
        n=n->next;
        }

    }
    free(ch1);
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *dic = fopen(dictionary,"r");
    if (dic == NULL)
    return false;

    char s[LENGTH+1];
       while(fscanf(dic,"%s",s) != EOF){
        node *n = malloc(sizeof(node));
        if (n == NULL)
        return false;

        strcpy(n->word,s);
        int pos = hash(s);
        if (table[pos] == NULL){
        table [pos] = n;
        n->next = NULL;
        word_count++;

        }
        else
        {
            n->next = table[pos];
            table[pos] = n;
            word_count++;
        }
       }
    fclose(dic);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i=0; i<N; i++){
    node *n = table[i];
    node *tmp =NULL;
    while (n != NULL){
       tmp = n;
       n = n->next;
       free(tmp);
    }
    }
    return true;
}


