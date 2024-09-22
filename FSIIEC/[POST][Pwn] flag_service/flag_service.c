#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// compilation : gcc -fPIE -fstack-protector-all -D_FORTIFY_SOURCE=2 -Wl,-z,now -Wl,-z,relro -o flag_service flag_service.c

#define MAX_NAME_SIZE 16

void ignore_me_init_buffering()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void print_flag(void) {
    FILE* fp = fopen("flag.txt", "r");
    char flag[100];
    fgets(flag, sizeof(flag), fp);
    puts(flag);
}

int get_int_input(long min, long max)
{
    long val = -1;
    int nb_try = 0;
    while(1)
    {
        char buff[10];
        fgets(buff, 10, stdin);
        char *validate = NULL;
        val = strtol(buff, &validate, 10);
        if(!(*validate == buff[0]))
        {
            if(min <= val && val <= max)
                break;
        }
        nb_try++;
        if(nb_try >= 5)
        {
            printf("you have tried too many times ! aborting...\n");
            return -1;
        }
        printf("please enter a valid choice\n");
        printf("your choice :\n");
    }  
    return (int) val;
}

typedef struct s_order
{
    int total_value;
    int nb_flags;
} order;



int main(int argc, char *argv[])
{
    ignore_me_init_buffering();
    int balance = 1;
    int my_flags = 0;
    order *current_order = NULL;
    int already_freed = 1;

    char *name = NULL;
    
    int running = 1;

    while(running)
    {
        printf(" _____ _               ____                  _          \n");
        printf("|  ___| | __ _  __ _  / ___|  ___ _ ____   _(_) ___ ___ \n");
        printf("| |_  | |/ _` |/ _` | \\___ \\ / _ \\ '__\\ \\ / / |/ __/ _ \\\n");
        printf("|  _| | | (_| | (_| |  ___) |  __/ |   \\ V /| | (_|  __/\n");
        printf("|_|   |_|\\__,_|\\__, | |____/ \\___|_|    \\_/ |_|\\___\\___|\n");
        printf("               |___/                                    \n");


        if(name == NULL)
        {
            printf("hi guest ! what do you want to do ?\n", name);
        }else {
            printf("hi %s ! what do you want to do ?\n", name);
        }
        printf("your balance : %d$\n\n", balance);
        if(current_order == NULL)
        {
            printf("you don't have any order currently\n\n");
        }else {
            printf("your order :\n| nb flags : %d\n| total value : %d$\n\n", current_order->nb_flags, current_order->total_value);
        }


        printf("1 - change my name\n");
        printf("2 - start a new order\n");
        printf("3 - delete my order\n");
        printf("4 - confirm my order\n");
        printf("5 - exit\n");
        
        int choice = get_int_input(1,6);
        if(choice == -1) break;
        switch(choice)
        {
            case 1 : // change my name
                printf("enter your name :\n");
                if(name != NULL) free(name);
                name = malloc(MAX_NAME_SIZE*sizeof(char));
                
                char *res = fgets(name,MAX_NAME_SIZE, stdin);
                if(res != name)
                {
                    printf("error with name !\n");
                    strcpy(name, "unknown");
                }else {
                    name[strlen(name)-1] = '\0';
                }
            break;
            case 2 : // start a new order
                printf("how many flags do you want ? \n(100$ per flag, max 9999 flags)\n");
                int nb = get_int_input(1,9999);
                if(already_freed != 1)
                {
                    free(current_order);
                }
                current_order = malloc(sizeof(order));
                current_order->nb_flags = nb;
                current_order->total_value = nb*100;
                printf("you want %d flags, which will cost %d$\n", nb, nb*100);
                already_freed = 0;
                fflush(stdin);
            break;
            case 3 : // delete my order
                if(already_freed != 1)
                {
                    current_order->nb_flags = 0;
                    current_order->total_value = 999;
                    free(current_order);
                    already_freed = 1;
                    printf("you deleted your order !\n");
                }else {
                    printf("you don't have any order to delete\n");
                }
            break;
            case 4 : // confirm my order
                if(current_order->total_value >= 0 && current_order->total_value <= balance)
                {
                    balance = balance - current_order->total_value;
                    my_flags = current_order->nb_flags;
                    printf("you successfully bought the flag !\n");
                    printf("you now have %d flags\n", my_flags);
                    
                }
                else {
                    printf("you don't have enough money to buy those flags !\n");
                }
                if(my_flags > 0)
                {
                    print_flag();
                    running = 0;
                }
            break;
            case 5 : // exit
                printf("Bye !\n");
                running = 0;
            break;
            default:
                printf("not a valid input\n\n");
            break;
        }

    }

    if(already_freed != 1) free(current_order);
    if(name != NULL) free(name);
    
    return 0;
}
