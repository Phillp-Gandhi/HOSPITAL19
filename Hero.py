def hero(heroText):
    hero = '''<!-- ======= Hero Section ======= -->
<section id="hero" class="d-flex align-items-center">
  <div class="container">
    
    <a href="#main-links" class="btn-get-started scrollto">{}</a>
  </div>
</section><!-- End Hero -->'''.format(heroText)

    return hero