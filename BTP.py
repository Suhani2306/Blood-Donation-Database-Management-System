
import pymysql

class EMU:
    def __init__(self):
        self.conn = pymysql.connect(host="localhost", user="root", passwd="root@123", db="Blood_Donation", charset='utf8')
        self.c = self.conn.cursor()
        print("Connection established. Welcome!")
        print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
        self.nav = ""    

# ------------------------------------------------- LOGIN
        while(self.nav !="q"):
            self.nav = input("\nSelect user:\n(d) - donor, \n(b) - blood bank, \n(m) - medical facility, \n(q) - exit\n")
            if(self.nav== "d"):
                self.d_log()
            elif(self.nav=="b"):
                self.b_log()
            elif(self.nav=="m"):
                self.m_log()
        print("\nConnection ceased!")
        self.conn.close()
    def d_log(self):
        login = input("\nlogin: ")
        v = self.c.execute("select id_donor from blood_donor where id_donor='"+login+"';")
        if(v==0):
            print("no such donor")
            self.nav=""
        else:
            password = input("password: ")
            i = self.c.execute("select id_donor from blood_donor where id_donor='"+login+"' and d_pass ='"+password+"';")
            self.nav=""
            if(i==0):
                print("wrong password, try again")
            else:
                print("\nWelcome!\n")
                self.nav="q"
                self.menu()
    def b_log(self):
        login = input("\nlogin: ")
        v = self.c.execute("select id_bank from blood_bank where id_bank='"+login+"';")
        if(v==0):
            print("no such bank")
            self.nav=""
        else:
            password = input("password: ")
            i = self.c.execute("select id_bank from blood_bank where id_bank='"+login+"' and b_pass ='"+password+"';")
            if(i==0):
                print("wrong password, try again")
                self.nav=""
            else:
                print("\nWelcome!\n")
                self.nav="q"
                self.menu()
    def m_log(self):
        login = input("\nlogin: ")
        v = self.c.execute("select id_facility from med_facility where id_facility='"+login+"';")
        if(v==0):
            print("no such medical facility")
            self.nav=""
        else:
            password = input("password: ")
            i = self.c.execute("select id_facility from med_facility where id_facility='"+login+"' and m_pass ='"+password+"';")
            if(i==0):
                print("wrong password, try again")
                self.nav=""
            else:
                print("\nWelcome!\n")
                self.nav="q"
                self.menu()

# ------------------------------------------------- MENU
    def menu(self):
        self.nav = ""
        while(self.nav != "q"):
            self.nav = input("\nMenu:\n(1) - donor list,\n(2) - add new donor,\n(3) - update donor,\n(4) - donation list,\n(5) - add new donation,\n(6) - supplies,\n(7) - update supplies,\n(8) - request list,\n(9) - add new request,\n(10) - update request,\n(11) - transport list,\n(12) - medical facility list,\n(13) - blood bank list,\n(q) - exit\n")
            if(self.nav == "1"):
                self.sdnr()
            elif(self.nav == "2"):
                self.adnr()
            elif(self.nav == "3"):
                self.updnr()
            elif(self.nav == "4"):
                self.sdnt()
            elif(self.nav == "5"):
                self.adnt()
            elif(self.nav == "6"):
                self.ssup()
            elif(self.nav == "7"):
                self.upsup()
            elif(self.nav == "8"):
                self.srq()
            elif(self.nav == "9"):
                self.addrq()
            elif(self.nav == "10"):
                self.uprq() 
            elif(self.nav == "11"):
                self.st()
            elif(self.nav == "12"):
                self.sf()          
            elif(self.nav == "13"):
                self.sb()                            

# ------------------------------------------------- DONOR LIST
    def sdnr(self):
        self.c.execute("SELECT id_donor, donor_firstname, donor_lastname, donor_email, birth_date FROM blood_donor order by id_donor;")
        res = self.c.fetchall()   
        print("%-5s %-15s %-15s %-25s %-12s" % ('id', 'first name', 'last name', 'e-mail adress', 'birth date'))
        print("==========================================================================")
        for v in res:
            id_donor = v[0]
            donor_firstname = v[1]
            donor_lastname = v[2]
            donor_email = v[3]
            birth_date = v[4]
            print("%-5s %-15s %-15s %-25s %-12s" % (id_donor, donor_firstname, donor_lastname, donor_email, birth_date))
        print("\n")

# ------------------------------------------------- NEW DONOR  
    def adnr(self):
        ''' I
        id_donor = input ('id: ')
        donor_firstname = input ('first name: ')
        donor_lastname = input ('last name: ')
        donor_email = input ('e-mail adress: ')
        birth_date = input ('birth date: ')
        self.c.execute("INSERT INTO blood_donor VALUES (id_donor, donor_firstname, donor_lastname, donor_email, birth_date);")
        self.conn.commit()
        print("data entered")
        '''
        ''' II
        adnr = ("INSERT INTO blood_donor" "(id_donor, donor_firstname, donor_lastname, donor_email, birth_date)" "VALUES (%(id_donor)s, %(donor_firstname)s, donor_lastnames, %(donor_email)s, %(birth_date)s)")
        adnr = {'id_donor': input ('id: '),'donor_firstname': input ('first name: '),'donor_lastname': input ('last name: '),'donor_email': input ('e-mail adress: '),'birth_date': input ('birth date: ')}
        self.c.execute(adnr)
        self.conn.commit()
        print("data entered")
        '''
        ''' III
        id_donor = input ('id: ')
        donor_firstname = input ('first name: ')
        donor_lastname = input ('last name: ')
        donor_email = input ('e-mail adress: ')
        birth_date = input ('birth date: ')
        self.c.execute("""INSERT INTO blood_donor (id_donor, donor_firstname, donor_lastname, donor_email, birth_date) VALUES ("%s", "%s", "%s", "%s", "%s")""" % (id_donor, donor_firstname, donor_lastname, donor_email, birth_date))
        self.conn.commit()
        print("data entered")        
        '''
        ''' IV - sukces '''

        self.c.execute("INSERT INTO blood_donor(donor_firstname, donor_lastname, donor_email, birth_date) VALUES ( %s, %s, %s, %s)", (input("first name: "), input("last name: "), input("e-mail adress: "), input("birth date: ")))
        self.conn.commit()
        print("\n---new donor entered---\n")

# ------------------------------------------------- UPDATE DONOR
    def updnr(self):
        self.nav = ""
        while(self.nav != "b"):        
            self.nav = input("\nUpdate:\n(1) - donor id,\n(2) - first name,\n(3) - last name,\n(4) - e-mail adress,\n(5) - birth date,\n(6) - remove donor from the list,\n(b) - go back to menu\n")
            if(self.nav == "1"):
                self.did()
            elif(self.nav == "2"):
                self.dfn()
            elif(self.nav == "3"):
                self.dln()
            elif(self.nav == "4"):
                self.de()
            elif(self.nav == "5"):
                self.dbd()
            elif(self.nav == "6"):
                self.drmv()
        self.menu()
    def did(self):
        self.c.execute("""UPDATE blood_donor SET id_donor=%s WHERE id_donor=%s""", (input('\nset new id: '), input("current id: ")))
        self.conn.commit()
        print("\n---id updated---\n")
    def dfn(self):
        self.c.execute("""UPDATE blood_donor SET donor_firstname=%s WHERE id_donor=%s""", (input('\nset new first name: '), input("id: ")))
        self.conn.commit()
        print("\n---first name updated---\n")
    def dln(self):
        self.c.execute("""UPDATE blood_donor SET donor_lastname=%s WHERE id_donor=%s""", (input('\nset new last name: '), input("id: ")))
        self.conn.commit()
        print("\n---last name updated---\n") 
    def de(self):
        self.c.execute("""UPDATE blood_donor SET donor_email=%s WHERE id_donor=%s""", (input('\nset new e-mail adress: '), input("id: ")))
        self.conn.commit()
        print("\n---e-mail adress updated---\n")  
    def dbd(self):
        self.c.execute("""UPDATE blood_donor SET birth_date=%s WHERE id_donor=%s""", (input('\nset new birth date: '), input("id: ")))
        self.conn.commit()
        print("\n---birth date updated---\n")
    def drmv(self):
        self.c.execute("DELETE FROM blood_donor WHERE id_donor=%s", (input("id: ")))
        self.conn.commit()
        print("\n---donor removed---\n")

# ------------------------------------------------- DONATION LIST
    def sdnt(self):
        self.c.execute("SELECT id_donation, donation_date, blood_type_donation, blood_quantity_donation, id_donor FROM blood_donation order by id_donation;")
        res = self.c.fetchall()   
        print("%-6s %-15s %-10s %-10s %-10s" % ('\nid', 'date', 'type', 'quantity', 'donor id'))
        print("====================================================")     
        for v in res:
            id_donation = v[0]
            donation_date = v[1]
            blood_type_donation = v[2]
            blood_quantity_donation = v[3]
            id_donor = v[4]
            print("%-5s %-15s %-10s %-10s %-10s" % (id_donation, donation_date, blood_type_donation, blood_quantity_donation, id_donor))
        print("\n")

# ------------------------------------------------- NEW DONATION
    def adnt(self):
        self.c.execute("INSERT INTO blood_donation (donation_date, blood_type_donation, blood_quantity_donation, id_donor, id_bank) VALUES (%s, %s, %s, %s, %s)", (input("date: "), input("blood type: "), input("quantity: "), input("donor id: "), input("bank id: ")))
        self.conn.commit()
        print("\n---new donation entered---\n")

# ------------------------------------------------- SUPPLY LIST
    def ssup(self):
        self.c.execute("SELECT id_bank, blood_type_supply, blood_quantity_supply FROM blood_bank_supplies order by id_bank;")
        res = self.c.fetchall()
        print("%-11s %-10s %-10s" % ('\nbank id', 'type', 'quantity(ml)'))
        print("=================================")     
        for v in res:
            id_bank = v[0]
            blood_type_supply = v[1]
            blood_quantity_supply = v[2]
            print("%-10s %-10s %-10s" % (id_bank, blood_type_supply, blood_quantity_supply))
        print("\n")

# ------------------------------------------------- UPDATE SUPPLY LIST
    def upsup(self):
        self.nav = ""
        print("\nUpdate:")
        while(self.nav != "b"):        
            self.nav = input("(1) - update supplies,\n(b) - go back to main menu\n")
            if(self.nav == "1"):
                self.us()
        self.menu()
    def us(self):
        self.c.execute("""UPDATE blood_bank_supplies SET blood_quantity_supply=%s WHERE blood_type_supply=%s and id_bank=%s""", (input("\nset new quantity (ml): "), input("enter blood type: "), input("enter bank id: ")))
        self.conn.commit()
        print("\n---supplies updated---\n")

# ------------------------------------------------- REQUEST LIST
    def srq(self):
        self.c.execute("SELECT id_request, request_type, request_quantity, request_date, id_facility, id_bank FROM blood_request order by id_request;")
        res = self.c.fetchall()   
        print("%-5s %-10s %-15s %-12s %-12s %-12s" % ('id', 'type', 'quantity (ml)', 'date', 'facility id', 'bank id'))
        print("==================================================================")
        for v in res:
            id_request = v[0]
            request_type = v[1]
            request_quantity = v[2]
            request_date = v[3]
            id_facility = v[4]
            id_bank = v[5]
            print("%-5s %-10s %-15s %-12s %-12s %-12s" % (id_request, request_type, request_quantity, request_date, id_facility, id_bank))
        print("\n")
        
# ------------------------------------------------- NEW REQUEST
    def addrq(self):
        self.c.execute("INSERT INTO blood_request (request_type, request_quantity, request_date, id_facility, id_bank) VALUES (%s, %s, %s, %s, %s)", (input("blood type: "), input("quantity (ml): "), input("request date: "), input("facility id: "), input("bank id: ")))
        self.conn.commit()
        print("\n---new request entered---\n")

# ------------------------------------------------- UPDATE DONOR
    def uprq(self):
        self.nav = ""
        while(self.nav != "b"):        
            self.nav = input("\nUpdate:\n(1) - blood type,\n(2) - blood quantity,\n(3) - request date,\n(4) - facility id,\n(5) - bank id,\n(6) - remove request from the list,\n(b) - go back to menu\n")
            if(self.nav == "1"):
                self.rt()
            elif(self.nav == "2"):
                self.rq()
            elif(self.nav == "3"):
                self.rd()
            elif(self.nav == "4"):
                self.rf()
            elif(self.nav == "5"):
                self.rb()
            elif(self.nav == "6"):
                self.delr()
        self.menu()
    def rt(self):
        self.c.execute("""UPDATE blood_request SET request_type=%s WHERE id_request=%s""", (input('\nset new blood type: '), input("request id: ")))
        self.conn.commit()
        print("\n---blood type updated---\n")
    def rq(self):
        self.c.execute("""UPDATE blood_request SET request_quantity=%s WHERE id_request=%s""", (input('\nset new blood quantity: '), input("request id: ")))
        self.conn.commit()
        print("\n---quantity updated---\n")
    def rd(self):
        self.c.execute("""UPDATE blood_request SET request_date=%s WHERE id_request=%s""", (input('\nset new request date: '), input("id: ")))
        self.conn.commit()
        print("\n---date updated---\n") 
    def rf(self):
        self.c.execute("""UPDATE blood_request SET id_facility=%s WHERE id_request=%s""", (input('\nset new facility id: '), input("id: ")))
        self.conn.commit()
        print("\n---facility id updated---\n")  
    def rb(self):
        self.c.execute("""UPDATE blood_request SET id_bank=%s WHERE id_request=%s""", (input('\nset new bank id: '), input("id: ")))
        self.conn.commit()
        print("\n---bank id updated---\n")

# ------------------------------------------------- TRANSPORT LIST
    def st(self):
        self.c.execute("SELECT id_transport, blood_type, transport_quantity, transport_date, id_facility, id_bank FROM blood_transport order by id_transport;")
        res = self.c.fetchall()   
        print("%-5s %-10s %-15s %-12s %-12s %-12s" % ('id', 'type', 'quantity (ml)', 'date', 'facility id', 'bank id'))
        print("==================================================================")
        for v in res:
            id_transport = v[0]
            blood_type = v[1]
            transport_quantity = v[2]
            transport_date = v[3]
            id_facility = v[4]
            id_bank = v[5]
            print("%-5s %-10s %-15s %-12s %-12s %-12s" % (id_transport, blood_type, transport_quantity, transport_date, id_facility, id_bank))
        print("\n")
    
# ------------------------------------------------- MEDICAL FACILITIES LIST
    def sf(self):
        self.c.execute("SELECT id_facility, facility_name, facility_adress FROM med_facility order by id_facility;")
        res = self.c.fetchall()   
        print("%-5s %-40s %-40s" % ('id', 'facility name', 'facility adress'))
        print("==============================================================")
        for v in res:
            id_facility = v[0]
            facility_name = v[1]
            facility_adress = v[2]
            print("%-5s %-40s %-40s" % (id_facility, facility_name, facility_adress))
        print("\n")

# ------------------------------------------------- BLOOD BANK LIST
    def sb(self):
        self.c.execute("SELECT id_bank, bank_name, bank_adress FROM blood_bank order by id_bank;")
        res = self.c.fetchall()   
        print("%-5s %-55s %-40s" % ('id', 'bank name', 'bank adress'))
        print("============================================================================")
        for v in res:
            id_bank = v[0]
            bank_name = v[1]
            bank_adress = v[2]
            print("%-5s %-55s %-40s" % (id_bank, bank_name, bank_adress))
        print("\n")

start = EMU()
