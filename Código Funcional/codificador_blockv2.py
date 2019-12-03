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

    def __init__(self, message='',paridade=''):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Codificador',   # will show up in GRC
            in_sig=[np.uint8],
            out_sig=[np.uint8]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.message = message
        self.paridade = paridade 



    class codificador(blk):
        #Tomando o exemplo do código de Hamming -> 4 bits de mensagem e 3 bits de paridade
        #atributos : bits de paridade, tamanho   
        # Packed to unpacked -> para não depender dos parâmetros do meu bloco : separo bytes bit a bit e crio
        # uma lógica para receber os bits para que caracterize a mensagem     

        def__init__(
            self,
            k_par='',
            v_msg = ''):
 
            self.k_par = k_par # Número de bits paridade
            self.v_msg = v_msg  # Número de bits de mensagem 
            self.n_cod = self.v_msg+self.k_par # vetor código
            self.matrix = np.zeros((self.k_par,self.n_cod)) # declarando a matriz geradora

            def matrix(self,self.matrix):
                ident = np.zeros((self.k_par,self.n_cod)) # criando a matriz identidade "deslocada"
                for i in range(self.k_par):
                    for j in range(self.n_cod):
                        if j == i+self.k_par-1:
                        ident[i,j] = 1
                        else:
                        ident[i,j] = 0 

                 for i in range(self.k_par):
                    for j in range(self.n_cod):
                        if j <= i+self.k_par-1:
                        ident[i,j] = 1         # codificação de Hamming(mais simples por enquanto)


                self.matrix = ident
                return self.matrix          #Executando a codificação mais simples
                        
                        
                        

    def work(self, input_items, output_items):
         G = codificador()
         G.k_par = paridade
         G.v_msg = message
         

        
        while True:
            v = v.append(input_items[0,7])
            if len(v) = message:
                break

        c = np.dot(v,G.matrix)

        output_items[0][:] = c
        return output_items



