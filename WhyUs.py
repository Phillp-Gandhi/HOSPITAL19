

def whyUs(whyTitle,whyText,whyUrl,whyLinkText,linkOneUrl,linkOneText,linkTwoUrl,linkTwoText,linkThreeUrl,linkThreeText):



    whyUs = '''<!-- ======= Why Us Section ======= -->
<section id="why-us" class="why-us">
  <div class="container">

    <div class="row">
      <div class="col-lg-4 d-flex align-items-stretch">
        <div class="content">
          <h3>{}</h3>
          <p>
            {}
          </p>
          <div class="text-center">
            <a href="{}" class="more-btn">{} <i class="bx bx-chevron-right"></i></a>
          </div>
        </div>
      </div>
      <div class="col-lg-8 d-flex align-items-stretch">
        <div class="icon-boxes d-flex flex-column justify-content-center">
          <div class="row">
            <div class="col-xl-4 d-flex align-items-stretch">
              <div class="icon-box mt-4 mt-xl-0">
                <a href="{}"><i class="bx bx-receipt"></i>
                <h4>{}</h4>
                </a>
              </div>
            </div>
            <div class="col-xl-4 d-flex align-items-stretch">
              <div class="icon-box mt-4 mt-xl-0">
                <a href="{}"><i class="bx bx-cube-alt"></i>
                <h4>{}</h4>
                </a>
              </div>
            </div>
            <div class="col-xl-4 d-flex align-items-stretch">
              <div class="icon-box mt-4 mt-xl-0">
                <a href="{}"><i class="bx bx-images"></i>
                <h4>{}</h4>
                </a>
              </div>
            </div>
          </div>
        </div><!-- End .content-->
      </div>
    </div>

  </div>
</section><!-- End Why Us Section -->'''.format(whyTitle,whyText,whyUrl,whyLinkText,linkOneUrl,linkOneText,linkTwoUrl,linkTwoText,linkThreeUrl,linkThreeText)
    return whyUs