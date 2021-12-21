import TalkToExpert
import VisitInstitution
import SeeMoreInformation
import SeeRelatedIssues


def getAService(want):

    if want == 'TalkToExpert':
        return TalkToExpert.about('Othopedics')
    elif want == 'VisitInstitution':
        return VisitInstitution.about('Othopedics')
    elif want == 'SeeMoreInformation':
        return SeeMoreInformation.about('Othopedics')
    elif want == 'SeeRelatedIssues':
        return SeeRelatedIssues.about('Othopedics')
