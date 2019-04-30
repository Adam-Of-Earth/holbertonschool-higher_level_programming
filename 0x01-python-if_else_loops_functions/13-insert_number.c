#include "lists.h"

/**
 * insert_node - inserts number into a linked list
 * @head: head of linked list
 * @number: number to insert
 * Retun: address of new node (sucsess) NULL (falure)
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *move;

	if (head == NULL)
		return (NULL);
	move = *head;
	node = malloc(sizeof(listint_t));
	node->n = number;
	node->next = NULL;
	if (*head == NULL)
		*head = node;
	else
	{
		while (move->next->n < number)
		{
			move = move->next;
		}
		node->next = move->next;
		move->next = node;
	}
	return (node);
}
