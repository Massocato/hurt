import tkinter as tk

root = tk.Tk()
root.geometry("600x540")

# Função para inserir o texto na área de texto
def inserir_victoria():
    texto = '\n'.join([''.join([('victoria'[(x-y)%len('victoria')] if 
                                 ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else ' ') 
                                 for x in range(-30, 30)]) 
                                 for y in range(15, -15, -1)])
    inserirTexto.delete(1.0, "end")
    inserirTexto.insert(1.0, texto)

# Criando a área de texto onde a arte será exibida
inserirTexto = tk.Text(root, height=30)
inserirTexto.pack()

# Criando o botão que chama a função de exibir o texto
botao = tk.Button(root, 
                  height=1, 
                  width=10, 
                  text="victoria",
                  command=inserir_victoria)
botao.pack()

root.mainloop()
