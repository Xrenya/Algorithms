#include <stdio.h>
#include <stdlib.h>


typedef struct tag_obj {
  int data;
  struct tag_obj *next;
} LINKED_LIST;

LINKED_LIST* push(LINKED_LIST *top, int data) {
  LINKED_LIST *ptr = malloc(sizeof(LINKED_LIST));
  ptr->data = data;
  ptr->next = top;
  return ptr;
}

LINKED_LIST* pop(LINKED_LIST *top) {
  if (top == NULL) return top;
  printf("Deleted: %d\n", top->data);
  LINKED_LIST *ptr_next = top->next;
  free(top);
  return ptr_next;
}


int main(void) {
  LINKED_LIST *top = NULL;
  top = push(top, 1);
  top = push(top, 2);
  top = push(top, 3);
  printf("%d\n", top->data);
  top = pop(top);
  printf("%d\n", top->data);
  return 0;
}
