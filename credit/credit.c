#include <cs50.h>
#include <stdio.h>

void check_card(long n);
int check_digit(int a);
bool check_valid(long n);

int main(void)
{
    long n = get_long("Number: ");
    bool r = check_valid(n);
    if (r == true)
        check_card(n);
    else
        printf("INVALID\n");
}

bool check_valid(long n)
{
    int s1, s2, i = 0;
    while (n != 0)
    {
        if (i % 2 == 0)
        {
            s1 = s1 + (n % 10);
        }
        else
        {
            s2 = s2 + check_digit((n % 10) * 2);
        }
        n = n / 10;
        i++;
    }
    s2 = s2 + s1;
    if (s2 % 2 == 0)
        return true;
    else
        return false;
}

int check_digit(int a)
{
    if (a > 9)
    {
        int x = a % 10;
        a = x / 10;
        return x + a;
    }
    else
        return a;
}

void check_card(long n)
{
    int a = n / 10000000000000;
    int v = n / 1000000000000000;
    int vs = n / 1000000000000;
    int m = n / 100000000000000;

    if ((v == 4) || (vs == 4))
        printf("VISA\n");
    else if ((a == 34) || (a == 37))
        printf("AMEX\n");
    else if ((m >= 51) && (m <= 55))
        printf("MASTERCARD\n");
    else
        printf("INVALID\n");
}
