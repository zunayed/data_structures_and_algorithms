/*
Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node
Input: the node c from the linked list a->b->c->d->e
Result: nothing isreturned, but the new linked list looks like a- >b- >d->e
*/
#include "data_structures/linked_list.h"

void delete_node_from_middle (List::Node* n){
    if (n->next_node == NULL || n == NULL){
        return;
    }

    n->data = n->next_node->data;
    n->next_node = n->next_node->next_node;
    
}

int main(){
    List Test;
    
    Test.AddNode(1);
    Test.AddNode(2);
    Test.AddNode(3);
    Test.AddNode(4);
    Test.AddNode(5);
    Test.AddNode(6);
    Test.PrintList();

    // get a middle node
    List::Node* middle = Test.head->next_node->next_node->next_node;
    delete_node_from_middle(middle);
    std::cout << "After deleting middle node\n";
    Test.PrintList();

}
