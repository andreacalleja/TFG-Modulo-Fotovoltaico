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
import os
import datetime

# Carga de librerias PySpice
default_library_path = "C:\\users\\andre\\Desktop"
if sys.platform == "linux":
    default_library_path = "."

spice_library = SpiceLibrary(default_library_path)


def gui():
    # instanciar tkinter
    window = tk.Tk()
    frame_texto_nombre = tk.Frame(bg="white", width=30, height=20)
    frame_texto_descripcion = tk.Frame(bg="white", width=30, height=30)
    frame_texto_sp = tk.Frame(bg="white", width=30, height=20)
    frame_texto_orientacion = tk.Frame(bg="white", width=30, height=20)
    frame_texto_area_a = tk.Frame(bg="white", width=30, height=20)
    frame_texto_area_l = tk.Frame(bg="white", width=30, height=20)
    frame_texto_celula_a = tk.Frame(bg="white", width=30, height=20)
    frame_texto_celula_l = tk.Frame(bg="white", width=30, height=20)
    frame_texto_nstrings = tk.Frame(bg="white", width=30, height=20)
    frame_texto_intensidad = tk.Frame(bg="white", width=30, height=30)
    frame_texto_Rs = tk.Frame(bg="white", width=30, height=20)
    frame_texto_Rsh = tk.Frame(bg="white", width=30, height=20)
    frame_texto_temp = tk.Frame(bg="white", width=30, height=20)
    frame_texto_dbypass = tk.Frame(bg="white", width=30, height=20)
    frame_texto_sombra = tk.Frame(bg="white", width=30, height=20)

    # frame texto nombre
    label_texto_nombre = tk.Label(master=frame_texto_nombre,
                                  text="Nombre del modelo:",
                                  bg="white")  # width=10, height=1,
    label_texto_nombre.pack()  # añadir la etiqueta al frame
    frame_texto_nombre.pack(fill=tk.X)  # añadimos el frame a la interfaz
    # frame input
    frame_input_nombre = tk.Frame()
    input_nombre = tk.Text(frame_input_nombre,
                           height=1,
                           width=20)
    input_nombre.pack()
    frame_input_nombre.pack(fill=tk.X)  # añadimos el frame a la interfaz

    # frame texto descripcion
    label_texto_descripcion = tk.Label(master=frame_texto_descripcion,
                                  text="Descripcion del modelo:",
                                  bg="white")  # width=10, height=1,
    label_texto_descripcion.pack()  # añadir la etiqueta al frame
    frame_texto_descripcion.pack(fill=tk.X)  # añadimos el frame a la interfaz
    # frame input
    frame_input_descripcion = tk.Frame()
    input_descripcion = tk.Text(frame_input_descripcion,
                           height=1,
                           width=20)
    input_descripcion.pack()
    frame_input_descripcion.pack(fill=tk.X)  # añadimos el frame a la interfaz

    # frame texto serie/paralelo
    label_texto_sp = tk.Label(master=frame_texto_sp,
                              text="Conexion serie o paralelo:",
                              bg="white")  # width=10, height=1,
    label_texto_sp.pack()  # añadir la etiqueta al frame
    frame_texto_sp.pack(fill=tk.X)  # añadimos el frame a la interfaz

    # desplegable
    frame_input_sp = tk.Frame()

    combo_sp = ttk.Combobox(
        frame_input_sp,
        state='readonly',
        values=["s", "p"]
    )
    combo_sp.pack()  # añadir la etiqueta al frame
    frame_input_sp.pack(fill=tk.X)

    # frame texto orientacion
    label_texto_orientacion = tk.Label(master=frame_texto_orientacion,
                                       text="Orientacion en x o en y:",
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
    label_texto_area_a = tk.Label(master=frame_texto_area_a,
                                  text="¿Base del area disponible (cm)?:",
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
    # frame texto largo area
    label_texto_area_l = tk.Label(master=frame_texto_area_l,
                                  text="¿Altura del area disponible (cm)?:",
                                  bg="white")  # width=10, height=1,
    label_texto_area_l.pack()  # añadir la etiqueta al frame
    frame_texto_area_l.pack(fill=tk.X)  # añadimos el frame a la interfaz
    # frame input
    frame_input_area_l = tk.Frame()
    input_area_l = tk.Entry(frame_input_area_l,
                            # height=1,
                            # width=20
                            )
    input_area_l.pack()
    frame_input_area_l.pack(fill=tk.X)  # añadimos el frame a la interfaz
    # frame texto area celula ancho
    label_texto_celula_a = tk.Label(master=frame_texto_celula_a,
                                    text="Medida de la base de la celula(cm):",
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
    label_texto_celula_l = tk.Label(master=frame_texto_celula_l,
                                    text="Medida del largo de la celula(cm):",
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
    label_texto_nstrings = tk.Label(master=frame_texto_nstrings,
                                    text="Numero de strings:",
                                    bg="white")  # width=10, height=1,
    label_texto_nstrings.pack()  # añadir la etiqueta al frame
    frame_texto_nstrings.pack(fill=tk.X)  # añadimos el frame a la interfaz
    # frame input
    frame_input_nstrings = tk.Frame()
    input_nstrings = tk.Text(frame_input_nstrings,
                             height=1,
                             width=20)
    input_nstrings.pack()
    frame_input_nstrings.pack(fill=tk.X)

    # frame texto intensidad
    label_texto_intensidad = tk.Label(master=frame_texto_intensidad,
                                    text="Indique el valor de la densidad de corriente (A/cm2):",
                                    bg="white")  # width=10, height=1,
    label_texto_intensidad.pack()  # añadir la etiqueta al frame
    frame_texto_intensidad.pack(fill=tk.X)  # añadimos el frame a la interfaz
    # frame input
    frame_input_intensidad = tk.Frame()
    input_intensidad= tk.Text(frame_input_intensidad,
                             height=1,
                             width=20)
    input_intensidad.pack()
    frame_input_intensidad.pack(fill=tk.X)

    # frame texto Rs
    label_texto_Rs = tk.Label(master=frame_texto_Rs,
                                  text="Indique el valor de Rs (Ohm·cm2):",
                                  bg="white")  # width=10, height=1,
    label_texto_Rs.pack()  # añadir la etiqueta al frame
    frame_texto_Rs.pack(fill=tk.X)  # añadimos el frame a la interfaz
    # frame input
    frame_input_Rs = tk.Frame()
    input_Rs = tk.Text(frame_input_Rs,
                           height=1,
                           width=20)
    input_Rs.pack()
    frame_input_Rs.pack(fill=tk.X)  # añadimos el frame a la interfaz

    # frame texto Rsh
    label_texto_Rsh = tk.Label(master=frame_texto_Rsh,
                                  text="Indique el valor de Rp (Ohm·cm2):",
                                  bg="white")  # width=10, height=1,
    label_texto_Rsh.pack()  # añadir la etiqueta al frame
    frame_texto_Rsh.pack(fill=tk.X)  # añadimos el frame a la interfaz
    # frame input
    frame_input_Rsh = tk.Frame()
    input_Rsh = tk.Text(frame_input_Rsh,
                           height=1,
                           width=20)
    input_Rsh.pack()
    frame_input_Rsh.pack(fill=tk.X)  # añadimos el frame a la interfaz
    # frame texto temperatura de simulación
    label_texto_temp = tk.Label(master=frame_texto_temp,
                                  text="Indique la temperatura de simulación (ªC):",
                                  bg="white")  # width=10, height=1,
    label_texto_temp.pack()  # añadir la etiqueta al frame
    frame_texto_temp.pack(fill=tk.X)  # añadimos el frame a la interfaz
    # frame input
    frame_input_temp = tk.Frame()
    input_temp = tk.Text(frame_input_temp,
                           height=1,
                           width=20)
    input_temp.pack()
    frame_input_temp.pack(fill=tk.X)  # añadimos el frame a la interfaz
    # frame texto diodo
    label_texto_dbypass = tk.Label(master=frame_texto_dbypass,
                                   text="Indique la conexión del diodo bypass:",
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
    # frame texto sombra
    label_texto_sombra = tk.Label(master=frame_texto_sombra,
                                  text="Indique el patrón de sombreado:",
                                  bg="white")  # width=10, height=1,
    label_texto_sombra.pack()  # añadir la etiqueta al frame
    frame_texto_sombra.pack(fill=tk.X)  # añadimos el frame a la interfaz
    # desplegable
    frame_input_sombra = tk.Frame()

    combo_sombra = ttk.Combobox(
        frame_input_sombra,
        state='readonly',
        values=["Patrón aleatorio", "Patrón personalizado"]
    )
    combo_sombra.pack()  # añadir la etiqueta al frame
    frame_input_sombra.pack(fill=tk.X)

    # frame button
    frame_button = tk.Frame()
    button = tk.Button(
        text="ok",
        fg="White",
        bg="Black",
        width=5,
        height=1,
        command=lambda: guardar(input_nombre,
                                input_descripcion,
                                combo_sp,
                                combo_orientacion,
                                input_area_a,
                                input_area_l,
                                input_celula_a,
                                input_celula_l,
                                input_nstrings,
                                input_intensidad,
                                input_Rs,
                                input_Rsh,
                                input_temp,
                                combo_dbypass,
                                combo_sombra)  # metodo guardar información
    )
    # Add widget to a window
    button.pack()
    frame_button.pack(fill=tk.X)

    # Create GUI
    window.mainloop()


def guardar_fichero(intensidad, voltage,nombre,descripcion,conexion,orientacion,area_a,area_l,ancho,altura_celula,nstrings,fuente_intensidad,Rs,Rsh,temp,dbypass,m):
    """ TODO añadir descripcion metodo """

    ruta_absoluta = os.path.abspath('.')
    ruta_absoluta = os.path.join(ruta_absoluta, 'output')

    date = datetime.datetime.now()
    out_file = "{}_{}_{}_{}_{}_{}_{}.csv".format(nombre,
                                                    date.year,
                                                    date.month,
                                                    date.day,
                                                    date.hour,
                                                    date.minute,
                                                    date.second)

    ruta_absoluta = os.path.join(ruta_absoluta, out_file)

    out_wd = open(ruta_absoluta, 'w')

    if len(intensidad) != len(voltage):
        print("#" * 50)
        print("Error")
        sys.exit(0)

    out_wd.write("Descripción del modelo: {}\n".format(descripcion))

    out_wd.write("Conexion: {} "
                 "Orientacion: {} "
                 "Base modulo (cm): {} "
                 "Altura modulo (cm): {} "
                 "Base célula (cm): {} "
                 "Altura célua (cm): {} "
                 "Numero de strings: {} "
                 "Densidad de corriente (A/cm2): {} "
                 "Rs (Ohm·cm2): {} "
                 "Rsh (Ohm·cm2): {} "
                 "Temperatura de simulación (ªC): {} "
                 "Conexion bypass: {} \n".format(conexion,
                                                 orientacion,
                                                 area_a,
                                                 area_l,
                                                 ancho,
                                                 altura_celula,
                                                 nstrings,
                                                 fuente_intensidad,
                                                 Rs,
                                                 Rsh,
                                                 temp,
                                                 dbypass))
    out_wd.write("Patrón de sombreado: {}\n".format(str(m).replace("\n", "")))

    out_wd.write("Voltaje (V), Intensidad (A)\n")

    for index in range(len(intensidad)):
        out_wd.write("{}, {}\n".format(round(float(voltage[index]), 2),
                                       round(float(intensidad[index]), 3))
                     )

    pop_up("Simulación guardada en: {}".format(ruta_absoluta))


def trasponer(ancho, largo, base_celula, altura_celula, orientacion):
    """ TODO añadir descripcion metodo """

    n_filas = math.floor(largo / altura_celula)
    n_columnas = math.floor(ancho / base_celula)
    celulas_totales = n_filas * n_columnas
    if orientacion == 'y':
        #n_filas, n_columnas = n_columnas, n_filas
        n_filas = math.floor(ancho / altura_celula)
        n_columnas = math.floor(largo / base_celula)
    print("Numero de filas: {}".format(n_filas))
    print("Numero de columnas: {}".format(n_columnas))

    return n_filas, n_columnas


def pop_up(texto):
    """ Pop-up con mensaje quepasado por parametro """
    messagebox.showwarning('Aviso', texto)


def datos_correctos(n_filas, n_strings):
    """ Comprobar si n_strings es multiplo de n_filas """
    if n_filas % n_strings != 0:
        pop_up('DATOS INCORRECTOS: Introduce para el numero de strings un multiplo de {} menor o igual:'.format(n_filas))
        return False
    return True


def guardar(nombre,
            descripcion,
            sp,
            orientacion,
            area_a,
            area_l,
            celula_a,
            celula_l,
            nstrings,
            intensidad,
            Rs,
            Rsh,
            temp,
            dbypass,
            sombra):
    """ TODO añadir descripcion """
    # ancho=input_area_a.get(1.0, "end-1c")
    nombre=nombre.get(1.0, "end-1c")
    descripcion=descripcion.get(1.0, "end-1c")
    conexion = sp.get()
    orientacion = orientacion.get()
    ancho = float(area_a.get(1.0, "end-1c"))
    largo = float(area_l.get())
    # largo = int(area_l.get(1.0, "end-1c"))
    base_celula = float(celula_a.get(1.0, "end-1c"))
    altura_celula = float(celula_l.get(1.0, "end-1c"))
    nstrings = int(nstrings.get(1.0, "end-1c"))
    fuente_intensidad=float(intensidad.get(1.0, "end-1c"))
    Rs=float(Rs.get(1.0, "end-1c"))
    Rsh=float(Rsh.get(1.0, "end-1c"))
    temp=float(temp.get(1.0, "end-1c"))
    dbypass = dbypass.get()
    sombra = sombra.get()
    area_celula=float(base_celula*altura_celula)
    print(conexion, orientacion, ancho, largo, base_celula, altura_celula,
          nstrings)
    n_filas, n_columnas = trasponer(ancho, largo, base_celula, altura_celula,
                                    orientacion)
    n_celulas_string, lim_volt_serie, lim_volt_paralelo, lim_int_serie, lim_int_paralelo = celulas_por_string(
        n_filas, nstrings, n_columnas, orientacion)

    m = crear_matriz(nstrings, n_celulas_string, sombra)

    if datos_correctos(n_filas, nstrings) and m is not None:
        modulo_fotovoltaico = crear_modulo_fotovoltaico(conexion, orientacion,
                                                        nstrings,
                                                        n_celulas_string,
                                                        dbypass, m, fuente_intensidad,Rs,Rsh,area_celula)
        # modulo_fotovoltaico = crear_modulo_fotovoltaico(conexion=conex, orientacion=orientacion, strings=strings, n_celula_string=n_celula_string,
        # bypass=d_bypass)
        sim = simulacion(modulo_fotovoltaico, conexion, lim_volt_serie,
                         lim_volt_paralelo,temp)
        intensidad, voltage = extraer_valores(sim)
        dibujar(intensidad, voltage, conexion, lim_volt_serie,
                lim_volt_paralelo, lim_int_serie, lim_int_paralelo)
        guardar_fichero(intensidad, voltage,nombre,descripcion,conexion,orientacion,ancho,largo,ancho,altura_celula,nstrings,fuente_intensidad,Rs,Rsh,temp,dbypass,m)

    return conexion, sombra, fuente_intensidad,Rs,Rsh,temp


def crear_circuito_serie(strings, n_celula_string, bypass, m,fuente_intensidad,Rs,Rsh,area_celula):
    """ Creamos circuito """
    I = (fuente_intensidad * area_celula) @ u_A
    Rs = Rs / area_celula
    Rsh = Rsh / area_celula
    circuit = Circuit('Test')
    circuit.include(spice_library['1N4148'])
    circuit.model('Bypass', 'D', IS=3e-7, RS=2.9 / 1000, N=0.01, EG=0.1, XTI=3,
                  BV=600, IBV=1e-5, CJO=1.36534e-10,
                  M=0.743776, VJ=0.781554, FC=0.5, TT=5.54918e-8, KF=0, AF=1)
    # circuit.R('neg', 's1_n1_1', circuit.gnd, 0.02 @ u_Ω)
    circuit.I('1_1', circuit.gnd, 'in1_1', I * m[0][0])
    circuit.X('D1_1', '1N4148', 'in1_1', circuit.gnd)
    circuit.R('p1_1', 'in1_1', circuit.gnd, Rsh @ u_Ω)
    circuit.R('s1_1', 'in1_1', 'vin1_1', Rs @ u_Ω)
    if not n_celula_string == 1:
        circuit.R('c1_1', 'vin1_1', 'vout2_1', 0.02/area_celula @ u_Ω)

    if bypass == 'Sin diodo':
        for j in range(1, strings + 1):
            for i in range(1, n_celula_string + 1):
                if not (j == 1 and i == 1):
                    circuit.I('{}_{}'.format(i, j), 'vout{}_{}'.format(i, j),
                              'in{}_{}'.format(i, j), I * m[j - 1][i - 1])
                    circuit.X('D{}_{}'.format(i, j), '1N4148',
                              'in{}_{}'.format(i, j), 'vout{}_{}'.format(i, j))
                    circuit.R('p{}_{}'.format(i, j), 'in{}_{}'.format(i, j),
                              'vout{}_{}'.format(i, j), Rsh @ u_Ω)
                    circuit.R('s{}_{}'.format(i, j), 'in{}_{}'.format(i, j),
                              'vin{}_{}'.format(i, j), Rs @ u_Ω)
                    if not i == n_celula_string:
                        circuit.R('c{}_{}'.format(i, j),
                                  'vin{}_{}'.format(i, j),
                                  'vout{}_{}'.format(i + 1, j),
                                  0.02 @ u_Ω)
            if not j == strings:
                circuit.R('c{}_{}'.format(i, j), 'vin{}_{}'.format(i, j),
                          'vout1_{}'.format(j + 1), 0.02 @ u_Ω)



    elif bypass == 'Diodo por string':
        # Bucle
        for j in range(1, strings + 1):
            for i in range(1, n_celula_string + 1):
                if not (i == 1 and j == 1):
                    circuit.I('{}_{}'.format(i, j), 'vout{}_{}'.format(i, j),
                              'in{}_{}'.format(i, j), I * m[j - 1][i - 1])
                    circuit.X('D{}_{}'.format(i, j), '1N4148',
                              'in{}_{}'.format(i, j), 'vout{}_{}'.format(i, j))
                    circuit.R('p{}_{}'.format(i, j), 'in{}_{}'.format(i, j),
                              'vout{}_{}'.format(i, j), Rsh @ u_Ω)
                    circuit.R('s{}_{}'.format(i, j), 'in{}_{}'.format(i, j),
                              'vin{}_{}'.format(i, j), Rs @ u_Ω)
                    if not i == n_celula_string:
                        circuit.R('c{}_{}'.format(i, j),
                                  'vin{}_{}'.format(i, j),
                                  'vout{}_{}'.format(i + 1, j),
                                  0.02 @ u_Ω)
            circuit.Diode('Bypass{}'.format(j), 'in1_{}'.format(j),
                          'vin{}_{}'.format(n_celula_string, j),
                          model='Bypass')
            if not j == strings:
                circuit.R('c{}_{}'.format(i, j), 'vin{}_{}'.format(i, j),
                          'vout1_{}'.format(j + 1), 0.02/area_celula @ u_Ω)

    elif bypass == 'Diodo por celula':
        # Bucle
        circuit.Diode('Bypass1_1',
                      'in1_1',
                      'vin1_1', model='Bypass')
        for j in range(1, strings + 1):
            for i in range(1, n_celula_string + 1):
                if not (i == 1 and j == 1):
                    circuit.I('{}_{}'.format(i, j), 'vout{}_{}'.format(i, j),
                              'in{}_{}'.format(i, j), I * m[j - 1][i - 1])
                    circuit.X('D{}_{}'.format(i, j), '1N4148',
                              'in{}_{}'.format(i, j), 'vout{}_{}'.format(i, j))
                    circuit.R('p{}_{}'.format(i, j), 'in{}_{}'.format(i, j),
                              'vout{}_{}'.format(i, j), Rsh @ u_Ω)
                    circuit.R('s{}_{}'.format(i, j), 'in{}_{}'.format(i, j),
                              'vin{}_{}'.format(i, j), Rs @ u_Ω)
                    circuit.Diode('Bypass{}_{}'.format(i, j),
                                  'in{}_{}'.format(i, j),
                                  'vin{}_{}'.format(i, j), model='Bypass')
                    if not i == n_celula_string:
                        circuit.R('c{}_{}'.format(i, j),
                                  'vin{}_{}'.format(i, j),
                                  'vout{}_{}'.format(i + 1, j),
                                  0.02 @ u_Ω)

            if not j == strings:
                circuit.R('c{}_{}'.format(i, j), 'vin{}_{}'.format(i, j),
                          'vout1_{}'.format(j + 1), 0.02/area_celula @ u_Ω)

    circuit.R('cc', 'vin{}_{}'.format(n_celula_string, strings), 'pos',
              0.020 @ u_Ω)
    circuit.V('bias', 'pos', circuit.gnd, 1 @ u_V)
    print(circuit)
    return circuit


def crear_circuito_paralelo(strings, n_celula_string, bypass, m, fuente_intensidad,Rs,Rsh,area_celula):
    """ Creamos circuito """
    I = (fuente_intensidad * area_celula) @ u_A
    Rs = Rs / area_celula
    Rsh = Rsh / area_celula
    circuit = Circuit('Test')
    circuit.include(spice_library['1N4148'])
    circuit.model('Bypass', 'D', IS=3e-7, RS=2.9 / 1000, N=0.01, EG=0.1, XTI=3,
                  BV=600, IBV=1e-5, CJO=1.36534e-10,
                  M=0.743776, VJ=0.781554, FC=0.5, TT=5.54918e-8, KF=0, AF=1)
    # circuit.R('neg', circuit.gnd, 's1_n1_1', 0.02 @ u_Ω)

    if bypass == 'Sin diodo':

        for j in range(1, strings + 1):
            circuit.I('1_{}'.format(j), circuit.gnd, 'in1_{}'.format(j),
                      I * m[j - 1][0])
            circuit.X('D1_{}'.format(j), '1N4148', 'in1_{}'.format(j),
                      circuit.gnd)
            circuit.R('p1_{}'.format(j), 'in1_{}'.format(j), circuit.gnd,
                      Rsh @ u_Ω)
            circuit.R('s1_{}'.format(j), 'in1_{}'.format(j),
                      'vin1_{}'.format(j), Rs @ u_Ω)
            if not n_celula_string == 1:
                circuit.R('c1_{}'.format(j), 'vin1_{}'.format(j),
                          'vout2_{}'.format(j), 0.02 @ u_Ω)

            for i in range(2, n_celula_string + 1):
                circuit.I('{}_{}'.format(i, j), 'vout{}_{}'.format(i, j),
                          'in{}_{}'.format(i, j), I * m[j - 1][i - 1])
                circuit.X('D{}_{}'.format(i, j), '1N4148',
                          'in{}_{}'.format(i, j), 'vout{}_{}'.format(i, j))
                circuit.R('p{}_{}'.format(i, j), 'in{}_{}'.format(i, j),
                          'vout{}_{}'.format(i, j), Rsh @ u_Ω)
                circuit.R('s{}_{}'.format(i, j), 'in{}_{}'.format(i, j),
                          'vin{}_{}'.format(i, j), Rs @ u_Ω)

                if not i == n_celula_string:
                    circuit.R('c{}_{}'.format(i, j), 'vin{}_{}'.format(i, j),
                              'vout{}_{}'.format(i + 1, j), 0.02 @ u_Ω)
                elif i == n_celula_string and j != strings:
                    circuit.R('c{}_{}'.format(i, j), 'vin{}_{}'.format(i, j),
                              'in{}_{}'.format(1, j+1), 0.02 @ u_Ω)

        circuit.R('c{}'.format(j), 'vin{}_{}'.format(n_celula_string, j),
                      'pos', 0.02 @ u_Ω)


    elif bypass == 'Diodo por string':
        for j in range(1, strings + 1):
            circuit.I('1_{}'.format(j), circuit.gnd, 'in1_{}'.format(j),
                      I * m[j - 1][0])
            circuit.X('D1_{}'.format(j), '1N4148', 'in1_{}'.format(j),
                      circuit.gnd)
            circuit.R('p1_{}'.format(j), 'in1_{}'.format(j), circuit.gnd,
                      Rsh @ u_Ω)
            circuit.R('s1_{}'.format(j), 'in1_{}'.format(j),
                      'vin1_{}'.format(j), Rs @ u_Ω)
            if not n_celula_string == 1:
                circuit.R('c1_{}'.format(j), 'vin1_{}'.format(j),
                          'vout2_{}'.format(j), 0.02 @ u_Ω)

            for i in range(2, n_celula_string + 1):
                circuit.I('{}_{}'.format(i, j), 'vout{}_{}'.format(i, j),
                          'in{}_{}'.format(i, j), I * m[j - 1][i - 1])
                circuit.X('D{}_{}'.format(i, j), '1N4148',
                          'in{}_{}'.format(i, j), 'vout{}_{}'.format(i, j))
                circuit.R('p{}_{}'.format(i, j), 'in{}_{}'.format(i, j),
                          'vout{}_{}'.format(i, j), Rsh @ u_Ω)
                circuit.R('s{}_{}'.format(i, j), 'in{}_{}'.format(i, j),
                          'vin{}_{}'.format(i, j), Rs @ u_Ω)

                if not i == n_celula_string:
                    circuit.R('c{}_{}'.format(i, j), 'vin{}_{}'.format(i, j),
                              'vout{}_{}'.format(i + 1, j), 0.02 @ u_Ω)
                elif i == n_celula_string and j != strings:
                    circuit.R('c{}_{}'.format(i, j), 'vin{}_{}'.format(i, j),
                              'in{}_{}'.format(1, j+1), 0.02 @ u_Ω)
            circuit.Diode('Bypass{}'.format(j), 'in1_{}'.format(j),
                          'vin{}_{}'.format(n_celula_string, j),
                          model='Bypass')

        circuit.R('c{}'.format(j), 'vin{}_{}'.format(n_celula_string, j),
                      'pos', 0.02 @ u_Ω)

    elif bypass == 'Diodo por celula':

        for j in range(1, strings + 1):
            circuit.I('1_{}'.format(j), circuit.gnd, 'in1_{}'.format(j),
                      I * m[j - 1][0])
            circuit.X('D1_{}'.format(j), '1N4148', 'in1_{}'.format(j),
                      circuit.gnd)
            circuit.R('p1_{}'.format(j), 'in1_{}'.format(j), circuit.gnd,
                      Rsh @ u_Ω)
            circuit.R('s1_{}'.format(j), 'in1_{}'.format(j),
                      'vin1_{}'.format(j), Rs @ u_Ω)
            if not n_celula_string == 1:
                circuit.R('c1_{}'.format(j), 'vin1_{}'.format(j),
                          'vout2_{}'.format(j), 0.02 @ u_Ω)

            for i in range(2, n_celula_string + 1):
                circuit.I('{}_{}'.format(i, j), 'vout{}_{}'.format(i, j),
                          'in{}_{}'.format(i, j), I * m[j - 1][i - 1])
                circuit.X('D{}_{}'.format(i, j), '1N4148',
                          'in{}_{}'.format(i, j), 'vout{}_{}'.format(i, j))
                circuit.R('p{}_{}'.format(i, j), 'in{}_{}'.format(i, j),
                          'vout{}_{}'.format(i, j), Rsh @ u_Ω)
                circuit.R('s{}_{}'.format(i, j), 'in{}_{}'.format(i, j),
                          'vin{}_{}'.format(i, j), Rs @ u_Ω)
                circuit.Diode('Bypass{}_{}'.format(i, j),
                              'in{}_{}'.format(i, j), 'vin{}_{}'.format(i, j),
                              model='Bypass')
                if not i == n_celula_string:
                    circuit.R('c{}_{}'.format(i, j), 'vin{}_{}'.format(i, j),
                              'vout{}_{}'.format(i + 1, j), 0.02 @ u_Ω)
                elif i == n_celula_string and j != strings:
                    circuit.R('c{}_{}'.format(i, j), 'vin{}_{}'.format(i, j),
                              'in{}_{}'.format(1, j+1), 0.02 @ u_Ω)

        circuit.R('c{}'.format(j), 'vin{}_{}'.format(n_celula_string, j),
                      'pos', 0.02 @ u_Ω)

    circuit.V('bias', 'pos', circuit.gnd, 1 @ u_V)
    print(circuit)
    return circuit


def simulacion(circuit, conexion, lim_volt_serie, lim_volt_paralelo,temp):
    """ Para cada resistencia sacamos intensidad """
    # for resistance in (circuit.Rpos):
    #    resistance.plus.add_current_probe(circuit)
    simulator = circuit.simulator(temperature=temp, nominal_temperature=25)
    if conexion == 's':
        analysis = simulator.dc(Vbias=slice(0, lim_volt_serie, 0.01))
    else:
        analysis = simulator.dc(Vbias=slice(0, lim_volt_paralelo, 0.01))

    return analysis


def extraer_valores(analysis):
    """ Extraer corriente y voltage dado el analisis """
    current = analysis.branches['vbias']
    voltage = analysis.nodes['pos']
    return current, voltage


def dibujar(intensidad, voltage, conexion, lim_volt_serie, lim_volt_paralelo,
            lim_int_serie, lim_int_paralelo):
    """ Grafica tension frente a intensidad """
    plt.xlabel('Tensión (V)')
    plt.ylabel('Corriente (A)')
    plt.title('Curva I-V')
    """
    if conexion == 's':
        plt.xlim(0, lim_volt_serie)
        plt.ylim(0, lim_int_serie, 0.01)
    else:
        plt.xlim(0, lim_volt_paralelo)
        plt.ylim(0, lim_int_paralelo, 0.01)
    """

    plt.plot(voltage, intensidad)
    plt.show()
    "Guardar gráfica"
    archivo_salida = 'grafica.png'
    plt.savefig(archivo_salida)


def devolver_conexion():
    """  """
    while True:
        conexion = input(
            "¿Quieres conectar las células del módulo en serie o en paralelo? (s/p)")
        if conexion == 's' or conexion == 'p':
            break
    return conexion


def devolver_orientacion():
    while True:
        orientacion_strings = input(
            "¿En que dirección quieres orientar los strings del módulo? (x/y)")
        if orientacion_strings == 'x' or orientacion_strings == 'y':
            break
    return orientacion_strings


def numero_strings(orientacion):
    ancho = int(input("¿Cual es el ancho del area disponible (cm2)?: "))
    largo = int(input("¿Cual es el largo del area disponible(cm2)?:  "))
    x = int(input("Medida de la base de la celula(cm2): "))
    y = int(input("Medida de la altura de la celula(cm2): "))
    # Si la disivision de n_filas y n_columnas no da un entero, coger la parte entera del decimal
    n_filas = math.floor(largo / y)
    n_columnas = math.floor(ancho / x)
    celulas_totales = n_filas * n_columnas
    while True:
        n_strings = int(input("Numero de strings:"))
        # Comprobar si n_strings es multiplo de n_filas
        if n_filas % n_strings != 0:
            n_strings = int(input(
                "Introduce un multiplo de {} menor o igual:".format(n_filas)))
            if n_strings > n_filas:
                n_strings = int(input(
                    "Introduce un multiplo de {} menor o igual:".format(
                        n_filas)))
            break
        break
    # si la orientacion es y cambiar filas por columna
    if orientacion == 'y':
        n_filas, n_columnas = n_columnas, n_filas
    print("Numero de filas: {}".format(n_filas))
    print("Numero de columnas: {}".format(n_columnas))
    return n_filas, n_strings, n_columnas, celulas_totales


def celulas_por_string(filas, strings, columnas, orientacion):
    n_celulas = math.floor((filas * columnas) / strings)
    print("Numero de celulas por string: {}".format(n_celulas))
    """"
     #Si la orientacion del modulo es y el numero de celulas por string se calcula a raiz de las columnas
    if orientacion == 'y':
        n_celulas = math.floor(columnas / strings)
    """
    lim_volt_paralelo = n_celulas * 0.9
    lim_int_paralelo = strings * 0.04
    lim_volt_serie = n_celulas * strings * 0.9
    lim_int_serie = 0.1

    return n_celulas, \
           lim_volt_serie, \
           lim_volt_paralelo, \
           lim_int_serie, \
           lim_int_paralelo


def diodo_bypass():
    while True:
        bypass = int(input(
            "Indica la opcion deseada:\n "
            "1.Diseño sin diodo bypass\n "
            "2.Diseño con diodo bypass por string\n "
            "3.Diseño con diodo bypass por celula")
        )
        if bypass == 1 or bypass == 2 or bypass == 3:
            break
    return bypass


def crear_modulo_fotovoltaico(conexion,
                              orientacion,
                              strings,
                              n_celula_string,
                              bypass,
                              m,
                              fuente_intensidad,
                              Rs,
                              Rsh,area_celula):
    """ TODO añadir descripcion de metodo """
    if conexion == 's':
        return crear_circuito_serie(strings, n_celula_string, bypass, m,fuente_intensidad,Rs,Rsh,area_celula)

    elif conexion == 'p':
        return crear_circuito_paralelo(strings, n_celula_string, bypass, m,fuente_intensidad,Rs,Rsh,area_celula)


def crear_matriz(strings, n_celula_string, sombra):
    """ TODO añadir descripcion de metodo """
    if sombra == 'Patrón aleatorio':
        m_irradiancia = np.random.randint(0, 2, (strings, n_celula_string))
    elif sombra == 'Patrón personalizado':
        # MatrixWindow(strings, n_celula_string)

        out_file = 'matriz.csv'
        matriz_fd = open(out_file, 'r')

        collected_matrix = []

        for fila in matriz_fd:
            matriz_fila = []
            for columna in fila.rstrip().split(','):
                matriz_fila.append(float(columna))

            collected_matrix.append(matriz_fila)

        m_irradiancia = np.array(np.matrix(collected_matrix))

        # TODO comprobar tamaño matriz
        if m_irradiancia.shape != (strings, n_celula_string):
            print("ERROR")
            pop_up("El tamaño de la matriz introducida no es correcto")
            m_irradiancia = None

    print(m_irradiancia)

    return m_irradiancia


class MatrixWindow:
    def __init__(self, strings, n_celula_string):
        # self.ventana = tk.Tk()
        self.ventana = tk.Toplevel(window)
        self.ventana.title("Rellena la matriz")
        entries = []
        for i in range(strings):
            fila_entries = []
            for j in range(n_celula_string):
                entry = tk.Entry(self.ventana)
                entry.grid(row=i + 3, column=j)
                fila_entries.append(entry)
            entries.append(fila_entries)
        btn_aceptar = tk.Button(self.ventana, text="Aceptar",
                                # command=lambda: guardar_valores(entries)
                                command=lambda: self.close(entries)
                                )
        btn_aceptar.grid(row=2, column=0, columnspan=2)

        self.ventana.mainloop()

        return 'B'

    def close(self, entradas):
        collected_matrix = []
        for linea in entradas:
            row_matrix = []
            for columna in linea:
                num = int(columna.get())
                row_matrix.append(num)
            collected_matrix.append(row_matrix)

        m_irradiancia = np.matrix(collected_matrix)



        self.ventana.destroy()

        return 'A'


def guardar_valores(entradas):
    """ TODO Guardamos los valores de la matriz del pop-up,
    creamos el tipo de dato numpy matrix y lo devolvemos
     """
    collected_matrix = []
    for linea in entradas:
        row_matrix = []
        for columna in linea:
            num = int(columna.get())
            row_matrix.append(num)
        collected_matrix.append(row_matrix)

    m_irradiancia = np.matrix(collected_matrix)
    # ventana.destroy

    """ TODO esto se podria borrar
    m_irradiancia = []
    for i in range(strings):
        fila = []
        for j in range(n_celula_string):
            valor = int(entries[i][j].get())
            fila.append(valor)
        m_irradiancia.append(fila)
    """


if __name__ == "__main__":
    """ TODO poner un if-else para saber si meternos en consola o GUI
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