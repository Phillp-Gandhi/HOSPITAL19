import TalkToExpert
import VisitInstitution
import SeeMoreInformation
import SeeRelatedIssues


def getAService(want):

    if want == 'TalkToExpert':
        return TalkToExpert.aboutSubstanceAbuse('Substance Abuse')
    elif want == 'VisitInstitution':
        return VisitInstitution.aboutSubstanceAbuse('Substance Abuse')
    elif want == 'SeeMoreInformation':
        return SeeMoreInformation.about('Substance Abuse')
    elif want == 'SeeRelatedIssues':
        return SeeRelatedIssues.aboutSubstanceAbuse('Substance Abuse')
