import TalkToExpert
import VisitInstitution
import SeeMoreInformation
import SeeRelatedIssues


def getAService(want):

    if want == 'TalkToExpert':
        return TalkToExpert.aboutTesting('Testing')
    elif want == 'VisitInstitution':
        return VisitInstitution.aboutTesting('Testing')
    elif want == 'SeeMoreInformation':
        return SeeMoreInformation.about('Testing')
    elif want == 'SeeRelatedIssues':
        return SeeRelatedIssues.aboutTesting('Testing')
