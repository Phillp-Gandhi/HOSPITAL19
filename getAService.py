import TalkToExpert
import VisitInstitution
import SeeMoreInformation
import SeeRelatedIssues


def getAService(want,about):
    
    if want == 'TalkToExpert':
        return TalkToExpert.TalkToExpert(about)
    elif want == 'VisitInstitution':
        return VisitInstitution.VisitInstitution(about)
    elif want == 'SeeMoreInformation':
        return SeeMoreInformation.SeeMoreInformation(about)
    elif want == 'SeeRelatedIssues':
        return SeeRelatedIssues.SeeRelatedIssues(about)
    