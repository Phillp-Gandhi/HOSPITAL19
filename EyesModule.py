import TalkToExpert
import VisitInstitution
import SeeMoreInformation
import SeeRelatedIssues


def getAService(want):

    if want == 'TalkToExpert':
        return TalkToExpert.aboutEyes('Eyes')
    elif want == 'VisitInstitution':
        return VisitInstitution.aboutEyes('Eyes')
    elif want == 'SeeMoreInformation':
        return SeeMoreInformation.about('Eyes')
    elif want == 'SeeRelatedIssues':
        return SeeRelatedIssues.aboutEyes('Eyes')
