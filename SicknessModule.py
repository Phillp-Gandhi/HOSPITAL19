import TalkToExpert
import VisitInstitution
import SeeMoreInformation
import SeeRelatedIssues


def getAService(want):

    if want == 'TalkToExpert':
        return TalkToExpert.aboutSickness('Sickness')
    elif want == 'VisitInstitution':
        return VisitInstitution.aboutSickness('Sickness')
    elif want == 'SeeMoreInformation':
        return SeeMoreInformation.about('Sickness')
    elif want == 'SeeRelatedIssues':
        return SeeRelatedIssues.aboutSickness('Sickness')
