//
// Created by Taha CAKMAK on 26.11.2023.
//

#ifndef CS300HW2_AVL_AVLTREE_H
#define CS300HW2_AVL_AVLTREE_H
template<class Obj>
class AvlTree{
    public:
    explicit AvlTree(Obj x);
    AvlTree();

    //~AvlTree();

    const Obj& findMin() const;
    const Obj & findMax() const;
    const Obj & find( const Obj & x ) const;
    bool isEmpty( ) const;

    //void makeEmpty( );
    void insert(Obj x);
    //void remove( const Obj & x );



private:
    struct Node{
        Obj key;
        Node* left;
        Node* right;
        int height;
        Node(Obj k, Node* l, Node* r): key(k), left(l), right(r), height(0){}
    };
    Node* root;

    //const Obj & findMinSubTree(Node * n);
    //const Obj & findMaxSubTree (Node * n);

    void insertP( const Obj & x, Node* &t);

    const int & getHeight(Node * n) const;
    void heightUpdate(Node * n);
    void rotateWithLeftChild( Node * & k2 ) const;
    void rotateWithRightChild (Node * & k1) const;
    void doubleWithLeftChild (Node * & k1) const;
    void doubleWithRightChild ( Node * & k1 ) const;


    int max(int i , int j) const;


};

template<class Obj>
void AvlTree<Obj>::insert(Obj x) {
    insertP(x,root);
}

template<class Obj>
void AvlTree<Obj>::doubleWithRightChild(AvlTree::Node *&k1) const {
    rotateWithLeftChild( k1->right );
    rotateWithRightChild( k1 );
}

template<class Obj>
void AvlTree<Obj>::doubleWithLeftChild(AvlTree::Node *&k1) const {
    rotateWithRightChild( k1->left );
    rotateWithLeftChild( k1 );

}

template<class Obj>
int AvlTree<Obj>::max(int i, int j)const {
    return (i >= j) ? i : j;
}
template<class Comparable>
void AvlTree<Comparable>::rotateWithRightChild
        ( Node * & k1 ) const
{
    Node *k2 = k1->right;
    k1->right = k2->left;
    k2->left = k1;
    k1->height = max( getHeight( k1->left ), getHeight( k1->right ) ) + 1;
    k2->height = max( getHeight( k2->right ), k1->height ) + 1;
    k1 = k2;
}




template<class Obj>
void AvlTree<Obj>::rotateWithLeftChild( Node * & k2 ) const
{
    Node *k1 = k2->left;
    k2->left = k1->right;
    k1->right = k2;
    k2->height = max( getHeight( k2->left ), getHeight( k2->right ) ) + 1;
    k1->height = max( getHeight( k1->left ), k2->height ) + 1;
    k2 = k1;
}


template<class Obj>
void AvlTree<Obj>::insertP(const Obj &x, Node * &t) {
        if ( t == nullptr ){
            t = new Node( x, nullptr, nullptr );
        }

        else if ( x < t->key ) {
            insertP( x, t->left );

            if ( getHeight( t->left ) - getHeight( t->right ) == 2 ){
                if ( x < t->left->key ) {
                    // X was inserted to the left-left subtree!
                    rotateWithLeftChild( t );
                }
                else{
                    // X was inserted to the left-right subtree!
                    doubleWithLeftChild( t );
                }
            }
        }

        else if( t->key < x ){
            // Otherwise X is inserted to the right subtree
            insertP( x, t->right );
            if ( getHeight( t->right ) - getHeight( t->left ) == 2 ){
                // height of the right subtree increased
                if ( t->right->key < x )
                    // X was inserted to right-right subtree
                    rotateWithRightChild( t );
                else // X was inserted to right-left subtree
                    doubleWithRightChild( t );
            }
        }
    else
        ;  // Duplicate; do nothing

    // update the height the node
    heightUpdate(t);
}





template<class Obj>
AvlTree<Obj>::AvlTree() {
    root = nullptr;
}

template<class Obj>
AvlTree<Obj>::AvlTree(Obj x) {
    root = new Node(x, nullptr, nullptr);
}


template<class Obj>
void AvlTree<Obj>::heightUpdate(AvlTree::Node *n) {
    int i = (n->left == nullptr) ? 0:n->left->height;
    int j = (n->right == nullptr) ? 0:n->right->height;

    n->height = 1 + max(i,j);
}

template<class Obj>
const int &AvlTree<Obj>::getHeight(AvlTree::Node *n) const {
    if(n == nullptr){
        return 0;
    }
    return n->height ;
}

template<class Obj>
const Obj& AvlTree<Obj>::findMax() const {
    Node* temp = root;
    while (temp->right != nullptr){
        temp = temp->right;
    }
    return temp->key;
}
template<class Obj>
const Obj &AvlTree<Obj>::findMin() const {
    Node* temp =root;
    while(root->left != nullptr){
        temp = root->left;
    }
    return temp->key;
}
template<class Obj>
const Obj &AvlTree<Obj>::find(const Obj &x) const {
    Node* temp = root;
    Obj* result = nullptr;
    while (temp != nullptr){
        if(temp->key > x){
            temp = temp->left;
        }
        else if(temp->key < x){
            temp = temp->right;
        } else{
            result = &temp->key;
            break;
        }
    }
    return result;
}
template<class Obj>

bool AvlTree<Obj>::isEmpty() const {
    return root == nullptr;
}


#endif //CS300HW2_AVL_AVLTREE_H


