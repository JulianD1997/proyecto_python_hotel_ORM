.. aplicacion hotel documentation master file, created by
   sphinx-quickstart on Sun Aug 28 20:36:43 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Bienvenido a la documentacion de la aplicacion hotel teressitta!
============================================

    Esta aplicación fue creada con el fin de darle una optimización a la administración de un hotel donde se puede crear, leer, 
    actualizar y borrar una reserva de un cliente. Cuenta con tres apartados dentro:Espacio de formularios: Acá se puede realizar 
    diferentes tipos de consultas, podemos ingresar Nombre, apellido, DNI, habitación, fecha de entrada y fecha de salida para 
    poder generar una nueva reserva. Igualmente, este espacio nos permite actualizar los datos de una reserva, ya que 
    automáticamente envía los datos del cliente que deseemos actualizar. También nos permite ejecutar la búsqueda de clientes por 
    medio de los formularios, podemos buscar por: nombre, apellido, DNI, habitación fecha de entrada y fecha de salida. Por último 
    tenemos un botón multifuncional que nos permite guardar, buscar y actualizar según su valor
    (Este valor es el nombre que tiene el botón en el momento).
    Espacio de lectura de clientes: Este nos brinda la facilidad de ver todos los clientes registrados hasta el momento, 
    igualmente se podrá visualizar los clientes que coinciden con la búsqueda. Este espacio también los brinda seleccionar un cliente 
    para posterior darle al botón Update o Delete situados en la caja de herramientas y para más facilidad, darle doble al cliente que se 
    quiera modificar para que enviar los datos a los formularios. 
    Espacio de Herramientas: Nos ofrece 5 tipos de botones: 
    Botón Created: borrar los formularios y actualiza el valor del botón multifuncional situado en el espacio formulario con el valor "Save".
    Botón Clients: borrar formularios y actualizar la vista del treeview con todos los datos de los clientes registrados hasta el momento.
    Botón Search: borrar todos los formularios para que el cliente pueda realizar una búsqueda, esta búsqueda se puede realizar ingresando 
    un solo campo o varios. Igualmente, cambia el valor del botón multifuncional a "Search". 
    Botón Update: Esté nos permite enviar todos los datos del cliente seleccionado en el treeview situado en client list. 
    Botón Delete: por último el botón Delete que nos permite borrar un cliente seleccionado del treeview situado en client list, para la 
    confirmación de borrado de reserva, saldrá un cuadro de confirmación que preguntara si está seguro de eliminarlo el cliente cada acción 
    tiene un mensaje de alerta que nos informara si fue correcta la operación o incorrecta.

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
