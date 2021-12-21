import TalkToExpert
import VisitInstitution
import SeeMoreInformation
import SeeRelatedIssues


def getAService(want):

    if want == 'TalkToExpert':
        return TalkToExpert.aboutAbuse('Abuse')
    elif want == 'VisitInstitution':
        return VisitInstitution.aboutAbuse('Abuse')
    elif want == 'SeeMoreInformation':
        return SeeMoreInformation.about('Abuse')
    elif want == 'SeeRelatedIssues':
        return SeeRelatedIssues.aboutAbuse('Abuse')
