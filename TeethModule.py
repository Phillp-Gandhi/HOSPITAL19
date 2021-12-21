import TalkToExpert
import VisitInstitution
import SeeMoreInformation
import SeeRelatedIssues


def getAService(want):

    if want == 'TalkToExpert':
        return TalkToExpert.aboutTeeth('Teeth')
    elif want == 'VisitInstitution':
        return VisitInstitution.aboutTeeth('Teeth')
    elif want == 'SeeMoreInformation':
        return SeeMoreInformation.about('Teeth')
    elif want == 'SeeRelatedIssues':
        return SeeRelatedIssues.aboutTeeth('Teeth')
