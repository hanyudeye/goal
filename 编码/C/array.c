// 对数组的操作

#include <stdio.h>

// 显示n个数组成员,从头开始
void show_array(int *array, int n)
{
	printf("n 个数组为:\n");
	for (int i = 0; i < n; i++)
	{
		printf("%5.d",array[i]);
	}

	printf("\n");
}

int main()
{

	int array[] = {1, 2, 1, 2, 2, 1, 1};
	int n = 5;
	//	显示前5个数组值

	show_array(array, n);
	return 0;
}
