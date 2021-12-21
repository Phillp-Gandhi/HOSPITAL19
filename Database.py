import MySQLdb, Location

def getIssueCategories():
    conn = MySQLdb.connect("hospital19.mysql.pythonanywhere-services.com","hospital19","HorseSabuniAluoch","hospital19$priest" )

    cursor = conn.cursor()


    cursor.execute("""SET @s = CONCAT("SELECT issueCategoryName, issueCategoryLink, issueCategoryFaIcon FROM issueCategories""")
    cursor.execute("PREPARE stmt FROM @s")
    cursor.execute("EXECUTE stmt")
    issueCategories = cursor.fetchall()
    cursor.close()
    conn.close()



    return issueCategories

def getIssueData(issue):
    conn = MySQLdb.connect("hospital19.mysql.pythonanywhere-services.com","hospital19","HorseSabuniAluoch","hospital19$priest" )

    cursor = conn.cursor()

    resut = {}


    cursor.execute("SET @i = '%s'"% (issue))


    cursor.execute("""SET @s = CONCAT("SELECT subIssueName, subIssueData FROM subIssuesTable WHERE subIssueCategory LIKE '%", @i , "%'") """)
    cursor.execute("PREPARE stmt FROM @s")
    cursor.execute("EXECUTE stmt")
    issues = cursor.fetchall()
    cursor.close()
    conn.close()

    numres = len(issues)

    if numres == 0:
        return ['No Data', 'That issue was not found']
    else:
        return issues

def savePatientQuestion(patientName,patientEmail,patientPhone,patientLocation,patientLatitude,patientLongitude,patientSubIssue,patientMessage):


    conn = MySQLdb.connect("hospital19.mysql.pythonanywhere-services.com","hospital19","HorseSabuniAluoch","hospital19$priest" )

    cursor = conn.cursor()

    cursor.execute("SET @i = '%s'"% (patientSubIssue))
    cursor.execute("SET @n = '%s'"% (patientName))
    cursor.execute("SET @e = '%s'"% (patientEmail))
    cursor.execute("SET @p = '%s'"% (patientPhone))
    cursor.execute("SET @la = '%s'"% (patientLatitude))
    cursor.execute("SET @lo = '%s'"% (patientLongitude))
    cursor.execute("SET @m = '%s'"% (patientMessage))
    cursor.execute("SET @loc = '%s'"% (patientLocation))

    cursor.execute("""SET @s = CONCAT("INSERT INTO patientQuestionsTable (patientName,patientEmail,patientPhone,patientLocation,patientLatitude,patientLongitude,patientSubIssue,patientMessage)
                   VALUES ('", @n , "', '", @e , "', '", @p , "', '", @loc , "','", @la , "', '", @lo , "','", @i , "','", @m , "')")""")
    cursor.execute("PREPARE stmt FROM @s")
    cursor.execute("EXECUTE stmt")
    conn.commit()
    cursor.close()
    conn.close()

    return 'Submitted successfully'

def clinicFor(lowerLonLimit,highLonLimit,lowerLatLimit,highLatLimit,issue):
    conn = MySQLdb.connect("hospital19.mysql.pythonanywhere-services.com","hospital19","HorseSabuniAluoch","hospital19$priest" )

    cursor = conn.cursor()

    resut = {}


    cursor.execute("SET @d = '%s'"% (lowerLonLimit))
    cursor.execute("SET @e = '%s'"% (highLonLimit))
    cursor.execute("SET @f = '%s'"% (lowerLatLimit))
    cursor.execute("SET @g = '%s'"% (highLatLimit))
    cursor.execute("SET @h = '%s'"% (issue))
    table = str(issue) + str('Table')
    cursor.execute("SET @table = '%s'"% (table))

    cursor.execute("""SET @s = CONCAT("SELECT hospitalName, hospitalDescription, hospitalEmail, hospitalPhone, hospitalLocation, hospitaltLatitude, hospitalLongitude, hospitalImage, hospitalTwLink, hospitalFbLink, hospitalInLink, hospitalLnLink, isAdmitting from ", @table , " WHERE isAdmitting = 'yes' OR hospitalLatitude BETWEEN ", @f , " AND ", @g , " AND hospitalLongitude BETWEEN ", @d , " AND ", @e , ")""")

    #cursor.execute("""SET @s = CONCAT("SELECT hospitalId FROM ", @t , " WHERE isAdmitting = 'yes' OR latitude BETWEEN ", @f , " AND ", @g , " AND longitude BETWEEN ", @d , " AND ", @e , ")""")
    cursor.execute("PREPARE stmt FROM @s")
    cursor.execute("EXECUTE stmt")
    clinics = cursor.fetchall()
    cursor.close()
    conn.close()
    clinicsForThisIssue = '''
    <!-- ======= Doctors Section ======= -->
    <section id="doctors" class="doctors">
      <div class="container">

        <div class="section-title">
          <h2>Hospitals / Clinics</h2>
          <p>These are the hospitals close to your set location and/or are currently accepting physical service for patients with {} issues.</p>
          <p>To reset your location <a href="https://hospital19.pythonanywhere.com/set-location">click here</a>.</p>
          <p>To see all hospitals treating {} <a href="https://hospital19.pythonanywhere.com/visit-clinic?issue={}">click here</a>.</p>
          <p>To see all hospitals, <a href="https://hospital19.pythonanywhere.com/visit-clinic?all>click here</a></p>
        </div>

        <div class="row">
    '''.format(issue,issue,issue)
    for clinic in clinics:
        hospitalName = clinics[0]
        HospitalDescription = clinics[1]
        HospitalLevel = clinics[2]
        HospitalLocation =clinics[3]
        isAdmitting = clinics[4]
        hospitalPhone = clinics[5]
        hospitalEmail = clinics[6]
        hospitalImageLink = clinics[7]
        twLink = clinics[8]
        fbLink = clinics[9]
        inLink = clinics[10]
        lnLink = clinics[11]

        clinicsForThisIssue = str(clinicsForThisIssue) + '''
        <div class="col-lg-6">
            <div class="member d-flex align-items-start">
              <div class="pic"><img src="{}" class="img-fluid" alt="{}"></div>
              <div class="member-info">
                <h4>{}</h4>
                <span>Level: {} </span>
                <p>{}</p>
                <p>{}</p>
                <p>Location: {}</p>
                <p>Phone: {}</p>
                <p>Email: {}</p>
                <div class="social">
                  <a href="{}"><i class="ri-twitter-fill"></i></a>
                  <a href="{}"><i class="ri-facebook-fill"></i></a>
                  <a href="{}"><i class="ri-instagram-fill"></i></a>
                  <a href="{}"> <i class="ri-linkedin-box-fill"></i> </a>
                </div>
              </div>
            </div>
          </div>'''.format(hospitalImageLink,hospitalName,hospitalName,HospitalLevel,isAdmitting,HospitalDescription,HospitalLocation,hospitalPhone,hospitalEmail,twLink,fbLink,inLink,lnLink)



    #for id in ids:
    #    cursor.execute("SET @i = %s "% (id))
     #   cursor.execute("""SET @o = CONCAT("SELECT hospitalName, HospitalDescription, HospitalLevel, HospitalLocation FROM hospitalDetailsTable
      #                 WHERE hospitalId = ", @i , "")""")
       # cursor.execute("PREPARE stmt FROM @o")
        #cursor.execute("EXECUTE stmt")
    #    hospitalDetails = cursor.fetchall()
    #    hospitalName = hospitalDetails[0]
    #    HospitalDescription = hospitalDetails[1]
    #    HospitalLevel = hospitalDetails[2]
    #    HospitalLocation =hospitalDetails[3]
     #   clinics = '''<div>
      #  <p></p>
       # <p></p>
        #<p></p>
    #    <p></p>
     #   </div>'''


    '''
    get hospitalId from issueTable
        where isAdmiting=yes

    get hospitalName, HospitalDescription, HospitalLevel, HospitalLocation from hospitalDetails
        where hospitalID = hospitalId

    get HospitalLocation HospitalLocation

    where issue =issue and location is 50km radius
    '''

    return clinicsForThisIssue

def addHospital(hospitalName, hospitalDescription, hospitalEmail, hospitalPhone, hospitalLocation,    hospitaltLatitude, hospitalLongitude, hospitalImage, hospitalTwLink, hospitalFbLink, hospitalInLink, hospitalLnLink, isAdmitting):

    conn = MySQLdb.connect("hospital19.mysql.pythonanywhere-services.com","hospital19","HorseSabuniAluoch","hospital19$priest" )

    cursor = conn.cursor()
    issueTable = str(issue) + 'issueTable'

    cursor.execute("SET @issueTable = '%s"% ())
    cursor.execute("SET hospitalName = '%s"% (hospitalName))
    cursor.execute("SET hospitalDescription = '%s"% (hospitalDescription))
    cursor.execute("SET hospitalEmail = '%s"% (hospitalEmail))
    cursor.execute("SET hospitalPhone = '%s"% (hospitalPhone))
    cursor.execute("SET hospitalLocation = '%s"% (hospitalLocation))
    cursor.execute("SET hospitaltLatitude = '%s"% (hospitaltLatitude))
    cursor.execute("SET hospitalLongitude = '%s"% (hospitalLongitude))
    cursor.execute("SET hospitalTwLink = '%s"% (hospitalImage))
    cursor.execute("SET hospitalFbLink = '%s"% (hospitalTwLink))
    cursor.execute("SET hospitalInLink = '%s"% (hospitalFbLink))
    cursor.execute("SET hospitalLnLink = '%s"% (hospitalInLink))
    cursor.execute("SET isAdmitting = '%s"% (hospitalLnLink))
    cursor.execute("SET isAdmitting = '%s"% (isAdmitting))


    cursor.execute("""SET @s = CONCAT("INSERT INTO hospitalsTable (hospitalName, hospitalDescription, hospitalEmail, hospitalPhone, hospitalLocation,
    hospitaltLatitude, hospitalLongitude, hospitalImage, hospitalTwLink, hospitalFbLink, hospitalInLink, hospitalLnLink, isAdmitting) VALUES ()")""")
    cursor.execute("""SET @s = CONCAT("INSERT INTO hospitalsTable (hospitalName, hospitalDescription, hospitalEmail, hospitalPhone, hospitalLocation,
    hospitaltLatitude, hospitalLongitude, hospitalImage, hospitalTwLink, hospitalFbLink, hospitalInLink, hospitalLnLink, isAdmitting) VALUES ()")""")

    curosr.execute("PREPARE stmt FROM @s")
    cursor.execute("EXECUTE stmt")
    addedHospital = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.cross()

    return result

def getAllHospitals(issue):
    conn = MySQLdb.connect("hospital19.mysql.pythonanywhere-services.com","hospital19","HorseSabuniAluoch","hospital19$priest" )

    cursor = conn.cursor()


    resut = {}
    table = str(issue) + 'ClinicsTable'

    cursor.execute("SET @table = '%s'"% (table))

    cursor.execute("""SET @s = CONCAT("SELECT hospitalName, hospitalDescription, hospitalEmail, hospitalPhone, hospitalLocation, hospitaltLatitude, hospitalLongitude, hospitalImage, hospitalTwLink, hospitalFbLink, hospitalInLink, hospitalLnLink, isAdmitting from ", @table , " where isAdmitting = 'yes'")""")

    #cursor.execute("""SET @s = CONCAT("SELECT hospitalName, HospitalDescription, HospitalLevel, HospitalLocation, isAdmitting, hospitalPhone, hospitalEmail, hospitalImage, twLink, fbLink, inLink, lnLink")""")

    #cursor.execute("""SET @s = CONCAT("SELECT hospitalId FROM ", @t , " WHERE isAdmitting = 'yes' OR latitude BETWEEN ", @f , " AND ", @g , " AND longitude BETWEEN ", @d , " AND ", @e , ")""")
    cursor.execute("PREPARE stmt FROM @s")
    cursor.execute("EXECUTE stmt")
    clinics = cursor.fetchall()
    cursor.close()
    conn.close()
    clinicsForThisIssueWithoutLocation = '''
    <!-- ======= Doctors Section ======= -->
    <section id="doctors" class="doctors">
      <div class="container">

        <div class="section-title">
          <h2>Hospitals / Clinics</h2>
          <p>All hospitals</p>
          To reset your location <a href="https://hospital19.pythonanywhere.com/set-location">click here</a>.
        </div>

        <div class="row">'''
    for clinic in clinics:
        hospitalName = clinic[0]
        HospitalDescription = clinic[1]
        HospitalLevel = clinic[2]
        HospitalLocation =clinic[3]
        isAdmitting = clinic[4]
        hospitalPhone = clinic[5]
        hospitalEmail = clinic[6]
        hospitalImageLink = clinic[7]
        twLink = clinic[8]
        fbLink = clinic[9]
        inLink = clinic[10]
        lnLink = clinic[11]


        clinicsForThisIssueWithoutLocation = str(clinicsForThisIssueWithoutLocation) + '''
        <div class="col-lg-6">
            <div class="member d-flex align-items-start">
              <div class="pic"><img src="{}" class="img-fluid" alt="{}"></div>
              <div class="member-info">
                <h4>{}</h4>
                <span>Level: {} </span>
                <p>{}</p>
                <p>{}</p>
                <p>Location: {}</p>
                <p>Phone: {}</p>
                <p>Email: {}</p>
                <div class="social">
                  <a href="{}"><i class="ri-twitter-fill"></i></a>
                  <a href="{}"><i class="ri-facebook-fill"></i></a>
                  <a href="{}"><i class="ri-instagram-fill"></i></a>
                  <a href="{}"> <i class="ri-linkedin-box-fill"></i> </a>
                </div>
              </div>
            </div>
          </div>'''.format(hospitalImageLink,hospitalName,hospitalName,HospitalLevel,isAdmitting,HospitalDescription,HospitalLocation,hospitalPhone,hospitalEmail,twLink,fbLink,inLink,lnLink)

    clinicsForThisIssueWithoutLocation = clinicsForThisIssueWithoutLocation + '''</div>

      </div>
    </section><!-- End Doctors Section -->'''

    return clinicsForThisIssueWithoutLocation

def getHospitalsWithoutLocation(issue):
    conn = MySQLdb.connect("hospital19.mysql.pythonanywhere-services.com","hospital19","HorseSabuniAluoch","hospital19$priest" )

    cursor = conn.cursor()

    resut = {}



    cursor.execute("SET @h = '%s'"% (issue))
    table = str(issue) + str('Table')
    cursor.execute("SET @t = '%s'"% (table))

    cursor.execute("""SET @s = CONCAT("SELECT hospitalName, HospitalDescription, HospitalLevel, HospitalLocation, isAdmitting, hospitalPhone, hospitalEmail, hospitalImage, twLink, fbLink, inLink, lnLink
                   FROM ", @t , " WHERE isAdmitting = 'yes'")""")

    #cursor.execute("""SET @s = CONCAT("SELECT hospitalId FROM ", @t , " WHERE isAdmitting = 'yes' OR latitude BETWEEN ", @f , " AND ", @g , " AND longitude BETWEEN ", @d , " AND ", @e , ")""")
    cursor.execute("PREPARE stmt FROM @s")
    cursor.execute("EXECUTE stmt")
    clinics = cursor.fetchall()
    cursor.close()
    conn.close()
    clinicsForThisIssueWithoutLocation = '''
    <!-- ======= Doctors Section ======= -->
    <section id="doctors" class="doctors">
      <div class="container">

        <div class="section-title">
          <h2>Hospitals / Clinics</h2>
          <p>These are the hospitals currently accepting physical service for patients with {} issues.</p>
          <p>To reset your location <a href="https://hospital19.pythonanywhere.com/set-location">click here</a>.</p>
          <p>To see all hospitals treating {} <a href="https://hospital19.pythonanywhere.com/visit-clinic?issue={}">click here</a>.</p>

        </div>

        <div class="row">'''.format(issue,issue,issue)
    for clinic in clinics:
        hospitalName = clinics[0]
        HospitalDescription = clinics[1]
        HospitalLevel = clinics[2]
        HospitalLocation =clinics[3]
        isAdmitting = clinics[4]
        hospitalPhone = clinics[5]
        hospitalEmail = clinics[6]
        hospitalImageLink = clinics[7]
        twLink = clinics[8]
        fbLink = clinics[9]
        inLink = clinics[10]
        lnLink = clinics[11]


        clinicsForThisIssueWithoutLocation = str(clinicsForThisIssueWithoutLocation) + '''
        <div class="col-lg-6">
            <div class="member d-flex align-items-start">
              <div class="pic"><img src="{}" class="img-fluid" alt="{}"></div>
              <div class="member-info">
                <h4>{}</h4>
                <span>Level: {} </span>
                <p>{}</p>
                <p>{}</p>
                <p>Location: {}</p>
                <p>Phone: {}</p>
                <p>Email: {}</p>
                <div class="social">
                  <a href="{}"><i class="ri-twitter-fill"></i></a>
                  <a href="{}"><i class="ri-facebook-fill"></i></a>
                  <a href="{}"><i class="ri-instagram-fill"></i></a>
                  <a href="{}"> <i class="ri-linkedin-box-fill"></i> </a>
                </div>
              </div>
            </div>
          </div>'''.format(hospitalImageLink,hospitalName,hospitalName,HospitalLevel,isAdmitting,HospitalDescription,HospitalLocation,hospitalPhone,hospitalEmail,twLink,fbLink,inLink,lnLink)

    clinicsForThisIssueWithoutLocation = clinicsForThisIssueWithoutLocation + '''</div>

      </div>
    </section><!-- End Doctors Section -->'''
    return clinicsForThisIssueWithoutLocation