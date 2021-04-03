// Consonant Count and Pattern

#include <stdio.h>

int consonantCount(char*);
void patternPrinting(int); 

int main() 
{ 
	int test_cases;
    scanf("%d", &test_cases);

    while(test_cases--)
    {
        char str[31];

        scanf(" %[^\n]%*c", str); 

        int n = consonantCount(str);

        patternPrinting(n);    
    }

	return 0; 
}

// Function to count number consonant

int consonantCount(char* str) 
{ 
	int consonants = 0;
	char ch; 

	for (int i = 0; str[i] != '\0'; i++)
	{ 
		ch = str[i]; 
 
		if (ch == 'a' || ch == 'A'
			|| ch == 'e' || ch == 'E'
			|| ch == 'i' || ch == 'I'
			|| ch == 'o' || ch == 'O'
			|| ch == 'u' || ch == 'U'
			|| ch == ' ') 
			continue; 

		else
			consonants++; 
	} 

	return consonants; 
}

// Function for Pattern Printing
void patternPrinting(int n)
{
	for(int i = 0 ; i < n ; i++)
	{
		for(int j = n-1 ; j > i; j--)
			printf(" ");

		for(int k = 0; k <= i; k++)
		{
			if(k & 1)
				printf("1");
			else
				printf("0");
		}
		printf("\n");
	}
}