#include <stdio.h>

void goodp(int);
bool check(int);

int n;
int GP[80];
int key = 0;

int main()
{
	int i,j,k;
	
	scanf("%d",&n); 
	
	goodp(0);
	
	for(i = 0;i < n;i++)
	{
		printf("%d",GP[i]);
	}
	
	return 0;
}

void goodp(int a)
{
	int i,j,k;
	
	if(a == n)
	{
		key = 1;
		return; 
	}
	else if(a == 0)
	{
		GP[a] = 1;
		goodp(a+1);
	}
	else
	{
		for(i = 1;i < 4;i++)
		{
			GP[a] = i;
			if(check(a) == true)
			{
				goodp(a+1);
				if(key == 1)
				{
					return;
				}
			}
		}
	}
}

bool check(int b)
{
	int i,j;
	
	for(i = 1;i <= (b+1)/2;i++)
	{
		for(j = 0;j < i;j++)
		{
			if(GP[b-j] != GP[b-i-j])
			{
				break;
			}
		}
		if(j == i)
		{
			return false;
		}
	}
	return true;
}