import MySQLdb

def hospitalsTreatingIn(issue,latitude,longitude):
    lowerLonLimit = longitude - 0.009
    highLonLimit = longitude + 0.009
    lowerLatLimit = int(latitude) - 0.008
    highLatLimit = int(latitude) + 0.008
    hospitals = findHospitals(lowerLonLimit,highLonLimit,lowerLatLimit,highLatLimit,issue)
    hospitals = '''
    recommendations = "<select name="department" id="department" class="form-select">"
    hospitalId = 
    for hospital in hospitals:
        hospitalId = hospital[0]
        hospitalName = hospitals[1]
        addThis = "<option value="{}">{}</option>".format(hospitalId,hospitalName)
        recommendations = recommendations + addThis
    recommendations = recommendations + ""</select>
    
    <select name="department" id="department" class="form-select">
                <option value="">Select Department</option>
                <option value="Department 1">Department 1</option>
                <option value="Department 2">Department 2</option>
                <option value="Department 3">Department 3</option>
              </select>'''.format('')
    
def clinicFor(issue):
    title = 'Hospitals Treating {}'.format(issue)
    text = str(title) + 'Hospitals Here'
    return text

def findHospitals(lowerLonLimit,highLonLimit,lowerLatLimit,highLatLimit,issue):
    conn = MySQLdb.connect("BIZBIZ.mysql.pythonanywhere-services.com","BIZBIZ","myResults","BIZBIZ$p" )

    cursor = conn.cursor()

    resut = {}


    cursor.execute("SET @d = '%s'"% (lowerLonLimit))
    cursor.execute("SET @e = '%s'"% (highLonLimit))
    cursor.execute("SET @f = '%s'"% (lowerLatLimit))
    cursor.execute("SET @g = '%s'"% (highLatLimit))
    cursor.execute("SET @h = '%s'"% (issue))

    
    cursor.execute("""SET @s = CONCAT("SELECT hospitalName, hospitalId, FROM hospitalsTable WHERE issue LIKE '%", @h , "%' AND hospitalLatitude BETWEEN ", @f , " AND ", @g , " AND hospitalLongitude BETWEEN ", @d , " AND ", @e , " UNION SELECT hospitalName, hospitalId FROM hospitalsTable WHERE hospitalName LIKE '%", @h , "%' AND hospitalLatitude BETWEEN ", @f , " AND ", @g , " AND hospitalLongitude BETWEEN ", @d , " AND ", @e , """)
    cursor.execute("PREPARE stmt FROM @s")
    cursor.execute("EXECUTE stmt")
    hospitals = cursor.fetchall()
    cursor.close()
    conn.close()

    numres = len(hospitals)
    recommendations = """<select name="department" id="department" class="form-select">"""

    if numres == 0:
        cursor.execute("SET @d = '%s'"% (lowerLonLimit))
        cursor.execute("SET @e = '%s'"% (highLonLimit))
        cursor.execute("SET @f = '%s'"% (lowerLatLimit))
        cursor.execute("SET @g = '%s'"% (highLatLimit))
        cursor.execute("SET @h = '%s'"% (issue))

        
        cursor.execute("""SET @s = CONCAT("SELECT hospitalName, hospitalId, FROM hospitalsTable WHERE issue LIKE '%", @h , "%' AND hospitalLatitude BETWEEN ", @f , " AND ", @g , " AND hospitalLongitude BETWEEN ", @d , " AND ", @e , " UNION SELECT hospitalName, hospitalId FROM hospitalsTable WHERE hospitalName LIKE '%", @h , "%' AND hospitalLatitude BETWEEN ", @f , " AND ", @g , " AND hospitalLongitude BETWEEN ", @d , " AND ", @e , """)
        cursor.execute("PREPARE stmt FROM @s")
        cursor.execute("EXECUTE stmt")
        hospitals = cursor.fetchall()
        cursor.close()
        conn.close()
        
        numres = len(hospitals)
        
        
        return """<select name="department" id="department" class="form-select"><option value="none">No hospital</option>"""
    else:
        
        
        for hospital in hospitals:
            hospitalName = hospitals[0]
            hospitalId = hospital[1]
            addThis = """<option value="{}">{}</option>""".format(hospitalId,hospitalName)
            recommendations = recommendations + addThis
            
    
        recommendations = recommendations  + "</select>"
        
        
        
        

