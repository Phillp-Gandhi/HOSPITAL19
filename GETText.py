from flask import render_template
import Elements

def homepage():

    title = 'Hospital 19'
    issue = ''



    text = '''Welcome to Hospital 19
    This is a service to give you quick access to health information and services

    The service prioritizes on:
    1. Easy to use for differently enabled people
    2. Relevant local referals and information
    3. Availability of up-to-date information about hospital admitions

    The main aim of the service is to:
    1. Increase mental health awareness
    2. Ease unnesesary congestion in hospitals
    3. Help clients get accurate information on where to go for treatment

    <a class="" href="https://hospital19.pythonanywhere.com/get-a-service">GET A SERVICE</a>-------<a class="" href="https://hospital19.pythonanywhere.com/hospital-recommendations">SEE HOSPITALS</a>--------<a class="" href="https://hospital19.pythonanywhere.com/many-services">MEDICAL ISSUES</a>'''
    return text
def getService():
    
    mainLinks = '''<!-- ======= Why Us Section ======= -->
  <section id="why-us" class="why-us">
    <div class="container">

      <div class="row">
        <div class="col-lg-4 d-flex align-items-stretch">
          <div class="content">
            <h3>Why Choose Hospital 19?</h3>
            <p>
              Happiness comes from fellowship but COVID-19 has made it impossible at the moment. So we need to end spread and return everything to sharing, giving and trusting.
            </p>
            <div class="text-center">
              <a href="#" class="more-btn">Learn More <i class="bx bx-chevron-right"></i></a>
            </div>
          </div>
        </div>

        <!-- START OF MAIN-LINKS -->
        <div class="col-lg-8 d-flex align-items-stretch" id='main-links'>
          <div class="icon-boxes d-flex flex-column justify-content-center">
            <div class="row">
              <div class="col-xl-4 d-flex align-items-stretch">
                <div class="icon-box mt-4 mt-xl-0">
                  <a class='links' href='http://hospital19.pythonanywher.com/get-a-service'><i class="bx bx-receipt"></i>
                  <h4>Get a service</h4></a>
                </div>
              </div>
              <div class="col-xl-4 d-flex align-items-stretch">
                <div class="icon-box mt-4 mt-xl-0">
                  <a class='links' href='http://hospital19.pythonanywher.com'><i class="bx bx-cube-alt"></i>
                  <h4>See Hospitals</h4></a>
                  
                </div>
              </div>
              <div class="col-xl-4 d-flex align-items-stretch">
                <div class="icon-box mt-4 mt-xl-0">
                  <a class='links' href='http://hospital19.pythonanywher.com'><i class="bx bx-images"></i>
                  <h4>Medical issues</h4></a>
                </div>
              </div>
              
            </div>
          </div><!-- End .content-->
        </div>
        <!-- END OF MAIN-LINKS -->
      </div>

    </div>
  </section><!-- End Why Us Section -->
    '''
    
    text = '''
        Whatever you're going through, there is help for you. Please reach out to a facility or expert near you.
    We highly recommend that reach out to a professional, but if you're not ready,

    we have included tones of information to help you start understanding the problem.

    If you're ready to get help, click on the issue that's troubling you.

    <a class="" href="https://hospital19.pythonanywhere.com/manage-stress">AM STRESSED</a>----------AM INJURED----------AM SICK----------I WAS ABUSED
    '''
    return text
def manageStress(title):


    text = '''Am sorry to hear that you're feeling stressed.

What is stress?:
            <a class="" href="https://hospital19.pythonanywhere.com/manage-stress#getService">GET SERVICE NOW</a>
        What causes stress?:

        Is stress good?: No

        What to do when feeling stress?: Something. {}

        '''.format(Elements.getServiceForm1(title))
    return text

def injuries():
    text = ''
    return text

def sickness():
    text = ''
    return text
def abuse():
    text = ''
    return text
def teeth():
    text = ''
    return text
def eyes():
    text = ''
    return text
def substanceAbuse():
    text = ''
    return text
def counselling():
    text = ''
    return text
def othopedics():
    text = ''
    return text
def manyServices():
    text = ''
    return text
def appointments():
    text = ''
    return text
def ambulance():
    text = ''
    return text
def addHospital():
    text = ''
    return text
def patientDetails():
    text = ''
    return text
def hospitals():
    text = 'All <strong>Hospitals</strong> Here'
    return text
