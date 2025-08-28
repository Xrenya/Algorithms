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
  printf("Deleted ListNode: %d\n", top->data);
  LINKED_LIST *ptr_next = top->next;
  free(top);
  return ptr_next;
}

void show(LINKED_LIST *top) {
  LINKED_LIST *cur = top;
  while (cur != NULL) {
    printf("ListNode(val=%d)\n", cur->data);
    cur = cur->next;
  }
}

void remove_node(LINKED_LIST **top, int val) { // since there is a copy of the pointer so we have to access the pointer in the main using **
    LINKED_LIST *cur = *top;
    LINKED_LIST *prev = NULL;

    while (cur != NULL) {
        if (cur->data == val) {
            if (prev == NULL) {
                *top = cur->next;
            } else {
                prev->next = cur->next;
            }
            printf("Removed ListNode: %d\n", cur->data);
            free(cur);
            return;
        }
        prev = cur;
        cur = cur->next;
    }
}

/*
LINKED_LIST* remove_node(LINKED_LIST *top, int val) {
  LINKED_LIST *dummy = malloc(sizeof(LINKED_LIST));
  dummy->data = -1;
  dummy->next = top;
  
  LINKED_LIST *prev = dummy;
  LINKED_LIST *cur = top;
  
  while (cur != NULL && cur->data != val) {
    prev = cur;
    cur = cur->next;
  }
  
  if (cur != NULL) {
    prev->next = cur->next;
    free(cur);
  }
  
  LINKED_LIST *new_top = dummy->next;
  free(dummy);
  
  return new_top;
}
*/


int main(void) {
  LINKED_LIST *top = NULL,  *cur = NULL;
  top = push(top, 1);
  top = push(top, 2);
  top = push(top, 3);
  top = push(top, 4);
  cur = top;
  show(top);
  remove_node(&top, 2);
  show(top);

  // free space
  while (top) {
      top = pop(top);
  }
  return 0;
}
