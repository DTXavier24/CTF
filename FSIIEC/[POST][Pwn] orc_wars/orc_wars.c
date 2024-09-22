#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

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

int main(void)
{
    ignore_me_init_buffering();
    int gold = 1000;
    int player_orcs = 20;
    int enemy_orcs = 554;
    int mercenaries = 0;
    int trained = 0;
    
    int running = 1;
    int first = 1;

    while(running)
    {
        printf("____ ____ ____    _ _ _ ____ ____ ____\n");
        printf("|  | |__/ |       | | | |__| |__/ [__ \n");
        printf("|__| |  \\ |___    |_|_| |  | |  \\ ___]\n\n");
        
        if(first)
        {   
            printf("Reporting for duty ! The ennemies are coming !!\n");
            first = 0;
        }
        
        printf("General, what are the orders ?\n");
        printf("Your gold : %dg\n\n", gold);
        printf("Your army \n");
        printf("| Orcs : %d\n", player_orcs);
        printf("| Mercenaries : %d\n\n", mercenaries);
        printf("1 - Scout enemy\n");
        printf("2 - Attack enemy\n");
        printf("3 - Train troops\n");
        printf("4 - Buy mercenaries\n");
        printf("5 - Flee like a coward\n");

        int choice = get_int_input(1,6);
        if(choice == -1) break;
        switch(choice)
        {
            case 1 : // scout
                printf("Go scout the enemy !\n");
                fflush(stdout);
                sleep(1);
                printf("Scout reporting for duty ! We are doomed !! The enemies are at least 500 !!\n");
                fflush(stdout);
                sleep(2);
            break;
            case 2 : // attack
                printf("Lets attack them !! For our kingdom !!!\n");
                fflush(stdout);
                sleep(0.5);
                printf("Aaargh !! *battle noises*\n");
                fflush(stdout);
                sleep(2);
                if(player_orcs + mercenaries >= enemy_orcs)
                {
                    if(player_orcs + mercenaries == enemy_orcs)
                    {
                        printf("The two armies killed each-other. You are alive, one could argue this is a win...\n");
                        printf("Your flag, but at what cost ?...\n");
                    }else {
                        printf("You won the battle !!\n");
                        printf("Your flag : \n");
                    }
                    fflush(stdout);
                    sleep(2);
                    print_flag();
                }else {
                    printf("You lost the battle, and were killed...\n");
                    printf("X_X\n");
                }   
                fflush(stdout);
                sleep(2);
                running = 0;
            break;
            case 3 : // train troops
                if(trained < 10)
                {
                    trained++;
                    player_orcs++;
                    printf("Go train more troops !\n");
                    fflush(stdout);
                    sleep(1);
                    printf("*You train one more troop, Will it be enough ?*\n");
                    printf("(trainings left : %d)\n", 10-trained);
                    fflush(stdout);
                    sleep(2);
                }else {
                    printf("There isn't anyone left to train...\n");
                    fflush(stdout);
                    sleep(2);
                }
            break;
            case 4 : // buy mercenaries
                printf("Go hire some mercenaries !\n");
                fflush(stdout);
                sleep(1);
                printf("*How many do you want ?*\n");
                printf("(100g per mercenary)\n");
                int nb = get_int_input(0,__INT_MAX__);
                if(nb*100 <= gold)
                {
                    printf("You hired %d mercenaries for %dg !\n");
                    mercenaries = nb;
                    gold = gold - nb*100;
                }else {
                    printf("You don't have enough gold for those mercenaries ! \n");
                }

                fflush(stdout);
                sleep(2);
            break;
            case 5 : // flee
                printf("*Sneakily goes away*\n");
                fflush(stdout);
                sleep(1);
                printf("General, we need you !! Come back here !!\n");
                printf("(fleeing is not an option, *coward*)\n");
                fflush(stdout);
                sleep(2);
            break;
            default:
                printf("hummmmmmmm\n");
                printf("*thinks*\n");
            break;
        }

    }

    return 0;
}

