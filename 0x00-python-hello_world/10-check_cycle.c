#include "lists.h"

/**
 * check_cycle - checks a linked list to see if its a cycle
 * @list: head of linked list
 *
 * Return: 1 (suscess) 0 (failure)
 */
int check_cycle(listint_t *list)
{
	listint_t *first, *bot;

	if (list == NULL || list->next == NULL)
		return (0);
	bot = first = list;
	while (bot != NULL)
	{
		if (bot->next == NULL)
			return (0);
		bot = bot->next;
		if (bot == first)
			return (1);
	}
	return (0);
}
