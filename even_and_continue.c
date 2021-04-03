#include <stdio.h>

int main()
{
    int test_cases;
    scanf("%d", &test_cases);

    while(test_cases--)
    {
    	int a, b, k;   
    	scanf("%d %d %d", &a, &b, &k);

    	int even_count;

    	even_count = ((b-a) / 2) + 1;

    	if(a&1 && b&1)
    		even_count--;

    	if((k >= a && k <= b) && !(k & 1))
    		even_count--;

	    printf("%d\n", even_count);	
    }
    
    return 0;
}