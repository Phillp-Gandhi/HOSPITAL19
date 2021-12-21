
import GETText, Hospitals, Elements, Metadata, secure
import StressModule, InjuryModule, SicknessModule, AbuseModule, TeethModule, EyesModule, SubstanceAbuseModule, TestingModule, CounsellingModule, OthopedicsModule, Location, Database

from flask import Flask, Markup, render_template, request, redirect, url_for, session
from http import cookies
import os



app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET'])
def homepage():
    title = 'Hospital 19'
    metaData = Markup(Metadata.homepage())
    header = Markup(Elements.header())
    homeHero = Markup(Elements.homeHero())
    whyUs = Markup(Elements.homeWhyUs())
    footer = Markup(Elements.footer())
    pageContent = Markup(Elements.category_Information())
    return render_template('index.html', title=title, pageContent=pageContent, metaData=metaData,header=header,homeHero=homeHero,whyUs=whyUs,footer=footer)

@app.route('/get-a-service', methods=['GET'])
def getService():

    title = 'Get a Service'
    metaData = Markup(Metadata.getAService())
    header = Markup(Elements.header())
    whyUs = Markup(Elements.getAServiceWhyUs())
    footer = Markup(Elements.footer())
    pageContent = Markup(Elements.category_Information())
    return render_template('index.html', title=title, metaData=metaData,header=header,whyUs=whyUs,footer=footer,pageContent=pageContent)

@app.route('/manage-stress', methods=['GET', 'POST'])
def stressIssue():

    if request.method == "GET":
        title = 'Managing stress'
        header = Markup(Elements.header())
        metaData = Markup(Metadata.stress())
        whyUs = Markup(Elements.manageStressWhyUs())
        footer = Markup(Elements.footer())
        pageContent = StressModule.getAService('SeeMoreInformation')
        pageContent = pageContent.replace('&quot;', '''"''')
        pageContent = Markup(pageContent)


        return render_template('index.html', title=title, metaData=metaData,header=header,whyUs=whyUs,footer=footer,pageContent=pageContent)

    elif request.method == "POST":

        try:
            request.form['action']
        except:
            return 'Please go back and click on Get A Service'
        else:
            want = secure.sanitizeIncomingData(request.form['action'])



        if secure.InternalDataVerification_getAService(want) == 'notOkay':
            return 'There was a problem. Please try again'
        else:

            html = Markup(StressModule.getAService(want))
            return html



@app.route('/injuries', methods=['GET', 'POST'])
def injuryIssue():
    if request.method == "GET":

        title = 'Injury'
        metaData = Markup(Metadata.getAService())
        header = Markup(Elements.header())
        whyUs = Markup(Elements.injuryWhyUs())
        footer = Markup(Elements.footer())
        pageContent = Markup(InjuryModule.getAService('SeeMoreInformation'))
        return render_template('index.html', title=title, metaData=metaData,header=header,whyUs=whyUs,footer=footer,pageContent=pageContent)


    elif request.method == "POST":

        try:
            request.form['action']
        except:
            return 'Please go back and click on Get A Service'
        else:
            want = secure.sanitizeIncomingData(request.form['action'])



        if secure.InternalDataVerification_getAService(want) == 'notOkay':
            return 'There was a problem. Please try again'
        else:

            html = Markup(InjuryModule.getAService(want))
            return html

    else:
        secure.stopOtherVerbs()


@app.route('/sickness', methods=['GET', 'POST'])
def sicknessIssue():
    if request.method == "GET":
        title = 'Injury'
        metaData = Markup(Metadata.sickness())
        header = Markup(Elements.header())
        whyUs = Markup(Elements.sicknessWhyUs())
        footer = Markup(Elements.footer())
        pageContent = Markup(SicknessModule.getAService('SeeMoreInformation'))
        return render_template('index.html', title=title, metaData=metaData,header=header,whyUs=whyUs,footer=footer,pageContent=pageContent)

    elif request.method == "POST":

        try:
            request.form['action']
        except:
            return 'Please go back and click on Get A Service'
        else:
            want = secure.sanitizeIncomingData(request.form['action'])

        if secure.InternalDataVerification_getAService(want) == 'notOkay':
            return 'There was a problem. Please try again'
        else:

            html = Markup(SicknessModule.getAService(want))
            return html
    else:
        secure.stopOtherVerbs()

@app.route('/abuse', methods=['GET', 'POST'])
def abuseIssue():
    if request.method == "GET":
        title = 'Injury'
        metaData = Markup(Metadata.homepage())
        header = Markup(Elements.header)
        whyUs = Markup(Elements.abuseWhyUs())
        footer = Markup(Elements.footer)
        pageContent = Markup(AbuseModule.getAService('SeeMoreInformation'))
        return render_template('index.html', title=title, metaData=metaData,header=header,whyUs=whyUs,footer=footer,pageContent=pageContent)


    elif request.method == "POST":

        try:
            request.form['action']
        except:
            return 'Please go back and click on Get A Service'
        else:
            want = secure.sanitizeIncomingData(request.form['action'])



        if secure.InternalDataVerification_getAService(want) == 'notOkay':
            return 'There was a problem. Please try again'
        else:

            html = Markup(AbuseModule.getAService(want))
            return html
    else:
        secure.stopOtherVerbs()

@app.route('/teeth', methods=['GET', 'POST'])
def toothIssue():
    if request.method == "GET":
        title = 'Injury'
        metaData = Markup(Metadata.tooth())
        header = Markup(Elements.header())
        whyUs = Markup(Elements.teethWhyUs())
        footer = Markup(Elements.footer())
        pageContent = Markup(TeethModule.getAService('SeeMoreInformation'))
        return render_template('index.html', title=title, metaData=metaData,header=header,whyUs=whyUs,footer=footer,pageContent=pageContent)


    elif request.method == "POST":

        try:
            request.form['action']
        except:
            return 'Please go back and click on Get A Service'
        else:
            want = secure.sanitizeIncomingData(request.form['action'])



        if secure.InternalDataVerification_getAService(want) == 'notOkay':
            return 'There was a problem. Please try again'
        else:

            html = Markup(TeethModule.getAService(want))
            return html

@app.route('/eyes', methods=['GET', 'POST'])
def eyeIssue():
    if request.method == "GET":
        title = 'Injury'
        metaData = Markup(Metadata.eyes())
        header = Markup(Elements.header())
        whyUs = Markup(Elements.eyesWhyUs())
        footer = Markup(Elements.footer())
        pageContent = Markup(EyesModule.getAService('SeeMoreInformation'))
        return render_template('index.html', title=title, metaData=metaData,header=header,whyUs=whyUs,footer=footer,pageContent=pageContent)


    elif request.method == "POST":

        try:
            request.form['action']
        except:
            return 'Please go back and click on Get A Service'
        else:
            want = secure.sanitizeIncomingData(request.form['action'])



        if secure.InternalDataVerification_getAService(want) == 'notOkay':
            return 'There was a problem. Please try again'
        else:

            html = Markup(EyesModule.getAService(want))
            return html
    else:
        secure.stopOtherVerbs()

@app.route('/substance-abuse', methods=['GET', 'POST'])
def substaceAbuseIssue():
    if request.method == "GET":
        title = 'Injury'
        metaData = Markup(Metadata.substanceAbuse())
        header = Markup(Elements.header())
        whyUs = Markup(Elements.substanceAbuseWhyUs())
        footer = Markup(Elements.footer())
        pageContent = Markup(SubstanceAbuseModule.getAService('SeeMoreInformation'))
        return render_template('index.html', title=title, metaData=metaData,header=header,whyUs=whyUs,footer=footer,pageContent=pageContent)


    elif request.method == "POST":

        try:
            request.form['action']
        except:
            return 'Please go back and click on Get A Service'
        else:
            want = secure.sanitizeIncomingData(request.form['action'])



        if secure.InternalDataVerification_getAService(want) == 'notOkay':
            return 'There was a problem. Please try again'
        else:

            html = Markup(SubstanceAbuseModule.getAService(want))
            return html
    else:
        secure.stopOtherVerbs()

@app.route('/testing', methods=['GET', 'POST'])
def testingIssue():
    if request.method == "GET":

        title = 'Testing'
        metaData = Markup(Metadata.testing())
        header = Markup(Elements.header())
        whyUs = Markup(Elements.testingWhyUs())
        footer = Markup(Elements.footer())
        pageContent = Markup(TestingModule.getAService('SeeMoreInformation'))
        return render_template('index.html', title=title, metaData=metaData,header=header,whyUs=whyUs,footer=footer,pageContent=pageContent)


    elif request.method == "POST":

        try:
            request.form['action']
        except:
            return 'Please go back and click on Get A Service'
        else:
            want = secure.sanitizeIncomingData(request.form['action'])



        if secure.InternalDataVerification_getAService(want) == 'notOkay':
            return 'There was a problem. Please try again'
        else:

            html = Markup(TestingModule.getAService(want))
            return html
    else:
        secure.stopOtherVerbs

@app.route('/patient-details', methods=['GET'])
def patientDetails():
    if request.method == "GET":

        title = 'Testing'
        metaData = Markup('NO CACHING NO CRAWLING')
        header = Markup(Elements.header())
        whyUs = Markup(Elements.patientDetailsWhyUs())
        footer = Markup(Elements.footer())
        pageContent = Markup('')

        return render_template('index.html', title=title, metaData=metaData,header=header,whyUs=whyUs,footer=footer,pageContent=pageContent)

@app.route('/add-hospitals', methods=['GET'])
def addHospital():
    if request.method == "GET":

        title = 'Testing'
        metaData = Markup('NO CACHING NO CRAWLING')
        header = Markup(Elements.header())
        whyUs = Markup(Elements.patientDetailsWhyUs())
        footer = Markup(Elements.footer())
        pageContent = Markup('')

        return render_template('index.html', title=title, metaData=metaData,header=header,whyUs=whyUs,footer=footer,pageContent=pageContent)

    elif request.method == "POST":

        title = ''
        text = ''




        return render_template('index.html', title=title, text=text)
    else:
        secure.stopOtherVerbs()


@app.route('/counselling', methods=['GET', 'POST'])
def counsellingIssue():
    if request.method == "GET":


        title = 'Counseling'
        metaData = Markup(Metadata.counselling())
        header = Markup(Elements.header())
        whyUs = Markup(Elements.counsellingWhyUs())
        footer = Markup(Elements.footer())
        pageContent = Markup(CounsellingModule.getAService('SeeMoreInformation'))

        return render_template('index.html', title=title, metaData=metaData,header=header,whyUs=whyUs,footer=footer,pageContent=pageContent)

    elif request.method == "POST":

        try:
            request.form['action']
        except:
            return 'Please go back and click on Get A Service'
        else:
            want = secure.sanitizeIncomingData(request.form['action'])



        if secure.InternalDataVerification_getAService(want) == 'notOkay':
            return 'There was a problem. Please try again'
        else:

            html = Markup(CounsellingModule.getAService(want))
            return html
    else:
        secure.stopOtherVerbs()

@app.route('/hospital-recommendations', methods=['GET', 'POST'])
def hospitalRecomendations():
    if request.method == "GET":
        title = 'Hospitals'
        metaData = Markup(Metadata.hospitalRecommendations())
        header = Markup(Elements.header())
        whyUs = Markup(Elements.hospitalRecommendationsWhyUs())
        footer = Markup(Elements.footer())
        pageContent = ''




        return render_template('index.html', title=title, metaData=metaData,header=header,whyUs=whyUs,footer=footer,pageContent=pageContent)

    elif request.method == "POST":
        try:

            issue = secure.InternalDataVerification_getAService(request.form['issue'])
        except:
            redirect(url_for('hospitalRecomendations'))
        else:
            title = 'Hospital recommendations'
            issue = secure.InternalDataVerification_getAService(request.form['issue'])
            text = Markup(Hospitals.ClinicFor(issue))
        return render_template('index.html', title=title,text=text)
    else:
        secure.stopOtherVerbs()
@app.route('/visit-clinic')
def visitClinic():
    if request.method == "GET":
        try:

            issue = secure.sanitizeIncomingData(request.args['issue'])
        except:
            return redirect(url_for('getService'))
        else:
            issue = secure.sanitizeIncomingData(request.args['issue'])
            try:
                where = secure.sanitizeIncomingData(request.args['location'])

                isWhereOkay = secure.internalDataVerification_visitClinic(where)
            except:


                title = 'Visit a Hospital to get a service'
                metaData = Markup(Metadata.visitClinic())
                header = Markup(Elements.header())
                whyUs = Markup(Elements.visitClinicWhyUs(issue))
                footer = Markup(Elements.footer())
                pageContent = ''
                return render_template('index.html', title=title, metaData=metaData,header=header,whyUs=whyUs,footer=footer,pageContent=pageContent)
            else:
                where = secure.sanitizeIncomingData(request.args['location'])
                isWhereOkay = secure.internalDataVerification_visitClinic(where)
                if isWhereOkay  != 'notOkay' and where == 'inASpecificArea':
                    title = 'Visit a Hospital to get a service'
                    metaData = Markup(Metadata.visitClinic())
                    header = Markup(Elements.header())
                    whyUs = Markup(Elements.visitClinicWhyUs(issue))
                    footer = Markup(Elements.footer())
                    try:
                        location = secure.sanitizeIncomingData(session['location'][0])
                    except:
                        pageContent = Markup(Elements.setLocationForm(issue))
                        return render_template('index.html', title=title, metaData=metaData,header=header,whyUs=whyUs,footer=footer,pageContent=pageContent)
                    else:
                        location = secure.sanitizeIncomingData(session['location'][0])
                        latLong = Location.getCoordinates(location)
                        latitude = latLong[0]
                        longitude = latLong[1]
                        pageContent = Markup(Elements.getClinics(issue,latitude,longitude))
                        return render_template('index.html', title=title, metaData=metaData,header=header,whyUs=whyUs,footer=footer,pageContent=pageContent)
                elif isWhereOkay  != 'notOkay' and where == 'anywhereInKenya':
                    title = 'Visit a Hospital to get a service'
                    metaData = Markup(Metadata.visitClinic())
                    header = Markup(Elements.header())
                    whyUs = Markup(Elements.visitClinicWhyUs(issue))
                    footer = Markup(Elements.footer())
                    pageContent = Markup(Elements.getAllHospitals(issue))
                    return render_template('index.html', title=title, metaData=metaData,header=header,whyUs=whyUs,footer=footer,pageContent=pageContent)
                elif isWhereOkay == 'notOkay':
                    return redirect(url_for('getService'))

        try:
            issue = secure.sanitizeIncomingData(request.args['issue'])
        except:
            if request.args['allHospitals'] == 'yes':
                pageContent = Markup(Elements.getAllHospitals())
        else:
            issue = secure.sanitizeIncomingData(request.args['issue'])

        try:
            location = secure.sanitizeIncomingData(session['location'])
        except:
            redirect(url_for('setLocationPage'))
        else:

            title = 'Doctor Advice'
            metaData = Markup(Metadata.doctoAdvice())
            header = Markup(Elements.header())
            whyUs = Markup(Elements.doctorsAdviceWhyUs())
            footer = Markup(Elements.footer())
            pageContent = Markup(Elements.visitIssueCategories())

            return render_template('index.html', title=title, metaData=metaData,header=header,whyUs=whyUs,footer=footer,pageContent=pageContent)

    elif request.method == "POST":
        try:
            issue = secure.sanitizeIncomingData(request.form['issue'])
        except:
            redirect(url_for('visitClinic'))
        else:
            issue = secure.sanitizeIncomingData(request.form['issue'])
            location = session['location']
            title = 'Doctor Advice'
            metaData = Markup(Metadata.doctoAdvice())
            header = Markup(Elements.header())
            whyUs = Markup(Elements.doctorsAdviceWhyUs())
            footer = Markup(Elements.footer())
            pageContent = Markup(Elements.getClinics(issue,location))

@app.route('/doctors-advice', methods=['GET', 'POST'])
def doctorAdvice():
    if request.method == "GET":
        title = 'Othopedics'
        metaData = Markup(Metadata.appointments())
        header = Markup(Elements.header())
        whyUs = Markup(Elements.appointmentsWhyUs())
        footer = Markup(Elements.footer())
        pageContent = Markup('')

        try:
            issue = request.args['issue']
        except:
            return redirect(url_for('getService'))
        else:
            issue = request.args['issue']
            appointmentForm = Markup(Elements.appointmentForm(issue))

        return render_template('index.html', title=title, metaData=metaData,header=header,whyUs=whyUs,footer=footer,pageContent=pageContent,others=appointmentForm)

    elif request.method == "POST":
        patientName = secure.sanitizeIncomingData(request.form['name'])
        patientEmail = secure.sanitizeIncomingData(request.form['email'])
        patientPhone = secure.sanitizeIncomingData(request.form['phone'])
        patientLocation = secure.sanitizeIncomingData(request.form['location'])

        latLong = Location.getCoordinates(patientLocation)
        patientLatitude = latLong[0]
        patientLongitude= latLong[1]
        session['location'] = [patientLocation,patientLatitude,patientLongitude]
        patientSubIssue = secure.sanitizeIncomingData(request.form['issue'])
        message = request.form['message']
        patientMessage = secure.sanitizeIncomingData(message)
        pageContent = Database.savePatientQuestion(patientName,patientEmail,patientPhone,patientLocation,patientLatitude,patientLongitude,patientSubIssue,patientMessage)
        '''BREAK DOWN LOCATION TO COORDINATES AND SEND DATA TO DBMS'''

        title = 'Message Sent'

        metaData = Markup(Metadata.doctoAdvice())
        header = Markup(Elements.header())
        whyUs = Markup(Elements.doctorsAdviceWhyUs())
        footer = Markup(Elements.footer())
        #pageContent = Markup(Elements.appointmentForm())




        return render_template('index.html', title=title, metaData=metaData,header=header,whyUs=whyUs,footer=footer,pageContent=pageContent)


@app.route('/more-information', methods=['POST'])
def moreInformation():
    title = 'More Information'
    metaData = Markup(Metadata.doctoAdvice())
    header = Markup(Elements.header())
    whyUs = Markup(Elements.doctorsAdviceWhyUs())
    footer = Markup(Elements.footer())
    cDcImport = Markup(Elements.cDcImport())
    pageContent = Markup('')

    return render_template('index.html', title=title, metaData=metaData,header=header,whyUs=whyUs,footer=footer,pageContent=pageContent)


@app.route('/many-services', methods=['GET'])
def manyServices():
    if request.method == "GET":

        title = 'Hospitals'
        metaData = Markup(Metadata.manyServices())
        header = Markup(Elements.header())
        whyUs = Markup(Elements.manyServicesWhyUs())
        footer = Markup(Elements.footer())

        pageContent = Markup('')

        return render_template('index.html', title=title, metaData=metaData,header=header,whyUs=whyUs,footer=footer,pageContent=pageContent)

    elif request.method == "POST":

        title = ''
        text = ''




        return render_template('index.html', title=title, text=text)

@app.route('/othopedics', methods=['GET', 'POST'])
def othopedicIssue():
    if request.method == "GET":

        title = 'Othopedics'
        metaData = Markup(Metadata.othopedics())
        header = Markup(Elements.header())
        whyUs = Markup(Elements.othopedicsWhyUs())
        footer = Markup(Elements.footer())
        pageContent = Markup(OthopedicsModule.getAService('SeeMoreInformation'))

        return render_template('index.html', title=title, metaData=metaData,header=header,whyUs=whyUs,footer=footer,pageContent=pageContent)


    elif request.method == "POST":

        try:
            request.form['action']
        except:
            return 'Please go back and click on Get A Service'
        else:
            want = secure.sanitizeIncomingData(request.form['action'])



        if secure.InternalDataVerification_getAService(want) == 'notOkay':
            return 'There was a problem. Please try again'
        else:

            html = Markup(OthopedicsModule.getAService(want))
            return html
    else:
        secure.stopOtherVerbs()

@app.route('/set-location', methods=['POST'])
def setLocationPage():
    where = secure.sanitizeIncomingData(request.form['location'])
    issue = secure.sanitizeIncomingData(request.form['issue'])
    latLong = Location.getCoordinates(where)
    latitude = latLong[0]
    longitude = latLong[1]
    session.pop('location', None)
    session['location'] = [where,latitude,longitude]
    return redirect(url_for('visitClinic'))

@app.route('/appointments', methods = ['GET', 'POST'])
def appointMents():
    if request.method == "GET":
        title = 'Othopedics'
        metaData = Markup(Metadata.appointments())
        header = Markup(Elements.header())
        whyUs = Markup(Elements.appointmentsWhyUs())
        footer = Markup(Elements.footer())
        pageContent = Markup('')

        try:
            issue = request.args['issue']
        except:
            return redirect(url_for('getService'))
        else:
            issue = request.args['issue']
            appointmentForm = Markup(Elements.appointmentForm(issue))

        return render_template('index.html', title=title, metaData=metaData,header=header,whyUs=whyUs,footer=footer,pageContent=pageContent,others=appointmentForm)
    elif request.method == "POST":

        title = ''
        text = ''




        return render_template('index.html', title=title, text=text)
    else:
        secure.stopOtherVerbs()

@app.route('/ambulance', methods=['GET'])
def ambuLance():
    if request.method == "GET":
        title = 'Othopedics'
        metaData = Markup(Metadata.ambulance())
        header = Markup(Elements.header())
        whyUs = Markup(Elements.ambulanceWhyUs())
        footer = Markup(Elements.footer())
        cDcImport = Markup(Elements.cDcImport())
        pageContent = Markup('')

        return render_template('index.html', title=title, metaData=metaData,header=header,whyUs=whyUs,footer=footer,pageContent=pageContent)
    elif request.method == "POST":

        title = ''
        text = ''




        return render_template('index.html', title=title, text=text)

@app.errorhandler(404)
def errfourhu(err):
    return 'Not found'

@app.errorhandler(500)
def errfourhu(err):
    return 'An error occured'

if __name__ == "__main__":
    app.run(debug = False)
