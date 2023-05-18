import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import tkinter as tk
from tkinter import ttk, messagebox
import PySpice.Logging.Logging as Logging
import math

logger = Logging.setup_logging()
from PySpice.Doc.ExampleTools import find_libraries
from PySpice.Spice.Netlist import Circuit
from PySpice.Spice.Library import SpiceLibrary
from PySpice.Unit import *
from PySpice.Physics.SemiConductor import ShockleyDiode
from PySpice.Spice.Netlist import Circuit, SubCircuit
import sys

# Carga de librerias PySpice
default_library_path = "C:\\users\\andre\\Desktop"
if sys.platform == "linux":
    default_library_path = "."

spice_library = SpiceLibrary(default_library_path)


def gui():
    # instanciar tkinter
    window = tk.Tk()
    frame_texto_sp = tk.Frame(bg="white", width=30, height=20)
    frame_texto_orientacion = tk.Frame(bg="white", width=30, height=20)
    frame_texto_area_a = tk.Frame(bg="white", width=30, height=20)
    frame_texto_area_l = tk.Frame(bg="white", width=30, height=20)
    frame_texto_celula_a = tk.Frame(bg="white", width=30, height=20)
    frame_texto_celula_l = tk.Frame(bg="white", width=30, height=20)
    frame_texto_nstrings = tk.Frame(bg="white", width=30, height=20)
    frame_texto_dbypass = tk.Frame(bg="white", width=30, height=20)

    #frame texto serie/paralelo
    label_texto_sp = tk.Label(master=frame_texto_sp, text="Conexion serie o paralelo:",
                                  bg="white")  # width=10, height=1,
    label_texto_sp.pack()  # añadir la etiqueta al frame
    frame_texto_sp.pack(fill=tk.X)  # añadimos el frame a la interfaz

    # desplegable
    frame_input_sp = tk.Frame()

    combo_sp = ttk.Combobox(
        frame_input_sp,
        state='readonly',
        values=["s","p"]
    )
    combo_sp.pack()  # añadir la etiqueta al frame
    frame_input_sp.pack(fill=tk.X)

    # frame texto orientacion
    label_texto_orientacion = tk.Label(master=frame_texto_orientacion, text="Orientacion en x o en y:",
                              bg="white")  # width=10, height=1,
    label_texto_orientacion.pack()  # añadir la etiqueta al frame
    frame_texto_orientacion.pack(fill=tk.X)  # añadimos el frame a la interfaz
    # desplegable
    frame_input_orientacion = tk.Frame()

    combo_orientacion = ttk.Combobox(
        frame_input_orientacion,
        state='readonly',
        values=["x", "y"]
    )
    combo_orientacion.pack()  # añadir la etiqueta al frame
    frame_input_orientacion.pack(fill=tk.X)


    # frame texto ancho area
    label_texto_area_a = tk.Label(master=frame_texto_area_a, text="¿Cual es el ancho del area disponible (cm)?:",
                              bg="white")  # width=10, height=1,
    label_texto_area_a.pack()  # añadir la etiqueta al frame
    frame_texto_area_a.pack(fill=tk.X)  # añadimos el frame a la interfaz
    # frame input
    frame_input_area_a = tk.Frame()
    input_area_a = tk.Text(frame_input_area_a,
                       height=1,
                       width=20)
    input_area_a.pack()
    frame_input_area_a.pack(fill=tk.X)  # añadimos el frame a la interfaz
    # frame texto r2
    label_texto_area_l = tk.Label(master=frame_texto_area_l, text="¿Cual es el largo del area disponible (cm)?:",
                              bg="white")  # width=10, height=1,
    label_texto_area_l.pack()  # añadir la etiqueta al frame
    frame_texto_area_l.pack(fill=tk.X)  # añadimos el frame a la interfaz
    # frame input
    frame_input_area_l = tk.Frame()
    input_area_l = tk.Text(frame_input_area_l,
                       height=1,
                       width=20)
    input_area_l.pack()
    frame_input_area_l.pack(fill=tk.X)  # añadimos el frame a la interfaz
    # frame texto area celula ancho
    label_texto_celula_a = tk.Label(master=frame_texto_celula_a, text="Medida de la base de la celula(cm):",
                                  bg="white")  # width=10, height=1,
    label_texto_celula_a.pack()  # añadir la etiqueta al frame
    frame_texto_celula_a.pack(fill=tk.X)  # añadimos el frame a la interfaz
    # frame input
    frame_input_celula_a = tk.Frame()
    input_celula_a = tk.Text(frame_input_celula_a,
                           height=1,
                           width=20)
    input_celula_a.pack()
    frame_input_celula_a.pack(fill=tk.X)
    # frame texto area celula largo
    label_texto_celula_l = tk.Label(master=frame_texto_celula_l, text="Medida del largo de la celula(cm):",
                                    bg="white")  # width=10, height=1,
    label_texto_celula_l.pack()  # añadir la etiqueta al frame
    frame_texto_celula_l.pack(fill=tk.X)  # añadimos el frame a la interfaz
    # frame input
    frame_input_celula_l = tk.Frame()
    input_celula_l = tk.Text(frame_input_celula_l,
                             height=1,
                             width=20)
    input_celula_l.pack()
    frame_input_celula_l.pack(fill=tk.X)
    # frame texto nstrings
    label_texto_nstrings = tk.Label(master=frame_texto_nstrings, text="Numero de strings:",
                                    bg="white")  # width=10, height=1,
    label_texto_nstrings.pack()  # añadir la etiqueta al frame
    frame_texto_nstrings.pack(fill=tk.X)  # añadimos el frame a la interfaz
    # frame input
    frame_input_nstrings  = tk.Frame()
    input_nstrings = tk.Text(frame_input_nstrings,
                             height=1,
                             width=20)
    input_nstrings .pack()
    frame_input_nstrings .pack(fill=tk.X)
    #frame texto diodo
    label_texto_dbypass = tk.Label(master=frame_texto_dbypass, text="Indique la conexión del diodo bypass:",
                                  bg="white")  # width=10, height=1,
    label_texto_dbypass.pack()  # añadir la etiqueta al frame
    frame_texto_dbypass.pack(fill=tk.X)  # añadimos el frame a la interfaz
    # desplegable
    frame_input_dbypass = tk.Frame()

    combo_dbypass = ttk.Combobox(
        frame_input_dbypass,
        state='readonly',
        values=["Sin diodo", "Diodo por string", "Diodo por celula"]
    )
    combo_dbypass.pack()  # añadir la etiqueta al frame
    frame_input_dbypass.pack(fill=tk.X)
    # frame button
    frame_button = tk.Frame()
    button = tk.Button(
        text="ok",
        fg="White",
        bg="Black",
        width=5,
        height=1,
        command=lambda: guardar(combo_sp,
                                combo_orientacion,
                                input_area_a,
                                input_area_l,
                                input_celula_a,
                                input_celula_l,
                                input_nstrings,
                                combo_dbypass)  # metodo guardar información
    )
    # Add widget to a window
    button.pack()
    frame_button.pack(fill=tk.X)
    window.mainloop()
def trasponer(ancho,largo,base_celula,altura_celula,orientacion):
    n_filas = math.floor(ancho / altura_celula)
    n_columnas = math.floor(largo / base_celula)
    celulas_totales = n_filas * n_columnas
    if orientacion == 'y':
        n_filas,n_columnas=n_columnas,n_filas
    print("Numero de filas: {}".format(n_filas))
    print("Numero de columnas: {}".format(n_columnas))

    return n_filas,n_columnas
def pop_up(texto):
    messagebox.showwarning('Datos incorrectos',texto)
def datos_correctos(n_filas,n_strings):

    # Comprobar si n_strings es multiplo de n_filas
    if n_filas % n_strings != 0:
        pop_up('Introduce un multiplo de {} menor o igual:'.format(n_filas))
        return False
    return True

def guardar(sp,orientacion,area_a,area_l,celula_a,celula_l,nstrings,dbypass):
    # ancho=input_area_a.get(1.0, "end-1c")
    conexion = sp.get()
    orientacion = orientacion.get()
    ancho = int(area_a.get(1.0, "end-1c"))
    largo = int(area_l.get(1.0, "end-1c"))
    base_celula = int(celula_a.get(1.0, "end-1c"))
    altura_celula = int(celula_l.get(1.0, "end-1c"))
    nstrings = int(nstrings.get(1.0, "end-1c"))
    dbypass =dbypass.get()
    print(conexion,orientacion,ancho,largo,base_celula,altura_celula,nstrings)
    n_filas,n_columnas=trasponer(ancho,largo, base_celula, altura_celula, orientacion)
    n_celulas_string, lim=celulas_por_string(n_filas,nstrings,n_columnas,orientacion)
    if datos_correctos(n_filas,nstrings):

        m = crear_matriz(nstrings, n_celulas_string)
        modulo_fotovoltaico = crear_modulo_fotovoltaico(conexion, orientacion,nstrings, n_celulas_string, dbypass, m)
        #modulo_fotovoltaico = crear_modulo_fotovoltaico(conexion=conex, orientacion=orientacion, strings=strings, n_celula_string=n_celula_string,
                                                        #bypass=d_bypass)
        sim = simulacion(modulo_fotovoltaico,lim)
        intensidad, voltage = extraer_valores(sim)
        dibujar(intensidad, voltage,lim)

def crear_circuito_serie(strings, n_celula_string, bypass, m):
    """ Creamos circuito """
    I = 0.03944 @ u_A
    circuit = Circuit('Test')
    circuit.include(spice_library['1N4148'])
    circuit.model('Bypass', 'D', IS=3e-7, RS=2.9 / 1000, N=0.01, EG=0.1, XTI=3, BV=600, IBV=1e-5, CJO=1.36534e-10,
                  M=0.743776, VJ=0.781554, FC=0.5, TT=5.54918e-8, KF=0, AF=1)
    #circuit.R('neg', 's1_n1_1', circuit.gnd, 0.02 @ u_Ω)
    circuit.I('1_1', circuit.gnd, 'in1_1', I*m[0][0])
    circuit.X('D1_1', '1N4148', 'in1_1', circuit.gnd)
    circuit.R('p1_1', 'in1_1', circuit.gnd, 604711 @ u_Ω)
    circuit.R('s1_1', 'in1_1', 'vin1_1', 1.6 @ u_Ω)
    if not n_celula_string == 1:
        circuit.R('c1_1','vin1_1','vout2_1',0.02 @ u_Ω)


    if bypass == 'Sin diodo':
        for j in range(1, strings + 1):
            for i in range(1, n_celula_string + 1):
                if not (j == 1 and i == 1):
                    circuit.I('{}_{}'.format(i, j), 'vout{}_{}'.format(i, j), 'in{}_{}'.format(i, j), I*m[j-1][i-1])
                    circuit.X('D{}_{}'.format(i, j), '1N4148', 'in{}_{}'.format(i, j), 'vout{}_{}'.format(i, j))
                    circuit.R('p{}_{}'.format(i, j), 'in{}_{}'.format(i, j), 'vout{}_{}'.format(i, j), 604711 @ u_Ω)
                    circuit.R('s{}_{}'.format(i, j), 'in{}_{}'.format(i, j), 'vin{}_{}'.format(i, j), 1.6 @ u_Ω)
                    if not i == n_celula_string:
                        circuit.R('c{}_{}'.format(i, j), 'vin{}_{}'.format(i, j), 'vout{}_{}'.format(i + 1, j),
                                  0.02 @ u_Ω)
            if not j == strings:
                circuit.R('c{}_{}'.format(i,j), 'vin{}_{}'.format(i, j), 'vout1_{}'.format(j + 1), 0.02 @ u_Ω)



    elif bypass == 'Diodo por string':
        #Bucle
        for j in range(1, strings + 1):
            for i in range(1, n_celula_string + 1):
                if not (i == 1 and j == 1):
                    circuit.I('{}_{}'.format(i, j), 'vout{}_{}'.format(i, j), 'in{}_{}'.format(i, j), I*m[j-1][i-1])
                    circuit.X('D{}_{}'.format(i, j), '1N4148', 'in{}_{}'.format(i, j), 'vout{}_{}'.format(i, j))
                    circuit.R('p{}_{}'.format(i, j), 'in{}_{}'.format(i, j), 'vout{}_{}'.format(i, j), 604711 @ u_Ω)
                    circuit.R('s{}_{}'.format(i, j), 'in{}_{}'.format(i, j), 'vin{}_{}'.format(i, j), 1.6 @ u_Ω)
                    if not i == n_celula_string:
                        circuit.R('c{}_{}'.format(i, j), 'vin{}_{}'.format(i, j), 'vout{}_{}'.format(i + 1, j),
                                  0.02 @ u_Ω)
            circuit.Diode('Bypass{}'.format(j), 'in1_{}'.format(j), 'vin{}_{}'.format(n_celula_string, j),
                          model='Bypass')
            if not j == strings:
                circuit.R('c{}_{}'.format(i,j), 'vin{}_{}'.format(i, j), 'vout1_{}'.format(j + 1), 0.02 @ u_Ω)




    elif bypass == 'Diodo por celula':
        # Bucle
         for j in range(1, strings + 1):
            for i in range(1, n_celula_string + 1):
                if not (i == 1 and j == 1):
                    circuit.I('{}_{}'.format(i, j), 'vout{}_{}'.format(i, j), 'in{}_{}'.format(i, j), I*m[j-1][i-1])
                    circuit.X('D{}_{}'.format(i, j), '1N4148', 'in{}_{}'.format(i, j), 'vout{}_{}'.format(i, j))
                    circuit.R('p{}_{}'.format(i, j), 'in{}_{}'.format(i, j), 'vout{}_{}'.format(i, j), 604711 @ u_Ω)
                    circuit.R('s{}_{}'.format(i, j), 'in{}_{}'.format(i, j), 'vin{}_{}'.format(i, j), 1.6 @ u_Ω)
                    circuit.Diode('Bypass{}_{}'.format(i,j), 'in{}_{}'.format(i, j), 'vin{}_{}'.format(i, j), model='Bypass')
                    if not i == n_celula_string:
                        circuit.R('c{}_{}'.format(i, j), 'vin{}_{}'.format(i, j), 'vout{}_{}'.format(i + 1, j),
                                  0.02 @ u_Ω)

            if not j == strings:
                circuit.R('c{}_{}'.format(i,j), 'vin{}_{}'.format(i, j), 'vout1_{}'.format(j + 1), 0.02 @ u_Ω)

    circuit.R('cc', 'vin{}_{}'.format(n_celula_string, strings), 'pos', 0.020 @ u_Ω)
    circuit.V('bias', 'pos', 'vout{}_{}'.format(n_celula_string, strings), 1 @ u_V)
    print(circuit)
    return circuit


def crear_circuito_paralelo(strings,n_celula_string, bypass, m):
    """ Creamos circuito """
    I = 0.03944 @ u_A
    circuit = Circuit('Test')
    circuit.include(spice_library['1N4148'])
    circuit.model('Bypass', 'D', IS=3e-7, RS=2.9 / 1000, N=0.01, EG=0.1, XTI=3, BV=600, IBV=1e-5, CJO=1.36534e-10,
                  M=0.743776, VJ=0.781554, FC=0.5, TT=5.54918e-8, KF=0, AF=1)
    #circuit.R('neg', circuit.gnd, 's1_n1_1', 0.02 @ u_Ω)

    if bypass == 'Sin diodo':

        for j in range(1, strings + 1):
            circuit.I('1_{}'.format(j), circuit.gnd, 'in1_{}'.format(j), I*m[j-1][0])
            circuit.X('D1_{}'.format(j), '1N4148', 'in1_{}'.format(j), circuit.gnd)
            circuit.R('p1_{}'.format(j), 'in1_{}'.format(j), circuit.gnd, 604711 @ u_Ω)
            circuit.R('s1_{}'.format(j), 'in1_{}'.format(j), 'vin1_{}'.format(j), 1.6 @ u_Ω)
            if not n_celula_string == 1:
                circuit.R('c1_{}'.format(j), 'vin1_{}'.format(j), 'vout2_{}'.format(j), 0.02 @ u_Ω)

            for i in range(2, n_celula_string + 1):
                circuit.I('{}_{}'.format(i, j), 'vout{}_{}'.format(i, j), 'in{}_{}'.format(i, j), I*m[j-1][i-1])
                circuit.X('D{}_{}'.format(i, j), '1N4148', 'in{}_{}'.format(i, j), 'vout{}_{}'.format(i, j))
                circuit.R('p{}_{}'.format(i, j), 'in{}_{}'.format(i, j), 'vout{}_{}'.format(i, j), 604711 @ u_Ω)
                circuit.R('s{}_{}'.format(i, j), 'in{}_{}'.format(i, j), 'vin{}_{}'.format(i, j), 1.6 @ u_Ω)

                if not i == n_celula_string:
                    circuit.R('c{}_{}'.format(i, j), 'vin{}_{}'.format(i, j), 'vout{}_{}'.format(i + 1, j), 0.02 @ u_Ω)

            circuit.R('c{}'.format(j), 'vin{}_{}'.format(n_celula_string, j), 'pos', 0.02 @ u_Ω)


    elif bypass == 'Diodo por string':
        for j in range(1, strings + 1):
            circuit.I('1_{}'.format(j), circuit.gnd, 'in1_{}'.format(j), I*m[j-1][0])
            circuit.X('D1_{}'.format(j), '1N4148', 'in1_{}'.format(j), circuit.gnd)
            circuit.R('p1_{}'.format(j), 'in1_{}'.format(j), circuit.gnd, 604711 @ u_Ω)
            circuit.R('s1_{}'.format(j), 'in1_{}'.format(j), 'vin1_{}'.format(j), 1.6 @ u_Ω)
            if not n_celula_string == 1:
                circuit.R('c1_{}'.format(j), 'vin1_{}'.format(j), 'vout2_{}'.format(j), 0.02 @ u_Ω)

            for i in range(2, n_celula_string + 1):
                circuit.I('{}_{}'.format(i, j), 'vout{}_{}'.format(i, j), 'in{}_{}'.format(i, j), I*m[j-1][i-1])
                circuit.X('D{}_{}'.format(i, j), '1N4148', 'in{}_{}'.format(i, j), 'vout{}_{}'.format(i, j))
                circuit.R('p{}_{}'.format(i, j), 'in{}_{}'.format(i, j), 'vout{}_{}'.format(i, j), 604711 @ u_Ω)
                circuit.R('s{}_{}'.format(i, j), 'in{}_{}'.format(i, j), 'vin{}_{}'.format(i, j), 1.6 @ u_Ω)

                if not i == n_celula_string:
                    circuit.R('c{}_{}'.format(i, j), 'vin{}_{}'.format(i, j), 'vout{}_{}'.format(i + 1, j), 0.02 @ u_Ω)
            circuit.Diode('Bypass{}'.format(j), 'in1_{}'.format(j), 'vin{}_{}'.format(n_celula_string, j),
                          model='Bypass')

            circuit.R('c{}'.format(j), 'vin{}_{}'.format(n_celula_string, j), 'pos', 0.02 @ u_Ω)

    elif bypass == 'Diodo por celula':

        for j in range(1, strings + 1):
            circuit.I('1_{}'.format(j), circuit.gnd, 'in1_{}'.format(j), I*m[j-1][0])
            circuit.X('D1_{}'.format(j), '1N4148', 'in1_{}'.format(j), circuit.gnd)
            circuit.R('p1_{}'.format(j), 'in1_{}'.format(j), circuit.gnd, 604711 @ u_Ω)
            circuit.R('s1_{}'.format(j), 'in1_{}'.format(j), 'vin1_{}'.format(j), 1.6 @ u_Ω)
            if not n_celula_string == 1:
                circuit.R('c1_{}'.format(j), 'vin1_{}'.format(j), 'vout2_{}'.format(j), 0.02 @ u_Ω)

            for i in range(2, n_celula_string + 1):
                circuit.I('{}_{}'.format(i, j), 'vout{}_{}'.format(i, j), 'in{}_{}'.format(i, j), I*m[j-1][i-1])
                circuit.X('D{}_{}'.format(i, j), '1N4148', 'in{}_{}'.format(i, j), 'vout{}_{}'.format(i, j))
                circuit.R('p{}_{}'.format(i, j), 'in{}_{}'.format(i, j), 'vout{}_{}'.format(i, j), 604711 @ u_Ω)
                circuit.R('s{}_{}'.format(i, j), 'in{}_{}'.format(i, j), 'vin{}_{}'.format(i, j), 1.6 @ u_Ω)
                circuit.Diode('Bypass{}_{}'.format(i, j), 'in{}_{}'.format(i, j), 'vin{}_{}'.format(i, j),
                              model='Bypass')
                if not i == n_celula_string:
                    circuit.R('c{}_{}'.format(i, j), 'vin{}_{}'.format(i, j), 'vout{}_{}'.format(i + 1, j), 0.02 @ u_Ω)

            circuit.R('c{}'.format(j), 'vin{}_{}'.format(n_celula_string, j), 'pos', 0.02 @ u_Ω)

    circuit.V('bias', 'pos', circuit.gnd, 1 @ u_V)
    print(circuit)
    return circuit


def simulacion(circuit,lim):
    """ Para cada resistencia sacamos intensidad """
   # for resistance in (circuit.Rpos):
    #    resistance.plus.add_current_probe(circuit)
    simulator = circuit.simulator(temperature=25, nominal_temperature=25)
    analysis = simulator.dc(Vbias=slice(0, lim, 0.01))
    return analysis


def extraer_valores(analysis):
    """ Extraer corriente y voltage dado el analisis """
    current = analysis.branches['vbias']
    voltage = analysis.nodes['pos']
    return current, voltage


def dibujar(intensidad, voltage, lim):
    """ Grafica tension frente a intensidad """
    plt.xlabel('Voltage [V]')
    plt.ylabel('Current')
    plt.ylim(0, 0.5, 0.3)
    plt.xlim(0, lim)
    plt.plot(voltage, intensidad)
    plt.show()


def devolver_conexion():
    """  """
    while True:
        conexion = input("¿Quieres conectar las células del módulo en serie o en paralelo? (s/p)")
        if conexion == 's' or conexion == 'p':
            break
    return conexion


def devolver_orientacion():
    while True:
        orientacion_strings = input("¿En que dirección quieres orientar los strings del módulo? (x/y)")
        if orientacion_strings == 'x' or orientacion_strings == 'y':
            break
    return orientacion_strings


def numero_strings(orientacion):
    ancho = int(input("¿Cual es el ancho del area disponible (cm2)?: "))
    largo = int(input("¿Cual es el largo del area disponible(cm2)?:  "))
    x = int(input("Medida de la base de la celula(cm2): "))
    y = int(input("Medida de la altura de la celula(cm2): "))
    # Si la disivision de n_filas y n_columnas no da un entero, coger la parte entera del decimal
    n_filas = math.floor(ancho / y)
    n_columnas = math.floor(largo / x)
    celulas_totales = n_filas * n_columnas
    while True:
        n_strings = int(input("Numero de strings:"))
        # Comprobar si n_strings es multiplo de n_filas
        if n_filas % n_strings != 0:
            n_strings = int(input("Introduce un multiplo de {} menor o igual:".format(n_filas)))
            if n_strings > n_filas:
                n_strings = int(input("Introduce un multiplo de {} menor o igual:".format(n_filas)))
            break
        break
    #si la orientacion es y cambiar filas por columna
    if orientacion == 'y':
        n_filas,n_columnas=n_columnas,n_filas
    print("Numero de filas: {}".format(n_filas))
    print("Numero de columnas: {}".format(n_columnas))
    return n_filas, n_strings, n_columnas


def celulas_por_string(filas, strings, columnas, orientacion):
    n_celulas = math.floor(filas / strings)
    print("Numero de celulas por string: {}".format(n_celulas))
    """"
     #Si la orientacion del modulo es y el numero de celulas por string se calcula a raiz de las columnas
    if orientacion == 'y':
        n_celulas = math.floor(columnas / strings)
    """
    lim = n_celulas * strings
    return n_celulas, lim



def diodo_bypass():
    while True:
        bypass = int(input(
            "Indica la opcion deseada:\n 1.Diseño sin diodo bypass\n 2.Diseño con diodo bypass por string\n 3.Diseño con diodo bypass por celula"))
        if bypass == 1 or bypass == 2 or bypass == 3:
            break
    return bypass


def crear_modulo_fotovoltaico(conexion, orientacion, strings, n_celula_string, bypass,m):
    if conexion == 's':
        return crear_circuito_serie(strings, n_celula_string, bypass,m)

    elif conexion == 'p':
        return crear_circuito_paralelo(strings, n_celula_string, bypass, m)


def crear_matriz(strings, n_celula_string):
    """ """
    m_irradiancia = np.random.randint(1, 2, (strings, n_celula_string))
    print(m_irradiancia)
    return m_irradiancia


if __name__ == "__main__":
    """
    conex = devolver_conexion()
    orientacion = devolver_orientacion()
    filas, strings ,columnas = numero_strings(orientacion)
    n_celula_string, lim = celulas_por_string(filas,strings, columnas, orientacion)
    d_bypass = diodo_bypass()
    m = crear_matriz(strings, n_celula_string)
    modulo_fotovoltaico = crear_modulo_fotovoltaico(conex,orientacion,strings,n_celula_string,d_bypass,m)
    #modulo_fotovoltaico = crear_modulo_fotovoltaico(conexion=conex, orientacion=orientacion, strings=strings, n_celula_string=n_celula_string,
                                                    #bypass=d_bypass)
    sim = simulacion(modulo_fotovoltaico,lim)
    intensidad, voltage = extraer_valores(sim)
    dibujar(intensidad, voltage,lim)
    """
    gui()
