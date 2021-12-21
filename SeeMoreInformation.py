from flask import render_template, Markup
import Database


def about(issue):


    issueTitles = '''
        <!-- ======= Departments Section ======= -->
    <section id="departments" class="departments">
      <div class="container">

        <div class="section-title">
          <h2>{}</h2>
          <p>See the information about various types of {} problem and click above to talk to an expert or visit a clinic near you.</p>
        </div>

        <div class="row">
          <div class="col-lg-3">
            <ul class="nav nav-tabs flex-column">
        '''.format(issue,issue)
    issueDatas = '''<div class="col-lg-9 mt-4 mt-lg-0">
            <div class="tab-content">'''


    allIssues = Database.getIssueData(issue)
    tabNumber = 1
    for issues in allIssues:

        issueTitle = issues[0]
        issueData = issues[1]
        if tabNumber == 1:
            issueTitles = str(issueTitles) + str('''
            <li class="nav-item">
                <a class="nav-link active show" data-bs-toggle="tab" href="#tab-{}">{}</a>
              </li>'''.format(tabNumber,issueTitle))
            issueDatas = issueDatas + '''
        <div class="tab-pane active show" id="tab-{}">
                <div class="row">
                <div class="col-lg-8 details order-2 order-lg-1">

                    <p>{}</p>
                  </div></div></div>'''.format(tabNumber,issueData)
        else:
            issueTitles = str(issueTitles) + str('''
            <li class="nav-item">
                <a class="nav-link" data-bs-toggle="tab" href="#tab-{}">{}</a>
              </li>'''.format(tabNumber,issueTitle))
            issueDatas = str(issueDatas) + '''
        <div class="tab-pane" id="tab-{}">
                <div class="row">
                <div class="col-lg-8 details order-2 order-lg-1">

                    {}
                  </div></div></div>'''.format(tabNumber,issueData)
        tabNumber = tabNumber + 1
    issueTitles = str(issueTitles) + '</ul></div>'
    issueDatas = str(issueDatas) + '''</div>
          </div>
        </div>

      </div>
    </section><!-- End Departments Section -->'''

    pageContent = str(issueTitles) + str(issueDatas)
    return pageContent