#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define magic_nbr 512

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Need 1 command line\n");
        return 1;
    }

    FILE *f = fopen(argv[1], "r");
    if (f == NULL)
    {
        printf("corrupted file");
        return 1;
    }
    uint8_t tmp[magic_nbr];
    int fl_nbr = 0;
    int gotcha = 0;
    char fl_name[8];
    FILE *nimage = NULL;

    while (fread(tmp, 1, magic_nbr, f))
    {
        if (tmp[0] == 0xff && tmp[1] == 0xd8 && tmp[2] == 0xff && (tmp[3] & 0xf0) == 0xe0)
        {
            gotcha++;
        }

        if ((gotcha != 0) && (fl_nbr == 0))
        {
            sprintf(fl_name, "%03i.jpg", fl_nbr);
            nimage = fopen(fl_name, "w");
            fwrite(tmp, 1, magic_nbr, nimage);
            gotcha = 0;
            fl_nbr++;
        }

        else if (gotcha != 0)
        {
            fclose(nimage);
            sprintf(fl_name, "%03i.jpg", fl_nbr);
            nimage = fopen(fl_name, "w");
            fwrite(tmp, 1, magic_nbr, nimage);
            gotcha = 0;
            fl_nbr++;
        }
        else if (fl_nbr != 0)
            fwrite(tmp, 1, magic_nbr, nimage);
    }

    fclose(nimage);
    fclose(f);
}
