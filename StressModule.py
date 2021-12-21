import TalkToExpert
import VisitInstitution
import SeeMoreInformation
import SeeRelatedIssues


def getAService(want):

    if want == 'TalkToExpert':
        return TalkToExpert.aboutStress('stress')
    elif want == 'VisitInstitution':
        return VisitInstitution.aboutStress('stress')
    elif want == 'SeeMoreInformation':
        return SeeMoreInformation.about('Stress')
    elif want == 'SeeRelatedIssues':
        return SeeRelatedIssues.aboutStress('stress')

def about():
    stress1Title = 'Work/Job stress'
    stress1Data = ''
    stress2Title = 'Relationship'
    stress2Data = ''
    stress3Title = ''
    stress3Data = ''
    stress4Title = ''
    stress4Data = ''
    stressTitles = [stress1Title,stress2Title,stress3Title,stress4Title]
    stressDatas = [stress1Data,stress2Data,stress3Data,stress4Data]
    about = ''
    stressSection = '''
        <!-- ======= Departments Section ======= -->
    <section id="departments" class="departments">
      <div class="container">

        <div class="section-title">
          <h2>Stress</h2>
          <p>What is making you stressed?</p>
        </div>

        <div class="row">
          <div class="col-lg-3">
            <ul class="nav nav-tabs flex-column">
        '''
    for stressTitle in stressTitles:
        stressSection = str(stressSection) + str('''<li class="nav-item">
                <a class="nav-link active show" data-bs-toggle="tab" href="#tab-1">{}</a>
              </li>'''.format('stressTitles'))
    stressSection = stressSection + str('''</ul></div><div class="col-lg-9 mt-4 mt-lg-0">
            <div class="tab-content">
              <div class="tab-pane active show" id="tab-1">
                <div class="row">''')
    for stressData in stressDatas:
        stressSection = stressSection + '''<div class="col-lg-8 details order-2 order-lg-1">

                    <p>{}</p>
                  </div>'''.format(stressData)
    stressSection = stressSection + '''</div>
              </div>
            </div>
          </div>
        </div>

      </div>
    </section><!-- End Departments Section -->'''
    return about