#include <stdio.h>
#include <algorithm>
#include <string>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

using namespace std;

void Letter(bool (&arr)[3], int letterindex)
{
	for (int i = 0; i<3;i++)
	{
		if(i == letterindex)
			arr[i] = 1;
		else
			arr[i] = 0;
	}
}

string solution(int A, int B, int C)
{
	string dstr;
	bool islast[] = {0,0,0};
	bool isinvalid[] = {0,0,0};
	while(A>0 || B>0 || C>0)
	{
		printf("isinvalidb %d\n", isinvalid[1]);
		if (!isinvalid[0])
		{
			printf("a is valid\n");
			if (A>0 && (A >= B || isinvalid[1]) && (A>=C || isinvalid[2]))
			{
				dstr += "a";
				--A;
				if (islast[0] == 1)
				{
					Letter(isinvalid, 0);
				}
				else
				{
					Letter(islast, 0);
					Letter(isinvalid, -1);
				}
				continue;
			}
		}
		if (!isinvalid[1])
		{
			if (B>0 && (B >= A || isinvalid[0]) && (B>=C || isinvalid[2]))
			{
				dstr += "b";
				--B;
				if (islast[1] == 1)
				{
					Letter(isinvalid, 1);
				}
				else
				{
					Letter(islast, 1);
					Letter(isinvalid, -1);
				}
				continue;
			}
		}
		if (!isinvalid[2])
		{
			if (C>0 && (C >= B || isinvalid[1]) && (C>=A || isinvalid[0]))
			{
				dstr += "c";
				--C;
				if (islast[2] == 1)
				{
					Letter(isinvalid, 2);
				}
				else
				{
					Letter(islast, 2);
					Letter(isinvalid, -1);
				}
				continue;
			}
		}
		break;
	}
	return dstr;
}

int main()
{
	string dstr = solution(10,5,0);
	printf("%s\n", dstr.c_str());
	return 0;
}
