from flask import render_template

def aboutStress():
    title = 'Talk To A Feel Good Expert'
    issue = 'Stress'
    text = '''-------CODE GOES HERE------Your name, Phone, Email, Age, location, subject, Message, capture, submit, reset-----END OF CODE'''
    return text
def aboutInjury():
    title = 'Talk To An Injuries Expert'
    issue = 'Injury'
    text = '''-------CODE GOES HERE------Your name, Phone, Email, Age, location, subject, Message, capture, submit, reset-----END OF CODE'''
    return render_template('TalkToExpert.html',title=title,issue=issue,text=text)
def aboutSickness():
    title = 'Talk To A Doctor'
    issue = 'Sickness'
    text = '''-------CODE GOES HERE------Your name, Phone, Email, Age, location, subject, Message, capture, submit, reset-----END OF CODE'''
    return render_template('TalkToExpert.html',title=title,issue=issue,text=text)
def aboutAbuse():
    title = 'Talk To A Sexual and Gender Based Violence Expert'
    issue = 'Abuse'
    text = '''-------CODE GOES HERE------Your name, Phone, Email, Age, location, subject, Message, capture, submit, reset-----END OF CODE'''
    return render_template('TalkToExpert.html',title=title,issue=issue,text=text)
def aboutTeeth():
    title = 'Talk To A Dentist about Teeth'
    issue = 'Teeth'
    text = '''-------CODE GOES HERE------Your name, Phone, Email, Age, location, subject, Message, capture, submit, reset-----END OF CODE'''
    return render_template('TalkToExpert.html',title=title,issue=issue,text=text)
def aboutEyes():
    title = 'Talk To An Optician About Eyes'
    issue = 'Eyes'
    text = '''-------CODE GOES HERE------Your name, Phone, Email, Age, location, subject, Message, capture, submit, reset-----END OF CODE'''
    return render_template('TalkToExpert.html',title=title,issue=issue,text=text)
def aboutSubstanceAbuse():
    title = 'Talk To A Substance Or Drug Abuse/ Addiction Specialist'
    issue = 'Substance Abuse'
    text = '''-------CODE GOES HERE------Your name, Phone, Email, Age, location, subject, Message, capture, submit, reset-----END OF CODE'''
    return render_template('TalkToExpert.html',title=title,issue=issue,text=text)
def aboutTesting():
    title = 'Talk To A Testing Specialist'
    issue = 'Testing'
    text = '''-------CODE GOES HERE------Your name, Phone, Email, Age, location, subject, Message, capture, submit, reset-----END OF CODE'''
    return render_template('TalkToExpert.html',title=title,issue=issue,text=text)
def aboutCounselling():
    title = 'Talk to a Counsellor'
    issue = 'Counselling'
    text = '''-------CODE GOES HERE------Your name, Phone, Email, Age, location, subject, Message, capture, submit, reset-----END OF CODE'''
    return render_template('TalkToExpert.html',title=title,issue=issue,text=text)
def aboutOthopedics():
    title = 'Talk To A Bones Doctor'
    issue = 'Othopedics'
    text = '''-------CODE GOES HERE------Your name, Phone, Email, Age, location, subject, Message, capture, submit, reset-----END OF CODE'''
    return render_template('TalkToExpert.html',title=title,issue=issue,text=text)
