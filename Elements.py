import WhyUs, Hero, Hospitals, Location, Database

def getServiceForm1(title):
    form = '''<form class="" action="https://hospital19.pythonanywhere.com/manage-stress" method="POST">
        <select name="action" id="getService">
        <option value="TalkToExpert">TALK TO A FEEL GOOD HEALTH EXPERT (recommended)</option>
        <option value="VisitInstitution">VISIT A FEEL GOOD INSTITUTION</option>
        <option value="SeeMoreInformation">SEE MORE INFORMATION ABOUT {}</option>
        <option value="SeeRelatedIssues">SEE RELATED ISSUES</option>
        </select><button type="submit">GET SERVICE</button>
        </form>'''.format(title)
    return form

def homeHero():
    heroLinkText = 'Quick Service'
    homeHero =''' <!-- ======= Hero Section ======= -->
  <section id="hero" class="d-flex align-items-center">
    <div class="container">

      <a href="#main-links" class="btn-get-started scrollto">{}</a>
    </div>
  </section><!-- End Hero -->'''.format(heroLinkText)
    return homeHero

def homeWhyUs():

    whyTitle = 'Why Choose Hospital 19?'
    whyText = 'Happiness comes from fellowship but COVID-19 has made it impossible at the moment. So we need to end spread and return everything to sharing, giving and trusting'
    whyUrl = 'https://hospital19.pythonanywhere.com/contact'
    whyLinkText = 'LEARN MORE'
    linkOneUrl = 'https://hospital19.pythonanywhere.com/get-a-service'
    linkOneText = 'Get A Service'
    linkTwoUrl = 'https://hospital19.pythonanywhere.com/injuries'
    linkTwoText = 'See Hospitals'
    linkThreeUrl = 'https://hospital19.pythonanywhere.com/medical-issues'
    linkThreeText = 'Medical issues'
    homeWhyUs = WhyUs.whyUs(whyTitle,whyText,whyUrl,whyLinkText,linkOneUrl,linkOneText,linkTwoUrl,linkTwoText,linkThreeUrl,linkThreeText)

    return homeWhyUs

def getAServiceWhyUs():

    whyTitle = '<br />Help is Out There.'
    whyText = 'Happiness comes from fellowship but COVID-19 has made it impossible at the moment. So we need to end spread and return everything to sharing, giving and trusting'
    whyUrl = 'https://hospital19.pythonanywhere.com/contact'
    whyLinkText = 'LEARN MORE'
    linkOneUrl = 'https://hospital19.pythonanywhere.com/manage-stress'
    linkOneText = 'Am stressed'
    linkTwoUrl = 'https://hospital19.pythonanywhere.com/injuries'
    linkTwoText = 'Am injured'
    linkThreeUrl = 'https://hospital19.pythonanywhere.com/sickness'
    linkThreeText = 'Am sick'
    getAServiceWhyUs = WhyUs.whyUs(whyTitle,whyText,whyUrl,whyLinkText,linkOneUrl,linkOneText,linkTwoUrl,linkTwoText,linkThreeUrl,linkThreeText)

    return getAServiceWhyUs

def hero():

    heroText = 'Quick Service'

    hero = Hero.hero(heroText)

    return hero

def manageStressWhyUs():
    whyTitle = '<br />What is stress?'
    whyText = 'Happiness comes from fellowship but COVID-19 has made it impossible at the moment. So we need to end spread and return everything to sharing, giving and trusting'
    whyUrl = 'https://hospital19.pythonanywhere.com/contact'
    whyLinkText = 'LEARN MORE'
    linkOneUrl = 'https://hospital19.pythonanywhere.com/doctors-advice?issue=stress'
    linkOneText = 'Talk to an Expert'
    linkTwoUrl = 'https://hospital19.pythonanywhere.com/visit-clinic?issue=stress'
    linkTwoText = 'Visit a Feel Good Clinic'
    linkThreeUrl = 'https://hospital19.pythonanywhere.com/medical-issues?issue=stress'
    linkThreeText = 'See Related issues'
    manageStressWhyUs = WhyUs.whyUs(whyTitle,whyText,whyUrl,whyLinkText,linkOneUrl,linkOneText,linkTwoUrl,linkTwoText,linkThreeUrl,linkThreeText)
    return manageStressWhyUs

def injuryWhyUs():

  whyTitle = '<br />About Injuries'
  whyText = 'Happiness comes from fellowship but COVID-19 has made it impossible at the moment. So we need to end spread and return everything to sharing, giving and trusting'
  whyUrl = 'https://hospital19.pythonanywhere.com/contact'
  whyLinkText = 'LEARN MORE'
  linkOneUrl = 'https://hospital19.pythonanywhere.com/doctors-advice?issue=injury'
  linkOneText = 'Talk to an Expert'
  linkTwoUrl = 'https://hospital19.pythonanywhere.com/visit-clinic?issue=injury'
  linkTwoText = 'Visit a Clinic'
  linkThreeUrl = 'https://hospital19.pythonanywhere.com/medical-issues?issue=injury'
  linkThreeText = 'See Related issues'
  injuryWhyUs = WhyUs.whyUs(whyTitle,whyText,whyUrl,whyLinkText,linkOneUrl,linkOneText,linkTwoUrl,linkTwoText,linkThreeUrl,linkThreeText)

  return injuryWhyUs

def sicknessWhyUs():
    whyTitle = '<br />About Illnesses'
    whyText = 'Happiness comes from fellowship but COVID-19 has made it impossible at the moment. So we need to end spread and return everything to sharing, giving and trusting'
    whyUrl = 'https://hospital19.pythonanywhere.com/contact'
    whyLinkText = 'LEARN MORE'
    linkOneUrl = 'https://hospital19.pythonanywhere.com/doctors-advice?issue=sickness'
    linkOneText = 'Talk to an Expert'
    linkTwoUrl = 'https://hospital19.pythonanywhere.com/visit-clinic?issue=sickness'
    linkTwoText = 'Visit a Clinic'
    linkThreeUrl = 'https://hospital19.pythonanywhere.com/medical-issues?issue=sickness'
    linkThreeText = 'See Related issues'
    sicknessWhyUs = WhyUs.whyUs(whyTitle,whyText,whyUrl,whyLinkText,linkOneUrl,linkOneText,linkTwoUrl,linkTwoText,linkThreeUrl,linkThreeText)

    return sicknessWhyUs

def cDcImport(page):

  cDcImport = ''''''
  return cDcImport

def abuseWhyUs():

  whyTitle = '<br />About Abuse'
  whyText = 'Happiness comes from fellowship but COVID-19 has made it impossible at the moment. So we need to end spread and return everything to sharing, giving and trusting'
  whyUrl = 'https://hospital19.pythonanywhere.com/contact'
  whyLinkText = 'LEARN MORE'
  linkOneUrl = 'https://hospital19.pythonanywhere.com/doctors-advice?issue=abuse'
  linkOneText = 'Talk to an Expert'
  linkTwoUrl = 'https://hospital19.pythonanywhere.com/visit-clinic?issue=abuse'
  linkTwoText = 'Visit a Counseling Clinic'
  linkThreeUrl = 'https://hospital19.pythonanywhere.com/medical-issues'
  linkThreeText = 'See Related issues'
  sicknessWhyUs = WhyUs.whyUs(whyTitle,whyText,whyUrl,whyLinkText,linkOneUrl,linkOneText,linkTwoUrl,linkTwoText,linkThreeUrl,linkThreeText)
  return abuseWhyUs

def teethWhyUs():
  whyTitle = '<br />About Teeth'
  whyText = 'Happiness comes from fellowship but COVID-19 has made it impossible at the moment. So we need to end spread and return everything to sharing, giving and trusting'
  whyUrl = 'https://hospital19.pythonanywhere.com/contact'
  whyLinkText = 'LEARN MORE'
  linkOneUrl = 'https://hospital19.pythonanywhere.com/doctors-advice?issue=teeth'
  linkOneText = 'Talk to an Expert'
  linkTwoUrl = 'https://hospital19.pythonanywhere.com/visit-clinic?issue=teeth'
  linkTwoText = 'Visit a Dentist Clinic'
  linkThreeUrl = 'https://hospital19.pythonanywhere.com/medical-issues?issue=teeth'
  linkThreeText = 'See Related issues'
  teethWhyUs = WhyUs.whyUs(whyTitle,whyText,whyUrl,whyLinkText,linkOneUrl,linkOneText,linkTwoUrl,linkTwoText,linkThreeUrl,linkThreeText)
  return teethWhyUs

def eyesWhyUs():
  whyTitle = '<br />About Eyes'
  whyText = 'Happiness comes from fellowship but COVID-19 has made it impossible at the moment. So we need to end spread and return everything to sharing, giving and trusting'
  whyUrl = 'https://hospital19.pythonanywhere.com/contact'
  whyLinkText = 'LEARN MORE'
  linkOneUrl = 'https://hospital19.pythonanywhere.com/doctors-advice?issue=eyes'
  linkOneText = 'Talk to an Expert'
  linkTwoUrl = 'https://hospital19.pythonanywhere.com/visit-clinic?issue=eyes'
  linkTwoText = 'Visit an eye Clinic'
  linkThreeUrl = 'https://hospital19.pythonanywhere.com/medical-issues?issue=eyes'
  linkThreeText = 'See Related issues'
  eyesWhyUs = WhyUs.whyUs(whyTitle,whyText,whyUrl,whyLinkText,linkOneUrl,linkOneText,linkTwoUrl,linkTwoText,linkThreeUrl,linkThreeText)
  return eyesWhyUs

def substanceAbuseWhyUs():
  whyTitle = '<br />About Substance Abuse & Addiction'
  whyText = 'Happiness comes from fellowship but COVID-19 has made it impossible at the moment. So we need to end spread and return everything to sharing, giving and trusting'
  whyUrl = 'https://hospital19.pythonanywhere.com/contact'
  whyLinkText = 'LEARN MORE'
  linkOneUrl = 'https://hospital19.pythonanywhere.com/doctors-advice?issue=substanceAbuse'
  linkOneText = 'Talk to an Expert'
  linkTwoUrl = 'https://hospital19.pythonanywhere.com/visit-clinic?issue=substanceAbuse'
  linkTwoText = 'Visit an eye Clinic'
  linkThreeUrl = 'https://hospital19.pythonanywhere.com/medical-issues?issue=eyes'
  linkThreeText = 'See Related issues'
  eyesWhyUs = WhyUs.whyUs(whyTitle,whyText,whyUrl,whyLinkText,linkOneUrl,linkOneText,linkTwoUrl,linkTwoText,linkThreeUrl,linkThreeText)
  return eyesWhyUs


def testingWhyUs():
  whyTitle = '<br />About Testing'
  whyText = 'Happiness comes from fellowship but COVID-19 has made it impossible at the moment. So we need to end spread and return everything to sharing, giving and trusting'
  whyUrl = 'https://hospital19.pythonanywhere.com/contact'
  whyLinkText = 'LEARN MORE'
  linkOneUrl = 'https://hospital19.pythonanywhere.com/doctors-advice?issue=testing'
  linkOneText = 'Talk to an Expert'
  linkTwoUrl = 'https://hospital19.pythonanywhere.com/visit-clinic?issue=testing'
  linkTwoText = 'Visit a Clinic'
  linkThreeUrl = 'https://hospital19.pythonanywhere.com/medical-issues?issue=testing'
  linkThreeText = 'See Related issues'
  testingWhyUs = WhyUs.whyUs(whyTitle,whyText,whyUrl,whyLinkText,linkOneUrl,linkOneText,linkTwoUrl,linkTwoText,linkThreeUrl,linkThreeText)
  return testingWhyUs

def patientDetailsWhyUs():
  whyTitle = '<br />Enter your details'
  whyText = 'Name, Age, Location, Issue, Message, Hospital'
  whyUrl = 'https://hospital19.pythonanywhere.com/contact'
  whyLinkText = 'LEARN MORE'
  linkOneUrl = 'https://hospital19.pythonanywhere.com/manage-stress'
  linkOneText = 'F'
  linkTwoUrl = 'https://hospital19.pythonanywhere.com/injuries'
  linkTwoText = 'Visit a Clinic'
  linkThreeUrl = 'https://hospital19.pythonanywhere.com/medical-issues'
  linkThreeText = 'See Related issues'
  patientDetailsWhyUs = WhyUs.whyUs(whyTitle,whyText,whyUrl,whyLinkText,linkOneUrl,linkOneText,linkTwoUrl,linkTwoText,linkThreeUrl,linkThreeText)
  return patientDetailsWhyUs

def counsellingWhyUs():
  whyTitle = '<br />About Testing'
  whyText = 'Happiness comes from fellowship but COVID-19 has made it impossible at the moment. So we need to end spread and return everything to sharing, giving and trusting'
  whyUrl = 'https://hospital19.pythonanywhere.com/contact'
  whyLinkText = 'LEARN MORE'
  linkOneUrl = 'https://hospital19.pythonanywhere.com/doctors-advice?issue=counselling'
  linkOneText = 'Talk to an Expert'
  linkTwoUrl = 'https://hospital19.pythonanywhere.com/visit-clinic?issue=teeth'
  linkTwoText = 'Visit a Clinic'
  linkThreeUrl = 'https://hospital19.pythonanywhere.com/medical-issues?issue=counselling'
  linkThreeText = 'See Related issues'
  counsellingWhyUs = WhyUs.whyUs(whyTitle,whyText,whyUrl,whyLinkText,linkOneUrl,linkOneText,linkTwoUrl,linkTwoText,linkThreeUrl,linkThreeText)
  return counsellingWhyUs

def hospitalRecommendationsWhyUs():
  whyTitle = '<br />About Testing'
  whyText = 'Happiness comes from fellowship but COVID-19 has made it impossible at the moment. So we need to end spread and return everything to sharing, giving and trusting'
  whyUrl = 'https://hospital19.pythonanywhere.com/contact'
  whyLinkText = 'LEARN MORE'
  linkOneUrl = 'https://hospital19.pythonanywhere.com/manage-stress'
  linkOneText = 'Talk to an Expert'
  linkTwoUrl = 'https://hospital19.pythonanywhere.com/injuries'
  linkTwoText = 'Visit a Clinic'
  linkThreeUrl = 'https://hospital19.pythonanywhere.com/medical-issues'
  linkThreeText = 'See Related issues'
  hospitalRecommendationsWhyUs = WhyUs.whyUs(whyTitle,whyText,whyUrl,whyLinkText,linkOneUrl,linkOneText,linkTwoUrl,linkTwoText,linkThreeUrl,linkThreeText)
  return hospitalRecommendationsWhyUs

def doctorsAdviceWhyUs():
  whyTitle = '<br />About Testing'
  whyText = 'Happiness comes from fellowship but COVID-19 has made it impossible at the moment. So we need to end spread and return everything to sharing, giving and trusting'
  whyUrl = 'https://hospital19.pythonanywhere.com/contact'
  whyLinkText = 'LEARN MORE'
  linkOneUrl = 'https://hospital19.pythonanywhere.com/manage-stress'
  linkOneText = 'Talk to an Expert'
  linkTwoUrl = 'https://hospital19.pythonanywhere.com/injuries'
  linkTwoText = 'Visit a Clinic'
  linkThreeUrl = 'https://hospital19.pythonanywhere.com/medical-issues'
  linkThreeText = 'See Related issues'
  doctorsAdviceWhyUs = WhyUs.whyUs(whyTitle,whyText,whyUrl,whyLinkText,linkOneUrl,linkOneText,linkTwoUrl,linkTwoText,linkThreeUrl,linkThreeText)
  return doctorsAdviceWhyUs

def manyServicesWhyUs():
  whyTitle = '<br />About Testing'
  whyText = 'Happiness comes from fellowship but COVID-19 has made it impossible at the moment. So we need to end spread and return everything to sharing, giving and trusting'
  whyUrl = 'https://hospital19.pythonanywhere.com/contact'
  whyLinkText = 'LEARN MORE'
  linkOneUrl = 'https://hospital19.pythonanywhere.com/manage-stress'
  linkOneText = 'Talk to an Expert'
  linkTwoUrl = 'https://hospital19.pythonanywhere.com/injuries'
  linkTwoText = 'Visit a Clinic'
  linkThreeUrl = 'https://hospital19.pythonanywhere.com/medical-issues'
  linkThreeText = 'See Related issues'
  manyServicesWhyUs = WhyUs.whyUs(whyTitle,whyText,whyUrl,whyLinkText,linkOneUrl,linkOneText,linkTwoUrl,linkTwoText,linkThreeUrl,linkThreeText)
  return manyServicesWhyUs

def othopedicsWhyUs():
  whyTitle = '<br />About Testing'
  whyText = 'Happiness comes from fellowship but COVID-19 has made it impossible at the moment. So we need to end spread and return everything to sharing, giving and trusting'
  whyUrl = 'https://hospital19.pythonanywhere.com/contact'
  whyLinkText = 'LEARN MORE'
  linkOneUrl = 'https://hospital19.pythonanywhere.com/doctors-advice?issue=othopedics'
  linkOneText = 'Talk to an Expert'
  linkTwoUrl = 'https://hospital19.pythonanywhere.com/visit-clinic?issue=othopedics'
  linkTwoText = 'Visit a Clinic'
  linkThreeUrl = 'https://hospital19.pythonanywhere.com/medical-issues?issue=othopedics'
  linkThreeText = 'See Related issues'
  othopedicsWhyUs = WhyUs.whyUs(whyTitle,whyText,whyUrl,whyLinkText,linkOneUrl,linkOneText,linkTwoUrl,linkTwoText,linkThreeUrl,linkThreeText)
  return othopedicsWhyUs

def appointmentsWhyUs():
  whyTitle = '<br />Talk to Experts'
  whyText = 'Happiness comes from fellowship but COVID-19 has made it impossible at the moment. So we need to end spread and return everything to sharing, giving and trusting'
  whyUrl = 'https://hospital19.pythonanywhere.com/contact'
  whyLinkText = 'LEARN MORE'
  linkOneUrl = 'https://hospital19.pythonanywhere.com/manage-stress'
  linkOneText = 'Talk to an Expert'
  linkTwoUrl = 'https://hospital19.pythonanywhere.com/injuries'
  linkTwoText = 'Visit a Clinic'
  linkThreeUrl = 'https://hospital19.pythonanywhere.com/medical-issues'
  linkThreeText = 'See Related issues'
  appointmentsWhyUs = WhyUs.whyUs(whyTitle,whyText,whyUrl,whyLinkText,linkOneUrl,linkOneText,linkTwoUrl,linkTwoText,linkThreeUrl,linkThreeText)
  return appointmentsWhyUs



def visitClinicWhyUs(issue):

    whyTitle = '<br />Visit a Clinic Near You'
    whyText = 'Happiness comes from fellowship but COVID-19 has made it impossible at the moment. So we need to end spread and return everything to sharing, giving and trusting'
    whyUrl = 'https://hospital19.pythonanywhere.com/contact'
    whyLinkText = 'LEARN MORE'
    linkOneUrl = 'https://hospital19.pythonanywhere.com/visit-clinic?issue={}&location=inASpecificArea'.format(issue)
    linkOneText = 'See Hospitals in a Specific Area'
    linkTwoUrl = 'https://hospital19.pythonanywhere.com/visit-clinic?issue={}&location=anywhereInKenya'.format(issue)
    linkTwoText = 'See hospitals anywhere in Kenya'
    linkThreeUrl = 'https://hospital19.pythonanywhere.com/medical-issues'
    linkThreeText = 'See Related issues'
    appointmentsWhyUs = WhyUs.whyUs(whyTitle,whyText,whyUrl,whyLinkText,linkOneUrl,linkOneText,linkTwoUrl,linkTwoText,linkThreeUrl,linkThreeText)
    return appointmentsWhyUs


def footer():
    footer = '''<!-- ======= Footer ======= -->
    <footer id="footer">


  <div class="container d-md-flex py-4">

    <div class="me-md-auto text-center text-md-start">
      <div class="copyright">
        &copy; Copyright <strong><span>Hospital 19</span></strong>. All Rights Reserved
      </div>
      <div class="credits">
        <!-- All the links in the footer should remain intact. -->
        <!-- You can delete the links only if you purchased the pro version. -->
        <!-- Licensing information: https://bootstrapmade.com/license/ -->
        <!-- Purchase the pro version with working PHP/AJAX contact form: https://bootstrapmade.com/medilab-free-medical-bootstrap-theme/ -->
        Graphic Designed by <a href="https://bootstrapmade.com/">BootstrapMade</a>
      </div><div class = 'credits'>Other partners: <a class='links' href='http://hospital19.pythonanywher.com'>CDC</a></div><div>
    </div>
    <div class="social-links text-center text-md-right pt-3 pt-md-0">
      <a href="#" class="twitter"><i class="bx bxl-twitter"></i></a>
      <a href="#" class="facebook"><i class="bx bxl-facebook"></i></a>
      <a href="#" class="instagram"><i class="bx bxl-instagram"></i></a>
      <a href="#" class="google-plus"><i class="bx bxl-skype"></i></a>
      <a href="#" class="linkedin"><i class="bx bxl-linkedin"></i></a>
    </div>
  </div></div>
</footer><!-- End Footer -->
'''
    return footer

def header():
    header = '''<header id="header" class="fixed-top">
        <div class="container d-flex align-items-center">

          <h1 class="logo me-auto"><a href="/">Hospital 19</a></h1>
          <!-- Uncomment below if you prefer to use an image logo -->
          <!-- <a href="index.html" class="logo me-auto"><img src="assets/img/logo.png" alt="" class="img-fluid"></a>-->

          <nav id="navbar" class="navbar order-last order-lg-0">
            <ul>
              <li><a class="nav-link scrollto active" href="https://hospital19.pythonanywhere.com">Home</a></li>
              <li><a class="nav-link scrollto" href="https://hospital19.pythonanywhere.com/hospital-recommendations">See Hospitals</a></li>
              <li><a class="nav-link scrollto" href="https://hospital19.pythonanywhere.com/many-services">Medical Issues</a></li>
              <li class="dropdown"><a href="#"><span>Get A service</span> <i class="bi bi-chevron-down"></i></a>
                <ul>
                  <li><a href="https://hospital19.pythonanywhere.com/manage-stress">Am Stressed</a></li>
                  <li class="dropdown"><a href="#"><span>Others</span> <i class="bi bi-chevron-right"></i></a>
                    <ul>

                      <li><a href="https://hospital19.pythonanywhere.com/">Talk to a a medical expert</a></li>
                      <li><a href="https://hospital19.pythonanywhere.com/">See all issues</a></li>
                    </ul>
                  </li>
                  <li><a href="https://hospital19.pythonanywhere.com/injuries">Am Injured</a></li>
                      <li><a href="https://hospital19.pythonanywhere.com/sickness">Am Sick</a></li>
                      <li><a href="https://hospital19.pythonanywhere.com/">I was Abused</a></li>
                </ul>
              </li>
              <li><a class="nav-link scrollto" href="#contact">Contact</a></li>
            </ul>
            <i class="bi bi-list mobile-nav-toggle"></i>
          </nav><!-- .navbar -->

          <a href="/get-a-service" class="appointment-btn scrollto"><span class="d-none d-md-inline">Get a</span> Service</a>

        </div>
      </header><!-- End Header -->'''

    return header
def getClinics(issue,latitude,longitude):

  lowerLonLimit = longitude - 0.45
  highLonLimit = longitude + 0.45
  lowerLatLimit = int(latitude) - 0.4
  highLatLimit = int(latitude) + 0.4

  clinics = Database.clinicFor(lowerLonLimit,highLonLimit,lowerLatLimit,highLatLimit,issue)
  return clinics
def setLocationForm(issue):
  locationForm = '''
  <form action="set-location" method="POST">

  <div class="col-md-4 form-group mt-3 mt-md-0">
  <input name="issue" type="text" value="{}" hidden>
  <input type="text" class="form-control" name="location" id="location" placeholder="Enter your Location" data-rule="minlen:" data-msg="Please enter at least 3 chars">
  <div class="validate"></div>
  </div>
  <button>SET THIS AS YOUR LOCATION</button>
  </form>
  '''.format(issue)
  return locationForm

def visitIssueCategories():
  allIssueCategories = Database.getIssueCategories()
  categories = '''<!-- ======= Services Section ======= -->
    <section id="services" class="services">
      <div class="container">

        <div class="section-title">
          <h2>Categories</h2>
          <p>Select the kind of issue you need help with</p>
        </div><div class="row">'''
  for issueCategory in allIssueCategories:
    categoryName = issueCategory[0]
    #categoryLink = issueCategory[1]
    categoryFaIcon = issueCategory[2]
    categories = categories + '''

          <div class="col-lg-4 col-md-6 d-flex align-items-stretch">
            <div class="icon-box">
              <form action="" method="POST"><input name="issue" value="{}" hidden><button type="submit"><div class="icon"><i class="fas {}"></i></div>
              <h4>{}</h4>
              <p></p></button></form>
            </div>
          </div>
    '''.format(categoryName,categoryFaIcon,categoryName)
  categories = categories + '''</div></div></section><!-- End Services Section -->'''
  return visitIssueCategories
def getAllHospitals(issue):
  allHospitals = Database.getAllHospitals(issue)
  return allHospitals
def getHospitalsWithoutLocation(issue):
  hospitals = Database.getHospitalsWithoutLocation(issue)
  return hospitals
def visitClinicIssuesForm():
  allIssueCategories = Database.get
  visitClinicIssuesForm = '''
  <!-- ======= Services Section ======= -->
    <section id="services" class="services">
      <div class="container">

        <div class="section-title">
          <h2>Categories</h2>
          <p>Select the kind of issue you need help with</p>
        </div>

        <div class="row">
          <div class="col-lg-4 col-md-6 d-flex align-items-stretch">
            <div class="icon-box">
              <div class="icon"><i class="fas fa-heartbeat"></i></div>
              <h4><a href="https://hospital19.pythonanywhere.com/manage-stress">Stress</a></h4>
              <p></p>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 d-flex align-items-stretch mt-4 mt-md-0">
            <div class="icon-box">
              <div class="icon"><i class="fas fa-pills"></i></div>
              <h4><a href="https://hospital19.pythonanywhere.com/injuries">Injury</a></h4>
              <p></p>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 d-flex align-items-stretch mt-4">
            <div class="icon-box">
              <div class="icon"><i class="fas fa-dna"></i></div>
              <h4><a href="https://hospital19.pythonanywhere.com/sickness">Sickness</a></h4>
              <p></p>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 d-flex align-items-stretch mt-4 mt-lg-0">
            <div class="icon-box">
              <div class="icon"><i class="fas fa-hospital-user"></i></div>
              <h4><a href="https://hospital19.pythonanywhere.com/abuse">Abuse</a></h4>
              <p></p>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 d-flex align-items-stretch mt-4">
            <div class="icon-box">
              <div class="icon"><i class="fas fa-wheelchair"></i></div>
              <h4><a href="https://hospital19.pythonanywhere.com/teeth">Teeth</a></h4>
              <p></p>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 d-flex align-items-stretch mt-4">
            <div class="icon-box">
              <div class="icon"><i class="fas fa-notes-medical"></i></div>
              <h4><a href="https://hospital19.pythonanywhere.com/eyes">Eyes</a></h4>
              <p></p>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 d-flex align-items-stretch mt-4">
            <div class="icon-box">
              <div class="icon"><i class="fas fa-notes-medical"></i></div>
              <h4><a href="https://hospital19.pythonanywhere.com/substance-abuse">Substance Abuse</a></h4>
              <p></p>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 d-flex align-items-stretch mt-4">
            <div class="icon-box">
              <div class="icon"><i class="fas fa-notes-medical"></i></div>
              <h4><a href="https://hospital19.pythonanywhere.com/testing">Testing</a></h4>
              <p></p>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 d-flex align-items-stretch mt-4">
            <div class="icon-box">
              <div class="icon"><i class="fas fa-notes-medical"></i></div>
              <h4><a href="https://hospital19.pythonanywhere.com/counselling">Counseling</a></h4>
              <p></p>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 d-flex align-items-stretch mt-4">
            <div class="icon-box">
              <div class="icon"><i class="fas fa-notes-medical"></i></div>
              <h4><a href="https://hospital19.pythonanywhere.com/othopedics">Othopedics</a></h4>
              <p></p>
            </div>
          </div>

        </div>

      </div>
    </section><!-- End Services Section -->
  '''
def category_Information():
  category_Information = '''
  <!-- ======= Services Section ======= -->
    <section id="services" class="services">
      <div class="container">

        <div class="section-title">
          <h2>Categories</h2>
          <p>Select the kind of issue you need help with</p>
        </div>

        <div class="row">
          <div class="col-lg-4 col-md-6 d-flex align-items-stretch">
            <div class="icon-box">
              <div class="icon"><i class="fas fa-heartbeat"></i></div>
              <h4><a href="https://hospital19.pythonanywhere.com/manage-stress">Stress</a></h4>
              <p></p>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 d-flex align-items-stretch mt-4 mt-md-0">
            <div class="icon-box">
              <div class="icon"><i class="fas fa-pills"></i></div>
              <h4><a href="https://hospital19.pythonanywhere.com/injuries">Injury</a></h4>
              <p></p>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 d-flex align-items-stretch mt-4">
            <div class="icon-box">
              <div class="icon"><i class="fas fa-dna"></i></div>
              <h4><a href="https://hospital19.pythonanywhere.com/sickness">Sickness</a></h4>
              <p></p>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 d-flex align-items-stretch mt-4 mt-lg-0">
            <div class="icon-box">
              <div class="icon"><i class="fas fa-hospital-user"></i></div>
              <h4><a href="https://hospital19.pythonanywhere.com/abuse">Abuse</a></h4>
              <p></p>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 d-flex align-items-stretch mt-4">
            <div class="icon-box">
              <div class="icon"><i class="fas fa-wheelchair"></i></div>
              <h4><a href="https://hospital19.pythonanywhere.com/teeth">Teeth</a></h4>
              <p></p>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 d-flex align-items-stretch mt-4">
            <div class="icon-box">
              <div class="icon"><i class="fas fa-notes-medical"></i></div>
              <h4><a href="https://hospital19.pythonanywhere.com/eyes">Eyes</a></h4>
              <p></p>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 d-flex align-items-stretch mt-4">
            <div class="icon-box">
              <div class="icon"><i class="fas fa-notes-medical"></i></div>
              <h4><a href="https://hospital19.pythonanywhere.com/substance-abuse">Substance Abuse</a></h4>
              <p></p>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 d-flex align-items-stretch mt-4">
            <div class="icon-box">
              <div class="icon"><i class="fas fa-notes-medical"></i></div>
              <h4><a href="https://hospital19.pythonanywhere.com/testing">Testing</a></h4>
              <p></p>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 d-flex align-items-stretch mt-4">
            <div class="icon-box">
              <div class="icon"><i class="fas fa-notes-medical"></i></div>
              <h4><a href="https://hospital19.pythonanywhere.com/counselling">Counseling</a></h4>
              <p></p>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 d-flex align-items-stretch mt-4">
            <div class="icon-box">
              <div class="icon"><i class="fas fa-notes-medical"></i></div>
              <h4><a href="https://hospital19.pythonanywhere.com/othopedics">Othopedics</a></h4>
              <p></p>
            </div>
          </div>

        </div>

      </div>
    </section><!-- End Services Section -->
  '''
  return category_Information

def medicalIssues():
  medicalIssues = '''

  '''
  medicalIssues = Database.getIssueData(issue)
  return medicalIssues

def appointmentForm(issue):


  allissues = Database.getIssueData(issue)
  issuesInForm = '''<div class="col-md-4 form-group mt-3">
              <select name="issue" id="doctor" class="form-select">
                <option value="">Select Issue</option>'''
  for issues in allissues:

      issueName = issues[0]
      issuesInForm =issuesInForm + '''<option value="{}">{}</option>'''.format(issueName,issueName)
  issuesInForm=issuesInForm + '''</select>
              <div class="validate"></div>
            </div>'''
  appointmentForm = '''
  <!-- ======= Appointment Section ======= -->
    <section id="appointment" class="appointment section-bg">
      <div class="container">

        <div class="section-title">
          <h2>Talk to a Specialist</h2>
          <p>Please fill this form. When you submit, a medical specialist will contact you through the contacts you provide</p>
        </div>

        <form action="https://hospital19.pythonanywhere.com/doctors-advice" method="post" role="form" class="php-email-form">
          <div class="row">
            <div class="col-md-4 form-group">
              <input type="text" name="name" class="form-control" id="name" placeholder="Your Name" data-rule="minlen:4" data-msg="Please enter at least 4 chars">
              <div class="validate"></div>
            </div>
            <div class="col-md-4 form-group mt-3 mt-md-0">
              <input type="email" class="form-control" name="email" id="email" placeholder="Your Email" data-rule="email" data-msg="Please enter a valid email">
              <div class="validate"></div>
            </div>
            <div class="col-md-4 form-group mt-3 mt-md-0">
              <input type="tel" class="form-control" name="phone" id="phone" placeholder="Your Phone" data-rule="minlen:4" data-msg="Please enter at least 4 chars">
              <div class="validate"></div>
            </div>
          </div>
          <div class="row">
            <div class="col-md-4 form-group mt-3">
              <input type="text" name="location" class="form-control" id="date" placeholder="Your Location" data-rule="minlen:3" data-msg="Please enter at least  chars">
              <div class="validate"></div>
            </div>

            {}

          </div>

          <div class="form-group mt-3">
            <textarea class="form-control" name="message" rows="5" placeholder="Message (Optional)"></textarea>
            <div class="validate"></div>
          </div>

          <div class="text-center"><button type="submit">Make an Appointment</button></div>
        </form>

      </div>
    </section><!-- End Appointment Section -->
  '''.format(issuesInForm)
  return appointmentForm



def appointment________Form():

  location = Location.getCoordinates()
  latitude = location[0]
  longitude = location[1]

  hospitals = Hospitals.hospitalsTreatingIn(issue,latitude,longitude)

  appointmentForm = '''
  <!-- ======= Appointment Section ======= -->
    <section id="appointment" class="appointment section-bg">
      <div class="container">



        <form action="/appointments" method="post" role="form" class="php-email-form">
          <div class="row">
            <div class="col-md-4 form-group">
              <input type="text" name="name" class="form-control" id="name" placeholder="Enter your Name" data-rule="minlen:4" data-msg="Please enter at least 4 chars">
              <div class="validate"></div>
            </div>
            <div class="col-md-4 form-group mt-3 mt-md-0">
              <input type="email" class="form-control" name="email" id="email" placeholder="Enter your Email" data-rule="email" data-msg="Please enter a valid email">
              <div class="validate"></div>
            </div>
            <div class="col-md-4 form-group mt-3 mt-md-0">
              <input type="tel" class="form-control" name="phone" id="phone" placeholder="Enter your Phone" data-rule="minlen:4" data-msg="Please enter at least 4 chars">
              <div class="validate"></div>
            </div>
            <div class="col-md-4 form-group mt-3 mt-md-0">
              <input type="text" class="form-control" name="location" id="location" placeholder="Enter your Location" data-rule="minlen:" data-msg="Please enter at least 3 chars">
              <div class="validate"></div>
            </div>
          </div>
          <div class="row">
            <div class="col-md-4 form-group mt-3">
              <input type="datetime" name="date" class="form-control datepicker" id="date" placeholder="Appointment Date" data-rule="minlen:4" data-msg="Please enter at least 4 chars">
              <div class="validate"></div>
            </div>
            <div class="col-md-4 form-group mt-3">
              {}
              <div class="validate"></div>
            </div>

          </div>

          <div class="form-group mt-3">
            <textarea class="form-control" name="message" rows="5" placeholder="Message (Optional)"></textarea>
            <div class="validate"></div>
          </div>
          <div class="mb-3">
            <div class="loading">Loading</div>
            <div class="error-message"></div>
            <div class="sent-message">Your Message request has been sent successfully. Thank you!</div>
          </div>
          <div class="text-center"><button type="submit">{}</button></div>
        </form>

      </div>
    </section><!-- End Appointment Section -->'''


def homepageMainLinksgh():
    linkOneUrl = 'https://hospital19.pythonanywhere.com/get-a-service'
    linkOneText = 'Get A service'
    linkTwoUrl = 'https://hospital19.pythonanywhere.com/see-hospitals'
    linkTwoText = 'See Hospitals'
    linkThreeUrl = 'https://hospital19.pythonanywhere.com/many-services'
    linkThreeText = 'Medical issues'
    whyTitle = 'Why Choose Hospital 19?'
    whyText = 'Happiness comes from fellowship but COVID-19 has made it impossible at the moment. So we need to end spread and return everything to sharing, giving and trusting'
    whyUrl = 'https://hospital19.pythonanywhere.com/contact'
    whyLinkText = 'LEARN MORE'
    homepageMainLinks = [linkOneUrl,linkOneText,linkTwoUrl,linkTwoText,linkThreeUrl,linkThreeText,whyTitle,whyText,whyUrl,whyLinkText]

    homepageMainLinks = ''''''

def getAService():
    linkOneUrl = 'https://hospital19.pythonanywhere.com/manage-stress'
    linkOneText = 'Am stressed'
    linkTwoUrl = 'https://hospital19.pythonanywhere.com/injuries'
    linkTwoText = 'Am injured'
    linkThreeUrl = 'https://hospital19.pythonanywhere.com/medical-issues'
    linkThreeText = 'Medical issues'
    whyTitle = 'Why Choose Hospital 19?'
    whyText = '''Whatever you're going through, there is help for you. Please reach out to a facility or expert near you.
    We highly recommend that reach out to a professional, but if you're not ready,

    we have included tones of information to help you start understanding the problem.

    If you're ready to get help, click on the issue that's troubling you.
    '''
    whyUrl = 'https://hospital19.pythonanywhere.com/contact'
    whyLinkText = 'LEARN MORE'
    homepageMainLinks = [linkOneUrl,linkOneText,linkTwoUrl,linkTwoText,linkThreeUrl,linkThreeText,whyTitle,whyText,whyUrl,whyLinkText]
    return getAService