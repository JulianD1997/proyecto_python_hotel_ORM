from datetime import datetime
from tkcalendar import DateEntry
import tkinter
from tkinter import messagebox
from tkinter import ttk


class Interface:
    """
        Se inicializa todas las variables que tendrá nuestra interfaz
    """

    def __init__(self, root, controller):

        self.controller = controller
        self.root = root
        self.id_client = None
        self.name_client = tkinter.StringVar()
        self.last_name = tkinter.StringVar()
        self.dni = tkinter.StringVar()
        self.room = tkinter.StringVar()
        self.entry_date = tkinter.StringVar()
        self.exit_date = tkinter.StringVar()
        self.variable_button = tkinter.StringVar()
        self.name_error = tkinter.StringVar()
        self.last_name_error = tkinter.StringVar()
        self.dni_error = tkinter.StringVar()
        self.room_error = tkinter.StringVar()
        """
            Se deja la opción de seleccionar en el ComboBox y la opción de guardar en el botón del formulario
        """
        self.room.set("Select")
        self.variable_button.set("Save")
        self.__frames()
        self.__labels()
        """
            El comboBox se deja solamente como lectura para que el cliente 
            tenga que seleccionar la habitación
        """
        self.room_form = ttk.Combobox(self.__forms_frame, textvariable=self.room,
                                      state="readonly")
        self.__forms()
        self.__buttons()
        self.tree = ttk.Treeview(self.__data_list_frame)
        self.__tree_view()

    def run_window(self):
        """
            Este método se encarga de la ejecución de la aplicación y 
            de agregar el título de esta misma
        """
        self.root.resizable(False, False)
        self.root.title("Hotel teressitta")
        self.root.mainloop()

    def __frames(self):
        """
            Se declaran los espacios de trabajo y la ubicación de los mismos
        """
        self.__main_frame = ttk.Frame(self.root, padding=10)
        self.__forms_frame = ttk.LabelFrame(self.__main_frame, text="Client Form", padding=10)
        self.__data_list_frame = ttk.LabelFrame(self.__main_frame, text="Clients list", padding=10)
        self.__tools_frame = ttk.LabelFrame(self.__main_frame, text="Tools", padding=10)

        self.__main_frame.grid(column=0, row=0)
        self.__forms_frame.grid(column=0, row=0)
        self.__data_list_frame.grid(column=0, row=1, pady=5)
        self.__tools_frame.grid(column=0, row=2, pady=5)

    def __labels(self):
        self.__label_name = ttk.Label(self.__forms_frame, text="Name")
        self.__label_last_name = ttk.Label(self.__forms_frame, text="Last Name")
        self.__label_dni = ttk.Label(self.__forms_frame, text="DNI")
        self.__label_room = ttk.Label(self.__forms_frame, text="Room")
        self.__label_entry_date = ttk.Label(self.__forms_frame, text="Date Entry")
        self.__label_exit_date = ttk.Label(self.__forms_frame, text="Date exit")
        """
            Etiquetas que dan aviso a los campos faltantes en el 
            formulario cuando estos no se han ingresado o estén erróneos
        """
        self.__label_name_error = ttk.Label(self.__forms_frame, textvariable=self.name_error,
                                            foreground="Red")
        self.__label_last_name_error = ttk.Label(self.__forms_frame, textvariable=self.last_name_error,
                                                 foreground="Red")
        self.__label_dni_error = ttk.Label(self.__forms_frame, textvariable=self.dni_error,
                                           foreground="Red")
        self.__label_room_error = ttk.Label(self.__forms_frame, textvariable=self.room_error,
                                            foreground="Red")

        self.__label_name.grid(column=0, row=0, sticky="W E", padx=5)
        self.__label_last_name.grid(column=1, row=0, sticky="W E", padx=5)
        self.__label_dni.grid(column=2, row=0, sticky="W E", padx=5)
        self.__label_room.grid(column=3, row=0, sticky="W E", padx=5)
        self.__label_entry_date.grid(column=4, row=0, sticky="W E", padx=5)
        self.__label_exit_date.grid(column=5, row=0, sticky="W E", padx=5)

        self.__label_name_error.grid(column=0, row=2, sticky='W N', padx=5)
        self.__label_last_name_error.grid(column=1, row=2, sticky='W N', padx=5)
        self.__label_dni_error.grid(column=2, row=2, sticky='W N', padx=5)
        self.__label_room_error.grid(column=3, row=2, sticky='W N', padx=5)

    def __forms(self):
        """
            Se agrega variable con el día actual
        """
        today = datetime.now()
        self.__name_form = ttk.Entry(self.__forms_frame, validate="all",
                                     validatecommand=(self.__forms_frame.register(
                                         self.controller.validate_string), '%P'),
                                     textvariable=self.name_client)
        self.__last_name_form = ttk.Entry(self.__forms_frame, validate="all",
                                          validatecommand=(self.__forms_frame.register(
                                              self.controller.validate_string), '%P'),
                                          textvariable=self.last_name)
        self.__dni_form = ttk.Entry(self.__forms_frame, validate="all",
                                    validatecommand=(self.__forms_frame.register(
                                        self.controller.validate_number), '%P'),
                                    textvariable=self.dni)
        """
            Se agregan calendarios y se modifican para no poder seleccionar fechas
            anteriores al día actual
        """
        self.entry_date_form = DateEntry(self.__forms_frame, selectmode="dia",
                                         date_pattern='yyyy-MM-dd',
                                         textvariable=self.entry_date,
                                         state="readonly",
                                         mindate=today)
        self.__exit_date_form = DateEntry(self.__forms_frame, selectmode="dia",
                                          date_pattern='yyyy-MM-dd',
                                          textvariable=self.exit_date,
                                          state="readonly",
                                          mindate=today)

        self.__name_form.grid(column=0, row=1, sticky="W", padx=5)
        self.__last_name_form.grid(column=1, row=1, sticky="W", padx=5)
        self.__dni_form.grid(column=2, row=1, sticky="W", padx=5)
        self.room_form.grid(column=3, row=1, sticky="W", padx=5)
        self.entry_date_form.grid(column=4, row=1, sticky="W", padx=5)
        self.__exit_date_form.grid(column=5, row=1, sticky="W", padx=5)
        """
            Se ejecuta este método de la clase controlador para actualizar el comboBox 
            con las habitaciones disponibles
            """
        self.controller.avalible_rooms('', self.variable_button, self.room_form, self.entry_date, self.exit_date)
        """
            Se crea un evento que actúa al momento de seleccionar una fecha de entrada 
            y de salida, este ejecuta el método de la clase actual (date_event)
        """
        self.entry_date_form.bind("<<DateEntrySelected>>", self.__date_event)
        self.__exit_date_form.bind("<<DateEntrySelected>>", self.__date_event)

    def __buttons(self):
        """
            Botón multifuncional del formulario, el cual toma valores como guardar, actualizar y buscar
        """
        self.__action_button = ttk.Button(self.__forms_frame, textvariable=self.variable_button,
                                          padding="10 5 10 5",
                                          command=lambda: self.controller.action_press(self.format_data_client()))
        """
        Botones que se utilizan como herramientas para el CRUD de esta aplicación y modifican a su vez
        el valor del botón multifuncional situado en formulario.
        """
        self.__create_button = ttk.Button(self.__tools_frame, text="Create", padding="10 5 10 5",
                                          command=lambda: self.set_variables("Save"))
        self.__clients_button = ttk.Button(self.__tools_frame, text="Clients", padding="10 5 10 5",
                                           command=lambda: self.set_variables('Clients'))
        self.__query_button = ttk.Button(self.__tools_frame, text="Search",
                                         padding="10 5 10 5",
                                         command=lambda: self.set_variables("Search"))
        self.__update_button = ttk.Button(self.__tools_frame, text="Update",
                                          padding="10 5 10 5",
                                          command=lambda: self.__show_data())
        self.__delete_button = ttk.Button(self.__tools_frame, text="Delete",
                                          padding="10 5 10 5", command=lambda: self.controller.delete_client())

        self.__action_button.grid(column=5, row=2, sticky="W", pady=10)
        self.__create_button.grid(column=0, row=0, sticky="W", padx=20)
        self.__clients_button.grid(column=1, row=0, sticky="W", padx=20)
        self.__query_button.grid(column=2, row=0, sticky="W", padx=20)
        self.__update_button.grid(column=3, row=0, sticky="W", padx=20)
        self.__delete_button.grid(column=4, row=0, sticky="W", padx=20)

    def __tree_view(self):
        """
            Se crea el treeview que mostrara los datos de los clientes
            Se declara una barra de desplazamiento para visualizar todos los datos del treeview
        """
        self.__scrol = ttk.Scrollbar(self.__data_list_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.__scrol)
        self.tree['yscrollcommand'] = self.__scrol.set
        """
            Se declaran los nombres de las columnas del treeview
        """
        self.tree['columns'] = ('Name', 'Last Name', 'DNI', 'Room',
                                'Date Entry', 'Date Exit')
        self.tree.grid(column=0, row=0)
        self.__scrol.grid(column=1, row=0, sticky="N,S")
        """
            Se declaran las variables de cada columna del treeview
        """
        self.tree.column('#0', width=50, minwidth=10)
        self.tree.heading('#0', text='ID')
        self.tree.column('Name', width=120, minwidth=10)
        self.tree.heading('Name', text='Name')
        self.tree.column('Last Name', width=120, minwidth=10)
        self.tree.heading('Last Name', text='Last Name', )
        self.tree.column('DNI', width=100, minwidth=10)
        self.tree.heading('DNI', text='DNI')
        self.tree.column('Room', width=100, minwidth=10)
        self.tree.heading('Room', text='Room')
        self.tree.column('Date Entry', width=100, minwidth=10)
        self.tree.heading('Date Entry', text='Date Entry')
        self.tree.column('Date Exit', width=100, minwidth=10)
        self.tree.heading('Date Exit', text='Date Exit')
        """
            Se declaran eventos del treeview
        """
        self.tree.bind('<B1-Motion>', self.__recize_false)
        self.tree.bind('<Double-1>', self.__show_data)
        """
            Se ejecuta el método del controlador "read_clients" para visualizar 
            todos los datos ingresados hasta el momento
        """
        self.controller.read_clients(self.tree)

    def set_variables(self, action=""):
        """
            Método que se encarga de borrar todos los datos de los formularios
            y de darle valor al botón multifuncional dependiendo del botón de la caja herramientas
        """
        self.name_client.set("")
        self.last_name.set("")
        self.dni.set("")
        self.room.set("Select")
        if action == 'Clients':
            self.controller.read_clients(self.tree)
        elif action == "Search":
            self.variable_button.set("Search")
            self.entry_date.set("")
            self.exit_date.set("")
        else:
            self.variable_button.set("Save")
            today = datetime.now()
            date = str(today.strftime("%Y-%m-%d"))
            self.entry_date.set(date)
            self.exit_date.set(date)
        """
            Dependiendo del valor del botón multivariable, se mostrarán todas las habitaciones si el valor es buscar o 
            se mostrarán las habitaciones disponibles si el valor es guardar
        """
        self.controller.avalible_rooms('', self.variable_button, self.room_form, self.entry_date, self.exit_date)
        self.set_labels()

    def set_labels(self):
        """
            Borrar las etiquetas de errores de los formularios
        """
        self.name_error.set("")
        self.last_name_error.set("")
        self.dni_error.set("")
        self.room_error.set("")

    def __show_data(self, event=''):
        """
            Envía los datos a los formularios cuando se selecciona y acciona el botón, actualizar 
            o cuando se da doble clip en un cliente que este en el treeview, la excepción se encarga 
            cuando no se ha seleccionado un cliente y se oprima el botón actualizar situado la caja de
            herramientas
        """
        try:
            self.variable_button.set("Update")
            client = self.tree.item(self.tree.focus())
            self.id_client = client['text']
            self.name_client.set(client['values'][0])
            self.last_name.set(client['values'][1])
            self.dni.set(client['values'][2])
            self.room.set((client['values'][3]))
            self.entry_date.set(str(client['values'][4]))
            self.exit_date.set(str(client['values'][5]))
        except:
            self.message_box(['Update Client', 'please, You select the client want update'])

    @staticmethod
    def __recize_false(event):
        """
            Es un evento que se encarga de que el cliente no redimensione el tamaño de las columnas del treeview
        """
        return "break"

    def __date_event(self, event):
        """
        Este evento es ejecutado cuando se selecciona una fecha en el calendario y tiene como finalidad enviar los
        argumentos al método(avalible_rooms) del módulo controlador, para que se encargue de mostrar las habitaciones
        disponibles dentro del rango de fechas seleccionadas
        """
        self.controller.avalible_rooms("date_selected", self.variable_button, self.room_form, self.entry_date,
                                       self.exit_date)

    def format_data_client(self):
        """
        Formato de envío de datos, tipo diccionario para la manipulación de estos en los métodos del módulo controlador
        """
        data = {'id_client': self.id_client,
                'name': self.name_client.get().title(),
                'last_name': self.last_name.get().title(),
                'dni': self.dni.get(),
                'room': self.room.get(),
                'entry_date': self.entry_date.get(),
                'exit_date': self.exit_date.get()
                }
        return data

    @staticmethod
    def message_box(message=''):
        """
            Método para mostrar mensajes de alerta al usuario o para acreditar el borrado de un cliente
        """
        if message != '':
            messagebox.showinfo(message[0], message[1])
        else:
            ask = messagebox.askyesno("Delete Client",
                                      "Do you want to delete this client?")
            return ask
