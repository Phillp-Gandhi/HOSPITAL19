import TalkToExpert
import VisitInstitution
import SeeMoreInformation
import SeeRelatedIssues


def getAService(want):

    if want == 'TalkToExpert':
        return TalkToExpert.aboutInjury('Injury')
    elif want == 'VisitInstitution':
        return VisitInstitution.aboutInjury('Injury')
    elif want == 'SeeMoreInformation':
        return SeeMoreInformation.about('Injury')
    elif want == 'SeeRelatedIssues':
        return SeeRelatedIssues.aboutInjury('Injury')
