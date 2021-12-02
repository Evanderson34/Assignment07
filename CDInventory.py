#------------------------------------------#
# Title: Assignment06_Starter.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
#------------------------------------------#

# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object


# -- PROCESSING -- #
class DataProcessor:

    @staticmethod    
    def add_cd(strID,strTitle,stArtist):
        """Function to save dictionary row with input data to table
    
        Args:
            strID = undefined value
            strTitle = undefined value
            stArtist = undefined value
        
        Returns:
            None.
        """            
        intID = int(strID)
        dicRow = {'ID': strID, 'Title': strTitle, 'Artist': stArtist}
        lstTbl.append(dicRow)
        IO.show_inventory(lstTbl)
        
    @staticmethod    
    def delete_cd():
        """Function to delete row from table
    
        Args:
            None.
            
        Returns:
            None.
        """
        intRowNr = -1
        for row in lstTbl:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del lstTbl[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
            
class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        table.clear()  # this clears existing data and allows to load data from file
        objFile = open(strFileName, 'r')
        for line in objFile:
            data = line.strip().split(',')
            dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
            table.append(dicRow)
        objFile.close()

    @staticmethod
    def write_file():
        """Writes data into file
        
        Args:
            None
            
        Returns:
            None   
        
        """
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            lstValues = list(row.values())
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()


# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] Exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while True:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
            OneOfMenuOptions = choice in ['l', 'a', 'i', 'd', 's', 'x']
            if OneOfMenuOptions:
                break
            try:
                if not OneOfMenuOptions:
                    raise Exception('Invalid Option')
            except Exception as e:
                    print (e)     
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    @staticmethod
    def input_cd():
        """Function to request input data from user
    
        Args:
            None.
            
        Returns:
            None.
        """
        value1 = input('Enter ID: ').strip()
        value2 = input('What is the CD\'s title? ').strip()
        value3 = input('What is the Artist\'s name? ').strip()
        return value1,value2,value3 #returns a tuple

# 1. When program starts, read in the currently saved Inventory. If no inventory exists, a new file is created.
try:
    FileProcessor.read_file(strFileName, lstTbl)
except FileNotFoundError:
    print('Text file does not exist! New text file named \'CDInventory.txt\' created.\n')
    objFile = open(strFileName, 'w')
    objFile.close()
    FileProcessor.read_file(strFileName, lstTbl)


# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
   
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            try:
                FileProcessor.read_file(strFileName, lstTbl)
                IO.show_inventory(lstTbl)
            except FileNotFoundError:
                print('Text file does not exist! New text file named \'CDInventory.txt\' created.\n')
                objFile = open(strFileName, 'w')
                objFile.close()
                
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        try: 
            strID, strTitle, stArtist = IO.input_cd() #unpack and call at the same time
            # 3.3.2 Add item to the table
            DataProcessor.add_cd(strID,strTitle,stArtist)
            continue  # start loop back at top.
        except ValueError:
            print('\nINVALID INPUT DATA\nID MUST BE A NUMBER\n')
    
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
   
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove
        try:
            intIDDel = int(input('Which ID would you like to delete? ').strip())
        # 3.5.2 search thru table and delete CD
            blnCDRemoved = False     
            DataProcessor.delete_cd()
        except ValueError:
            print('\nINVALID INPUT DATA\nID MUST BE A NUMBER\n')
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileProcessor.write_file()
            
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')




