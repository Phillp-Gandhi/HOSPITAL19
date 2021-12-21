from flask import request, redirect, url_for

def stopOtherVerbs():
    if request.method != "POST" and request.method != "GET":
        redirect(url_for('homepage'))

def sanitizeIncomingData(data):

    want = data.replace('!', '&#33;')
    want = want.replace('<', '&lt;')
    want = want.replace('>', '&gt;')
    want = want.replace('$', '&#36;')
    want = want.replace('(', '&#40;')
    want = want.replace(')', '&#41;')
    want = want.replace('*', '&#42;')
    want = want.replace("""'""", '&apos;')
    want = want.replace('''"''', '&quot;')
    want = want.replace('.', '')
    want = want.replace('=', '')
    return want

def SanitizeOutgoingData(data):
    return data

def InternalDataVerification_getAService(want):
    if want == 'TalkToExpert' or want == 'VisitInstitution' or want == 'SeeMoreInformation' or want == 'SeeRelatedIssues':
        IsDataOkay = 'Okay'
        return want
    else:
        # IsDataOkay = 'Data Validation Failed'
        return 'notOkay'
def internalDataVerification_visitClinic(where):
    if where == 'inASpecificArea' or where == 'anywhereInKenya':
        return where
    else:
        return 'notOkay'
