"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, message=message,paridade=paridade):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Decodificador',   # will show up in GRC
            in_sig=[np.uint8],
            out_sig=[np.uint8]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.message = message
        self.paridade = paridade


    class decodificador(blk):

          
           def __init__(self,
            k_par='',
            v_msg=''):
            
            self.k_par = k_par #Número de bits de paridade 
            self.v_msg = v_msg #Número de bits de mensagem
            self.n_cod = self.k_par+self.v_msg
            self.matrix = np.zeros((k_par,n_cod)) # Matriz decodificadora


            def matrix(self,self.matrix):
                H_aux = np.zeros((k_par,n_cod)) #Declarando a matriz decodificadora
                
                for i in range(p):#Criando a matriz decodificadora apenas com a identidade
                    for j in range(n):
                        if j<k-1 and i==j:
                            H_aux[i,j]=1

                P_aux = np.zeros((p,n)) # Declarando matriz de paridade transposta

                for i in range(p):
                    for j in range(n):
                        if j >= k-1:
                          P_aux[i,j] = 1

                H = H_aux+P_aux
                self.matrxi = H
                return self.matrix





    def work(self, input_items, output_items):
        H = decodificador()
        H.k_par = paridade
        H.v_msg = message
        v = []
        while True:
            v = v.append(input_items[0,7])
            if len(v) = message:
                break

        c = np.dot(v,H.matrix)

        output_items[0][:] = c
        return output_items
