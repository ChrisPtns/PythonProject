class Kouti:
    """
    Κλάση που περιγράφει ένα κουτί συσκευασίας.
    Διαθέτει κρυφές ιδιότητες και μέθοδο υπολογισμού όγκου.
    """
    def __init__(self, xroma, kodikos, mikos, platos, ypsos):
        # Ορισμός κρυφών (private) ιδιοτήτων
        self.__xroma = xroma
        self.__kodikos = kodikos
        self.__mikos = mikos
        self.__platos = platos
        self.__ypsos = ypsos

    def ypologismos_ogkou(self):
        """
        Μέθοδος που υπολογίζει και επιστρέφει τον όγκο του κουτιού.
        Τύπος: Μήκος * Πλάτος * Ύψος
        """
        return self.__mikos * self.__platos * self.__ypsos

    def __str__(self):
        """
        Μέθοδος για την εμφάνιση των στοιχείων του κουτιού.
        """
        ogkos = self.ypologismos_ogkou()
        return (f"Κωδικός: {self.__kodikos} | Χρώμα: {self.__xroma} | "
                f"Διαστάσεις: {self.__mikos}x{self.__platos}x{self.__ypsos} | "
                f"Όγκος: {ogkos:.2f} cm3")

# --- Συναρτήσεις Κυρίως Προγράμματος ---

def dimiourgia_koution():
    """
    Συνάρτηση για την εισαγωγή δεδομένων και δημιουργία των κουτιών.
    """
    lista_koution = []
    AM = 25176  # Ο Αριθμός Μητρώου μου
    
    print(f"--- Κατασκευή Κουτιών (ΑΜ: {AM}) ---")
    
    while True:
        try:
            plithos = int(input("Πόσα κουτιά θέλετε να κατασκευάσετε; "))
            if plithos > 0:
                break
            print("Παρακαλώ δώστε θετικό αριθμό.")
        except ValueError:
            print("Σφάλμα: Δώστε ακέραιο αριθμό.")

    for i in range(plithos):
        print(f"\nΣτοιχεία Κουτιού {i+1}:")
        
        # Υπολογισμός Κωδικού σύμφωνα με την εκφώνηση:
        # Κωδικός = Αριθμός Μητρώου * Αριθμός Κουτιού (i+1)
        # Το i ξεκινάει από το 0, οπότε βάζουμε i+1 για να είναι 1, 2, 3...
        trexon_kodikos = AM * (i + 1)
        print(f"Αυτόματος Κωδικός Κουτιού: {trexon_kodikos}")
        
        xroma = input("Δώστε Χρώμα: ")
        
        # Έλεγχος εγκυρότητας διαστάσεων
        while True:
            try:
                m = float(input("Δώστε Μήκος (cm): "))
                p = float(input("Δώστε Πλάτος (cm): "))
                y = float(input("Δώστε Ύψος (cm): "))
                if m > 0 and p > 0 and y > 0:
                    break
                else:
                    print("Οι διαστάσεις πρέπει να είναι θετικοί αριθμοί.")
            except ValueError:
                print("Σφάλμα: Οι διαστάσεις πρέπει να είναι αριθμοί.")

        # Δημιουργία του αντικειμένου
        neo_kouti = Kouti(xroma, trexon_kodikos, m, p, y)
        
        # Προσθήκη στη λίστα
        lista_koution.append(neo_kouti)

    return lista_koution

def ektypwsi_paragogis(lista):
    """
    Συνάρτηση που εκτυπώνει τα στοιχεία και τον όγκο όλων των κουτιών.
    """
    print("\n" + "="*60)
    print("ΑΝΑΦΟΡΑ ΠΑΡΑΓΩΓΗΣ ΚΟΥΤΙΩΝ")
    print("="*60)
    
    if not lista:
        print("Δεν κατασκευάστηκαν κουτιά.")
    else:
        for i, kouti in enumerate(lista):
            # Η print καλεί αυτόματα την __str__ του αντικειμένου
            print(f"{i+1}. {kouti}")
            print("-" * 60)

# --- Κυρίως Πρόγραμμα ---

# 1. Δημιουργία κουτιών και αποθήκευση στη λίστα
koutia_list = dimiourgia_koution()

# 2. Εκτύπωση των αποτελεσμάτων
ektypwsi_paragogis(koutia_list)