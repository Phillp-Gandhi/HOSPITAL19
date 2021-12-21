import TalkToExpert
import VisitInstitution
import SeeMoreInformation
import SeeRelatedIssues


def getAService(want):

    if want == 'TalkToExpert':
        return TalkToExpert.aboutCounselling('Counselling')
    elif want == 'VisitInstitution':
        return VisitInstitution.aboutCounselling('Counselling')
    elif want == 'SeeMoreInformation':
        return SeeMoreInformation.about('Counselling')
    elif want == 'SeeRelatedIssues':
        return SeeRelatedIssues.aboutCounselling('Counselling')
