import mysql.connector


class Department:
    def __init__(self):
        pass

    def addDepartment(self,deptname,deptcontact,deptdetails):
        #connect database
        mysqldb = mysql.connector.connect(host="localhost", database="phcms", user="root", password="9494846620")
        #start database
        cursor = mysqldb.cursor()
        #call store procedure
        cursor.callproc("save_department",(deptname,deptcontact,deptdetails))
        #perform save operation
        mysqldb.commit()


    def getdepartment(self, id):
        departments = []
        # connect database
        mysqldb = mysql.connector.connect(host="localhost", database="phcms", user="root", password="9494846620")
        # start database
        cursor = mysqldb.cursor()
        # call store procedure
        cursor.callproc("get_department", (id,))
        # read the data
        for results in cursor.stored_results():
            for record in results.fetchall():
                departments.append({"id": record[0], "name": record[1], "contact": record[2], "record": record[3]})
        return departments



class Clinician:
    def __init__(self):
        pass

    def saveClinician(self,clinicianname, deptid, cliniciancontact, cliniciandetails):
        #connect database
        mysqldb = mysql.connector.connect(host="localhost", database="phcms", user="root", password="9494846620")
        #start database
        cursor = mysqldb.cursor()
        #call storeprocedure
        cursor.callproc("save_clinician",(clinicianname, deptid, cliniciancontact, cliniciandetails))
        #perform save operation
        mysqldb.commit()

    def getClinician(self, id):
        clinicians = []
        mysqldb = mysql.connector.connect(host="localhost", database="phcms", user="root", password="9494846620")
        cursor = mysqldb.cursor()
        cursor.callproc("get_clinician", (id,))
        for results in cursor.stored_results():
            for record in results.fetchall():
                clinicians.append({"id": record[0], "name": record[1], "department": record[2], "contact": record[3], "details": record[4]})
        return clinicians


class Patient:
    def __init__(self):
        pass

    def savePatient(self,patname, patcontact, pataddress, patdetails):
        #connect database
        mysqldb = mysql.connector.connect(host="localhost", database="phcms", user="root", password="9494846620")
        #start database
        cursor = mysqldb.cursor()
        #call storeprocedure
        cursor.callproc("save_patient",(patname, patcontact, pataddress, patdetails))
        #perform save operation
        mysqldb.commit()

    def getPatient(self, id):
        patients = []
        mysqldb = mysql.connector.connect(host="localhost", database="phcms", user="root", password="9494846620")
        cursor = mysqldb.cursor()
        cursor.callproc("get_patient", (id,))
        for results in cursor.stored_results():
            for record in results.fetchall():
                patients.append({"id": record[0], "name": record[1], "contact": record[2], "address": record[3], "details": record[4]})
        return patients




