#include <iostream>

using namespace std;


class nodo {

    public:
        nodo (int dato, nodo *siguiente = NULL) {
            int d = dato;
            nodo *sig = siguiente;
        }

     private:
        nodo *sig;
        int d;

    friend class lista;

};

class lista {
    nodo *h;

    public:
    void inicializar(){
        h = NULL;
    }

    void insertarPrincipio(int dato){
        nodo *tmp;

        tmp = h;
        h->sig = tmp;
        h->d = dato;
    }

    void mostrar(){
        nodo *tmp;
        tmp = h;
        while (h!=NULL){
            cout << tmp->d << endl;
            tmp = tmp->sig;
        }
    }
};


int main () {

    lista Lista;

    Lista.inicializar();
    Lista.insertarPrincipio(3);
    Lista.insertarPrincipio(2);
    Lista.insertarPrincipio(1);
    Lista.mostrar();
}
