class SmartPhone:
    """
    Κλάση που περιγράφει ένα SmartPhone.
    Περιλαμβάνει κρυφές (private) ιδιότητες.
    """
    def __init__(self, kataskeuastis, montelo, timi):
        # Ορισμός κρυφών ιδιοτήτων με διπλή κάτω παύλα (__)
        self.__kataskeuastis = kataskeuastis
        self.__montelo = montelo
        self.__timi = timi

def __str__(self):
        """
        Ειδική μέθοδος για την επιστροφή των στοιχείων του αντικειμένου
        σε μορφή κειμένου (string) όταν καλούμε την print().
        """
        return f"Κατασκευαστής: {self.__kataskeuastis} | Μοντέλο: {self.__montelo} | Τιμή: {self.__timi}€"
    
    

# --- Συναρτήσεις Κυρίως Προγράμματος ---

def dimiourgia_kai_eisagogi():
    """
    Συνάρτηση που ζητάει στοιχεία για 5 κινητά,
    δημιουργεί αντικείμενα και τα βάζει σε λίστα.
    """
    lista_kinhton = [] # Κενή λίστα
    print("--- Καταχώρηση 5 SmartPhones ---")

    for i in range(5):
        print(f"\nΣτοιχεία SmartPhone {i+1}:")
        k = input("Δώστε Κατασκευαστή: ")
        m = input("Δώστε Μοντέλο: ")
        
        # Έλεγχος ότι η τιμή είναι αριθμός
        while True:
            try:
                t = float(input("Δώστε Τιμή Λιανικής: "))
                break
            except ValueError:
                print("Σφάλμα: Η τιμή πρέπει να είναι αριθμός.")

        # Δημιουργία αντικειμένου της κλάσης SmartPhone
        neo_kinhto = SmartPhone(k, m, t)
        
        # Προσθήκη του αντικειμένου στη λίστα
        lista_kinhton.append(neo_kinhto)

    return lista_kinhton


def ektypwsi_listas(lista):
    """
    Συνάρτηση που δέχεται τη λίστα με τα αντικείμενα
    και τα εκτυπώνει στην οθόνη.
    """
    print("\n" + "="*40)
    print("ΛΙΣΤΑ ΚΑΤΑΧΩΡΗΜΕΝΩΝ SMARTPHONES")
    print("="*40)
    
    # Διασχίζουμε τη λίστα και τυπώνουμε κάθε αντικείμενο
    for i, kinhto in enumerate(lista):
        # Η print(kinhto) καλεί αυτόματα την μέθοδο __str__ της κλάσης
        print(f"{i+1}. {kinhto}") 
    print("-" * 40)


# --- Κυρίως Πρόγραμμα ---

# 1. Κλήση της συνάρτησης δημιουργίας αντικειμένων
# Η λίστα που επιστρέφεται αποθηκεύεται στη μεταβλητή my_phones
my_phones = dimiourgia_kai_eisagogi()

# 2. Κλήση της συνάρτησης εκτύπωσης
# Περνάμε τη λίστα my_phones ως όρισμα
ektypwsi_listas(my_phones)