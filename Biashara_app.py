#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, Markup, render_template, request, redirect, url_for, make_response, session, g
import codes, cocks, submitupdates, getformdata, subedits, dressup, viewpage, shopPros, agencypro
import templates, templtes
import MySQLdb, functools
from http import cookies
import os
import smtplib


app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/home')
def mainpage():
    title="BIASHARA EMPLOYERS"
    return render_template('home.html',title=title)
@app.route('/')
def homepage():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    title = 'Website Opportunites'
    picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')

    contspace = Markup('<br /><h2 class="titles">Opportunities of Having websites</h2><ol><li><h3 class="h3s">Access</h3><ul type="circle"><li><p>You get access to more clients on multiple states and places. Data such as country, interest and devices about your users is also available at no extra cost.</p></li><li><p>Your own clients also get access to your business within and outside work hours. They can check availability, access information and even make orders easily. E.g.: <a href="http://biasharaemployers.pythonanywhere.com/page?page=100" class="links">this website</a>.</p></li></ul></li><li><h3 class="h3s">Scalability</h3><p>It is cheaper and requires less effort to increase your number of clients using a website. Posting information on your website is cheaper that printing and employing advertisement agencies. Also increasing the size of your website is easier and cheaper than increasing the size of a physical office.</p></li><li><h3 class="h3s">Careers</h3><p>A website easily enables you to open virtual businesses, which is a great advantage for brokers and talented people.<br /><ul class="paragraph"><li><p> An artist can showcase his/her art on the website and share the website on social media to reach clients.</p></li> <li>A land broker can also showcase lands, apartments and itle deeds for sale without leaving his/her office or house.</li></ul><br /><p> Depending on the complexity of your website, especially when you operate a system, you may need to employ a web designer to improve and be updating your website. Such is an opportunity to comply with government policies regarding employing people with disability.</p></p></li><li><h3 class="h3s">Opportunity to earn</h3><p>It is a common practise to post adverts on your websites and earn advertisement revenue. Note that Google ads and Youtube ads require you to have your own <a class="links" href="requirements">domain name</a>. Meaning that free websites using <a class="links" href="requirements">subdomain names</a> cannot be used to access ad revenue</p></li><li><h3 class="h3s">Project boost</h3><p>It is a good thing to have your own website. Some corporates downgrade social profiles as unofficial and linking to such profiles in your proposals makes you seem unserious or unexperienced.</p></li><li><h3 class="h3s">A Virtual reality</h3><ul type="circle"><li><p>With this opportunity, you can make for yourself a great first impression on all who find you for the first time. You can use animations, videos, images and audio which enable your image to scale in a way that may be too expensive in real life.</p></li><li><p>Depending on your needs and the kind of work you do, you may find a website to be the office you could not afford in real life. Within a website, you can showcase your <a href="samples?sample=18" class="links">products and service</a> and get new clients contacting you on your set channels. It really makes running a home business much simpler.</p></li><ul type="circle"></li></ol></h3><h2 class="titles">How much it costs</h2><h3 class="h3s">Here are different ways to put up a website from the cheapest</h3><ol><li><h3 class="h3s">Create a free website using a free web builder with free <a href="requirements" class="links">hosting</a>.</h3><p>To break even, your host will advertise on your website or leave their name in your web address. To use your own <a href="requirements" class="links">domain</a> name (costs around $11) you will need to pay the host a fee. However, these builders are limited to what you can really use them for; they are not dynamic.</p></li><li><h3 class="h3s">Use a <a href="portfolio" class="links">free template.</a></h3><p>With this option you will already have the <a class="links" href="portfolio">design</a>. So, you will still need to purchase a <a href="requirements" class="links">domain</a> name and a <a href="requirements" class="links">hosting</a> plan. However, you will at least need some basic web design knowledge to instal the whole thing. And you cannot instal systems from <a href="portfolio" class="links">templates</a> without web development knowledge; It would be very difficult! Without such skills, you should get an expert to do the editing for you at a small price. <a class="links" href="contact">Contact us</a>.</p></li><li><h3 class="h3s">Hire experts to build a simple website for you.</h3><p>With this option, you will have to pay for labour, a <a href="requirements" class="links">domain</a> name and <a href="requirements" class="links">hosting</a> fees. <a href="requirements" class="links">domain</a> names and <a href="requirements" class="links">hosting</a> fees are usually paid yearly but most host charge a small fee of around $13 for the first year and anything from $40 for subsequent years.</p></li><li><h3 class="h3s">Create a management system</h3><p>A management system is very flexible in labour costs depending on the complexity and development time. <a href="requirements" class="links">Hosting</a> fees may also vary depending on how your expert decides to build the website and which tools he wants to use. It uses tools that are not available on free website builder plans.</p></li><li><h3 class="h3s">Updating and upgrading existing websites</h3><p>After you have a website, you need to keep updating it with data. For this you may hire your own expert or outsource an expert to do it for you. Again, this heavily depends on how the website was built. In that, was it built dynamicaly- so you can update it yourself OR was it a static- cannot be edited exept from the code itself. To make a static website more dynamic, you need to upgrade it. Upraging and updating costs are always negotiatable.</p></li></ol>')
    return render_template('index.html', account=account, title=title, picspace=picspace, contspace=contspace)


@app.route("/overview")
def over():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    title = "About us"
    picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')
    contspace = Markup('<br /><h2 class="titles">About BIASHARA EMPLOYERS</h2><h3 class="h3s"><div style="background-color:#eff0f2;">BIASHARA EMPLOYERS is a 2 year old IT firm which has been serving in Computer Maintenance, Web design, and internet-services support.</div></h3><h2 class="h3s">Biashara Employers was founded by Phillip G. Oloo who realized his passion for computer back in 2004 when he first used a computer to play computer games.</h2><h3 class="h3s"><div style="background-color:#d47de0;padding-left:30px">&#34;It was a Saturday and I had gone for the Saturday half-day tution. But on this day, whoever was responsible for openning the classrooms was late. The Pre-unit classrooms were open and we were instructed to go there for our tuition. However, being seventh graders, the boys were too proud to study in the kids classroom. So all the boys left school and went to play computer games with the 30 bob tuition fee. I followed along. Since then, I found good use for any 5 shillings I got. Later, that shop was closed and i found a computer college which also offered computer games where I started playing <a class="links" href="https://www.youtube.com/watch?v=kvgRpOHTDOc">Hercules</a>. By first year of high school I had completed the game.</h3></div><div style="background-color:#a17de0;padding-left:30px"><h3 class="h3s"> and started practising Microsft Word 2003. This made me always a step ahead of my class in computer studies. In the second year of High school, A friend introduced me to HTML and Virtual Basics 6.0 and I did more VB6.0 projects than HTML. However, I always loved using the internet and on weekends, I spent whole days in a C.B.D. Cyber Cafe and only broke for lunch. As expected, I scored highest in Computer Studies than all other subjects. At Daystar University I took a degree in Community Development but due to financial difficulties, I was forced into a 5 years break- upto December 2016. During the five years academic break I applied for a volunteering post at a Cyber cafe in Donholm; I wanted to be next to computers and Internet, in an environment where money is exchanged. It worked.</h3><h3 class="h3s">Soon I was employed and I was really happy. That is when I came up with the idea of a website where proffesionals could post articles and earn from ardverts. During development, i realized I did not have what it took to make such a website and took a small break.</h3><h3 class="h3s">Now, the Idea has evolved into BIASHARA EMPLOYERS which is a way to bring local people together with the belief that local people can sustainably support each other to reduce poverty, protect the planet and ensure prosperity for all.</h3><h3 class="h3s">BIASHARA EMPLOYERS envisions a post-cummunist society where people of diverse skills work in their own fields and improve their communities. Money is looked at as a less necessary tool whose current system has encouraged poverty, planet destruction and has pushed the poor into suffering and grief.&#34;</h3></div>')
    return render_template('index.html', account=account, title=title, picspace=picspace, contspace=contspace)

@app.route("/code", methods=['POST', 'GET'])
def code():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    if request.method == "GET":
        title = 'Code of Conduct'
        picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')
        contspace = Markup('<br /><h2 class="titles">Code of Conduct</h2><h3 class="h3s">Adopted from the book of Proverbs</h3><br /><br /><form action="" method="POST"><select name="code"><option value="1">Chapter 1</option><option value="2">Chapter 2</option><option value="3">Chapter 3</option><option value="4">Chapter 4</option><option value="5">Chapter 5</option><option value="6">Chapter 6</option><option value="7">Chapter 7</option><option value="8">Chapter 8</option><option value="9">Chapter 9</option><option value="10">Chapter 10</option><option value="11">Chapter 11</option><option value="12">Chapter 12</option><option value="13">Chapter 13</option><option value="14">Chapter 14</option><option value="15">Chapter 15</option><option value="16">Chapter 16</option><option value="17">Chapter 17</option><option value="18">Chapter 18</option><option value="19">Chapter 19</option><option value="20">Chapter 20</option><option value="21">Chapter 21</option><option value="22">Chapter 22</option><option value="23">Chapter 23</option><option value="24">Chapter 24</option><option value="25">Chapter 25</option><option value="26">Chapter 26</option><option value="27">Chapter 27</option><option value="28">Chapter 28</option><option value="29">Chapter 29</option><option value="30">Chapter 30</option><option value="31">Chapter 31</option></select><button>go</button></form><br /><h1>Proverbs 1 New International Reader&#039;s Version (NIRV)<br /><h2 class="titles">Purpose</h2><p><span><span>1 </span>These are the proverbs of Solomon. He was the son of David and the king of Israel.</span></p> <div><p><span><sup>2 </sup>Proverbs teach you wisdom and instruct you.</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>They help you understand wise sayings.</span></span><br /><span><sup>3 </sup>They provide you with instruction and help you live wisely.</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>They lead to what is right and honest and fair.</span></span><br /><span><sup>4 </sup>They give understanding to childish people.</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>They give knowledge and good sense to those who are young</span></span><br /><span><sup>5 </sup>Let wise people listen and add to what they have learned.</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>Let those who understand what is right get guidance.</span></span><br /><span><sup>6 </sup>What I&#039;m teaching also helps you understand proverbs and stories.</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>It helps you understand the sayings and riddles of those who are wise.</span></span><br /><span><sup>7 </sup>If you really want to gain knowledge, you must begin by having respect for the Lord.</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>But foolish people hate wisdom and instruction.</span></span><br /></p></div><h2 class="titles"><span>Think and Live Wisely</span></h2><h3 class="h3s"><span>A Warning Against Sinful Men</span></h3><div><p><span><sup>8 </sup>My son, listen to your father&#039s advice.</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>Don&#039t turn away from your mother&#039s teaching.</span></span><br /><span><sup>9 </sup>What they teach you will be like a beautiful crown on your head.</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>It will be like a chain to decorate your neck.</span></span></p></div><div><p><span><sup>10 </sup>My son, if sinful men tempt you,</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>don&#039t give in to them.</span></span><br /><span><sup>11 </sup>They might say, "Come along with us.</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>Let&#039s hide and wait to kill someone who hasn&#039t done anything wrong.</span></span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><br /><span><sup>12 </sup>Let&#039s swallow them alive, as the grave does.</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>Let&#039s swallow them whole, like those who go down into the pit.</span></span><br /><span><sup>13 </sup>We&#039ll get all kinds of valuable things.</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>We&#039ll fill our houses with what we steal.</span></span><br /><span><sup>14 </sup>Cast lots with us for what they own.</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>We&#039ll share everything we take from them."</span></span><br /><span><sup>15 </sup>My son, don&#039t go along with them.</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>Don&#039t even set your feet on their paths.</span></span><br /><span><sup>16 </sup>They are always in a hurry to sin.</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>They are quick to spill someone&#039s blood.</span></span><br /><span><sup>17 </sup>How useless it is to spread a net</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>where every bird can see it.</span></span><br /><span><sup>18 </sup>Those who hide and wait will spill their own blood.</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>They will be caught in their own trap.</span></span><br /><span><sup>19 </sup>That&#039s what happens to everyone</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>who goes after money in the wrong way.</span></span><br /><span><sup> </sup>That kind of money takes away</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>the life of those who get it.</span></span></p></div><br /><h3 class="h3s"><span>Wisdom&#039;s Warning</span></h3><div><p><span><sup>20 </sup>Out in the open wisdom calls out.</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>She raises her voice in a public place.</span></span><br /><span><sup>21 </sup>On top of the city wall she cries out.</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>Here is what she says near the gate of the city.</span></span></p></div>  <div><p><span><sup>22 </sup>"How long will you childish people love your childish ways?</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>How long will you rude people enjoy making fun of God and others?</span></span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>How long will you foolish people hate knowledge?</span></span><br /><span><sup>23 </sup>Pay attention to my warning!</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>Then I will pour out my thoughts to you.</span></span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>I will make known to you my teachings.</span></span><br /><span><sup>24 </sup>But you refuse to listen when I call out to you.</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>No one pays attention when I reach out my hand.</span></span><br /><span><sup>25 </sup>You turn away from all my advice.</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>And you do not accept my warning.</span></span><br /><span><sup>26 </sup>So I will laugh at you when you are in danger.</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>I will make fun of you when hard times come.</span></span><br /><span><sup>27 </sup>I will laugh when hard times hit you like a storm.</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>I will laugh when danger comes your way like a windstorm.</span></span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>I will make fun of you when suffering and trouble come.</span></span></p></div>  <div><p><span><sup>28 </sup>"Then you will call to me. But I won&#039;t answer.</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>You will look for me. But you won&#039;t find me.</span></span><br /><span><sup>29 </sup>You hated knowledge.</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>You didn&#039;t choose to have respect for the <span style="font-variant: small-caps">Lord</span>.</span></span><br /><span><sup>30 </sup>You wouldn&#039;t accept my advice.</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>You turned your backs on my warnings.</span></span><br /><span><sup>31 </sup>So you will eat the fruit of the way you have lived.</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>You will choke on the fruit of what you have planned.</span></span></p></div>  <div><p><span><sup>32 </sup>"The wrong path that childish people take will kill them.</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>Foolish people will be destroyed by being satisfied with the way they live.</span></span><br /><span><sup>33 </sup>But those who listen to me will live in safety.</span><br /><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>They will be at ease and have no fear of being harmed."</span></span></p></div> </div><form action="" method="POST"><select name="code"><option value="1">Chapter 1</option><option value="2">Chapter 2</option><option value="3">Chapter 3</option><option value="4">Chapter 4</option><option value="5">Chapter 5</option><option value="6">Chapter 6</option><option value="7">Chapter 7</option><option value="8">Chapter 8</option><option value="9">Chapter 9</option><option value="10">Chapter 10</option><option value="11">Chapter 11</option><option value="12">Chapter 12</option><option value="13">Chapter 13</option><option value="14">Chapter 14</option><option value="15">Chapter 15</option><option value="16">Chapter 16</option><option value="17">Chapter 17</option><option value="18">Chapter 18</option><option value="19">Chapter 19</option><option value="20">Chapter 20</option><option value="21">Chapter 21</option><option value="22">Chapter 22</option><option value="23">Chapter 23</option><option value="24">Chapter 24</option><option value="25">Chapter 25</option><option value="26">Chapter 26</option><option value="27">Chapter 27</option><option value="28">Chapter 28</option><option value="29">Chapter 29</option><option value="30">Chapter 30</option><option value="31">Chapter 31</option></select><button>go</button></form>')
        return render_template('index.html', account=account, title=title, picspace=picspace, contspace=contspace)
    elif request.method == "POST":
        chapter = request.form['code']
        title = 'Code of Conduct'
        picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')
        contspace = codes.getCode(chapter)
        return render_template('index.html', account=account, title=title, picspace=picspace, contspace=contspace)

@app.route("/partnership")
def partners():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    title = 'Partnership'
    picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')
    contspace = Markup('<br /><br /><p><h2 class="titles">The Agreement</h2></p><br /><p><h3 class="h3s">The purpose of this agreement is to forge alliances strong enough to break through difficult economic times.</h3></p><br /><p>Money is a store of value which I believe is nothing but an illusion which really is incapable of reflecting the true value of our work as human beings. Currently, a population of human beings can only do as much as the money that is available. In fact, a skilled worker may not work for his/her community without being offered some money. Ironically, this may be true even where the worker actually enjoys the work.</p><br /><p>In my view, <h3 class="h3s">a worker who enjoys a work should be free to do the work 24/7 if he/she likes it.</h3> And am quite sure that they can work long hours without payment and still feel rewarded by completion, advancement and importance of their work.</p><br /><p>A culture of work is what am calling for. <h3 class="h3s">A culture where people work for the good it brings and not just the money they make.</h3> Like all things made by humans, money will fall and wise people say &#39;if you want to see the future, look into the past&#39;. Like the financial crisis of 2008, people will panic when money falls but a wise man will learn a lesson from everyday life. if you&#39;re ever broke, go borrow at the shop where you regularly buy from. In the same way, businesses and experts need to form strong alliances from suppliers, to manufacturers, to distributors and to consumers.</p><br /><p>Resources are limited and if you spread your water across many crops, you&#39;ll only have so little for your crops. however, if you concentrate all your water on a single plant, you will have a fine crop and maybe some water to spare. in the same way, do not spread your loyalty across many businesses. You may need a loan one day and the banks refuse your application because of the little money in your account.</p><br /><p>Therefore, <h3 class="h3s">I urge businesses and experts to form alliances. Family members should also form business alliances among themselves to reduce poverty among themselves.</h3> The purpose of these alliances is not to grow rich but to develop parallel frameworks to the money and currency standard. The agreement is meant to drive development when people work for each other and do not keep &#39;value&#39; (money) to themselves. Under such an agreement, the profit incentive should be minimized and &#39;selfish&#39; keeping of value should be illegal and penalized.</p><br /><p><h2 class="titles">The parties must negotiate their own agreement terms.</h2> Present business models are a good idea of how a good alliance works. each department does its job and coordinates their activities without paying each other. Unlike separate business entities, departments don&#39;t pay each other for the work they do. They work together to grow and develop the organization. Each department services the other with what they need and vice versa.</p><br /><p>If the parties cannot agree to work for each other without paying, then let them agree to pay each other but maintain strict loyalty towards each other. They may also offer discounts to their ally members.</p><br /><p><h3 class="h3s">&#34;I don&#39;t think there&#39;s any overnight solution. I don&#39;t know anybody smart enough to sit down and write a brand new set of rules and we should all adhere to. I&#39;d think it&#39;s a process of negotiation among sovereign and independent nations and that&#39;s probably how as it should be; and it will evolve over time and I do think we learn from our mistakes. But the idea that there&#39;s some sort of basic right way to do it out there and there is one individual or group who have got all the answers, I&#39;d be deeply suspicious of that notion.&#34;</h3></p><br /><ol><li>Every man & woman should register as a B.E.</li><li>B.E. should search for B.E. businesses or experts when they need a service.</li><li>If the closest B.E. is able to assist, then they should.</li><li></li></ol></p><br /><p><h3 class="h3s">Remember, the Idea was that experts should be supported by people close to them & people who know each other e.g. Family members and friends.</h3></p><br /><p>Therefore/And, proximity sensors are vital if the system is to achieve this original concept.</p><br /><p>But since a required expert/service may not be available close by, results from the same city and country will be included. Otherwise, expanding the proximity range may give better results that clustering all results from outside the city together.</p><br /><br />')
    return render_template('index.html', account=account, title=title, picspace=picspace, contspace=contspace)

@app.route("/privacy")
def priv():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    title = 'Privacy Policy'
    picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')
    contspace = Markup('<br /><h1 class="titles">BIASHARA EMPLOYERS Privacy Policy</h1><p>April 6, 2018</p><p>We believe in privacy and we do not intentionally collect any of you data exept for the running and improvement of the system. However, we are a mash up project and the data you submit on this site or its affiliates, will be shared to third parties. The third parties may again share with other third parties in line with their own privacy policy and terms of use. </p><h2 class="titles">What information do we require to run the system?</h2><div><p>In order to run the system, we need basic information which represent your business. Such info includes:<ul type="circle"><li><p>Business name</p></li><li><p>email</p></li><li><p>web address</p></li><li><p>phone number</p></li><li><p>Business type</p></li><li><p>Summary</p></li><li><p>Country</p></li><li><p>City</p></li><li><p>Physical address</p></li><li><p>Address accuracy</p></li><li><p>Analytics data</p></li></ul> </p><p>We may require more or less information as we update our system. Kindly check the registeration page to see the information we require. Thanks.</p><p>Note: We believe in privacy and we may not embed adverts for your privacy and safety.</p></div><h2 class="titles">How do we learn information about you?</h2></header><div><p>We learn information about you when:</p><div class="paragraph"><ul type="circle"><li>you give it to us directly (e.g., When you register your business);</li><li>from google analytics e.g.<ul type="circle"><li>Queries users used to find our website</li><li>Pages users view on our websites</li><li>Countries where users are from</li><li>Devices users use to view our website</li><li>Whether users use web search, image search or video search e.t.c.</div></li></ul></li></ul></div><h2 class="titles">What do we do with your information once we have it?</h2><div><p>Generally, we use your information to help us provide and improve and services to you.</p></div><h2 class="titles">When do we share your information with others?</h2><div class="paragraph">When we submit it to our mash up partners for the sake of synchronization, <a href="requirements" class="links">hosting</a> and other outsourced (mash up) processes.</div><h2 class="titles">How do we store and protect your personal information?</h2><div><p>We aim for our system to be light weight and stateless. As such we do not need to store the information you give us. It will be stored by an external partner and so you should only share information you are willing to be shared all around the world.</p></div><h2 class="titles">What else should you know?</h2><div><p>We&#039;re a global organization and our computers are in several different places around the world. We also use service providers whose computers may also be in various countries. This means that your information might end up on one of those computers in another country, and that country may have a different level of data protection regulation than yours. By giving us information, you consent to this kind of transfer of your information. No matter what country your information is in, it may not be in our control, after you have submitted to us.</p></div><h2 class="titles">What if we change this privacy policy or any of our privacy notices?</h2><div><p>We may need to change this policy and our notices.  The updates will be posted online. If the changes are substantive, we will announce the update through usual channels for such announcements such as blog posts and forums. Your continued use of the product or service after the effective date of such changes constitutes your acceptance of such changes. To make your review more convenient, we will post an effective date at the top of the page.</p></div><br />')
    return render_template('index.html', account=account, title=title, picspace=picspace, contspace=contspace)

@app.route("/websites")
def websites():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    title = 'Websites samples'
    picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')
    limit = 5
    contspac = dressup.getSites(limit)
    contspace = '<br /><h2>The following are some of the products developed using this System. To create your own website, <a href="signup" class="links">Sign up</a> or <a href="signin" class="links">Sign in</a>.</h2><p>For customized websites, read through <a href="requirements" class="links">the requirements</a> then <a href="requirements#quote" class="links">Request quote</a>.</p>'
    contspace = contspace + contspac + '<br /><br />'
    contspace = Markup(contspace)
    heads='<meta name="robots" content="noachive">'
    return render_template('index.html', account=account, title=title, picspace=picspace, contspace=contspace, heads=heads)

@app.route("/templates", methods=['GET', 'POST'])
def port():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    title = 'Website templates'
    picspace = Markup('<img style="bgcolor:#a7a8aa;" src="http://biasharaemployers.pythonanywhere.com/static/samples/heroic.png" />')
    if request.method == 'GET':
        contspace = Markup('<table> <tr><td><h3 class="h3s">System</h3></td><td style="padding:10px;"><a href="http://bizbiz.pythonanywhere.com/find"><img src="static/sampone.png" class="imgs" /></a></td></tr> <tr><td><h3 class="h3s">Resume</h3></td><td style="padding:10px;"><a href="samples?sample=1"><img src="static/samples/rsm.png" /></a></td></tr> <tr><td><h3 class="h3s">Agency</h3></td><td style="padding:10px;"><a href="samples?sample=2"><img src="static/samples/agency.png" /></a></td></tr> <tr><td><h3 class="h3s">Freelancer</h3></td><td style="padding:10px;"><a href="samples?sample=3"><img src="static/samples/freelance.png" /></a></td></tr> <tr><td><h3 class="h3s">Landing page</h3></td><td style="padding:10px;"><a href="samples?sample=4"><img src="static/samples/landing.png" /></a></td></tr> <tr><td><h3 class="h3s">Grayscale</h3></td><td style="padding:10px;"><a href="samples?sample=5"><img src="static/samples/grayscale.png" /></a></td></tr> <tr><td><h3 class="h3s">Casual</h3></td><td style="padding:10px;"><a href="samples?sample=6-home"><img src="static/samples/casual.png" /></a></td></tr> <tr><td><h3 class="h3s">One page</h3></td><td style="padding:10px;"><a href="samples?sample=7"><img src="static/samples/onepage.png" /></a></td></tr> <tr><td><h3 class="h3s">Frontpage website</h3></td><td style="padding:10px;"><a href="samples?sample=8"><img src="static/samples/frontpage.png" /></a></td></tr> <tr><td><h3 class="h3s">Blog</h3></td><td style="padding:10px;"><a href="samples?sample=9"><img src="static/samples/blogsite.png" /></a></td></tr> <tr><td><h3 class="h3s">Modern business</h3></td><td style="padding:10px;"><a href="samples?sample=20"><img src="static/samples/modern.png" /></a></td></tr> <tr><td><h3 class="h3s">Shop</h3></td><td style="padding:10px;"><a href="samples?sample=18"><img src="static/samples/shop.png" /></a></td></tr></table><p><form action="" method="POST"><button type="submit">Other pages</button></form></p>')
        return render_template('index.html', account=account, title=title, picspace=picspace, contspace=contspace)
    elif request.method == 'POST':
        contspace = Markup('<table> <tr><td><h3 class="h3s">System</h3></td><td style="padding:10px;"><a href="http://bizbiz.pythonanywhere.com/find"><img src="static/sampone.png" class="imgs" /></a></td></tr> <tr><td><h3 class="h3s">Post</h3></td><td style="padding:10px;"><a href="samples?sample=10"><img src="static/samples/postpage.png" /></a></td></tr> <tr><td><h3 class="h3s">Fullpage</h3></td><td style="padding:10px;"><a href="samples?sample=11"><img src="static/samples/fullpage.png" /></a></td</tr> <tr><td><h3 class="h3s">Heroic</h3></td><td style="padding:10px;"><a href="samples?sample=12"><img src="static/samples/heroic.png" /></a></td</tr> <tr><td><h3 class="h3s">About page</h3></td><td style="padding:10px;"><a href="samples?sample=13"><img src="static/samples/About page.png" /></a></td</tr> <tr><td><h3 class="h3s">Small business</h3></td><td style="padding:10px;"><a href="samples?sample=14"><img src="static/samples/small business.png" /></a></td</tr> <tr><td><h3 class="h3s">Thumbnails</h3></td><td style="padding:10px;"><a href="samples?sample=15"><img src="static/samples/thumbnails.png" /></a></td</tr> <tr><td><h3 class="h3s">Shop Product</h3></td><td style="padding:10px;"><a href="samples?sample=19"><img src="static/samples/shopproduct.png" /></a></td</tr> <tr><td><h3 class="h3s">Simple sidebar</h3></td><td style="padding:10px;"><a href="samples?sample=21"><img src="static/samples/simplesidebar.png" /></a></td</tr> <tr><td><h3 class="h3s">4 Column Portfolio</h3></td><td style="padding:10px;"><a href="samples?sample=16"><img src="static/samples/4colport.png" /></a></td</tr> <tr><td><h3 class="h3s">3 Column Portfolio</h3></td><td style="padding:10px;"><a href="samples?sample=22"><img src="static/samples/3colport.png" /></a></td</tr> <tr><td><h3 class="h3s">2 Column portfolio</h3></td><td style="padding:10px;"><a href="samples?sample=23"><img src="static/samples/2colport.png" /></a></td</tr> <tr><td><h3 class="h3s">1 Column Portfolio</h3></td><td style="padding:10px;"><a href="samples?sample=24"><img src="static/samples/1colport.png" /></a></td</tr> <tr><td><h3 class="h3s">Portfolio item</h3></td><td style="padding:10px;"><a href="samples?sample=17"><img src="static/samples/portitem.png" /></a></td</tr> <tr><td><h3 class="h3s">Full width pics</h3></td><td style="padding:10px;"><a href="samples?sample=25"><img src="static/samples/fullwidth.png" /></a></td</tr> <tr><td><h3 class="h3s">The big picture</h3></td><td style="padding:10px;"><a href="samples?sample=26"><img src="static/samples/bigpicture.png" /></a></td</tr> <tr><td><h3 class="h3s">Logo nav</h3></td><td style="padding:10px;"><a href="samples?sample=27"><img src="static/samples/logonav.png" /></a></td</tr> <tr><td><h3 class="h3s">halfslider</h3></td><td style="padding:10px;"><a href="samples?sample=28"><img src="static/samples/halfslider.png" /></a></td</tr> <tr><td><h3 class="h3s">Scrolling Nav</h3></td><td style="padding:10px;"><a href="samples?sample=29"><img src="static/samples/scrollingnav.png" /></a></td</tr> </table><p><form action="" method="GET"><button type="submit">Website templates</button></form></p>')
        return render_template('index.html', account=account, title=title, picspace=picspace, contspace=contspace)

@app.route("/portfolio-pages")
def portot():
    title = 'Sample Websites pages'
    contspace = Markup('<br /><h2 class="titles" align="center">Website pages samples</h2>')
    return render_template('samples.html', title=title, contspace=contspace, page="page")
@app.route("/samples")
def sample4():

    try:
        sample = request.args['sample']

    except:
        return redirect(url_for('port'))
    else:
        sample = request.args['sample']

        return render_template('sampler.html', sample=sample)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    title = 'Sign up'
    picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')
    if request.method == "GET":
        try:
            g.user = session['user']
            g.password = session['password']
            g.uid = session['uid']
        except:
            account='out'
            session.pop('user', None)
            session.pop('uid', None)
            session.pop('password', None)
            contspace = Markup('<table colspan="2"><tr><th>Sign up</th></tr><form action="" method="POST"><tr><td><label>User Name: </label></td><td><input type="text" name="uName" placeholder="User name"></td></tr><tr><td><label>Password: </label></td><td><input type="password" name="uPass" placeholder="New password"></td></tr><tr><td><label>Confirm Password: </label></td><td><input type="password" name="cPass" placeholder="Confirm password"></td></tr><tr><td><button type="submit">Send</button></td><td><button type="reset">RESET</button></td></tr><tr><td></td><td></td></tr></form></table>')
            return render_template('index.html', account=account, title=title, picspace=picspace, contspace=contspace)
        else:
            account = 'in'
            if g.user and g.password:
                uName = g.user
                uPass = g.password

                checklogin = dressup.checklogin(uName,uPass)



                if checklogin == 'good':
                    return redirect(url_for('homepage'))
                elif checklogin == 'bad':
                    return render_template('index.html', account=account, title=title, picspace=picspace, contspace=contspace)
    elif request.method == "POST":
        session.pop('user', None)
        session.pop('uid', None)
        session.pop('password', None)
        uName = request.form['uName']
        uPass = request.form['uPass']
        cPass = request.form['cPass']



        session['user'] = uName
        session['password'] = uPass



        if uPass == cPass:
            if len(uPass) > 4:
                conn = MySQLdb.connect("BiasharaEmployers.mysql.pythonanywhere-services.com","BiasharaEmployer","IwillLove4ever","BiasharaEmployer$templates" )
                cursor = conn.cursor()

                cursor.execute("SET @u = '{}'".format(uName))
                cursor.execute("""SET @data = CONCAT("SELECT * FROM passwords WHERE uName = '", @u , "'")""")
                cursor.execute("PREPARE stmt FROM @data")
                c = cursor.execute("EXECUTE stmt")
                if c == 0:

                    cursor.execute("SET @uName = '{}'".format(uName))
                    cursor.execute("SET @uPass = '{}'".format(uPass))

                    cursor.execute("""SET @main = CONCAT("INSERT INTO passwords (uName,uPass) VALUES ('", @uName , "','", @uPass , "')")""")
                    cursor.execute("PREPARE stmt FROM @main")
                    cursor.execute("EXECUTE stmt")
                    conn.commit()
                    conn.close()
                    cursor.close()
                    return redirect(url_for('sign_in'))

                    '''#GET uID
                    uID = dressup.getuid(uName,uPass)

                    session['uid'] = uID
                    g.uid = session['uid']
                    session['password'] = uPass
                    g.password = session['password']
                    session['user'] = uName
                    g.user = session['user']




                    session['user'] = uName
                    session['password'] = uPass
                    account = 'in'

                    picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')
                    contspace = 'Welcome {}'.format(g.user)
                    return render_template('index.html', account=account, title=title, picspace=picspace, contspace=contspace)'''
                else:
                    account = 'out'
                    picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')
                    contspace = Markup('<table colspan="2"><tr><th>Sign up</th></tr><form action="submitLogin" method="POST"><tr><td><label>User Name: </label></td><td><input type="text" name="uName" placeholder="User name"></td></tr><tr><td><label>Password: </label></td><td><input type="password" name="uPass" placeholder="New password"></td></tr><tr><td><label>Confirm Password: </label></td><td><input type="password" name="cPass" placeholder="Confirm password"></td></tr><tr><td><button type="submit">Send</button></td><td><button type="reset">RESET</button></td></tr><tr><td></td><td><label>User name exists</label></td></tr></form></table>')
                    return render_template('index.html', account=account, title='Sign up', picspace=picspace, contspace=contspace)
            else:
                account = 'out'
                picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')
                contspace = Markup('<table colspan="2"><tr><th>Sign up</th></tr><form action="submitLogin" method="POST"><tr><td><label>User Name: </label></td><td><input type="text" name="uName" placeholder="User name"></td></tr><tr><td><label>Password: </label></td><td><input type="password" name="uPass" placeholder="New password"></td></tr><tr><td><label>Confirm Password: </label></td><td><input type="password" name="cPass" placeholder="Confirm password"></td></tr><tr><td><button type="submit">Send</button></td><td><button type="reset">RESET</button></td></tr><tr><td></td><td><i>Password is too short</i></td></tr></form></table>')
                return render_template('index.html', account=account, title='Sign up', picspace=picspace, contspace=contspace)
        else:
            account = 'out'
            picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')
            contspace = Markup('<table colspan="2"><tr><th>Sign up</th></tr><form action="submitLogin" method="POST"><tr><td><label>User Name: </label></td><td><input type="text" name="uName" placeholder="User name"></td></tr><tr><td><label>Password: </label></td><td><input type="password" name="uPass" placeholder="New password"></td></tr><tr><td><label>Confirm Password: </label></td><td><input type="password" name="cPass" placeholder="Confirm password"></td></tr><tr><td><button type="submit">Send</button></td><td><button type="reset">RESET</button></td></tr><tr><td></td><td><i>Passwords do not match </i></td></tr></form></table>')
            return render_template('index.html', account=account, title='Sign up', picspace=picspace, contspace=contspace)


@app.route("/submitLogin", methods=['POST', 'GET'])
def sublime():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    title = ''
    picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')
    if request.method == "GET":
        contspace = ''
        return render_template('index.html', account=account, title=title, picspace=picspace, contspace=contspace)
    elif request.method == "POST":

        uName = request.form['uName']
        uPass = request.form['uPass']
        cPass = request.form['cPass']

        session['user'] = uName
        session['password'] = uPass
        session['uid'] = dressup.getuid(uName,uPass)

        if uPass == cPass:
            if len(uPass) > 4:
                conn = MySQLdb.connect("BiasharaEmployers.mysql.pythonanywhere-services.com","BiasharaEmployer","IwillLove4ever","BiasharaEmployer$templates" )
                cursor = conn.cursor()

                cursor.execute("SET @u = '{}'".format(uName))
                cursor.execute("""SET @data = CONCAT("SELECT * FROM passwords WHERE uName = '", @u , "'")""")
                cursor.execute("PREPARE stmt FROM @data")
                c = cursor.execute("EXECUTE stmt")
                if c == 0:

                    cursor.execute("SET @uName = '{}'".format(uName))
                    cursor.execute("SET @uPass = '{}'".format(uPass))
                    #cursor.execute("SET @style = '{}'".format(style))
                    cursor.execute("""SET @main = CONCAT("INSERT INTO passwords (uName,uPass) VALUES ('", @uName , "','", @uPass , "')")""")

                    cursor.execute("PREPARE stmt FROM @main")
                    cursor.execute("EXECUTE stmt")
                    '''cursor.execute("""SET @secondary = CONCAT("INSERT INTO assets (style) VALUES ('", @style , "')")""")
                    cursor.execute("PREPARE stmt FROM @secondary")
                    cursor.execute("EXECUTE stmt")'''

                    add = cocks.addLogin(uName,uPass)
                    add = add['uName'].value
                    add = 'Welcome ' + add



                    conn.commit()
                    conn.close()
                    cursor.close()

                    picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')
                    #form = templates.form(style)
                    contspace = Markup('Succesfully signed up {}. You can now visit the <a href="dashboard" class="links">Dashboard</a> to create your first website.'.format(uName))
                    return render_template('index.html', account=account, title=add, picspace=picspace, contspace=contspace)
                else:
                    picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')
                    contspace = Markup('<table colspan="2"><tr><th>Sign up</th></tr><form action="submitLogin" method="POST"><tr><td><label>User Name: </label></td><td><input type="text" name="uName" placeholder="User name"></td></tr><tr><td><label>Password: </label></td><td><input type="password" name="uPass" placeholder="New password"></td></tr><tr><td><label>Confirm Password: </label></td><td><input type="password" name="cPass" placeholder="Confirm password"></td></tr><tr><td><button type="submit">Send</button></td><td><button type="reset">RESET</button></td></tr><tr><td><label>User name exists</label></td></tr></form></table>')
                    return render_template('index.html', account=account, title='Sign up', picspace=picspace, contspace=contspace)
            else:
                picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')
                contspace = Markup('<table colspan="2"><tr><th>Sign up</th></tr><form action="submitLogin" method="POST"><tr><td><label>User Name: </label></td><td><input type="text" name="uName" placeholder="User name"></td></tr><tr><td><label>Password: </label></td><td><input type="password" name="uPass" placeholder="New password"></td></tr><tr><td><label>Confirm Password: </label></td><td><input type="password" name="cPass" placeholder="Confirm password"></td></tr><tr><td><button type="submit">Send</button></td><td><button type="reset">RESET</button></td></tr><tr><td><i>Password is too short</i></td></tr></form></table>')
                return render_template('index.html', account=account, title='Sign up', picspace=picspace, contspace=contspace)
        else:
            picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')
            contspace = Markup('<table colspan="2"><tr><th>Sign up</th></tr><form action="submitLogin" method="POST"><tr><td><label>User Name: </label></td><td><input type="text" name="uName" placeholder="User name"></td></tr><tr><td><label>Password: </label></td><td><input type="password" name="uPass" placeholder="New password"></td></tr><tr><td><label>Confirm Password: </label></td><td><input type="password" name="cPass" placeholder="Confirm password"></td></tr><tr><td><button type="submit">Send</button></td><td><button type="reset">RESET</button></td></tr><tr><td><i>Passwords do not match </i></td></tr></form></table>')
            return render_template('index.html', account=account, title='Sign up', picspace=picspace, contspace=contspace)



@app.route("/mysites", methods=['GET', 'POST'])
def mysites():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')
    title = 'My pages'
    if request.method == "GET":
        try:
            g.user = session['user']
            g.password = session['password']
            g.uid = session['uid']
        except:
            return redirect(url_for('sign_in'))
        else:
            if g.user and g.password:
                uName = g.user
                uPass = g.password
                CHECK = dressup.checklogin(uName,uPass)


                if CHECK == 'good':


                    #GET ALL ASSETS
                    #assets=dressup.getassets(uID) this one brings assets in combobox
                    conn = MySQLdb.connect("BiasharaEmployers.mysql.pythonanywhere-services.com","BiasharaEmployer","IwillLove4ever","BiasharaEmployer$templates" )
                    cursor = conn.cursor()

                    cursor.execute("SET @id = '{}'".format(g.uid))
                    cursor.execute("""SET @getAssets = CONCAT("SELECT aID, aName, acDate, style FROM assets WHERE uID = '", @id , "' ORDER BY acDate ASC")""")
                    cursor.execute("PREPARE stmt FROM @getAssets")
                    cursor.execute("EXECUTE stmt")
                    assets = cursor.fetchall()
                    ast = str(assets)
                    if ast == '()':
                        contspace = Markup('Sorry {}, You have not created any website yet. <a class="links" href="dashboard-createwebsite">create now</a>'.format(g.user))
                        return render_template('dashboard.html', header='No website?', contspace=contspace, title=title)
                    cursor.close()
                    conn.close()

                    allas = ''
                    for asset in assets:
                        #asset = {}
                        for col in asset:
                            aid = asset[0]
                            aName = asset[1]
                            acDate = asset[2]
                            style = asset[3]
                            ass = {'aid': aid, 'aName': aName, 'acDate': acDate, 'style': style}

                        allas = allas + '<tr><td>{}</td><td>http://biasharaemployers.pythonanywhere.com/page?page={}</td><td><a class="links" href="http://biasharaemployers.pythonanywhere.com/page?page={}">go</a></td><tr>'.format(aName,aid,aid)

                    assets = Markup('<table border="1" width="90%"><tr><th>Website name</th><th>Address</th><th>visit</th></tr>{}</table>'.format(allas))
                    return render_template('dashboard.html', header='Your websites and their addresses', contspace=assets, title=title, uName=g.user)

@app.route("/editpage", methods=['GET', 'POST'])
def editter():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')
    title = 'Biashara editor'
    if request.method == "GET":
        contspace = ''
        return render_template('index.html', account=account, contspace=contspace, title=title, picspace=picspace)
    elif request.method == "POST":
        style = request.form['styles']

        form = templates.form(style)

        contspace = form
        return render_template('index.html', account=account, contspace=contspace, title=title, picspace=picspace)



@app.route("/updatepage", methods=['GET', 'POST'])
def savresume():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')

    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        return redirect(url_for('sign_in'))
    else:
        if g.user and g.password:
            #CHECK_LOGIN
            uName = g.user
            uPass = g.password
            checklogin = dressup.checklogin(uName,uPass)
            uID = g.uid

            if checklogin == 'good':


                if request.method == "POST":
                    style = request.form['style']

                    if style == 'shop':

                        g.user = session['user']
                        g.password = session['password']
                        #g.edit = session['edit']
                        if pageAction == 'addShop':
                            aName = request.form['aName']

                            addShop = dressup.addShop(uID,style,aName)
                            aID = addShop
                            session['edit'] = aID
                            g.edit = session['edit']
                            contspace = Markup('Your shop was added succesfully. You can now add products to your shop website.<br /><br /><form method="POST" action=""><input type="hidden" name="action1" value="addProduct"><label>Product Name: </label><input type="TEXT" name="pname"> <br /><label>Product price: </label><input type="TEXT" name="pprice"><br /><label>Description: </label><input type="TEXT" name="pdescription"><br /><label>Category: </label><input type="TEXT" name="pcategory"><br /><label>Subcategory: </label><input type="TEXT" name="psubcategory"><button type="submit">SEND</button> <button type="RESET">CLEAR FORM</button></form>')
                            return render_template('dashboard.html', contspace=contspace)
                        if pageAction == "aDd":
                            contspace = Markup(""" <form method="POST" action=""><input type="hidden" name="action1" value="addProduct"><label>Product Name: </label><input type="TEXT" name="pname"> <br /><label>Product price: </label><input type="TEXT" name="pprice"><br /><label>Description: </label><input type="TEXT" name="pdescription"><br /><label>Category: </label><input type="TEXT" name="pcategory"><br /><label>Subcategory: </label><input type="TEXT" name="psubcategory"><button type="submit">SEND</button> <button type="RESET">CLEAR FORM</button></form> """)
                            return render_template('dashboard.html', title=title, header='Add a product', uName=g.user, contspace=contspace)
                        elif pageAction == "uPdate":
                            contspace = Markup(""" <form method="POST" action=""><input type="hidden" name="action1" value="updateProduct"><label>Product Name: </label><input type="TEXT" name="pname"> <br /><label>Product price: </label><input type="TEXT" name="pprice"><br /><label>Description: </label><input type="TEXT" name="pdescription"><br /><label>Category: </label><input type="TEXT" name="pcategory"><br /><label>Subcategory: </label><input type="TEXT" name="psubcategory"><button type="submit">SEND</button> <button type="RESET">CLEAR FORM</button></form> """)
                            return render_template('dashboard.html', title=title, header='Update a product', uName=g.user, contspace=contspace)
                        elif pageAction == "dElete":
                            contspace = Markup('<form method="POST" action=""><input type="hidden" name="action1" value="deleteProduct"><p><label>Select product: <select name="product"><option value="##">Product1</option><option value="##">Product2</option></p>')
                            return render_template('dashboard.html', title=title, header='Add a product', uName=g.user, contspace=contspace)
                        elif pageAction == "sEttings":
                            contspace = Markup('<form method=""')
                            return render_template('dashboard.html', title=title, header='Add a product', uName=g.user, contspace=contspace)
                        elif pageAction == "addProduct":
                            aID = session['edit']
                            addProduct = dressup.addProduct(aID,pName,pPrice,pDescription,pCategory,pSubcategory)
                            if addProduct == 'success':
                                contspace = 'Product added succesfully'
                                return render_template('dashboard.html', uName=g.user, contspace=contspace, header='Add a product', title=title)
                            elif pageAction == "addShop":
                                contspace = Markup('')
                                return render_template('dashboard.html', title=title, uName=g.user, header='Added succesfully', contspace=contspace)
                            elif pageAction == "updateProduct":
                                contspace = Markup('')
                                return render_template('dashboard.html', title=title, uName=g.user, header='Updated succesfully', contspace=contspace)
                            elif pageAction == "deleteProduct":
                                contspace = Markup('')
                                return render_template('dashboard.html', title=title, uName=g.user, header='Deleted succesfully', contspace=contspace)

                    if style == 'resume':
                        fName = request.form['fName'].replace("'","&#39;")
                        lName = request.form['lName'].replace("'","&#39;")
                        aImage = request.form['aImage']
                        sAddress = request.form['sAddress'].replace("'","&#39;")
                        pHone = request.form['pHone'].replace("'","&#39;")
                        eMail =request.form['eMail'].replace("'","&#39;")
                        dEscription = request.form['dEscription'].replace("'", Markup('&#39;'))
                        tItle1 = request.form['tItle1'].replace("'","&#39;")
                        tItle2 = request.form['tItle2'].replace("'","&#39;")
                        tItle3 = request.form['tItle3'].replace("'","&#39;")
                        tItle4 = request.form['tItle4'].replace("'","&#39;")
                        cOmpany1 = request.form['cOmpany1'].replace("'","&#39;")
                        cOmpany2 = request.form['cOmpany2'].replace("'","&#39;")
                        cOmpany3 = request.form['cOmpany3'].replace("'","&#39;")
                        cOmpany4 = request.form['cOmpany4'].replace("'","&#39;")
                        dEscription1 = request.form['dEscription1'].replace("'","&#39;")
                        dEscription2 = request.form['dEscription2'].replace("'","&#39;")
                        dEscription3 = request.form['dEscription3'].replace("'","&#39;")
                        dEscription4 = request.form['dEscription4'].replace("'","&#39;")
                        exDate1 = request.form['exDate1'].replace("'","&#39;")
                        exDate2 = request.form['exDate2'].replace("'","&#39;")
                        exDate3 = request.form['exDate3'].replace("'","&#39;")
                        exDate4 = request.form['exDate4'].replace("'","&#39;")
                        iNstitution1 = request.form['iNstitution1'].replace("'","&#39;")
                        iNstitution2 = request.form['iNstitution2'].replace("'","&#39;")
                        pRogramme1 = request.form['pRogramme1'].replace("'","&#39;")
                        pRogramme2 = request.form['pRogramme2'].replace("'","&#39;")
                        cOurse1 = request.form['cOurse1'].replace("'","&#39;")
                        cOurse2 = request.form['cOurse2'].replace("'","&#39;")
                        gRade1 = request.form['gRade1'].replace("'","&#39;")
                        gRade2 = request.form['gRade2'].replace("'","&#39;")
                        edDate1 = request.form['edDate1'].replace("'","&#39;")
                        edDate2 = request.form['edDate2'].replace("'","&#39;")
                        sKill1 = request.form['sKill1'].replace("'","&#39;")
                        sKill2 = request.form['sKill2'].replace("'","&#39;")
                        sKill3 = request.form['sKill3'].replace("'","&#39;")
                        sKill4 = request.form['sKill4'].replace("'","&#39;")
                        sKill5 = request.form['sKill5'].replace("'","&#39;")
                        sKill6 = request.form['sKill6'].replace("'","&#39;")
                        iNterest1 = request.form['iNterest1'].replace("'","&#39;")
                        iNterest2 = request.form['iNterest2'].replace("'","&#39;")
                        iNterest3 = request.form['iNterest3'].replace("'","&#39;")
                        iNterest4 = request.form['iNterest4'].replace("'","&#39;")
                        iNterest5 = request.form['iNterest5'].replace("'","&#39;")
                        iNterest6 = request.form['iNterest6'].replace("'","&#39;")
                        aWard1 = request.form['aWard1'].replace("'","&#39;")
                        aWard2 = request.form['aWard2'].replace("'","&#39;")
                        aWard3 = request.form['aWard3'].replace("'","&#39;")
                        aWard4 = request.form['aWard4'].replace("'","&#39;")
                        aName = request.form['aName'].replace("'","&#39;")
                        style = request.form['style'].replace("'","&#39;")


                        clue = submitupdates.resume(style,uID,fName,lName,sAddress,pHone,eMail,dEscription,tItle1,tItle2,tItle3,tItle4,cOmpany1,cOmpany2,cOmpany3,cOmpany4,dEscription1,dEscription2,dEscription3,dEscription4,exDate1,exDate2,exDate3,exDate4,iNstitution1,iNstitution2,pRogramme1,pRogramme2,cOurse1,cOurse2,gRade1,gRade2,edDate1,edDate2,sKill1,sKill2,sKill3,sKill4,sKill5,sKill6,iNterest1,iNterest2,iNterest3,iNterest4,iNterest5,iNterest6,aWard1,aWard2,aWard3,aWard4,aName,aImage)
                        if clue == 'continue':
                            #contspace='Good. You exist as {}. You joined on {}'.format(g.user, uID)
                            return render_template('studio/resume.html', fName=fName, lName=lName, sAddress=sAddress, pHone=pHone, eMail=eMail, dEscription=dEscription, tItle1=tItle1, tItle2=tItle2, tItle3=tItle3, tItle4=tItle4, cOmpany1=cOmpany1, cOmpany2=cOmpany2, cOmpany3=cOmpany3, cOmpany4=cOmpany4, dEscription1=dEscription1, dEscription2=dEscription2, dEscription3=dEscription3, dEscription4=dEscription4, exDate1=exDate1, exDate2=exDate2, exDate3=exDate3, exDate4=exDate4, iNstitution1=iNstitution1, iNstitution2=iNstitution2, pRogramme1=pRogramme1, pRogramme2=pRogramme2, cOurse1=cOurse1, cOurse2=cOurse2, gRade1=gRade1, gRade2=gRade2, edDate1=edDate1, edDate2=edDate2, sKill1=sKill1, sKill2=sKill2, sKill3=sKill3, sKill4=sKill4, sKill5=sKill5, sKill6=sKill6, iNterest1=iNterest1, iNterest2=iNterest2, iNterest3=iNterest3, iNterest4=iNterest4, iNterest5=iNterest5, iNterest6=iNterest6, aWard1=aWard1, aWard2=aWard2, aWard3=aWard3, aWard4=aWard4, aImage=aImage)
                        else:
                            return render_template('index.html', account=account, title='Error', picspace=picspace, contspace='Something went wrong. Try again.')
                            #return render_template('index.html', account=account, title='Logged in', contspace=contspace, picspace=clue)
            elif checklogin == 'bad':
                return render_template("index.html", title='Not logged in', picspace=picspace, contspace='Your login details could not be found')

@app.route("/signin", methods=['GET', 'POST'])
def sign_in():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    title = 'Sign in'
    picspace = ''
    if request.method == "GET":
        contspace = Markup('<table colspan="2"><tr><th>Sign in</th></tr><form action="" method="POST"><tr><td><label>User Name: </label></td><td><input type="text" name="uName" placeholder="User name"></td></tr><tr><td><label>Password: </label></td><td><input type="password" name="uPass" placeholder="New password"></td></tr><tr><td><button type="submit">Send</button></td><td><button type="reset">RESET</button></td></tr><tr><td></td><td></td></tr></form></table>')
        return render_template('index.html', account=account, title=title, picspace=picspace, contspace=contspace)
    elif request.method == "POST":
        session.pop('user', None)
        session.pop('password', None)
        session.pop('uid', None)
        uName = request.form['uName']
        uPass = request.form['uPass']

        checklogin = dressup.checklogin(uName,uPass)
        if checklogin == 'good':
            uID = dressup.getuid(uName,uPass)

            session['user'] = uName
            session['password'] = uPass
            session['uid'] = uID
            account = 'in'

            g.user = session['user']
            g.password = session['password']
            g.uid = session['uid']
            return redirect(url_for('dash'))



        elif checklogin == 'bad':
            return redirect(url_for('sign_in'))




@app.route("/logout")
def logout():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    session.pop('user', None)
    session.pop('password', None)
    session.pop('uid', None)
    session.pop('edit', None)
    session.pop('aName', None)
    account = 'out'
    picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')
    return render_template('index.html', account=account, title='Logged out', picspace=picspace, contspace='You have been succesfully logged out!')
@app.route("/protected")
def protect():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    if g.user:
        contspace = session['user']
        return render_template('index.html', account=account, contspace=contspace)
    else:
        return render_template('index.html', account=account, contspace='Log in first')


@app.route("/user")
def getuser():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    try:
        g.user = session['user']
    except:
        return render_template('index.html', account=account, contspace='No user')
    else:
        if 'user' in session:
            return render_template('index.html', account=account, contspace=session['user'])






@app.route("/page")
def showpage():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    picspace = ''
    page = request.args['page']
    aID = page

    session['page'] = page

    style = dressup.getstyle(aID)

    if style == 'resume':
        rows = viewpage.resume(aID)
        if rows['fb'].count('http') == 0:
            rows['fb'] = 'https://' + rows['fb']
        if rows['tweet'].count('http') == 0:
            rows['tweet'] = 'https://' + rows['tweet']
        if rows['lin'].count('http') == 0:
            rows['lin'] = 'https://' + rows['lin']
        if rows['github'].count('http') == 0:
            rows['github'] = 'https://' + rows['github']
        aName =dressup.getaName(aID)

        return render_template('studio/resume.html', aName=aName, fbLink=rows['fb'], tweetLink=rows['tweet'], linLink=rows['lin'], githubLink=rows['github'], fName=rows['fName'], lName=rows['lName'], sAddress=rows['sAddress'], pHone=rows['pHone'], eMail=rows['eMail'], dEscription=rows['dEscription'], tItle1=rows['tItle1'], tItle2=rows['tItle2'], tItle3=rows['tItle3'], tItle4=rows['tItle4'], cOmpany1=rows['cOmpany1'], cOmpany2=rows['cOmpany2'], cOmpany3=rows['cOmpany3'], cOmpany4=rows['cOmpany4'], dEscription1=rows['dEscription1'], dEscription2=rows['dEscription2'], dEscription3=rows['dEscription3'], dEscription4=rows['dEscription4'], exDate1=rows['exDate1'], exDate2=rows['exDate2'], exDate3=rows['exDate3'], exDate4=rows['exDate4'], iNstitution1=rows['iNstitution1'], iNstitution2=rows['iNstitution2'], pRogramme1=rows['pRogramme1'], pRogramme2=rows['pRogramme2'], cOurse1=rows['cOurse1'], cOurse2=rows['cOurse2'], gRade1=rows['gRade1'], gRade2=rows['gRade2'], edDate1=rows['edDate1'], edDate2=rows['edDate2'], sKill1=rows['sKill1'], sKill2=rows['sKill2'], sKill3=rows['sKill3'], sKill4=rows['sKill4'], sKill5=rows['sKill5'], sKill6=rows['sKill6'], iNterest1=rows['iNterest1'], iNterest2=rows['iNterest2'], iNterest3=rows['iNterest3'], iNterest4=rows['iNterest4'], iNterest5=rows['iNterest5'], iNterest6=rows['iNterest6'], aWard1=rows['aWard1'], aWard2=rows['aWard2'], aWard3=rows['aWard3'], aWard4=rows['aWard4'], aImage=rows['aImage'])
    elif style == 'agency':

        try:
            section = request.args['section']
        except:
            try:
                getColors = agencypro.getColors(aID)
                tpMenu=getColors['tpMenu']
                tpLinks=getColors['tpLinks']
                welTo=getColors['welTo']
                sloganC=getColors['sloganC']
                tMoreb=getColors['tMoreb']
                tMoret=getColors['tMoret']
                hdNg=getColors['hdNg']
                sbHdng=getColors['sbHdng']
                titles=getColors['titles']
                nTxt=getColors['nTxt']
            except:
                tpMenu = 'black'
                tpLinks = 'white'
                welTo = 'white'
                sloganC = 'white'
                tMoreb = 'yellow'
                tMoret = 'white'
                hdNg = 'blue'
                sbHdng = 'black'
                titles = 'black'
                nTxt = 'black'
            else:
                getColors = agencypro.getColors(aID)
                tpMenu = getColors['tpMenu']
                tpLinks=getColors['tpLinks']
                welTo=getColors['welTo']
                sloganC=getColors['sloganC']
                tMoreb=getColors['tMoreb']
                tMoret=getColors['tMoret']
                hdNg=getColors['hdNg']
                sbHdng=getColors['sbHdng']
                titles=getColors['titles']
                nTxt=getColors['nTxt']
            aID=request.args['page']
            portstat=agencypro.getOthers(aID)['portstat']
            milestat=agencypro.getOthers(aID)['milestat']
            teamstat=agencypro.getOthers(aID)['teamstat']
            lastword = agencypro.getOthers(aID)['lastword']
            homeCont = agencypro.getHome(aID,tpMenu,tpLinks,welTo,sloganC,tMoreb,tMoret,hdNg,sbHdng,titles,nTxt,portstat,milestat,teamstat,lastword)
            #ln= Markup(homeCont['contacts']['ln'])
            fb= Markup(homeCont['contacts']['fb'])
            about = Markup(homeCont['contacts']['about'])
            abouts = homeCont['contacts']['about']
            tweet= Markup(homeCont['contacts']['tweet'])
            miles=Markup(homeCont['miles'])
            part = Markup(homeCont['part'])
            terms=''
            msg = Markup('<!-- Contact --> <section id="contact"> <div class="container"> <div class="row"> <div class="col-lg-12 text-center"> <h2 class="section-heading text-uppercase"><font style="color:{}">Contact Us</font></h2> <h3 class="section-subheading text-muted"><font style="color:{}">We&#39;re here for you</font></h3> </div> </div> <div class="row"> <div class="col-lg-12"> <form id="contactForm" name="sentMessage" method="POST" action="http://biasharaemployers.pythonanywhere.com/msgs"> <div class="row"> <div class="col-md-6"> <div class="form-group"> <input class="form-control" name="nmBox" id="name" type="text" placeholder="Your Name *" required data-validation-required-message="Please enter your name."> <p class="help-block text-danger"></p> </div> <div class="form-group"> <input class="form-control" name="emBox" id="email" type="email" placeholder="Your Email *" required data-validation-required-message="Please enter your email address."> <p class="help-block text-danger"></p> </div> <div class="form-group"> <input class="form-control" name="phBox" id="phone" type="tel" placeholder="Your Phone *" required data-validation-required-message="Please enter your phone number."> <p class="help-block text-danger"></p> </div> </div> <div class="col-md-6"> <div class="form-group"> <textarea class="form-control" name="msgBox" id="message" placeholder="Your Message *" required data-validation-required-message="Please enter a message."></textarea> <p class="help-block text-danger"></p> </div> </div><input type="hidden" name="action1" value="sendMsg"><input name="abcd" value="{}" type="hidden"><input type="hidden" name="page" value="{}"> <div class="clearfix"></div> <div class="col-lg-12 text-center"> <div id="success"></div> <button id="sendMessageButton" class="btn btn-primary btn-xl text-uppercase" type="submit">Send Message</button> </div> </div> </form> </div> </div> </div> </section>'.format(hdNg,sbHdng,aID,aID))
            team=Markup(homeCont['team'])
            privacy=''
            portfolio=Markup(homeCont['portfolio'])

            summary=Markup(homeCont['summary'])
            sLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=services')

            abLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=about')
            pLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'#portfolio')
            tLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'#team')
            cLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=contact')
            hLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}'.format(aID)

            slogan=Markup(homeCont['slogan'])
            name=Markup(homeCont['name'])
            logoLink=Markup(homeCont['logoLink'])
            pageImage = Markup(agencypro.getpageImage(aID))

            return render_template('studio/agency/agency.html',pageImage=pageImage,pageDesc=abouts[:194],welTo=welTo,tMoret=tMoret,tMoreb=tMoreb,sloganC=sloganC,tpMenu=tpMenu,tpLinks=tpLinks,hLink=hLink,abLink=abLink,sLink=sLink,pLink=pLink,tLink=tLink,cLink=cLink,msg=msg,part=part,team=team,miles=miles,logoLink=logoLink,name=name,slogan=slogan,summary=summary,portstat=portstat,portfolio=portfolio,privacy=privacy,terms=terms,tweet=tweet,fb=fb)

        else:
            try:
                getColors = agencypro.getColors(aID)
                tpMenu=getColors['tpMenu']
                tpLinks=getColors['tpLinks']
                welTo=getColors['welTo']
                sloganC=getColors['sloganC']
                tMoreb=getColors['tMoreb']
                tMoret=getColors['tMoret']
                hdNg=getColors['hdNg']
                sbHdng=getColors['sbHdng']
                titles=getColors['titles']
                nTxt=getColors['nTxt']
            except:
                tpMenu = ''
                tpLinks = ''
                welTo = ''
                sloganC = ''
                tMoreb = ''
                tMoret = ''
                hdNg = ''
                sbHdng = ''
                titles = ''
                nTxt = ''
            else:
                getColors = agencypro.getColors(aID)
                tpMenu = getColors['tpMenu']
                tpLinks=getColors['tpLinks']
                welTo=getColors['welTo']
                sloganC=getColors['sloganC']
                tMoreb=getColors['tMoreb']
                tMoret=getColors['tMoret']
                hdNg=getColors['hdNg']
                sbHdng=getColors['sbHdng']
                titles=getColors['titles']
                nTxt=getColors['nTxt']
            aID=request.args['page']
            section = request.args['section']
            if section == 'services':
                portstat=agencypro.getOthers(aID)['portstat']
                milestat=agencypro.getOthers(aID)['milestat']
                teamstat=agencypro.getOthers(aID)['teamstat']
                lastword = agencypro.getOthers(aID)['lastword']
                getHome = agencypro.getHome(aID,tpMenu,tpLinks,welTo,sloganC,tMoreb,tMoret,hdNg,sbHdng,titles,nTxt,portstat,milestat,teamstat,lastword)
                name=getHome['name']
                fServices = Markup(agencypro.getfServices(aID))
                services = Markup(agencypro.getServics(aID,titles,nTxt,hdNg,sbHdng))
                summary = Markup(agencypro.getHome(aID,tpMenu,tpLinks,welTo,sloganC,tMoreb,tMoret,hdNg,sbHdng,titles,nTxt,portstat,milestat,teamstat,lastword)['summary'])
                msg = Markup('<!-- Contact --> <section id="contact"> <div class="container"> <div class="row"> <div class="col-lg-12 text-center"> <h2 class="section-heading text-uppercase"><font style="color:{}">Contact Us</font></h2> <h3 class="section-subheading text-muted"><font style="color:{}">We&#39;re here for you</font></h3> </div> </div> <div class="row"> <div class="col-lg-12"> <form id="contactForm" name="sentMessage" method="POST" action="http://biasharaemployers.pythonanywhere.com/msgs"> <div class="row"> <div class="col-md-6"> <div class="form-group"> <input class="form-control" name="nmBox" id="name" type="text" placeholder="Your Name *" required data-validation-required-message="Please enter your name."> <p class="help-block text-danger"></p> </div> <div class="form-group"> <input class="form-control" name="emBox" id="email" type="email" placeholder="Your Email *" required data-validation-required-message="Please enter your email address."> <p class="help-block text-danger"></p> </div> <div class="form-group"> <input class="form-control" name="phBox" id="phone" type="tel" placeholder="Your Phone *" required data-validation-required-message="Please enter your phone number."> <p class="help-block text-danger"></p> </div> </div> <div class="col-md-6"> <div class="form-group"> <textarea class="form-control" name="msgBox" id="message" placeholder="Your Message *" required data-validation-required-message="Please enter a message."></textarea> <p class="help-block text-danger"></p> </div> </div><input type="hidden" name="action1" value="sendMsg"><input name="abcd" value="{}" type="hidden"><input type="hidden" name="page" value="{}"> <div class="clearfix"></div> <div class="col-lg-12 text-center"> <div id="success"></div> <button id="sendMessageButton" class="btn btn-primary btn-xl text-uppercase" type="submit">Send Message</button> </div> </div> </form> </div> </div> </div> </section>'.format(hdNg,sbHdng,aID,aID))
                #ln= Markup(homeCont['contacts']['email'])
                fb= getHome['contacts']['fb']
                about = Markup(getHome['contacts']['about'])
                abouts = getHome['contacts']['about']
                tweet= getHome['contacts']['tweet']
                sLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=services')
                pageImage = Markup(agencypro.getpageImage(aID))
                abLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=about')
                pLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'#portfolio')
                tLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'#team')
                cLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=contact')
                hLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}'.format(aID)
                logoLink = Markup(agencypro.getHome(aID,tpMenu,tpLinks,welTo,sloganC,tMoreb,tMoret,hdNg,sbHdng,titles,nTxt,portstat,milestat,teamstat,lastword)['logoLink'])
                #It's the services page
                return render_template('studio/agency/agency_services.html',pageImage=pageImage,pageDesc=abouts[:194],tpMenu=tpMenu,tpLinks=tpLinks,hLink=hLink,name=name,logoLink=logoLink,abLink=abLink,sLink=sLink,pLink=pLink,tLink=tLink,cLink=cLink,msg=msg,fb=fb,tweet=tweet,summary=summary,fServices=fServices,services=services)
            elif section == 'about':
                #It's the about page
                portstat=agencypro.getOthers(aID)['portstat']
                milestat=agencypro.getOthers(aID)['milestat']
                teamstat=agencypro.getOthers(aID)['teamstat']
                lastword = agencypro.getOthers(aID)['lastword']
                getHome = agencypro.getHome(aID,tpMenu,tpLinks,welTo,sloganC,tMoreb,tMoret,hdNg,sbHdng,titles,nTxt,portstat,milestat,teamstat,lastword)
                tweet= getHome['contacts']['tweet']

                sLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=services')
                msg = Markup('<!-- Contact --> <section id="contact"> <div class="container"> <div class="row"> <div class="col-lg-12 text-center"> <h2 class="section-heading text-uppercase"><font style="color:{}">Contact Us</font></h2> <h3 class="section-subheading text-muted"><font style="color:{}">We&#39;re here for you</font></h3> </div> </div> <div class="row"> <div class="col-lg-12"> <form id="contactForm" name="sentMessage" method="POST" action="http://biasharaemployers.pythonanywhere.com/msgs"> <div class="row"> <div class="col-md-6"> <div class="form-group"> <input class="form-control" name="nmBox" id="name" type="text" placeholder="Your Name *" required data-validation-required-message="Please enter your name."> <p class="help-block text-danger"></p> </div> <div class="form-group"> <input class="form-control" name="emBox" id="email" type="email" placeholder="Your Email *" required data-validation-required-message="Please enter your email address."> <p class="help-block text-danger"></p> </div> <div class="form-group"> <input class="form-control" name="phBox" id="phone" type="tel" placeholder="Your Phone *" required data-validation-required-message="Please enter your phone number."> <p class="help-block text-danger"></p> </div> </div> <div class="col-md-6"> <div class="form-group"> <textarea class="form-control" name="msgBox" id="message" placeholder="Your Message *" required data-validation-required-message="Please enter a message."></textarea> <p class="help-block text-danger"></p> </div> </div><input type="hidden" name="action1" value="sendMsg"><input name="abcd" value="{}" type="hidden"><input type="hidden" name="page" value="{}"> <div class="clearfix"></div> <div class="col-lg-12 text-center"> <div id="success"></div> <button id="sendMessageButton" class="btn btn-primary btn-xl text-uppercase" type="submit">Send Message</button> </div> </div> </form> </div> </div> </div> </section>'.format(hdNg,sbHdng,aID,aID))
                pageImage = Markup(agencypro.getpageImage(aID))
                abLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=about')
                pLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'#portfolio')
                tLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'#team')
                cLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=contact')
                hLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}'.format(aID)
                fb= getHome['contacts']['fb']
                logoLink = getHome['logoLink']
                name=getHome['name']
                contacts = dressup.getContact(aID)
                about=contacts['about']
                about = Markup('<section id="about"> <div class="container"> <div class="row"> <div class="col-lg-8 mx-auto"> <h2><font style="color:{}">About {}</font></h2> <p class="lead">{}</p> </div> </div> </div> </section>'.format(hdNg,name,about))
                city=Markup(contacts['city'])
                country=Markup(contacts['country'])
                email=Markup(contacts['email'])
                website=Markup(contacts['website'])
                abouts = getHome['contacts']['about']
                phone=Markup(contacts['phone'])
                paddress=Markup(contacts['pAddress'])
                abImage='<img src="' + contacts['abImage'] + '" class="center" />'
                abImage=Markup(abImage)
                contact = Markup('<section id="contacts"> <div class="container"> <div class="row"> <div class="col-lg-8 mx-auto"> <h2><font style="color:{}">Contact us</font></h2> <p class="lead">{}<br /> {}, {}, {}.<br /> <a href="mailto:{}">{}</a><br /> {}<br /> <a href="tel:{}">{}</a><br /><a href="whatsapp://send?text=I+am+Interested+in+{}&phone={}">Talk via WhatsApp</a></p> </div> </div> </div> </section>'.format(hdNg,name,paddress,city,country,email,email.replace("@", "[at]"),website,phone,phone,name,phone))
                return render_template('studio/agency/agency_services.html',pageImage=abImage,pageDesc=abouts[:194],tpMenu=tpMenu,tpLinks=tpLinks,hLink=hLink,abImage=abImage,contact=contact,about=about,city=city,country=country,email=email,website=website,phone=phone,paddress=paddress,name=name,logoLink=logoLink,sLink=sLink,pLink=pLink,tLink=tLink,cLink=cLink,msg=msg,fb=fb,tweet=tweet,)
            elif section == 'team':
                #It's the team page
                return render_template('agency_services.html')
            elif section == 'contact':
                portstat=agencypro.getOthers(aID)['portstat']
                milestat=agencypro.getOthers(aID)['milestat']
                teamstat=agencypro.getOthers(aID)['teamstat']
                lastword = agencypro.getOthers(aID)['lastword']
                getHome = agencypro.getHome(aID,tpMenu,tpLinks,welTo,sloganC,tMoreb,tMoret,hdNg,sbHdng,titles,nTxt,portstat,milestat,teamstat,lastword)
                tweet= getHome['contacts']['tweet']
                about = Markup(getHome['contacts']['about'])
                abouts = getHome['contacts']['about']
                sLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=services')
                msg = Markup('<!-- Contact --> <section id="contact"> <div class="container"> <div class="row"> <div class="col-lg-12 text-center"> <h2 class="section-heading text-uppercase"><font style="color:{}">Contact Us</font></h2> <h3 class="section-subheading text-muted"><font style="color:{}">We&#39;re here for you</font></h3> </div> </div> <div class="row"> <div class="col-lg-12"> <form id="contactForm" name="sentMessage" method="POST" action="http://biasharaemployers.pythonanywhere.com/msgs"> <div class="row"> <div class="col-md-6"> <div class="form-group"> <input class="form-control" name="nmBox" id="name" type="text" placeholder="Your Name *" required data-validation-required-message="Please enter your name."> <p class="help-block text-danger"></p> </div> <div class="form-group"> <input class="form-control" name="emBox" id="email" type="email" placeholder="Your Email *" required data-validation-required-message="Please enter your email address."> <p class="help-block text-danger"></p> </div> <div class="form-group"> <input class="form-control" name="phBox" id="phone" type="tel" placeholder="Your Phone *" required data-validation-required-message="Please enter your phone number."> <p class="help-block text-danger"></p> </div> </div> <div class="col-md-6"> <div class="form-group"> <textarea class="form-control" name="msgBox" id="message" placeholder="Your Message *" required data-validation-required-message="Please enter a message."></textarea> <p class="help-block text-danger"></p> </div> </div><input type="hidden" name="action1" value="sendMsg"><input name="abcd" value="{}" type="hidden"><input type="hidden" name="page" value="{}"> <div class="clearfix"></div> <div class="col-lg-12 text-center"> <div id="success"></div> <button id="sendMessageButton" class="btn btn-primary btn-xl text-uppercase" type="submit">Send Message</button> </div> </div> </form> </div> </div> </div> </section>'.format(hdNg,sbHdng,aID,aID))
                pageImage = Markup(agencypro.getpageImage(aID))
                abLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=about')
                pLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'#portfolio')
                tLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'#team')
                hLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}'.format(aID)
                cLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=contact')
                fb= getHome['contacts']['fb']
                logoLink = getHome['logoLink']
                name=getHome['name']
                contacts = dressup.getContact(aID)
                #about=contacts['about']
                city=Markup(contacts['city'])
                country=Markup(contacts['country'])
                email=Markup(contacts['email'])
                website=Markup(contacts['website'])
                phone=Markup(contacts['phone'])
                paddress=Markup(contacts['pAddress'])
                contact = Markup('<section id="contacts"> <div class="container"> <div class="row"> <div class="col-lg-8 mx-auto"> <h2><font style="color:{}">Contact us</font></h2> <p class="lead">{}<br /> {}, {}, {}.<br /> <a href="mailto:{}">{}</a><br /> {}<br /> <a href="tel:{}">{}</a><br /><a href="whatsapp://send?text=I+am+Interested+in+{}&phone={}">Talk via WhatsApp</a></p> </div> </div> </div> </section>'.format(hdNg,name,paddress,city,country,email,email.replace("@", "[at]"),website,phone,phone,name,phone))
                return render_template('studio/agency/agency_services.html',pageImage=pageImage,pageDesc=abouts[:194],tpMenu=tpMenu,tpLinks=tpLinks,hLink=hLink,city=city,country=country,email=email,website=website,phone=phone,paddress=paddress,name=name,logoLink=logoLink,sLink=sLink,pLink=pLink,tLink=tLink,abLink=abLink,cLink=cLink,msg=msg,fb=fb,tweet=tweet,contact=contact)



    elif style == 'shop':

        try:
            Idy = session['Fs']['aid']
            firstI = session['Fs']['firstI']
            secondI = session['Fs']['secondI']
            thirdI = session['Fs']['thirdI']
        except:
            getFimages = shopPros.getFimages(aID)
            session['Fs'] = {'aid': getFimages['aid'], 'firstI': getFimages['firstI'], 'secondI': getFimages['secondI'], 'thirdI': getFimages['thirdI']}
            firstI = session['Fs']['firstI']
            secondI = session['Fs']['secondI']
            thirdI = session['Fs']['thirdI']
        else:
            if session['Fs']['aid'] == aID:
                firstI = session['Fs']['firstI']
                secondI = session['Fs']['secondI']
                thirdI = session['Fs']['thirdI']
            else:
                getFimages = shopPros.getFimages(aID)
                session['Fs'] = {'firstI': getFimages['firstI'], 'secondI': getFimages['secondI'], 'thirdI': getFimages['thirdI']}
                firstI = session['Fs']['firstI']
                secondI = session['Fs']['secondI']
                thirdI = session['Fs']['thirdI']

        try:
            section = request.args['section']
        except:
            try:
                product = request.args['product']
            except:

                homecont = shopPros.viewHome(aID)
                #contspace = Markup('<div class="row"> <div class="col-lg-4 col-md-6 mb-4"> <div class="card h-100"> <a href="samples?sample=19"><img class="card-img-top" src="http://placehold.it/700x400" alt=""></a> <div class="card-body"> <h4 class="card-title"> <a href="samples?sample=19">Item One</a> </h4> <h5>$24.99</h5> <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!</p> </div> <div class="card-footer"> <small class="text-muted">&#9733; &#9733; &#9733; &#9733; &#9734;</small> </div> </div> </div> <div class="col-lg-4 col-md-6 mb-4"> <div class="card h-100"> <a href="samples?sample=19"><img class="card-img-top" src="http://placehold.it/700x400" alt=""></a> <div class="card-body"> <h4 class="card-title"> <a href="samples?sample=19">Item Two</a> </h4> <h5>$24.99</h5> <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur! Lorem ipsum dolor sit amet.</p> </div> <div class="card-footer"> <small class="text-muted">&#9733; &#9733; &#9733; &#9733; &#9734;</small> </div> </div> </div> <div class="col-lg-4 col-md-6 mb-4"> <div class="card h-100"> <a href="samples?sample=19"><img class="card-img-top" src="http://placehold.it/700x400" alt=""></a> <div class="card-body"> <h4 class="card-title"> <a href="samples?sample=19">Item Three</a> </h4> <h5>$24.99</h5> <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!</p> </div> <div class="card-footer"> <small class="text-muted">&#9733; &#9733; &#9733; &#9733; &#9734;</small> </div> </div> </div> <div class="col-lg-4 col-md-6 mb-4"> <div class="card h-100"> <a href="samples?sample=19"><img class="card-img-top" src="http://placehold.it/700x400" alt=""></a> <div class="card-body"> <h4 class="card-title"> <a href="samples?sample=19">Item Four</a> </h4> <h5>$24.99</h5> <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!</p> </div> <div class="card-footer"> <small class="text-muted">&#9733; &#9733; &#9733; &#9733; &#9734;</small> </div> </div> </div> <div class="col-lg-4 col-md-6 mb-4"> <div class="card h-100"> <a href="samples?sample=19"><img class="card-img-top" src="http://placehold.it/700x400" alt=""></a> <div class="card-body"> <h4 class="card-title"> <a href="samples?sample=19">Item Five</a> </h4> <h5>$24.99</h5> <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur! Lorem ipsum dolor sit amet.</p> </div> <div class="card-footer"> <small class="text-muted">&#9733; &#9733; &#9733; &#9733; &#9734;</small> </div> </div> </div> <div class="col-lg-4 col-md-6 mb-4"> <div class="card h-100"> <a href="samples?sample=19"><img class="card-img-top" src="http://placehold.it/700x400" alt=""></a> <div class="card-body"> <h4 class="card-title"> <a href="samples?sample=19">Item Six</a> </h4> <h5>$24.99</h5> <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!</p> </div> <div class="card-footer"> <small class="text-muted">&#9733; &#9733; &#9733; &#9733; &#9734;</small> </div> </div> </div> </div>')
                try:
                    aName = Markup(homecont['aName'])
                    contspace=Markup(homecont['contspace'])
                except:
                    aName=Markup(dressup.getaName(aID))
                    contspace='No products created yet'
                    hLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}'.format(aID)
                    cLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}&section={}'.format(aID,'about')
                    getSettings = dressup.getSettings(aID)
                    menubg = getSettings['menubg']
                    textcolor= getSettings['textcolor']
                    desccolor= getSettings['desccolor']
                    pricecolor= getSettings['pricecolor']
                    itemncolor= getSettings['itemncolor']

                    return render_template('studio/shop.html',menubg=menubg,textcolor=textcolor,desccolor=desccolor,itemncolor=itemncolor,pricecolor=pricecolor,hLink=hLink,cLink=cLink, aID=aID, aName=aName, contspace=contspace, firstI=firstI, secondI=secondI, thirdI=thirdI)
                else:
                    aName = Markup(homecont['aName'])
                    contspace=Markup(homecont['contspace'])
                    hLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}'.format(aID)
                    cLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}&section={}'.format(aID,'about')
                    getSettings = dressup.getSettings(aID)
                    menubg = getSettings['menubg']
                    textcolor= getSettings['textcolor']
                    desccolor= getSettings['desccolor']
                    pricecolor= getSettings['pricecolor']
                    itemncolor= getSettings['itemncolor']

                    return render_template('studio/shop.html',menubg=menubg,textcolor=textcolor,desccolor=desccolor,itemncolor=itemncolor,pricecolor=pricecolor,hLink=hLink,cLink=cLink, aID=aID, aName=aName, contspace=contspace, firstI=firstI, secondI=secondI, thirdI=thirdI)
            else:
                pID = request.args['product']
                product = shopPros.getProduct(aID,pID)
                aName = Markup(product['aName'])
                pName = Markup(product['pName'])
                pPrice = Markup(product['pPrice'])
                pDescription = Markup(product['pDescription'])
                pImage = (product['pImage'])
                hLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}'.format(aID)
                cLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}&section={}'.format(aID,'about')
                getSettings = dressup.getSettings(aID)

                menubg = getSettings['menubg']
                textcolor= getSettings['textcolor']
                desccolor= getSettings['desccolor']
                pricecolor= getSettings['pricecolor']
                itemncolor= getSettings['itemncolor']
                wPhone = shopPros.getPhone(aID)


                return render_template('studio/shopitem.html',wPhone=wPhone,pID=pID,menubg=menubg,textcolor=textcolor,desccolor=desccolor,itemncolor=itemncolor,pricecolor=pricecolor,hLink=hLink,cLink=cLink, aID=aID, aName=aName, pName=pName, pPrice=pPrice, pDescription=pDescription, pImage=pImage)
        else:
            section = request.args['section']
            if section == 'about':
                aID = request.args['page']
                aName = Markup(dressup.getaName(aID))
                about = Markup(dressup.getContact(aID)['about'])
                website = Markup(dressup.getContact(aID)['website'])
                phone = Markup(dressup.getContact(aID)['phone'])
                email = Markup(dressup.getContact(aID)['email'])
                paddress = Markup(dressup.getContact(aID)['pAddress'])
                country = Markup(dressup.getContact(aID)['country'])
                city = Markup(dressup.getContact(aID)['city'])
                fbLink = Markup(dressup.getContact(aID)['about'])
                tweetLink = Markup(dressup.getContact(aID)['tweet'])
                linLink = Markup(dressup.getContact(aID)['lin'])
                hLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}'.format(aID)
                cLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}&section={}'.format(aID,'about')
                getSettings = dressup.getSettings(aID)
                menubg = getSettings['menubg']
                textcolor= getSettings['textcolor']
                desccolor= getSettings['desccolor']
                pricecolor= getSettings['pricecolor']
                itemncolor= getSettings['itemncolor']
                return render_template('studio/about.html',menubg=menubg,textcolor=textcolor,desccolor=desccolor,itemncolor=itemncolor,pricecolor=pricecolor,hLink=hLink,cLink=cLink,aName=aName,about=about,website=website,phone=phone,email=email,paddress=paddress,country=country,city=city,fbLink=fbLink, tweetLink=tweetLink, linLink=linLink)
    else:
        contspace = 'Coming soon!'
        return render_template('index.html', account=account, picspace=picspace, contspace=contspace, title='Not there yet')

@app.route("/clients")
def serve():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    picspace = ''
    page = request.args['page']
    aID = page

    session['page'] = page

    style = dressup.getstyle(aID)

    if style == 'resume':
        rows = viewpage.resume(aID)
        if rows['fb'].count('http') == 0:
            rows['fb'] = 'https://' + rows['fb']
        if rows['tweet'].count('http') == 0:
            rows['tweet'] = 'https://' + rows['tweet']
        if rows['lin'].count('http') == 0:
            rows['lin'] = 'https://' + rows['lin']
        if rows['github'].count('http') == 0:
            rows['github'] = 'https://' + rows['github']
        aName =dressup.getaName(aID)

        return render_template('studio/resume.html', aName=aName, fbLink=rows['fb'], tweetLink=rows['tweet'], linLink=rows['lin'], githubLink=rows['github'], fName=rows['fName'], lName=rows['lName'], sAddress=rows['sAddress'], pHone=rows['pHone'], eMail=rows['eMail'], dEscription=rows['dEscription'], tItle1=rows['tItle1'], tItle2=rows['tItle2'], tItle3=rows['tItle3'], tItle4=rows['tItle4'], cOmpany1=rows['cOmpany1'], cOmpany2=rows['cOmpany2'], cOmpany3=rows['cOmpany3'], cOmpany4=rows['cOmpany4'], dEscription1=rows['dEscription1'], dEscription2=rows['dEscription2'], dEscription3=rows['dEscription3'], dEscription4=rows['dEscription4'], exDate1=rows['exDate1'], exDate2=rows['exDate2'], exDate3=rows['exDate3'], exDate4=rows['exDate4'], iNstitution1=rows['iNstitution1'], iNstitution2=rows['iNstitution2'], pRogramme1=rows['pRogramme1'], pRogramme2=rows['pRogramme2'], cOurse1=rows['cOurse1'], cOurse2=rows['cOurse2'], gRade1=rows['gRade1'], gRade2=rows['gRade2'], edDate1=rows['edDate1'], edDate2=rows['edDate2'], sKill1=rows['sKill1'], sKill2=rows['sKill2'], sKill3=rows['sKill3'], sKill4=rows['sKill4'], sKill5=rows['sKill5'], sKill6=rows['sKill6'], iNterest1=rows['iNterest1'], iNterest2=rows['iNterest2'], iNterest3=rows['iNterest3'], iNterest4=rows['iNterest4'], iNterest5=rows['iNterest5'], iNterest6=rows['iNterest6'], aWard1=rows['aWard1'], aWard2=rows['aWard2'], aWard3=rows['aWard3'], aWard4=rows['aWard4'], aImage=rows['aImage'])
    elif style == 'agency':

        try:
            section = request.args['section']
        except:
            try:
                getColors = agencypro.getColors(aID)
                tpMenu=getColors['tpMenu']
                tpLinks=getColors['tpLinks']
                welTo=getColors['welTo']
                sloganC=getColors['sloganC']
                tMoreb=getColors['tMoreb']
                tMoret=getColors['tMoret']
                hdNg=getColors['hdNg']
                sbHdng=getColors['sbHdng']
                titles=getColors['titles']
                nTxt=getColors['nTxt']
            except:
                tpMenu = 'black'
                tpLinks = 'white'
                welTo = 'white'
                sloganC = 'white'
                tMoreb = 'yellow'
                tMoret = 'white'
                hdNg = 'blue'
                sbHdng = 'black'
                titles = 'black'
                nTxt = 'black'
            else:
                getColors = agencypro.getColors(aID)
                tpMenu = getColors['tpMenu']
                tpLinks=getColors['tpLinks']
                welTo=getColors['welTo']
                sloganC=getColors['sloganC']
                tMoreb=getColors['tMoreb']
                tMoret=getColors['tMoret']
                hdNg=getColors['hdNg']
                sbHdng=getColors['sbHdng']
                titles=getColors['titles']
                nTxt=getColors['nTxt']
            aID=request.args['page']
            portstat=agencypro.getOthers(aID)['portstat']
            milestat=agencypro.getOthers(aID)['milestat']
            teamstat=agencypro.getOthers(aID)['teamstat']
            lastword = agencypro.getOthers(aID)['lastword']
            homeCont = agencypro.getHome(aID,tpMenu,tpLinks,welTo,sloganC,tMoreb,tMoret,hdNg,sbHdng,titles,nTxt,portstat,milestat,teamstat,lastword)
            #ln= Markup(homeCont['contacts']['ln'])
            fb= Markup(homeCont['contacts']['fb'])
            about = Markup(homeCont['contacts']['about'])
            abouts = homeCont['contacts']['about']
            tweet= Markup(homeCont['contacts']['tweet'])
            miles=Markup(homeCont['miles'])
            part = Markup(homeCont['part'])
            terms=''
            msg = Markup('<!-- Contact --> <section id="contact"> <div class="container"> <div class="row"> <div class="col-lg-12 text-center"> <h2 class="section-heading text-uppercase"><font style="color:{}">Contact Us</font></h2> <h3 class="section-subheading text-muted"><font style="color:{}">We&#39;re here for you</font></h3> </div> </div> <div class="row"> <div class="col-lg-12"> <form id="contactForm" name="" method="POST" action="../msgs.php"> <div class="row"> <div class="col-md-6"> <div class="form-group"> <input class="form-control" name="nmBox" id="name" type="text" placeholder="Your Name *" required data-validation-required-message="Please enter your name."> <p class="help-block text-danger"></p> </div> <div class="form-group"> <input class="form-control" name="emBox" id="email" type="email" placeholder="Your Email *" required data-validation-required-message="Please enter your email address."> <p class="help-block text-danger"></p> </div> <div class="form-group"> <input class="form-control" name="phBox" id="phone" type="tel" placeholder="Your Phone *" required data-validation-required-message="Please enter your phone number."> <p class="help-block text-danger"></p> </div> </div> <div class="col-md-6"> <div class="form-group"> <textarea class="form-control" name="msgBox" id="message" placeholder="Your Message *" required data-validation-required-message="Please enter a message."></textarea> <p class="help-block text-danger"></p> </div> </div><input type="hidden" name="action1" value="sendMsg"><input name="abcd" value="{}" type="hidden"><input type="hidden" name="page" value="{}"> <div class="clearfix"></div> <div class="col-lg-12 text-center"> <div id="success"></div> <button id="sendMessageButton" class="btn btn-primary btn-xl text-uppercase" type="submit">Send Message</button> </div> </div> </form> </div> </div> </div> </section>'.format(hdNg,sbHdng,aID,aID))
            team=Markup(homeCont['team'])
            privacy=''
            portfolio=Markup(homeCont['portfolio'])
            portstat=''
            summary=Markup(homeCont['summary'])
            #sLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=services')
            sLink = '../services'

            #abLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=about')
            abLink = '../about'

            #pLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'#portfolio')
            pLink = '#portfolio'

            #tLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'#team')

            tLink = '#team'

            #cLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=contact')
            cLink = '../contact'

            #hLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}'.format(aID)
            hLink = '../'

            slogan=Markup(homeCont['slogan'])
            name=Markup(homeCont['name'])
            pageTitle = name
            logoLink=Markup(homeCont['logoLink'])
            pageImage = Markup(agencypro.getpageImage(aID))
            pageDesc = abouts[:194]

            #return agencypro.homepage(pageImage,pageDesc,welTo,tMoret,tMoreb,sloganC,tpMenu,tpLinks,hLink,abLink,sLink,pLink,tLink,cLink,msg,part,team,miles,logoLink,name,slogan,summary,portstat,portfolio,privacy,terms,tweet,fb)

            return render_template('studio/agency/client_agency.html',pageTitle=pageTitle,pageImage=pageImage,pageDesc=abouts[:194],welTo=welTo,tMoret=tMoret,tMoreb=tMoreb,sloganC=sloganC,tpMenu=tpMenu,tpLinks=tpLinks,hLink=hLink,abLink=abLink,sLink=sLink,pLink=pLink,tLink=tLink,cLink=cLink,msg=msg,part=part,team=team,miles=miles,logoLink=logoLink,name=name,slogan=slogan,summary=summary,portstat=portstat,portfolio=portfolio,privacy=privacy,terms=terms,tweet=tweet,fb=fb)

        else:
            try:
                getColors = agencypro.getColors(aID)
                tpMenu=getColors['tpMenu']
                tpLinks=getColors['tpLinks']
                welTo=getColors['welTo']
                sloganC=getColors['sloganC']
                tMoreb=getColors['tMoreb']
                tMoret=getColors['tMoret']
                hdNg=getColors['hdNg']
                sbHdng=getColors['sbHdng']
                titles=getColors['titles']
                nTxt=getColors['nTxt']
            except:
                tpMenu = '#6ec454'
                tpLinks = 'brown'
                welTo = '#6ec454'
                sloganC = 'brown'
                tMoreb = 'purple'
                tMoret = 'pink'
                hdNg = '#6ec454'
                sbHdng = '#bec454'
                titles = '#6ec454'
                nTxt = 'black'
            else:
                getColors = agencypro.getColors(aID)
                tpMenu = getColors['tpMenu']
                tpLinks=getColors['tpLinks']
                welTo=getColors['welTo']
                sloganC=getColors['sloganC']
                tMoreb=getColors['tMoreb']
                tMoret=getColors['tMoret']
                hdNg=getColors['hdNg']
                sbHdng=getColors['sbHdng']
                titles=getColors['titles']
                nTxt=getColors['nTxt']
            aID=request.args['page']
            section = request.args['section']
            if section == 'services':
                portstat=agencypro.getOthers(aID)['portstat']
                milestat=agencypro.getOthers(aID)['milestat']
                teamstat=agencypro.getOthers(aID)['teamstat']
                lastword = agencypro.getOthers(aID)['lastword']
                getHome = agencypro.getHome(aID,tpMenu,tpLinks,welTo,sloganC,tMoreb,tMoret,hdNg,sbHdng,titles,nTxt,portstat,milestat,teamstat,lastword)
                name=getHome['name']
                pageTitle = 'Services - {}'.format(name)
                fServices = Markup(agencypro.getfServices(aID))
                services = Markup(agencypro.getServics(aID,titles,nTxt,hdNg,sbHdng))
                summary = Markup(agencypro.getHome(aID,tpMenu,tpLinks,welTo,sloganC,tMoreb,tMoret,hdNg,sbHdng,titles,nTxt,portstat,milestat,teamstat,lastword)['summary'])
                msg = Markup('<!-- Contact --> <section id="contact"> <div class="container"> <div class="row"> <div class="col-lg-12 text-center"> <h2 class="section-heading text-uppercase"><font style="color:{}">Contact Us</font></h2> <h3 class="section-subheading text-muted"><font style="color:{}">We&#39;re here for you</font></h3> </div> </div> <div class="row"> <div class="col-lg-12"> <form id="contactForm" name="" method="POST" action="../msgs.php"> <div class="row"> <div class="col-md-6"> <div class="form-group"> <input class="form-control" name="nmBox" id="name" type="text" placeholder="Your Name *" required data-validation-required-message="Please enter your name."> <p class="help-block text-danger"></p> </div> <div class="form-group"> <input class="form-control" name="emBox" id="email" type="email" placeholder="Your Email *" required data-validation-required-message="Please enter your email address."> <p class="help-block text-danger"></p> </div> <div class="form-group"> <input class="form-control" name="phBox" id="phone" type="tel" placeholder="Your Phone *" required data-validation-required-message="Please enter your phone number."> <p class="help-block text-danger"></p> </div> </div> <div class="col-md-6"> <div class="form-group"> <textarea class="form-control" name="msgBox" id="message" placeholder="Your Message *" required data-validation-required-message="Please enter a message."></textarea> <p class="help-block text-danger"></p> </div> </div><input type="hidden" name="action1" value="sendMsg"><input name="abcd" value="{}" type="hidden"><input type="hidden" name="page" value="{}"> <div class="clearfix"></div> <div class="col-lg-12 text-center"> <div id="success"></div> <button id="sendMessageButton" class="btn btn-primary btn-xl text-uppercase" type="submit">Send Message</button> </div> </div> </form> </div> </div> </div> </section>'.format(hdNg,sbHdng,aID,aID))
                #ln= Markup(homeCont['contacts']['email'])
                fb= getHome['contacts']['fb']
                about = Markup(getHome['contacts']['about'])
                abouts = getHome['contacts']['about']
                tweet= getHome['contacts']['tweet']
                sLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=services')
                pageImage = Markup(agencypro.getpageImage(aID))
                #abLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=about')
                #pLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'#portfolio')
                #tLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'#team')
                #cLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=contact')
                #hLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}'.format(aID)
                logoLink = Markup(agencypro.getHome(aID,tpMenu,tpLinks,welTo,sloganC,tMoreb,tMoret,hdNg,sbHdng,titles,nTxt,portstat,milestat,teamstat,lastword)['logoLink'])
                #It's the services page

                sLink = '../services'

                #abLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=about')
                abLink = '../about'

                #pLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'#portfolio')
                pLink = '../home#portfolio'

                #tLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'#team')

                tLink = '../home#team'

                #cLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=contact')
                cLink = '../contact'

                #hLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}'.format(aID)
                hLink = '/'


                return render_template('studio/agency/client_agency_services.html',pageTitle=pageTitle,pageImage=pageImage,pageDesc=abouts[:194],tpMenu=tpMenu,tpLinks=tpLinks,hLink=hLink,name=name,logoLink=logoLink,abLink=abLink,sLink=sLink,pLink=pLink,tLink=tLink,cLink=cLink,msg=msg,fb=fb,tweet=tweet,summary=summary,fServices=fServices,services=services)
            elif section == 'about':
                #It's the about page
                portstat=agencypro.getOthers(aID)['portstat']
                milestat=agencypro.getOthers(aID)['milestat']
                teamstat=agencypro.getOthers(aID)['teamstat']
                lastword = agencypro.getOthers(aID)['lastword']
                getHome = agencypro.getHome(aID,tpMenu,tpLinks,welTo,sloganC,tMoreb,tMoret,hdNg,sbHdng,titles,nTxt,portstat,milestat,teamstat,lastword)
                tweet= getHome['contacts']['tweet']

                sLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=services')
                msg = Markup('<!-- Contact --> <section id="contact"> <div class="container"> <div class="row"> <div class="col-lg-12 text-center"> <h2 class="section-heading text-uppercase"><font style="color:{}">Contact Us</font></h2> <h3 class="section-subheading text-muted"><font style="color:{}">We&#39;re here for you</font></h3> </div> </div> <div class="row"> <div class="col-lg-12"> <form id="contactForm" name="" method="POST" action="../msgs.php"> <div class="row"> <div class="col-md-6"> <div class="form-group"> <input class="form-control" name="nmBox" id="name" type="text" placeholder="Your Name *" required data-validation-required-message="Please enter your name."> <p class="help-block text-danger"></p> </div> <div class="form-group"> <input class="form-control" name="emBox" id="email" type="email" placeholder="Your Email *" required data-validation-required-message="Please enter your email address."> <p class="help-block text-danger"></p> </div> <div class="form-group"> <input class="form-control" name="phBox" id="phone" type="tel" placeholder="Your Phone *" required data-validation-required-message="Please enter your phone number."> <p class="help-block text-danger"></p> </div> </div> <div class="col-md-6"> <div class="form-group"> <textarea class="form-control" name="msgBox" id="message" placeholder="Your Message *" required data-validation-required-message="Please enter a message."></textarea> <p class="help-block text-danger"></p> </div> </div><input type="hidden" name="action1" value="sendMsg"><input name="abcd" value="{}" type="hidden"><input type="hidden" name="page" value="{}"> <div class="clearfix"></div> <div class="col-lg-12 text-center"> <div id="success"></div> <button id="sendMessageButton" class="btn btn-primary btn-xl text-uppercase" type="submit">Send Message</button> </div> </div> </form> </div> </div> </div> </section>'.format(hdNg,sbHdng,aID,aID))
                pageImage = Markup(agencypro.getpageImage(aID))
                #abLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=about')
                #pLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'#portfolio')
                #tLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'#team')
                #cLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=contact')
                #hLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}'.format(aID)

                sLink = '../services'

                #abLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=about')
                abLink = '../about'

                #pLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'#portfolio')
                pLink = '../home#portfolio'

                #tLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'#team')

                tLink = '../home#team'

                #cLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=contact')
                cLink = '../contact'

                #hLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}'.format(aID)
                hLink = '../'


                fb= getHome['contacts']['fb']
                logoLink = getHome['logoLink']
                name=getHome['name']
                pageTitle = 'About us - {}'.format(name)
                contacts = dressup.getContact(aID)
                about=contacts['about']
                about = Markup('<section id="about"> <div class="container"> <div class="row"> <div class="col-lg-8 mx-auto"> <h2><font style="color:{}">About {}</font></h2> <p class="lead">{}</p> </div> </div> </div> </section>'.format(titles,name,about))
                city=Markup(contacts['city'])
                country=Markup(contacts['country'])
                email=Markup(contacts['email'])
                website=Markup(contacts['website'])
                abouts = getHome['contacts']['about']
                phone=Markup(contacts['phone'])
                paddress=Markup(contacts['pAddress'])
                abImage='<img src="' + contacts['abImage'] + '" class="center" />'
                abImage=Markup(abImage)
                contact = Markup('<section id="contacts"> <div class="container"> <div class="row"> <div class="col-lg-8 mx-auto"> <h2><font style="color:{}">Contact us</font></h2> <p class="lead">{}<br /> {}, {}, {}.<br /> <a href="mailto:{}">{}</a><br /> {}<br /> <a href="tel:{}">{}</a><br /><a href="whatsapp://send?text=I+am+Interested+in+{}&phone={}">Talk via WhatsApp</a></p> </div> </div> </div> </section>'.format(hdNg,name,paddress,city,country,email,email,website,phone,phone,name,phone))
                return render_template('studio/agency/client_agency_services.html',pageTitle=pageTitle,pageImage=pageImage,pageDesc=abouts[:194],tpMenu=tpMenu,tpLinks=tpLinks,hLink=hLink,abImage=abImage,contact=contact,about=about,city=city,country=country,email=email,website=website,phone=phone,paddress=paddress,name=name,logoLink=logoLink,sLink=sLink,pLink=pLink,tLink=tLink,cLink=cLink,msg=msg,fb=fb,tweet=tweet,)
            elif section == 'team':
                #It's the team page
                return render_template('agency_services.html')
            elif section == 'contact':
                portstat=agencypro.getOthers(aID)['portstat']
                milestat=agencypro.getOthers(aID)['milestat']
                teamstat=agencypro.getOthers(aID)['teamstat']
                lastword = agencypro.getOthers(aID)['lastword']
                getHome = agencypro.getHome(aID,tpMenu,tpLinks,welTo,sloganC,tMoreb,tMoret,hdNg,sbHdng,titles,nTxt,portstat,milestat,teamstat,lastword)
                tweet= getHome['contacts']['tweet']
                about = Markup(getHome['contacts']['about'])
                abouts = getHome['contacts']['about']
                #sLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=services')
                msg = Markup('<!-- Contact --> <section id="contact"> <div class="container"> <div class="row"> <div class="col-lg-12 text-center"> <h2 class="section-heading text-uppercase"><font style="color:{}">Contact Us</font></h2> <h3 class="section-subheading text-muted"><font style="color:{}">We&#39;re here for you</font></h3> </div> </div> <div class="row"> <div class="col-lg-12"> <form id="contactForm" name="" method="POST" action="../msgs.php"> <div class="row"> <div class="col-md-6"> <div class="form-group"> <input class="form-control" name="nmBox" id="name" type="text" placeholder="Your Name *" required data-validation-required-message="Please enter your name."> <p class="help-block text-danger"></p> </div> <div class="form-group"> <input class="form-control" name="emBox" id="email" type="email" placeholder="Your Email *" required data-validation-required-message="Please enter your email address."> <p class="help-block text-danger"></p> </div> <div class="form-group"> <input class="form-control" name="phBox" id="phone" type="tel" placeholder="Your Phone *" required data-validation-required-message="Please enter your phone number."> <p class="help-block text-danger"></p> </div> </div> <div class="col-md-6"> <div class="form-group"> <textarea class="form-control" name="msgBox" id="message" placeholder="Your Message *" required data-validation-required-message="Please enter a message."></textarea> <p class="help-block text-danger"></p> </div> </div><input type="hidden" name="action1" value="sendMsg"><input name="abcd" value="{}" type="hidden"><input type="hidden" name="page" value="{}"> <div class="clearfix"></div> <div class="col-lg-12 text-center"> <div id="success"></div> <button id="sendMessageButton" class="btn btn-primary btn-xl text-uppercase" type="submit">Send Message</button> </div> </div> </form> </div> </div> </div> </section>'.format(hdNg,sbHdng,aID,aID))
                pageImage = Markup(agencypro.getpageImage(aID))

                #abLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=about')
                #pLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'#portfolio')
                #tLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'#team')
                #hLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}'.format(aID)
                #cLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=contact')

                sLink = '../services'

                #abLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=about')
                abLink = '../about'

                #pLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'#portfolio')
                pLink = '../home#portfolio'

                #tLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'#team')

                tLink = '../home#team'

                #cLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}{}'.format(aID,'&section=contact')
                cLink = '../contact'

                #hLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}'.format(aID)
                hLink = '../'


                fb= getHome['contacts']['fb']
                logoLink = getHome['logoLink']
                name=getHome['name']
                pageTitle = 'Contact us - {}'.format(name)
                contacts = dressup.getContact(aID)
                #about=contacts['about']
                city=Markup(contacts['city'])
                country=Markup(contacts['country'])
                email=Markup(contacts['email'])
                website=Markup(contacts['website'])
                phone=Markup(contacts['phone'])
                paddress=Markup(contacts['pAddress'])
                contact = Markup('<section id="contacts"> <div class="container"> <div class="row"> <div class="col-lg-8 mx-auto"> <h2><font style="color:{}">Contact us</font></h2> <p class="lead">{}<br /> {}, {}, {}.<br /> <a href="mailto:{}">{}</a><br /> {}<br /> <a href="tel:{}">{}</a><br /><a href="whatsapp://send?text=I+am+Interested+in+{}&phone={}">Talk via WhatsApp</a></p> </div> </div> </div> </section>'.format(hdNg,name,paddress,city,country,email,email,website,phone,phone,name,phone))
                return render_template('studio/agency/client_agency_services.html',pageTitle=pageTitle,pageImage=pageImage,pageDesc=abouts[:194],tpMenu=tpMenu,tpLinks=tpLinks,hLink=hLink,city=city,country=country,email=email,website=website,phone=phone,paddress=paddress,name=name,logoLink=logoLink,sLink=sLink,pLink=pLink,tLink=tLink,abLink=abLink,cLink=cLink,msg=msg,fb=fb,tweet=tweet,contact=contact)



    elif style == 'shop':

        try:
            Idy = session['Fs']['aid']
            firstI = session['Fs']['firstI']
            secondI = session['Fs']['secondI']
            thirdI = session['Fs']['thirdI']
        except:
            getFimages = shopPros.getFimages(aID)
            session['Fs'] = {'aid': getFimages['aid'], 'firstI': getFimages['firstI'], 'secondI': getFimages['secondI'], 'thirdI': getFimages['thirdI']}
            firstI = session['Fs']['firstI']
            secondI = session['Fs']['secondI']
            thirdI = session['Fs']['thirdI']
        else:
            if session['Fs']['aid'] == aID:
                firstI = session['Fs']['firstI']
                secondI = session['Fs']['secondI']
                thirdI = session['Fs']['thirdI']
            else:
                getFimages = shopPros.getFimages(aID)
                session['Fs'] = {'firstI': getFimages['firstI'], 'secondI': getFimages['secondI'], 'thirdI': getFimages['thirdI']}
                firstI = session['Fs']['firstI']
                secondI = session['Fs']['secondI']
                thirdI = session['Fs']['thirdI']

        try:
            section = request.args['section']
        except:
            try:
                product = request.args['product']
            except:

                homecont = shopPros.viewHome(aID)
                #contspace = Markup('<div class="row"> <div class="col-lg-4 col-md-6 mb-4"> <div class="card h-100"> <a href="samples?sample=19"><img class="card-img-top" src="http://placehold.it/700x400" alt=""></a> <div class="card-body"> <h4 class="card-title"> <a href="samples?sample=19">Item One</a> </h4> <h5>$24.99</h5> <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!</p> </div> <div class="card-footer"> <small class="text-muted">&#9733; &#9733; &#9733; &#9733; &#9734;</small> </div> </div> </div> <div class="col-lg-4 col-md-6 mb-4"> <div class="card h-100"> <a href="samples?sample=19"><img class="card-img-top" src="http://placehold.it/700x400" alt=""></a> <div class="card-body"> <h4 class="card-title"> <a href="samples?sample=19">Item Two</a> </h4> <h5>$24.99</h5> <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur! Lorem ipsum dolor sit amet.</p> </div> <div class="card-footer"> <small class="text-muted">&#9733; &#9733; &#9733; &#9733; &#9734;</small> </div> </div> </div> <div class="col-lg-4 col-md-6 mb-4"> <div class="card h-100"> <a href="samples?sample=19"><img class="card-img-top" src="http://placehold.it/700x400" alt=""></a> <div class="card-body"> <h4 class="card-title"> <a href="samples?sample=19">Item Three</a> </h4> <h5>$24.99</h5> <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!</p> </div> <div class="card-footer"> <small class="text-muted">&#9733; &#9733; &#9733; &#9733; &#9734;</small> </div> </div> </div> <div class="col-lg-4 col-md-6 mb-4"> <div class="card h-100"> <a href="samples?sample=19"><img class="card-img-top" src="http://placehold.it/700x400" alt=""></a> <div class="card-body"> <h4 class="card-title"> <a href="samples?sample=19">Item Four</a> </h4> <h5>$24.99</h5> <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!</p> </div> <div class="card-footer"> <small class="text-muted">&#9733; &#9733; &#9733; &#9733; &#9734;</small> </div> </div> </div> <div class="col-lg-4 col-md-6 mb-4"> <div class="card h-100"> <a href="samples?sample=19"><img class="card-img-top" src="http://placehold.it/700x400" alt=""></a> <div class="card-body"> <h4 class="card-title"> <a href="samples?sample=19">Item Five</a> </h4> <h5>$24.99</h5> <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur! Lorem ipsum dolor sit amet.</p> </div> <div class="card-footer"> <small class="text-muted">&#9733; &#9733; &#9733; &#9733; &#9734;</small> </div> </div> </div> <div class="col-lg-4 col-md-6 mb-4"> <div class="card h-100"> <a href="samples?sample=19"><img class="card-img-top" src="http://placehold.it/700x400" alt=""></a> <div class="card-body"> <h4 class="card-title"> <a href="samples?sample=19">Item Six</a> </h4> <h5>$24.99</h5> <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!</p> </div> <div class="card-footer"> <small class="text-muted">&#9733; &#9733; &#9733; &#9733; &#9734;</small> </div> </div> </div> </div>')
                try:
                    aName = Markup(homecont['aName'])
                    contspace=Markup(homecont['contspace'])
                except:
                    aName=Markup(dressup.getaName(aID))
                    contspace='No products created yet'
                    hLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}'.format(aID)
                    cLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}&section={}'.format(aID,'about')
                    getSettings = dressup.getSettings(aID)
                    menubg = getSettings['menubg']
                    textcolor= getSettings['textcolor']
                    desccolor= getSettings['desccolor']
                    pricecolor= getSettings['pricecolor']
                    itemncolor= getSettings['itemncolor']

                    return render_template('studio/shop.html',menubg=menubg,textcolor=textcolor,desccolor=desccolor,itemncolor=itemncolor,pricecolor=pricecolor,hLink=hLink,cLink=cLink, aID=aID, aName=aName, contspace=contspace, firstI=firstI, secondI=secondI, thirdI=thirdI)
                else:
                    aName = Markup(homecont['aName'])
                    contspace=Markup(homecont['contspace'])
                    hLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}'.format(aID)
                    cLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}&section={}'.format(aID,'about')
                    getSettings = dressup.getSettings(aID)
                    menubg = getSettings['menubg']
                    textcolor= getSettings['textcolor']
                    desccolor= getSettings['desccolor']
                    pricecolor= getSettings['pricecolor']
                    itemncolor= getSettings['itemncolor']

                    return render_template('studio/shop.html',menubg=menubg,textcolor=textcolor,desccolor=desccolor,itemncolor=itemncolor,pricecolor=pricecolor,hLink=hLink,cLink=cLink, aID=aID, aName=aName, contspace=contspace, firstI=firstI, secondI=secondI, thirdI=thirdI)
            else:
                pID = request.args['product']
                product = shopPros.getProduct(aID,pID)
                aName = Markup(product['aName'])
                pName = Markup(product['pName'])
                pPrice = Markup(product['pPrice'])
                pDescription = Markup(product['pDescription'])
                pImage = (product['pImage'])
                hLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}'.format(aID)
                cLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}&section={}'.format(aID,'about')
                getSettings = dressup.getSettings(aID)

                menubg = getSettings['menubg']
                textcolor= getSettings['textcolor']
                desccolor= getSettings['desccolor']
                pricecolor= getSettings['pricecolor']
                itemncolor= getSettings['itemncolor']
                wPhone = shopPros.getPhone(aID)


                return render_template('studio/shopitem.html',wPhone=wPhone,pID=pID,menubg=menubg,textcolor=textcolor,desccolor=desccolor,itemncolor=itemncolor,pricecolor=pricecolor,hLink=hLink,cLink=cLink, aID=aID, aName=aName, pName=pName, pPrice=pPrice, pDescription=pDescription, pImage=pImage)
        else:
            section = request.args['section']
            if section == 'about':
                aID = request.args['page']
                aName = Markup(dressup.getaName(aID))
                about = Markup(dressup.getContact(aID)['about'])
                website = Markup(dressup.getContact(aID)['website'])
                phone = Markup(dressup.getContact(aID)['phone'])
                email = Markup(dressup.getContact(aID)['email'])
                paddress = Markup(dressup.getContact(aID)['pAddress'])
                country = Markup(dressup.getContact(aID)['country'])
                city = Markup(dressup.getContact(aID)['city'])
                fbLink = Markup(dressup.getContact(aID)['about'])
                tweetLink = Markup(dressup.getContact(aID)['tweet'])
                linLink = Markup(dressup.getContact(aID)['lin'])
                hLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}'.format(aID)
                cLink = 'http://biasharaemployers.pythonanywhere.com/page?page={}&section={}'.format(aID,'about')
                getSettings = dressup.getSettings(aID)
                menubg = getSettings['menubg']
                textcolor= getSettings['textcolor']
                desccolor= getSettings['desccolor']
                pricecolor= getSettings['pricecolor']
                itemncolor= getSettings['itemncolor']
                return render_template('studio/about.html',menubg=menubg,textcolor=textcolor,desccolor=desccolor,itemncolor=itemncolor,pricecolor=pricecolor,hLink=hLink,cLink=cLink,aName=aName,about=about,website=website,phone=phone,email=email,paddress=paddress,country=country,city=city,fbLink=fbLink, tweetLink=tweetLink, linLink=linLink)
    else:
        contspace = 'Coming soon!'
        return render_template('index.html', account=account, picspace=picspace, contspace=contspace, title='Not there yet')




@app.route("/agency")
def agent():

    return render_template('studio/agency.html')

@app.route("/dashboard")
def dash():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    title='Dashboard'
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        picspace = ''
        return redirect(url_for('sign_in'))
    else:
        if g.user and g.password:
            uName = g.user
            uPass = g.password
            checklogin = dressup.checklogin(uName,uPass)


            if checklogin == 'good':
                contspace = Markup('by <a href="/">Biashara Employers</a><br /><br />Tips<br /><ol><li>To apply paragraphs when typing, use &lt;br&gt</li><li>When you want to make your website appear under a domain name like www.something.com , <a href="contact">let us know</a></li></ol>')
                return render_template('dashboard.html', uName=g.user, header='Welcome to Dashboard', contspace=contspace)
            elif checklogin == 'bad':
                picspace = ''
                title = 'Not logged in'
                return render_template('index.html', account=account, title=title, picspace=picspace, contspace='You must be logged in to view the dashboard')

@app.route("/dashboard-createwebsite")
def dashcreate():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    title='Create website'
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        picspace = ''
        return redirect(url_for('sign_in'))
    else:
        if g.user and g.password:
            uName = g.user
            uPass = g.password
            checklogin = dressup.checklogin(uName,uPass)


            if checklogin == 'good':
                contspace = Markup('<form action="dashboard-editpage" method="POST"><table> <tr><td><h3 class="h3s">System</h3></td><td style="padding:10px;"><a href="http://bizbiz.pythonanywhere.com/find"><img src="static/sampone.png" class="imgs" /></a></td></tr> <tr><td><h3 class="h3s"><input type="radio" name="styles" value="resume">Resume</h3></td><td style="padding:10px;"><a href="samples?sample=1"><img src="static/samples/rsm.png" /></a></td></tr> <tr><td><h3 class="h3s"><input type="radio" name="styles" value="shop">Shop</h3></td><td style="padding:10px;"><a href="samples?sample=18"><img src="static/samples/shop.png" /></a></td></tr><tr><td><h3 class="h3s"><input type="radio" name="styles" value="agency">Agency</h3></td><td style="padding:10px;"><a href="samples?sample=2"><img src="static/samples/agency.png" /></a></td></tr> <tr><td><h3 class="h3s"><input disabled type="radio" name="styles" value="freelancer">Freelancer</h3></td><td style="padding:10px;"><a href="samples?sample=3"><img src="static/samples/freelance.png" /></a></td></tr> <tr><td><h3 class="h3s"><input disabled type="radio" name="styles" value="landingpage">Landing page</h3></td><td style="padding:10px;"><a href="samples?sample=4"><img src="static/samples/landing.png" /></a></td></tr> <tr><td><h3 class="h3s"><input disabled type="radio" name="styles" value="grayscale">Grayscale</h3></td><td style="padding:10px;"><a href="samples?sample=5"><img src="static/samples/grayscale.png" /></a></td></tr> <tr><td><h3 class="h3s"><input disabled type="radio" name="styles" value="casual">Casual</h3></td><td style="padding:10px;"><a href="samples?sample=6-home"><img src="static/samples/casual.png" /></a></td></tr> <tr><td><h3 class="h3s"><input disabled type="radio" name="styles" value="onepagewonder">One page</h3></td><td style="padding:10px;"><a href="samples?sample=7"><img src="static/samples/onepage.png" /></a></td></tr> <tr><td><h3 class="h3s"><input disabled type="radio" name="styles" value="frontpage">Frontpage website</h3></td><td style="padding:10px;"><a href="samples?sample=8"><img src="static/samples/frontpage.png" /></a></td></tr> <tr><td><h3 class="h3s"><input disabled type="radio" name="styles" value="blog">Blog</h3></td><td style="padding:10px;"><a href="samples?sample=9"><img src="static/samples/blogsite.png" /></a></td></tr> <tr><td><h3 class="h3s"><input disabled type="radio" name="styles" value="modernbusiness">Modern business</h3></td><td style="padding:10px;"><a href="samples?sample=20"><img src="static/samples/modern.png" /></a></td></tr>  </table><table style="position: fixed; bottom: 300px; right: 100px;"> <tr><td><h4>Tips</h4><ol><li>Click on a style to see previw</li><li>Select using the button on the left then</li><li>Some styles are under construction(disabled)</li><li>When done, click confirm & continue</li></ol></td></tr> <tr><td><button style="background-color: #167BB3;color: white;cursor: pointer;font-family: Arial, Helvetica, sans-serif;font-size:16px" type="submit">CONFIRM & CONTINUE</button></td></tr> </table> </form>')
                return render_template('dashboard.html', uName=g.user, header='Create website', contspace=contspace)
            elif checklogin == 'bad':
                picspace = ''
                title = 'Not logged in'
                return render_template('index.html', account=account, title=title, picspace=picspace, contspace='You login details could not be found. Try signing in again')
@app.route("/dashboard-editpage", methods=['GET', 'POST'])
def dashedit():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        picspace = ''
        return redirect(url_for('sign_in'))
    else:
        if g.user and g.password:
            uName = g.user
            uPass = g.password
            checklogin = dressup.checklogin(uName,uPass)


            if checklogin == 'good':
                picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')
                title = 'Biashara editor'
                if request.method == "GET":
                    return redirect(url_for('dashcreate'))
                elif request.method == "POST":

                    style = request.form['styles']
                    if style == 'resume':
                        contspace = templates.form(style)
                        return render_template('dashboard.html', contspace=contspace, title=title, uName=g.user, header='Create resume website')
                    if style == 'agency':

                        try:
                            pageAction = request.form['action1']
                        except:
                            #contspace = Markup(templates.form(style))
                            #return render_template('dashboard.html', contspace=contspace, uName=g.user, header='Create a new agency website', title=title)
                            #return render_template('studio/agency.html')
                            contspace = Markup('<form method="POST" action=""><p><input type="hidden" name="styles" value="agency"><input type="hidden" name="action1" value="saveNEW"><label>Agency name: </label><input type="TEXT" name="aName"><button type="submit">SAVE</button></form>')
                            return render_template('dashboard.html', contspace=contspace, uName=g.user, header='Create a new agency website', title=title)
                        else:
                            pageAction = request.form['action1']
                            if pageAction == 'newAgency':
                                aName=request.form['aName'].replace("'", "&#39;")
                                slogan=request.form['slogan'].replace("'", "&#39;")
                                mainphrase=request.form['mainphrase'].replace("'", "&#39;")
                                subphrase=request.form['subphrase'].replace("'", "&#39;")
                                value1=request.form['value1'].replace("'", "&#39;")
                                value2=request.form['value2'].replace("'", "&#39;")
                                value3=request.form['value3'].replace("'", "&#39;")
                                value1des=request.form['value1des'].replace("'", "&#39;")
                                value2des=request.form['value2des'].replace("'", "&#39;")
                                value3des=request.form['value3des'].replace("'", "&#39;")
                                portstat=request.form['portstat'].replace("'", "&#39;")
                                aboutstat=request.form['aboutstat'].replace("'", "&#39;")
                                mem1date=request.form['mem1date'].replace("'", "&#39;")
                                mem1title=request.form['mem1title'].replace("'", "&#39;")
                                mem1des=request.form['mem1des'].replace("'", "&#39;")
                                mem2date=request.form['mem2date'].replace("'", "&#39;")
                                mem2title=request.form['mem2title'].replace("'", "&#39;")
                                mem2des=request.form['mem2des'].replace("'", "&#39;")
                                mem3date=request.form['mem3date'].replace("'", "&#39;")
                                mem3title=request.form['mem3title'].replace("'", "&#39;")
                                mem3des=request.form['mem3des'].replace("'", "&#39;")
                                mem4date=request.form['mem4date'].replace("'", "&#39;")
                                mem4title=request.form['mem4title'].replace("'", "&#39;")
                                mem4des=request.form['mem4des'].replace("'", "&#39;")
                                teamstat=request.form['teamstat'].replace("'", "&#39;")
                                statement=request.form['statement'].replace("'", "&#39;")
                                contstat=request.form['contstat'].replace("'", "&#39;")
                                copystat=request.form['copystat'].replace("'", "&#39;")

                                contspace = agencypro.newAgency(aName,slogan,mainphrase,subphrase,value1,value2,value3,value1des,value2des,value3des,portstat,aboutstat,mem1date,mem1title,mem1des,mem2date,mem2title,mem2des,mem3date,mem3title,mem3des,mem4date,mem4title,mem4des,teamstat,statement,contstat,copystat)
                                return render_template('dashboard.html', contspace=contspace, uName=g.user, header='Create a new agency website', title=title)
                            elif pageAction=='NEWWEB':
                                contspace = Markup('<form method="POST" action=""><p><input type="hidden" name="styles" value="agency"><input type="hidden" name="action1" value="saveNEW"><label>Agency name: </label><input type="TEXT" name="aName"><button type="submit">SAVE</button></form>')
                                return render_template('dashboard.html', contspace=contspace, title=title, uName=g.user, header='Create a new Agency website')
                            elif pageAction=='saveNEW':
                                style='agency'
                                aName=request.form['aName'].replace("'", "&#39;")
                                uID = session['uid']
                                contspace =Markup(agencypro.saveNEW(aName,style,uID))

                                return render_template('dashboard.html', contspace=contspace, title=title, uName=g.user, header='Create a new Agency website')
                        return render_template('dashboard.html', contspace=contspace, title=title, uName=g.user, header='Create Agency website')
                    if style == 'shop':
                        try:
                            pageAction = request.form['action1']
                        except:
                            contspace = templates.form(style)
                            return render_template('dashboard.html', contspace=contspace, title=title, uName=g.user, header='Create shop website')
                        else:
                            pageAction = request.form['action1']
                            if pageAction == 'addShop':
                                uID = session['uid']
                                aName = request.form['aName'].replace("'","&#39;")
                                contspace=Markup(shopPros.addShop(uID,style,aName))
                                #contspace='successful'
                                #if contspace == 'done':
                                    #return redirect(url_for('dashmodify'))
                                return render_template('dashboard.html', contspace=contspace, title=title, uName=g.user, header='Add shop')
                            elif pageAction == "addProductform":
                                #contspace = shopPros.addProduct(aID,pName,pPrice,pDescription,pCategory,pSubcategory,pImage)
                                contspace = Markup(""" <form method="POST" action="dashboard"><input type="hidden" name="action1" value="addProduct"><input type="hidden" name="styles" value="shop"><label>Product Name: </label><input type="TEXT" name="pname"> <br /><label>Product price: </label><input type="TEXT" name="pprice"><br /><label>Description: </label><input type="TEXT" name="pdescription"><br /><label>Category: </label><input type="TEXT" name="pcategory"><br /><label>Subcategory: </label><input type="TEXT" name="psubcategory"><label>Image(link): </label><input type="file" name="pImage" accept="image/*"><button type="submit">SEND</button> <button type="RESET">CLEAR FORM</button></form> """)
                                return render_template('dashboard.html', title=title, header='Add a product', uName=g.user, contspace=contspace)
                            elif pageAction == "uPdate":
                                contspace = Markup(""" <form method="POST" action=""><input type="hidden" name="action1" value="updateProduct"><input type="hidden" name="styles" value="shop"><label>Product Name: </label><input type="TEXT" name="pname"> <br /><label>Product price: </label><input type="TEXT" name="pprice"><br /><label>Description: </label><input type="TEXT" name="pdescription"><br /><label>Category: </label><input type="TEXT" name="pcategory"><br /><label>Subcategory: </label><input type="TEXT" name="psubcategory"><button type="submit">SEND</button> <button type="RESET">CLEAR FORM</button></form> """)
                                return render_template('dashboard.html', title=title, header='Update a product', uName=g.user, contspace=contspace)
                            elif pageAction == "dElete":
                                contspace = Markup('<form method="POST" action=""><input type="hidden" name="action1" value="deleteProduct"><input type="hidden" name="styles" value="shop"><p><label>Select product: <select name="product"><option value="##">Product1</option><option value="##">Product2</option></p>')
                                return render_template('dashboard.html', title=title, header='Delete a product', uName=g.user, contspace=contspace)
                            elif pageAction == "sEttings":
                                contspace = Markup('Settings go here')
                                return render_template('dashboard.html', title=title, header='Add a product', uName=g.user, contspace=contspace)
                            elif pageAction == "addProduct":
                                aID = session['edit']
                                pName = request.form['pname'].replace("'", "&#39;")
                                pPrice = request.form['pprice'].replace("'", "&#39;")
                                pDescription = request.form['pdescription'].replace("'", "&#39;")
                                pCategory = request.form['pcategory'].replace("'", "&#39;")
                                pSubcategory = request.form['psubcategory'].replace("'", "&#39;")
                                pImage = request.form['pImage']
                                contspace = shopPros.addproduct(aID,pName,pPrice,pDescription,pCategory,pSubcategory,pImage)

                                return render_template('dashboard.html', contspace=contspace, title=title, uName=g.user, header='Create website')
            elif checklogin == 'bad':
                picspace = ''
                title = 'Not logged in'
                return render_template('index.html', account=account, title=title, picspace=picspace, contspace='Your login details could not be found. Try signing in again')

@app.route("/dashboard-editpage-shop", methods=['GET', 'POST'])
def dasheditshop():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    title='Edit shop'
    if request.method == "POST":
        pageAction = request.form['action1']
        g.user = session['user']
        g.password = session['password']
        #g.edit = session['edit']

        if pageAction == "aDd":
            contspace = Markup(""" <form method="POST" action=""><input type="hidden" name="action1" value="addProduct"><label>Product Name: </label><input type="TEXT" name="pname"> <br /><label>Product price: </label><input type="TEXT" name="pprice"><br /><label>Description: </label><input type="TEXT" name="pdescription"><br /><label>Category: </label><input type="TEXT" name="pcategory"><br /><label>Subcategory: </label><input type="TEXT" name="psubcategory"><button type="submit">SEND</button> <button type="RESET">CLEAR FORM</button></form> """)
            return render_template('dashboard.html', title=title, header='Add a product', uName=g.user, contspace=contspace)
        elif pageAction == "uPdate":
            contspace = Markup(""" <form method="POST" action=""><input type="hidden" name="action1" value="updateProduct"><label>Product Name: </label><input type="TEXT" name="pname"> <br /><label>Product price: </label><input type="TEXT" name="pprice"><br /><label>Description: </label><input type="TEXT" name="pdescription"><br /><label>Category: </label><input type="TEXT" name="pcategory"><br /><label>Subcategory: </label><input type="TEXT" name="psubcategory"><button type="submit">SEND</button> <button type="RESET">CLEAR FORM</button></form> """)
            return render_template('dashboard.html', title=title, header='Update a product', uName=g.user, contspace=contspace)
        elif pageAction == "dElete":
            contspace = Markup('<form method="POST" action=""><input type="hidden" name="action1" value="setSettings"><p><label>Text color: </label><input type="TEXT" name="textcolor:></p><p><label>Description color: </label><input type="TEXT" name="desccolor:></p><p><label>Price color: </label><input type="TEXT" name="pricecolor:></p><p><label>Product names color: </label><input type="TEXT" name="itemncolor:></p><p><button type="submit">SUBMIT</button><button type="reset">CLEAR FORM</button></p>')
            return render_template('dashboard.html', title=title, header='Settings', uName=g.user, contspace=contspace)
        elif pageAction == "addProduct":

            if g.user and g.password:
                uName = g.user
                uPass = g.password
                checklogin = dressup.checklogin(uName,uPass)


                if checklogin == 'good':
                    aID = session['edit']
                    addProduct = dressup.addProduct(aID,pName,pPrice,pDescription,pCategory,pSubcategory)
                    if addProduct == 'success':
                        contspace = 'Product added succesfully'
                        return render_template('dashboard.html', uName=g.user, contspace=contspace, header='Add a product', title=title)
        elif pageAction == "addShop":




            contspace = Markup('')
            return render_template('dashboard.html', title=title, uName=g.user, header='Added succesfully', contspace=contspace)
        elif pageAction == "updateProduct":
            contspace = Markup('')
            return render_template('dashboard.html', title=title, uName=g.user, header='Updated succesfully', contspace=contspace)
        elif pageAction == "deleteProduct":
            contspace = Markup('')
            return render_template('dashboard.html', title=title, uName=g.user, header='Deleted succesfully', contspace=contspace)




@app.route("/dashboard-modify", methods=['GET', 'POST'])
def dashmodify():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    title='Modify website'
    if request.method == "GET":


        try:
            g.user = session['user']
            g.password = session['password']
            g.uid = session['uid']
        except:
            picspace = ''
            return redirect(url_for('sign_in'))
        else:
            if g.user and g.password:

                uName = g.user
                uPass = g.password

                checklogin = dressup.checklogin(uName,uPass)


                if checklogin == 'good':

                    g.user = session['user']
                    g.password = session['password']
                    g.uid = session['uid']
                    uID = g.uid

                    #GET ALL ASSETS
                    assets = dressup.getassets(uID)
                    return render_template('dashboard.html', header='Modify website', uName=g.user, contspace=assets, title=title)
    elif request.method == "POST":
        try:

            edit = request.form['edit']
        except:
            edit = session['edit']

        else:


            edit = request.form['edit']
            aID=edit
            session['aName']=dressup.getaName(aID)
            session.pop('edit', None)
            session['edit'] = edit
            g.edit = session['edit']


        try:
            g.user = session['user']
            g.password = session['password']
            g.uid = session['uid']
        except:
            return redirect(url_for('sign_in'))
        else:
            if g.user and g.password:
                uName = g.user
                uPass = g.password
                checklogin = dressup.checklogin(uName,uPass)


                if checklogin == 'good':
                    #GET style to know form
                    aID = session['edit']
                    style = dressup.getstyle(aID)





                    if style == 'resume':

                        formdata = getformdata.getresume(aID)

                        form = getformdata.getresume(aID)
                        contspace = form
                        return render_template('dashboard.html', uName=g.user, title=title, contspace=contspace)
                    elif style == 'agency':

                        try:
                            pageAction = request.form['action1']
                        except:

                            pageAction = 'agencyOptions'
                            title='Edit Agency'
                            contspace = Markup('<form action="" method="POST"><input type="radio" name="action1" value="showNslogan">Name and Slogan/Vision<br /><input type="radio" name="action1" value="showSummary">3 Summaries<br /><input type="radio" name="action1" value="showPortform">Portfolio<br /><input type="radio" name="action1" value="showMiles">Milestone<br /><input type="radio" name="action1" value="showTeamate">Team<br /><input type="radio" name="action1" value="showPartform">Partners<br /><input type="radio" name="action1" value="showServform">Services<br /><input type="radio" name="action1" value="showAbform">About<br /><input type="radio" name="action1" value="showOthers">Others<br /><button type="submit">Submit</button></form>')
                            return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Edit Agency website',title=title)

                        else:
                            pageAction = request.form['action1']
                            if pageAction == 'agencyOptions':

                                title='Edit Agency'
                                contspace = Markup('<form action="" method="POST"><input type="radio" name="action1" value="showNslogan">Name and Slogan/Vision<br /><input type="radio" name="action1" value="showSummary">3 Summaries<br /><input type="radio" name="action1" value="showPortform">Portfolio<br /><input type="radio" name="action1" value="showMiles">Milestone<br /><input type="radio" name="action1" value="showTeamate">Team<br /><input type="radio" name="action1" value="showPartform">Partners<br /><input type="radio" name="action1" value="showServform">Services<br /><input type="radio" name="action1" value="showAbform">About<br /><button type="submit">Submit</button></form>')
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Edit Agency website',title=title)
                                #return render_template('studio/agency.html', aName=aName, slogan=slogan, mainphrase=mainphrase, subphrase=subphrase, value1=value1, value2=value2, value3=value3, value1des=value1des, value2des=value2des, value3des=value3des, portstat=portstat, aboutstat=aboutstat, mem1date=mem1date, mem1title=mem1title, mem1des=mem1des,  mem2date=mem2date, mem2title=mem2title, mem2des=mem2des,  mem3date=mem3date, mem3title=mem3title, mem3des=mem3des)
                            elif pageAction == 'showNslogan':
                                cont = '''<html lang="en"> <head> <meta charset="utf-8"> <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"> <meta name="description" content="A website design company based in Donholm Ph. 5"> <meta name="author" content="BIASHARA EMPLOYERS"> <title>Biashara Website design</title> <!-- Bootstrap core CSS --> <link href="static/css/bootstrap.min.css" rel="stylesheet"> <link rel="shortcut icon" href="static/logo_raw.png"> <!-- Custom fonts for this template --> <link href="static/css/font-awesome.min.css" rel="stylesheet" type="text/css"> <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css"> <link href='https://fonts.googleapis.com/css?family=Kaushan+Script' rel='stylesheet' type='text/css'> <link href='https://fonts.googleapis.com/css?family=Droid+Serif:400,700,400italic,700italic' rel='stylesheet' type='text/css'> <link href='https://fonts.googleapis.com/css?family=Roboto+Slab:400,100,300,700' rel='stylesheet' type='text/css'> <!-- Custom styles for this template --> <link href="static/css/agency.min.css" rel="stylesheet"> </head> <body id="page-top">  <!-- Navigation --> <nav class="navbar navbar-expand-lg navbar-dark fixed-top" id="mainNav" style="background:black;height:5px;"> <div class="container"> <a class="navbar-brand js-scroll-trigger" href="#page-top">{}</a> <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation"> Menu <i class="fa fa-bars"></i> </button> <div class="collapse navbar-collapse" id="navbarResponsive"> <ul class="navbar-nav text-uppercase ml-auto"> <li class="nav-item"> <a class="nav-link js-scroll-trigger" href="#services">Services</a> </li> <li class="nav-item"> <a class="nav-link js-scroll-trigger" href="#portfolio">Portfolio</a> </li> <li class="nav-item"> <a class="nav-link js-scroll-trigger" href="#about">About</a> </li> <li class="nav-item"> <a class="nav-link js-scroll-trigger" href="#team">Team</a> </li> <li class="nav-item"> <a class="nav-link js-scroll-trigger" href="#contact">Contact</a> </li> </ul> </div> </div> </nav>'''.format(session['aName'])
                                spa = '''<br /><!-- Header --> <header class="masthead"> <div class="container"> <div class="intro-text"> <div class="intro-lead-in">Welcome To <form action="" method="POST"><input type="hidden" name="action1" value="saveNslogan"><input style="width:auto;opacity: 0.6" type="TEXT" placeholder="Enter text" name="name"></div> <div class="intro-heading text-uppercase"><input style="width:auto" type="TEXT" placeholder="Enter slogan/Vision" name="slogan"><br />Logo image: <input type="type" name="logoLink" placeholder="Link to Logo image "></div> </div> </div> </header><br /><button type="submit">Submit</button> <button type="reset">CLEAR FORM</button></form>'''
                                ce = '''</body></html>'''
                                contspace = Markup(cont + spa + ce)
                                title=''
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Edit Name and Slogan/Vision',title=title)
                            elif pageAction == 'showSummary':
                                cont = '''<html lang="en"> <head> <meta charset="utf-8"> <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"> <meta name="description" content="A website design company based in Donholm Ph. 5"> <meta name="author" content="BIASHARA EMPLOYERS"> <title>Biashara Website design</title> <!-- Bootstrap core CSS --> <link href="static/css/bootstrap.min.css" rel="stylesheet"> <link rel="shortcut icon" href="static/logo_raw.png"> <!-- Custom fonts for this template --> <link href="static/css/font-awesome.min.css" rel="stylesheet" type="text/css"> <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css"> <link href='https://fonts.googleapis.com/css?family=Kaushan+Script' rel='stylesheet' type='text/css'> <link href='https://fonts.googleapis.com/css?family=Droid+Serif:400,700,400italic,700italic' rel='stylesheet' type='text/css'> <link href='https://fonts.googleapis.com/css?family=Roboto+Slab:400,100,300,700' rel='stylesheet' type='text/css'> <!-- Custom styles for this template --> <link href="static/css/agency.min.css" rel="stylesheet"> </head> <body id="page-top">  <!-- Navigation --> <nav class="navbar navbar-expand-lg navbar-dark fixed-top" id="mainNav" style="background:black;height:5px;"> <div class="container"> <a class="navbar-brand js-scroll-trigger" href="#page-top">{}</a> <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation"> Menu <i class="fa fa-bars"></i> </button> <div class="collapse navbar-collapse" id="navbarResponsive"> <ul class="navbar-nav text-uppercase ml-auto"> <li class="nav-item"> <a class="nav-link js-scroll-trigger" href="#services">Services</a> </li> <li class="nav-item"> <a class="nav-link js-scroll-trigger" href="#portfolio">Portfolio</a> </li> <li class="nav-item"> <a class="nav-link js-scroll-trigger" href="#about">About</a> </li> <li class="nav-item"> <a class="nav-link js-scroll-trigger" href="#team">Team</a> </li> <li class="nav-item"> <a class="nav-link js-scroll-trigger" href="#contact">Contact</a> </li> </ul> </div> </div> </nav>'''.format(session['aName'])
                                spa = '''<br /><!-- Services --> <section id="services"> <div class="container"> <div class="row"> <div class="col-lg-12 text-center"> <h2 class="section- heading text-uppercase"><form action="" method="POST"><input type="hidden" name="action1" value="saveSummary"><input style="width:auto" type="TEXT" placeholder="Enter a title" name="mainphrase"></h2> <h3 class="section-subheading text-muted"><input style="width:auto" type="TEXT" placeholder="Enter a subtitle" name="subphrase"></h3> </div> </div> <div class="row text-center"> <div class="col-md- 4"> <input type="TEXT" name="sum1image" placeholder="Image link">  <h4 class="service-heading"><input style="width:auto" type="TEXT" placeholder="Value 1" name="value1"></h4> <p class="text-muted"><input style="width:auto" type="TEXT" placeholder="Value 1 description" name="value1des"></p> </div> <div class="col-md-4"> <input type="TEXT" name="sum2image" placeholder="imageLink"> <h4 class="service-heading"><input style="width:auto" type="TEXT" placeholder="Value 2" name="value2"></h4> <p class="text-muted"><input style="width:auto" type="TEXT" placeholder="Value 2 description" name="value2des"></p> </div> <div class="col-md-4"> <input type="TEXT" name="sum3image" placeholder="imageLink"> <h4 class="service-heading"><input style="width:auto" type="TEXT" placeholder="Value 3" name="value3"></h4> <p class="text-muted"><input style="width:auto" type="TEXT" placeholder="Value 3 description" name="value3des"></p> <BR /><button type="submit">Submit</button> <button type="reset">CLEAR FORM</button></form> </div> </div> </div> </section>'''
                                ce = '''</body></html>'''
                                contspace = Markup(cont + spa + ce)
                                title=''
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Edit summaries',title=title)
                            elif pageAction == 'showPortform':
                                contspace = Markup('''<br /><form method="POST" action=""><input type="radio" name="action1" value="addPortform">Add portfolio item<br /><input type="radio" name="action1" value="getPorts">Update portfolio item<br /><input type="radio" name="action1" value="delPort">Delete portfolio item<br /><button type="submit">Submit</button> <button type="reset">CLEAR FORM</button></form>''')
                                title=''
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Edit Portfolio items',title=title)
                            elif pageAction == 'showMiles':
                                cont = '''<html lang="en"> <head> <meta charset="utf-8"> <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"> <meta name="description" content="A website design company based in Donholm Ph. 5"> <meta name="author" content="BIASHARA EMPLOYERS"> <title>Biashara Website design</title> <!-- Bootstrap core CSS --> <link href="static/css/bootstrap.min.css" rel="stylesheet"> <link rel="shortcut icon" href="static/logo_raw.png"> <!-- Custom fonts for this template --> <link href="static/css/font-awesome.min.css" rel="stylesheet" type="text/css"> <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css"> <link href='https://fonts.googleapis.com/css?family=Kaushan+Script' rel='stylesheet' type='text/css'> <link href='https://fonts.googleapis.com/css?family=Droid+Serif:400,700,400italic,700italic' rel='stylesheet' type='text/css'> <link href='https://fonts.googleapis.com/css?family=Roboto+Slab:400,100,300,700' rel='stylesheet' type='text/css'> <!-- Custom styles for this template --> <link href="static/css/agency.min.css" rel="stylesheet"> </head> <body id="page-top">  <!-- Navigation --> <nav class="navbar navbar-expand-lg navbar-dark fixed-top" id="mainNav" style="background:black;height:5px;"> <div class="container"> <a class="navbar-brand js-scroll-trigger" href="#page-top">{}</a> <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation"> Menu <i class="fa fa-bars"></i> </button> <div class="collapse navbar-collapse" id="navbarResponsive"> <ul class="navbar-nav text-uppercase ml-auto"> <li class="nav-item"> <a class="nav-link js-scroll-trigger" href="#services">Services</a> </li> <li class="nav-item"> <a class="nav-link js-scroll-trigger" href="#portfolio">Portfolio</a> </li> <li class="nav-item"> <a class="nav-link js-scroll-trigger" href="#about">About</a> </li> <li class="nav-item"> <a class="nav-link js-scroll-trigger" href="#team">Team</a> </li> <li class="nav-item"> <a class="nav-link js-scroll-trigger" href="#contact">Contact</a> </li> </ul> </div> </div> </nav>'''.format(session['aName'])
                                spa = '''<ul class="timeline"> <li> <div class="timeline-image"> <form method="POST" action=""><input type="hidden" name="action1" value="saveMiles"><input type="text" name="mile1Pic" placeholder="Image link"> </div> <div class="timeline-panel"> <div class="timeline-heading"> <h4><input style="width:auto" type="TEXT" placeholder="Memory 1 Date" name="mem1date"></h4> <h4 class="subheading"><input style="width:auto" type="TEXT" placeholder="Memory 1 title" name="mem1title"></h4> </div> <div class="timeline-body"> <p class="text-muted"><input style="width:auto" type="TEXT" placeholder="Memory 1 description" name="mem1des"></p> </div> </div> </li> <li class="timeline-inverted"> <div class="timeline-image"> <input type="text" name="mile2Pic" placeholder="Image link"> </div> <div class="timeline-panel"> <div class="timeline-heading"> <h4><input style="width:auto" type="TEXT" placeholder="Memory 2 date" name="mem2date"></h4> <h4 class="subheading"><input style="width:auto" type="TEXT" placeholder="Memory 2 title" name="mem2title"></h4> </div> <div class="timeline-body"> <p class="text-muted"><input style="width:auto" type="TEXT" placeholder="Memory 2 description" name="mem2des"></p> </div> </div> </li> <li> <div class="timeline-image"> <input type="text" name="mile3Pic" placeholder="Image link"> </div> <div class="timeline-panel"> <div class="timeline-heading"> <h4><input style="width:auto" type="TEXT" placeholder="Memory 3 date" name="mem3date"></h4> <h4 class="subheading"><input style="width:auto" type="TEXT" placeholder="Memory 3 title" name="mem3title"></h4> </div> <div class="timeline-body"> <p class="text-muted"><input style="width:auto" type="TEXT" placeholder="Memory 3 description" name="mem3des"></p> </div> </div> </li> <li class="timeline-inverted"> <div class="timeline-image"> <input type="text" name="mile4Pic" placeholder="Image link"> </div> <div class="timeline-panel"> <div class="timeline-heading"> <h4><input style="width:auto" type="TEXT" placeholder="Memory 4 date" name="mem4date"></h4> <h4 class="subheading"><input style="width:auto" type="TEXT" placeholder="Memory 4 title" name="mem4title"></h4> </div> <div class="timeline-body"> <p class="text-muted"><input style="width:auto" type="TEXT" placeholder="Memory 4 description" name="mem4des"></p> </div> </div> </li> <li class="timeline-inverted"> <div class="timeline-image"> <h4>Be Part <br>Of Our <br>Story!</h4> </div> </li> </ul><br /><button type="submit">Submit</button> <button type="reset">CLEAR FORM</button></form>'''
                                #spa = '''<ul class="timeline"> <li> <div class="timeline-image"> <img class="rounded-circle img-fluid" src="static/img/about/1.jpg" alt=""> </div> <div class="timeline-panel"> <div class="timeline-heading"> <h4><input style="width:auto" type="TEXT" placeholder="Memory 1 Date" name="mem1date"></h4> <h4 class="subheading"><input style="width:auto" type="TEXT" placeholder="Memory 1 title" name="mem1title"></h4> </div> <div class="timeline-body"> <p class="text-muted"><input style="width:auto" type="TEXT" placeholder="Memory 1 description" name="mem1des"></p> </div> </div> </li> <li class="timeline-inverted"> <div class="timeline-image"> <img class="rounded-circle img-fluid" src="static/img/about/2.jpg" alt=""> </div> <div class="timeline-panel"> <div class="timeline-heading"> <h4><input style="width:auto" type="TEXT" placeholder="Memory 2 date" name="mem2date"></h4> <h4 class="subheading"><input style="width:auto" type="TEXT" placeholder="Memory 2 title" name="mem2title"></h4> </div> <div class="timeline-body"> <p class="text-muted"><input style="width:auto" type="TEXT" placeholder="Memory 2 description" name="mem2des"></p> </div> </div> </li> <li> <div class="timeline-image"> <img class="rounded-circle img-fluid" src="static/img/about/3.jpg" alt=""> </div> <div class="timeline-panel"> <div class="timeline-heading"> <h4><input style="width:auto" type="TEXT" placeholder="Memory 3 date" name="mem3date"></h4> <h4 class="subheading"><input style="width:auto" type="TEXT" placeholder="Memory 3 title" name="mem3title"></h4> </div> <div class="timeline-body"> <p class="text-muted"><input style="width:auto" type="TEXT" placeholder="Memory 3 description" name="mem3des"></p> </div> </div> </li> <li class="timeline-inverted"> <div class="timeline-image"> <img class="img-fluid" src="https://scontent.fnbo8-1.fna.fbcdn.net/v/t1.0-9/12717226_648278058646961_5804425856737814952_n.jpg?_nc_cat=0&oh=7a37aae01b9bb6f00952df9ebcc73b8d&oe=5C382CEB" alt="" style="border-radius:50%;height:100%"> </div> <div class="timeline-panel"> <div class="timeline-heading"> <h4><input style="width:auto" type="TEXT" placeholder="Memory 4 date" name="mem4date"></h4> <h4 class="subheading"><input style="width:auto" type="TEXT" placeholder="Memory 4 title" name="mem4title"></h4> </div> <div class="timeline-body"> <p class="text-muted"><input style="width:auto" type="TEXT" placeholder="Memory 4 description" name="mem4des"></p> </div> </div> </li> <li class="timeline-inverted"> <div class="timeline-image"> <h4>Be Part <br>Of Our <br>Story!</h4> </div> </li> </ul>'''
                                ce = '''</body></html>'''
                                contspace = Markup(cont + spa + ce)
                                title=''
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Edit Milestones',title=title)
                            elif pageAction == 'showTeamate':
                                contspace = Markup('''<br /><form method="POST" action=""><input type="radio" name="action1" value="addTmateform">Add Team member<br /><input type="radio" name="action1" value="getTmates">Update Team member<br /><input type="radio" name="action1" value="getdelTmate">Delete Team member<br /><button type="submit">Submit</button> <button type="reset">CLEAR FORM</button></form>''')
                                title=''
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Edit Team mates',title=title)
                            elif pageAction == 'showPartform':
                                contspace = Markup('''<br /><form method="POST" action=""><input type="radio" name="action1" value="addPartform">Add partner<br /><input type="radio" name="action1" value="getParts">Update partner data<br /><input type="radio" name="action1" value="getdelPart">Delete partner data<br /><button type="submit">Submit</button> <button type="reset">CLEAR FORM</button></form>''')
                                title=''
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Edit Partners',title=title)
                            elif pageAction == 'showServform':
                                contspace = Markup('''<br /><form method="POST" action=""><input type="radio" name="action1" value="addSform">Add Service<br /><input type="radio" name="action1" value="getServices">Update Service<br /><input type="radio" name="action1" value="getdelServices">Delete Service<br /><button type="submit">Submit</button> <button type="reset">CLEAR FORM</button></form>''')
                                title=''
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Edit Services',title=title)
                            elif pageAction == 'showAbform':
                                #contspace = Markup('''<br /><form method="POST" action=""><input type="radio" name="action1" value="addPortform">Add portfolio item<br /><input type="radio" name="action1" value="updatePortform">Update portfolio item<br /><input type="radio" name="action1" value="addPortform">Delete portfolio item<br /><button type="submit">Submit</button> <button type="reset">CLEAR FORM</button></form>''')
                                contspace = Markup(agencypro.about(aID))
                                title=''
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Edit About page',title=title)
                            elif pageAction == 'showOthers':
                                checkexist = agencypro.checkOthers(aID)
                                if checkexist == 'n':
                                    contspace = Markup('<form method="POST" action=""><input type="hidden" name="action1" value="newOthers"><label>Portfolio description: </label><input type="TEXT" name="portstat"><br /><label>Milestones description: </label><input type="TEXT" name="milestat"><br /><label>Team section description: </label><input type="TEXT" name="teamstat"><br /><label>Last word: </label><input type="TEXT" name="lastword"><br /><button type="submit">Submit</button> <button type="RESET">CLEAR FORM</button></form>')
                                    title = ''
                                    return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Edit other details',title=title)
                                elif checkexist == 'y':
                                    getOthers = agencypro.getOthers(aID)
                                    portstat = getOthers['portstat']
                                    milestat = getOthers['milestat']
                                    teamstat = getOthers['teamstat']
                                    lastword = getOthers['lastword']
                                    contspace = Markup('<form method="POST" action=""><input type="hidden" name="action1" value="updateOthers"><label>Portfolio description: </label><input type="TEXT" name="portstat" value={}><br /><label>Milestones description: </label><input type="TEXT" name="milestat" value={}><br /><label>Team section description: </label><input type="TEXT" name="teamstat" value={}><br /><label>Last word: </label><input type="TEXT" name="lastword" value={}><br /><button type="submit">Submit</button> <button type="RESET">CLEAR FORM</button></form>'.format(portstat,milestat,teamstat,lastword))
                                    title = ''
                                    return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Edit other details',title=title)
                            elif pageAction == 'updateOthers':
                                portstat = request.form['portstat'].replace("'", "&#39;")
                                milestat = request.form['milestat'].replace("'", "&#39;")
                                teamstat = request.form['teamstat'].replace("'", "&#39;")
                                lastword = request.form['lastword'].replace("'", "&#39;")
                                contspace = agencypro.updateOthers(aID,portstat,milestat,teamstat,lastword)
                                title = ''
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Edit other details',title=title)
                            elif pageAction == 'newOthers':
                                portstat = request.form['portstat'].replace("'", "&#39;")
                                milestat = request.form['milestat'].replace("'", "&#39;")
                                teamstat = request.form['teamstat'].replace("'", "&#39;")
                                lastword = request.form['lastword'].replace("'", "&#39;")
                                contspace = agencypro.newOthers(aID,portstat,milestat,teamstat,lastword)
                                title = ''
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Edit other details',title=title)

                            elif pageAction == 'noAbout':
                                abImage=request.form['abImage'].replace("'", "&#39;")
                                abDesc=request.form['abDesc'].replace("'", "&#39;")

                                contspace = Markup(agencypro.noAbout(aID,abImage,abDesc))
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Edit About page',title=title)
                            elif pageAction == 'yesAbout':
                                abImage=request.form['abImage'].replace("'", "&#39;")
                                abDesc=request.form['abDesc'].replace("'", "&#39;")

                                contspace = Markup(agencypro.yesAbout(aID,abImage,abDesc))
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Edit About page',title=title)
                            elif pageAction == 'addPartform':
                                contspace=Markup('''<br /><form method="POST" action=""><input type="hidden" name="action1" value="newPart"><label>Partner Image link: </label><input type="text" name="partImage"><br /><label>Partner Name: </label><input type="text" name="partName"><br /><label>Partner link: </label><input type="text" name="partLink"><br /><label>Twiter link: </label><input type="text" name="tweet"><br /><label>Facebook link: </label><input type="text" name="fb"><br /><label>LinkedIn link: </label><input type="text" name="ln"><br /><br /><button type="submit">Submit</button> <button type="reset">CLEAR FORM</button></form>''')
                                title=''
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Add Partner',title=title)
                            elif pageAction == 'newPart':
                                partImage = request.form['partImage'].replace("'", "&#39;")
                                partName = request.form['partName'].replace("'", "&#39;")
                                partLink = request.form['partLink'].replace("'", "&#39;")
                                tweet = request.form['tweet'].replace("'", "&#39;")
                                fb = request.form['fb'].replace("'", "&#39;")
                                ln = request.form['ln'].replace("'", "&#39;")
                                contspace = agencypro.newPart(aID,partImage,partName,partLink,tweet,fb,ln)
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Save Partner',title=title)
                            elif pageAction=='getParts':
                                contspace = Markup(agencypro.getParts(aID))
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Select partner',title=title)
                            elif pageAction == 'updatePform':
                                pID = request.form['Partner']
                                session['part']=pID
                                contspace = Markup(agencypro.getPdata(pID))
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Update partner data',title=title)
                            elif pageAction == 'updatePart':
                                pID = session['part']
                                partImage = request.form['partImage'].replace("'", "&#39;")
                                partName =  request.form['partName'].replace("'", "&#39;")
                                partLink = request.form['partLink'].replace("'", "&#39;")
                                tweet = request.form['tweet'].replace("'", "&#39;")
                                fb = request.form['fb'].replace("'", "&#39;")
                                ln = request.form['ln'].replace("'", "&#39;")
                                contspace=Markup(agencypro.updateP(pID,partImage,partName,partLink,tweet,fb,ln))
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Update partner data',title=title)
                            elif pageAction == 'getdelPart':
                                contspace=Markup(agencypro.getdelP(aID))
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Delete member data',title=title)
                            elif pageAction == 'delP':
                                pID = request.form['partners']
                                contspace = Markup(agencypro.deleteP(pID))
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Delete  member data',title=title)
                            elif pageAction == 'addSform':
                                contspace=Markup('''<br /><form method="POST" action=""><input type="hidden" name="action1" value="newS"><label>Service Image link: </label><input type="text" name="servImage"><br /><label>Service Name: </label><input type="text" name="servName"><br /><label>Service description: </label><input type="text" name="servDesc"><br /><br /><button type="submit">Submit</button> <button type="reset">CLEAR FORM</button></form>''')
                                title=''
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Add Service',title=title)
                            elif pageAction == 'newS':
                                servImage = request.form['servImage'].replace("'", "&#39;")
                                servName = request.form['servName'].replace("'", "&#39;")
                                servDesc = request.form['servDesc'].replace("'", "&#39;")
                                contspace = agencypro.newS(aID,servImage,servName,servDesc)
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Save Service',title=title)
                            elif pageAction=='getServices':
                                contspace = Markup(agencypro.getServices(aID))
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Select service',title=title)
                            elif pageAction == 'updateSform':
                                pID = request.form['Service']
                                session['serv']=pID
                                contspace = Markup(agencypro.getSdata(pID))
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Update service data',title=title)
                            elif pageAction == 'updateS':
                                pID = session['serv']
                                servImage = request.form['servImage'].replace("'", "&#39;")
                                servName =  request.form['servName'].replace("'", "&#39;")
                                servDesc = request.form['servDesc'].replace("'", "&#39;")
                                contspace=Markup(agencypro.updateS(pID,servImage,servName,servDesc))
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Update service data',title=title)
                            elif pageAction == 'getdelServices':
                                contspace=Markup(agencypro.getdelS(aID))
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Delete service data',title=title)
                            elif pageAction == 'delS':
                                pID = request.form['partners']
                                contspace = Markup(agencypro.deleteS(pID))
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Delete  service data',title=title)
                            elif pageAction =='addTmateform':
                                contspace=Markup('''<br /><form method="POST" action=""><input type="hidden" name="action1" value="newTmate"><label>Member Image link: </label><input type="text" name="tmateImage"><br /><label>Member Name: </label><input type="text" name="tmateName"><br /><label>Member position: </label><input type="text" name="tmatePost"><br /><label>Twitter link: </label><input type="text" name="tweet"><br /><label>Facebook link: </label><input type="text" name="fb"><br /><label>LinkedIn link: </label><input type="text" name="ln"><br /><br /><button type="submit">Submit</button> <button type="reset">CLEAR FORM</button></form>''')
                                title=''
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Add Team member',title=title)
                            elif pageAction == 'addPortform':
                                contspace=Markup('''<br /><form method="POST" action=""><input type="hidden" name="action1" value="newPort"><label>Image link: </label><input type="text" name="portImage"><br /><label>Title: </label><input type="text" name="portTitle"><br /><label>Description: </label><input type="text" name="portDesc"><br /><br /><button type="submit">Submit</button> <button type="reset">CLEAR FORM</button></form>''')
                                title=''
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Add  item',title=title)
                            elif pageAction == 'newTmate':
                                tmateImage = request.form['tmateImage'].replace("'", "&#39;")
                                tmateName = request.form['tmateName'].replace("'", "&#39;")
                                tmatePost = request.form['tmatePost'].replace("'", "&#39;")
                                tweet = request.form['tweet'].replace("'", "&#39;")
                                fb = request.form['fb'].replace("'", "&#39;")
                                ln = request.form['ln'].replace("'", "&#39;")
                                contspace = agencypro.newTmate(aID,tmateImage,tmateName,tmatePost,tweet,fb,ln)
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Save Team member',title=title)
                            elif pageAction == 'newPort':
                                portImage = request.form['portImage']
                                portTitle = request.form['portTitle']
                                portDesc = request.form['portDesc']
                                contspace = agencypro.newPort(aID,portImage,portTitle,portDesc)
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Save item',title=title)
                            elif pageAction == 'getTmates':
                                contspace = Markup(agencypro.getTmates(aID))
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Select member',title=title)
                            elif pageAction == 'updateTform':
                                pID = request.form['Tmate']
                                session['tmate']=pID
                                contspace = Markup(agencypro.getTmatedata(pID))
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Update member data',title=title)
                            elif pageAction == 'updateTmate':
                                pID = session['tmate']
                                tmateImage = request.form['tmateImage'].replace("'", "&#39;")
                                tmateName =  request.form['tmateName'].replace("'", "&#39;")
                                tmatePost = request.form['tmatePost'].replace("'", "&#39;")
                                tweet = request.form['tweet'].replace("'", "&#39;")
                                fb = request.form['fb'].replace("'", "&#39;")
                                ln = request.form['ln'].replace("'", "&#39;")
                                contspace=Markup(agencypro.updateTmate(pID,tmateImage,tmateName,tmatePost,tweet,fb,ln))
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Update member data',title=title)
                            elif pageAction == 'getPorts':
                                contspace = Markup(agencypro.getPorts(aID))
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Select item',title=title)
                            elif pageAction == 'updatePortform':
                                pID = request.form['portfolio']
                                session['port']=pID
                                contspace = Markup(agencypro.getPortdata(pID))

                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Update item',title=title)
                            elif pageAction == 'updatePort':
                                portImage=request.form['portImage'].replace("'", "&#39;")
                                portTitle=request.form['portTitle'].replace("'", "&#39;")
                                portDesc=request.form['portDesc'].replace("'", "&#39;")
                                pID = session['port']

                                contspace=agencypro.updatePort(pID,portImage,portTitle,portDesc)
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Update item',title=title)
                            elif pageAction == 'getdelTmate':
                                contspace=Markup(agencypro.getdelT(aID))
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Delete member data',title=title)
                            elif pageAction=='delT':
                                pID = request.form['Tmate']
                                contspace = Markup(agencypro.deleteT(pID))
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Delete  member data',title=title)
                            elif pageAction=='delPort':
                                contspace=Markup(agencypro.getdelPort(aID))
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Delete item',title=title)
                            elif pageAction=='deletePort':
                                pID = request.form['portfolio']
                                contspace = Markup(agencypro.deletePort(pID))
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Delete item',title=title)
                            elif pageAction == 'saveMiles':
                                mile1Pic= request.form['mile1Pic'].replace("'", "&#39;")
                                mile2Pic= request.form['mile2Pic'].replace("'", "&#39;")
                                mile3Pic= request.form['mile3Pic'].replace("'", "&#39;")
                                mile4Pic= request.form['mile4Pic'].replace("'", "&#39;")
                                mem1date= request.form['mem1date'].replace("'", "&#39;")
                                mem2date= request.form['mem2date'].replace("'", "&#39;")
                                mem3date= request.form['mem3date'].replace("'", "&#39;")
                                mem4date= request.form['mem4date'].replace("'", "&#39;")
                                mem1des= request.form['mem1des'].replace("'", "&#39;")
                                mem2des= request.form['mem2des'].replace("'", "&#39;")
                                mem3des= request.form['mem3des'].replace("'", "&#39;")
                                mem4des= request.form['mem4des'].replace("'", "&#39;")
                                mem1title= request.form['mem1title'].replace("'", "&#39;")
                                mem2title= request.form['mem2title'].replace("'", "&#39;")
                                mem3title= request.form['mem3title'].replace("'", "&#39;")
                                mem4title= request.form['mem4title'].replace("'", "&#39;")

                                contspace = Markup(agencypro.saveMiles(aID,mile1Pic,mile2Pic,mile3Pic,mile4Pic,mem1date,mem2date,mem3date,mem4date,mem1des,mem2des,mem3des,mem4des,mem1title,mem2title,mem3title,mem4title))
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Save Milestones',title=title)

                            elif pageAction == 'saveNslogan':
                                name = request.form['name'].replace("'", "&#39;")
                                slogan = request.form['slogan'].replace("'", "&#39;")
                                logoLink = request.form['logoLink']
                                contspace = agencypro.saveNslogan(aID,name,slogan,logoLink)
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Save name and slogan/vision',title=title)
                            elif pageAction == 'saveSummary':
                                mainphrase= request.form['mainphrase'].replace("'", "&#39;")
                                subphrase= request.form['subphrase'].replace("'", "&#39;")
                                value1= request.form['value1'].replace("'", "&#39;")
                                value2= request.form['value2'].replace("'", "&#39;")
                                value3= request.form['value3'].replace("'", "&#39;")
                                value1des= request.form['value1des'].replace("'", "&#39;")
                                value2des= request.form['value2des'].replace("'", "&#39;")
                                value3des= request.form['value3des'].replace("'", "&#39;")
                                sum1image= request.form['sum1image'].replace("'", "&#39;")
                                sum2image= request.form['sum2image'].replace("'", "&#39;")
                                sum3image= request.form['sum3image'].replace("'", "&#39;")
                                #contspace = value1

                                contspace = agencypro.saveSummary(aID,mainphrase,subphrase,value1,value2,value3,value1des,value2des,value3des,sum1image,sum2image,sum3image)
                                return render_template('dashboard.html',contspace=contspace,uName=g.user,header='Save Summaries',title=title)
                            elif pageAction == 'newAgency':
                                aName=request.form['aName'].replace("'", "&#39;")
                                slogan=request.form['slogan'].replace("'", "&#39;")
                                mainphrase=request.form['mainphrase'].replace("'", "&#39;")
                                subphrase=request.form['subphrase'].replace("'", "&#39;")
                                value1=request.form['value1'].replace("'", "&#39;")
                                value2=request.form['value2'].replace("'", "&#39;")
                                value3=request.form['value3'].replace("'", "&#39;")
                                value1des=request.form['value1des'].replace("'", "&#39;")
                                value2des=request.form['value2des'].replace("'", "&#39;")
                                value3des=request.form['value3des'].replace("'", "&#39;")
                                portstat=request.form['portstat'].replace("'", "&#39;")
                                aboutstat=request.form['aboutstat'].replace("'", "&#39;")
                                mem1date=request.form['mem1date'].replace("'", "&#39;")
                                mem1title=request.form['mem1title'].replace("'", "&#39;")
                                mem1des=request.form['mem1des'].replace("'", "&#39;")
                                mem2date=request.form['mem2date'].replace("'", "&#39;")
                                mem2title=request.form['mem2title'].replace("'", "&#39;")
                                mem2des=request.form['mem2des'].replace("'", "&#39;")
                                mem3date=request.form['mem3date'].replace("'", "&#39;")
                                mem3title=request.form['mem3title'].replace("'", "&#39;")
                                mem3des=request.form['mem3des'].replace("'", "&#39;")
                                mem4date=request.form['mem4date'].replace("'", "&#39;")
                                mem4title=request.form['mem4title'].replace("'", "&#39;")
                                mem4des=request.form['mem4des'].replace("'", "&#39;")
                                teamstat=request.form['teamstat'].replace("'", "&#39;")
                                statement=request.form['statement'].replace("'", "&#39;")
                                contstat=request.form['contstat'].replace("'", "&#39;")
                                copystat=request.form['copystat'].replace("'", "&#39;")


                                contspace = agencypro.newAgency(aName,slogan,mainphrase,subphrase,value1,value2,value3,value1des,value2des,value3des,portstat,aboutstat,mem1date,mem1title,mem1des,mem2date,mem2title,mem2des,mem3date,mem3title,mem3des,mem4date,mem4title,mem4des,teamstat,statement,contstat,copystat)
                                return render_template('dashboard.html', contspace=contspace, uName=g.user, header='Create a new agency website', title=title)
                            elif pageAction == 'generalD':
                                header='Edit General details'
                                contspace=Markup('''<html lang="en"> <head> <meta charset="utf-8"> <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"> <meta name="description" content="A website design company based in Donholm Ph. 5"> <meta name="author" content="BIASHARA EMPLOYERS"> <title>Biashara Website design</title> <!-- Bootstrap core CSS --> <link href="static/css/bootstrap.min.css" rel="stylesheet"> <link rel="shortcut icon" href="static/logo_raw.png"> <!-- Custom fonts for this template --> <link href="static/css/font-awesome.min.css" rel="stylesheet" type="text/css"> <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css"> <link href='https://fonts.googleapis.com/css?family=Kaushan+Script' rel='stylesheet' type='text/css'> <link href='https://fonts.googleapis.com/css?family=Droid+Serif:400,700,400italic,700italic' rel='stylesheet' type='text/css'> <link href='https://fonts.googleapis.com/css?family=Roboto+Slab:400,100,300,700' rel='stylesheet' type='text/css'> <!-- Custom styles for this template --> <link href="static/css/agency.min.css" rel="stylesheet"> </head> <body id="page-top">  <!-- Navigation --> <nav class="navbar navbar-expand-lg navbar-dark fixed-top" id="mainNav" style="background:black;height:5px;"> <div class="container"> <a class="navbar-brand js-scroll-trigger" href="#page-top">THE TITLE</a> <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation"> Menu <i class="fa fa-bars"></i> </button> <div class="collapse navbar-collapse" id="navbarResponsive"> <ul class="navbar-nav text-uppercase ml-auto"> <li class="nav-item"> <a class="nav-link js-scroll-trigger" href="#services">Services</a> </li> <li class="nav-item"> <a class="nav-link js-scroll-trigger" href="#portfolio">Portfolio</a> </li> <li class="nav-item"> <a class="nav-link js-scroll-trigger" href="#about">About</a> </li> <li class="nav-item"> <a class="nav-link js-scroll-trigger" href="#team">Team</a> </li> <li class="nav-item"> <a class="nav-link js-scroll-trigger" href="#contact">Contact</a> </li> </ul> </div> </div> </nav> <!-- Header --> <header class="masthead"> <div class="container"> <div class="intro-text"> <div class="intro-lead-in">Welcome To <input style="width:auto;opacity: 0.6" type="TEXT" placeholder="Enter text" name="aName"></div> <div class="intro-heading text-uppercase"><input style="width:auto" type="TEXT" placeholder="Enter slogan" name="slogan"></div> <a class="btn btn-primary btn-xl text-uppercase js-scroll-trigger" href="services">Tell Me More</a> </div> </div> </header> <!-- Services --> <section id="services"> <div class="container"> <div class="row"> <div class="col-lg-12 text-center"> <h2 class="section-heading text-uppercase"><input style="width:auto" type="TEXT" placeholder="Enter a phrase" name="mainphrase"></h2> <h3 class="section-subheading text-muted"><input style="width:auto" type="TEXT" placeholder="Enter a subphrase" name="subphrase"></h3> </div> </div> <div class="row text-center"> <div class="col-md-4"> <span class="fa-stack fa-4x"> <i class="fa fa-circle fa-stack-2x text-primary"></i> <i class="fa fa-shopping-cart fa-stack-1x fa-inverse"></i> </span> <h4 class="service-heading"><input style="width:auto" type="TEXT" placeholder="Value 1" name="value1"></h4> <p class="text-muted"><input style="width:auto" type="TEXT" placeholder="Value 1 description" name="value1des"></p> </div> <div class="col-md-4"> <span class="fa-stack fa-4x"> <i class="fa fa-circle fa-stack-2x text-primary"></i> <i class="fa fa-laptop fa-stack-1x fa-inverse"></i> </span> <h4 class="service-heading"><input style="width:auto" type="TEXT" placeholder="Value 2" name="value2"></h4> <p class="text-muted"><input style="width:auto" type="TEXT" placeholder="Value 2 description" name="value2des"></p> </div> <div class="col-md-4"> <span class="fa-stack fa-4x"> <i class="fa fa-circle fa-stack-2x text-primary"></i> <i class="fa fa-lock fa-stack-1x fa-inverse"></i> </span><h4 class="service-heading"><input style="width:auto" type="TEXT" placeholder="Value 3" name="value3"></h4> <p class="text-muted"><input style="width:auto" type="TEXT" placeholder="Value 3 description" name="value3des"></p> </div> </div> </div> </section> <!-- Portfolio Grid --> <section class="bg-light" id="portfolio"> <div class="container"> <div class="row"> <div class="col-lg-12 text-center"> <h2 class="section-heading text-uppercase">Portfolio</h2> <h3 class="section-subheading text-muted"><input style="width:auto" type="TEXT" placeholder="Enter portfolio statement" name="portstat"></h3> </div> </div> <div class="row"> <div class="col-md-4 col-sm-6 portfolio-item"> <a class="portfolio-link" data-toggle="modal" href="samples?sample=1"> <div class="portfolio-hover"> <div class="portfolio-hover-content"> <i class="fa fa-plus fa-3x"></i> </div> </div> <img class="img-fluid" src="static/img/profile.jpg" alt=""> </a> <div class="portfolio-caption"> <h4>clarencetaylor.com</h4> <p class="text-muted">Resume</p> </div> </div> </div> </div> </section> <!-- About --> <section id="about"> <div class="container"> <div class="row"> <div class="col-lg-12 text-center"> <h2 class="section-heading text-uppercase">About</h2> <h3 class="section-subheading text-muted"><input style="width:auto" type="TEXT" placeholder="Enter an about you statement" name="aboutstat"></h3> </div> </div> <div class="row"> <div class="col-lg-12"> <ul class="timeline"> <li> <div class="timeline-image"> <img class="rounded-circle img-fluid" src="static/img/about/1.jpg" alt=""> </div> <div class="timeline-panel"> <div class="timeline-heading"> <h4><input style="width:auto" type="TEXT" placeholder="Memory 1 Date" name="mem1date"></h4> <h4 class="subheading"><input style="width:auto" type="TEXT" placeholder="Memory 1 title" name="mem1title"></h4> </div> <div class="timeline-body"> <p class="text-muted"><input style="width:auto" type="TEXT" placeholder="Memory 1 description" name="mem1des"></p> </div> </div> </li> <li class="timeline-inverted"> <div class="timeline-image"> <img class="rounded-circle img-fluid" src="static/img/about/2.jpg" alt=""> </div> <div class="timeline-panel"> <div class="timeline-heading"> <h4><input style="width:auto" type="TEXT" placeholder="Memory 2 date" name="mem2date"></h4> <h4 class="subheading"><input style="width:auto" type="TEXT" placeholder="Memory 2 title" name="mem2title"></h4> </div> <div class="timeline-body"> <p class="text-muted"><input style="width:auto" type="TEXT" placeholder="Memory 2 description" name="mem2des"></p> </div> </div> </li> <li> <div class="timeline-image"> <img class="rounded-circle img-fluid" src="static/img/about/3.jpg" alt=""> </div> <div class="timeline-panel"> <div class="timeline-heading"> <h4><input style="width:auto" type="TEXT" placeholder="Memory 3 date" name="mem3date"></h4> <h4 class="subheading"><input style="width:auto" type="TEXT" placeholder="Memory 3 title" name="mem3title"></h4> </div> <div class="timeline-body"> <p class="text-muted"><input style="width:auto" type="TEXT" placeholder="Memory 3 description" name="mem3des"></p> </div> </div> </li> <li class="timeline-inverted"> <div class="timeline-image"> <img class="rounded-circle img-fluid" src="static/img/about/4.jpg" alt=""> </div> <div class="timeline-panel"> <div class="timeline-heading"> <h4><input style="width:auto" type="TEXT" placeholder="Memory 4 date" name="mem4date"></h4> <h4 class="subheading"><input style="width:auto" type="TEXT" placeholder="Memory 4 title" name="mem4title"></h4> </div> <div class="timeline-body"> <p class="text-muted"><input style="width:auto" type="TEXT" placeholder="Memory 4 description" name="mem4des"></p></div> </div> </li> <li class="timeline-inverted"> <div class="timeline-image"> <h4>Be Part <br>Of Our <br>Story!</h4> </div> </li> </ul> </div> </div> </div> </section> <!-- Team --> <section class="bg-light" id="team"> <div class="container"> <div class="row"> <div class="col-lg-12 text-center"> <h2 class="section-heading text-uppercase">Our Amazing Team</h2> <h3 class="section-subheading text-muted"><input style="width:auto" type="TEXT" placeholder="Enter team statement" name="teamstat"></h3> </div> </div> <div class="row"> <div class="col-sm-4"> <div class="team-member"> <img class="mx-auto rounded-circle" src="static/img/team/1.jpg" alt=""> <h4>Kay Garland</h4> <p class="text-muted">Lead Designer</p> <ul class="list-inline social-buttons"> <li class="list-inline-item"> <a href="#"> <i class="fa fa-twitter"></i> </a> </li> <li class="list-inline-item"> <a href="#"> <i class="fa fa-facebook"></i> </a> </li> <li class="list-inline-item"> <a href="#"> <i class="fa fa-linkedin"></i> </a> </li> </ul> </div> </div> </div> <div class="row"> <div class="col-lg-8 mx-auto text-center"> <p class="large text-muted"><input style="width:auto;opacity: 0.6" type="TEXT" placeholder="Enter text here" name="statement"></p> </div> </div> </div> </section> <!-- Clients > <section class="py-5"> <div class="container"> <div class="row"> <div class="col-md-3 col-sm-6"> <a href="#"> <img class="img-fluid d-block mx-auto" src="static/img/logos/envato.jpg" alt=""> </a> </div> <div class="col-md-3 col-sm-6"> <a href="#"> <img class="img-fluid d-block mx-auto" src="static/img/logos/designmodo.jpg" alt=""> </a> </div> <div class="col-md-3 col-sm-6"> <a href="#"> <img class="img-fluid d-block mx-auto" src="static/img/logos/themeforest.jpg" alt=""> </a> </div> <div class="col-md-3 col-sm-6"> <a href="#"> <img class="img-fluid d-block mx-auto" src="static/img/logos/creative-market.jpg" alt=""> </a> </div> </div> </div> </section--> <!-- Contact --> <section id="contact"> <div class="container"> <div class="row"> <div class="col-lg-12 text-center"> <h2 class="section-heading text-uppercase">Contact Us</h2> <h3 class="section-subheading text-muted"><input type="TEXT" placeholder="Enter contact us statement" name="contstat"></h3> </div> </div> <div class="row"> <div class="col-lg-12"></div> </div> </div> </section> <!-- Footer --> <footer> <div class="container"> <div class="row"> <div class="col-md-4"> <span class="copyright">Copyright &copy; <input type="TEXT" placeholder="enter your name" name="copystat"></span> </div> <div class="col-md-4"> <ul class="list-inline social-buttons"> <li class="list-inline-item"> <a href="#"> <i class="fa fa-twitter"></i> </a> </li> <li class="list-inline-item"> <a href="#"> <i class="fa fa-facebook"></i> </a> </li> <li class="list-inline-item"> <a href="#"> <i class="fa fa-linkedin"></i> </a> </li> </ul> </div> <div class="col-md-4"> <ul class="list-inline quicklinks"> <li class="list-inline-item"> <a href="#">Privacy Policy</a> </li> <li class="list-inline-item"> <a href="#">Terms of Use</a> </li> </ul> </div> </div> </div> </footer> <!-- Portfolio Modals --> <!-- Modal 1 --> <div class="portfolio-modal modal fade" id="portfolioModal1" tabindex="-1" role="dialog" aria-hidden="true"> <div class="modal-dialog"> <div class="modal-content"> <div class="close-modal" data-dismiss="modal"> <div class="lr"> <div class="rl"></div> </div> </div> <div class="container"> <div class="row"> <div class="col-lg-8 mx-auto"> <div class="modal-body"> <!-- Project Details Go Here --> <h2 class="text-uppercase">Project Name</h2> <p class="item-intro text-muted">Lorem ipsum dolor sit amet consectetur.</p> <img class="img-fluid d-block mx-auto" src="static/img/portfolio/01-full.jpg" alt=""> <p>Use this area to describe your project. We believe that everyone has a right to earn a living as long as they have a skill / talent. Thats why we created <a href="http://bizbiz.pythonanywhere.com/register">the system</a> so that everyone can register and get clients in their local area</a>!</p> <ul class="list-inline"> <li>Date: January 2017</li> <li>Client: Threads</li> <li>Category: Illustration</li> </ul> <button class="btn btn-primary" data-dismiss="modal" type="button"> <i class="fa fa-times"></i>Close Project</button> </div> </div> </div> </div> </div> </div> </div> <!-- Modal 2 --> <div class="portfolio-modal modal fade" id="portfolioModal2" tabindex="-1" role="dialog" aria-hidden="true"> <div class="modal-dialog"> <div class="modal-content"> <div class="close-modal" data-dismiss="modal"> <div class="lr"> <div class="rl"></div> </div> </div> <div class="container"> <div class="row"> <div class="col-lg-8 mx-auto"> <div class="modal-body"> <!-- Project Details Go Here --> <h2 class="text-uppercase">Project Name</h2> <p class="item-intro text-muted">Lorem ipsum dolor sit amet consectetur.</p> <img class="img-fluid d-block mx-auto" src="static/img/portfolio/02-full.jpg" alt=""> <p>Use this area to describe your project. We believe that everyone has a right to earn a living as long as they have a skill / talent. Thats why we created <a href="http://bizbiz.pythonanywhere.com/register">the system</a> so that everyone can register and get clients in their local area</a>!</p> <ul class="list-inline"> <li>Date: January 2017</li> <li>Client: Explore</li> <li>Category: Graphic Design</li> </ul> <button class="btn btn-primary" data-dismiss="modal" type="button"> <i class="fa fa-times"></i> Close Project</button> </div> </div> </div> </div> </div> </div> </div> <!-- Modal 3 --> <div class="portfolio-modal modal fade" id="portfolioModal3" tabindex="-1" role="dialog" aria-hidden="true"> <div class="modal-dialog"> <div class="modal-content"> <div class="close-modal" data-dismiss="modal"> <div class="lr"> <div class="rl"></div> </div> </div> <div class="container"> <div class="row"> <div class="col-lg-8 mx-auto"> <div class="modal-body"> <!-- Project Details Go Here --> <h2 class="text-uppercase">Project Name</h2> <p class="item-intro text-muted">Lorem ipsum dolor sit amet consectetur.</p> <img class="img-fluid d-block mx-auto" src="static/img/portfolio/03-full.jpg" alt=""> <p>Use this area to describe your project. We believe that everyone has a right to earn a living as long as they have a skill / talent. Thats why we created <a href="http://bizbiz.pythonanywhere.com/register">the system</a> so that everyone can register and get clients in their local area</a>!</p> <ul class="list-inline"> <li>Date: January 2017</li> <li>Client: Finish</li> <li>Category: Identity</li> </ul> <button class="btn btn-primary" data-dismiss="modal" type="button"> <i class="fa fa-times"></i> Close Project</button> </div> </div> </div> </div> </div> </div> </div> <!-- Modal 4 --> <div class="portfolio-modal modal fade" id="portfolioModal4" tabindex="-1" role="dialog" aria-hidden="true"> <div class="modal-dialog"> <div class="modal-content"> <div class="close-modal" data-dismiss="modal"> <div class="lr"> <div class="rl"></div> </div> </div> <div class="container"> <div class="row"> <div class="col-lg-8 mx-auto"> <div class="modal-body"> <!-- Project Details Go Here --> <h2 class="text-uppercase">Project Name</h2> <p class="item-intro text-muted">Lorem ipsum dolor sit amet consectetur.</p> <img class="img-fluid d-block mx-auto" src="static/img/portfolio/04-full.jpg" alt=""> <p>Use this area to describe your project. We believe that everyone has a right to earn a living as long as they have a skill / talent. Thats why we created <a href="http://bizbiz.pythonanywhere.com/register">the system</a> so that everyone can register and get clients in their local area</a>!</p> <ul class="list-inline"> <li>Date: January 2017</li> <li>Client: Lines</li> <li>Category: Branding</li> </ul><button class="btn btn-primary" data-dismiss="modal" type="button"> <i class="fa fa-times"></i> Close Project</button> </div> </div> </div> </div> </div> </div> </div> <!-- Modal 5 --> <div class="portfolio-modal modal fade" id="portfolioModal5" tabindex="-1" role="dialog" aria-hidden="true"> <div class="modal-dialog"> <div class="modal-content"> <div class="close-modal" data-dismiss="modal"> <div class="lr"> <div class="rl"></div> </div> </div> <div class="container"> <div class="row"> <div class="col-lg-8 mx-auto"> <div class="modal-body"> <!-- Project Details Go Here --> <h2 class="text-uppercase">Project Name</h2> <p class="item-intro text-muted">Lorem ipsum dolor sit amet consectetur.</p> <img class="img-fluid d-block mx-auto" src="static/img/portfolio/05-full.jpg" alt=""> <p>Use this area to describe your project. We believe that everyone has a right to earn a living as long as they have a skill / talent. Thats why we created <a href="http://bizbiz.pythonanywhere.com/register">the system</a> so that everyone can register and get clients in their local area</a>!</p> <ul class="list-inline"> <li>Date: January 2017</li> <li>Client: Southwest</li> <li>Category: Website Design</li> </ul> <button class="btn btn-primary" data-dismiss="modal" type="button"> <i class="fa fa-times"></i> Close Project</button> </div> </div> </div> </div> </div> </div> </div> <!-- Modal 6 --> <div class="portfolio-modal modal fade" id="portfolioModal6" tabindex="-1" role="dialog" aria-hidden="true"> <div class="modal-dialog"> <div class="modal-content"> <div class="close-modal" data-dismiss="modal"> <div class="lr"> <div class="rl"></div> </div> </div> <div class="container"> <div class="row"> <div class="col-lg-8 mx-auto"> <div class="modal-body"> <!-- Project Details Go Here --> <h2 class="text-uppercase">Project Name</h2> <p class="item-intro text-muted">Lorem ipsum dolor sit amet consectetur.</p> <img class="img-fluid d-block mx-auto" src="static/img/portfolio/06-full.jpg" alt=""> <p>Use this area to describe your project. We believe that everyone has a right to earn a living as long as they have a skill / talent. Thats why we created <a href="http://bizbiz.pythonanywhere.com/register">the system</a> so that everyone can register and get clients in their local area</a>!</p> <ul class="list-inline"> <li>Date: January 2017</li> <li>Client: Window</li> <li>Category: Photography</li> </ul> <button class="btn btn-primary" data-dismiss="modal" type="button"> <i class="fa fa-times"></i> Close Project</button> </div> </div> </div> </div> </div> </div> </div> <button type="submit">SEND</button> <button type="reset">CLEAR FORM</button> </form> </body> </html>''')
                                return render_template('dashboard.html', contspace=contspace, uName=g.user, header=header)
                            elif pageAction == 'colors':
                                header='Edit Colors'
                                contspace=''
                                return render_template('dashboard.html', contspace=contspace, uName=g.user, header=header)
                            elif pageAction == 'Services':
                                header='Edit Services Details'
                                contspace=''
                                return render_template('dashboard.html', contspace=contspace, uName=g.user, header=header)
                            elif pageAction == 'sendMsg':
                                header='Send quick message'

                                nmBox = request.form['nmBox']
                                emBox = request.form['emBox']
                                phBox = request.form['phBox']
                                msgBox = request.form['msgBox']
                                contspace=Markup(dressup.sendMsg(aID,nmBox,emBox,phBox,msgBox))
                                return render_template('dashboard.html', contspace=contspace, uName=g.user, header=header)
                    elif style == 'shop':





                        try:
                            pageAction = request.form['action1']
                        except:
                            contspace = Markup('<p><form method="POST" action=""><label>Change shop name: </label><input type="TEXT" name="aName"><input type="hidden" name="styles" value="shop"><input type="hidden" name="action1" value="changeShopname"><button type="submit">Change</button></form><br /><form method="POST" action=""><input type="radio" name="action1" value="featuredIform">Set featured Images <br /><input type="radio" name="action1" value="addProductform">Add product <br /><input type="radio" name="action1" value="getProducts">Update product <br /><input type="radio" name="action1" value="deleteProductselect">Delete product <br /><input type="radio" name="action1" value="sEttings">Settings <br /><input type="submit"><input type="hidden" name="styles" value="shop"></form><br /></p>')
                            return render_template('dashboard.html', contspace=contspace, title=title, uName=g.user, header='Modify shop website')
                        else:
                            pageAction = request.form['action1']
                            if pageAction == 'addShop':
                                uID = session['uid']
                                aName = request.form['aName'].replace("'","&#39;")
                                contspace = Markup(shopPros.addShop(uID,style,aName))
                                return render_template('dashboard.html', contspace=contspace, title=title, uName=g.user, header='Add shop')
                            elif pageAction == 'changeShopname':
                                aName = request.form['aName'].replace("'", "&#39;")
                                contspace = shopPros.changeShopname(aID,aName)
                                return render_template('dashboard.html', contspace=Markup(contspace), title=title, uName=g.user, header='Shop edit')
                            elif pageAction == "addProductform":
                                #contspace = shopPros.addProduct()
                                contspace = Markup(""" <form method="POST" action=""><input type="hidden" name="action1" value="addProduct"><label>Product Name: </label><input type="TEXT" name="pname"> <br /><label>Product price: </label><input type="TEXT" name="pprice"><br /><label>Description: </label><input type="TEXT" name="pdescription"><br /><label>Category: </label><input type="TEXT" name="pcategory"><br /><label>Subcategory: </label><input type="TEXT" name="psubcategory"><label>Image(link): </label><input type="text" name="pImage"><button type="submit">SEND</button> <button type="RESET">CLEAR FORM</button></form> """)
                                return render_template('dashboard.html', title=title, header='Add a product', uName=g.user, contspace=contspace)
                            elif pageAction == "getProducts":
                                contspace = shopPros.getProducts(aID)

                                #contspace = Markup(""" <form method="POST" action=""><input type="hidden" name="action1" value="updateProduct"><label>Product Name: </label><input type="TEXT" name="pname"> <br /><label>Product price: </label><input type="TEXT" name="pprice"><br /><label>Description: </label><input type="TEXT" name="pdescription"><br /><label>Category: </label><input type="TEXT" name="pcategory"><br /><label>Subcategory: </label><input type="TEXT" name="psubcategory"><button type="submit">SEND</button> <button type="RESET">CLEAR FORM</button></form> """)
                                return render_template('dashboard.html', title=title, header='Your products', uName=g.user, contspace=contspace)
                            elif pageAction == "deleteProductselect":

                                contspace = shopPros.deleteProductselect(aID)
                                #contspace = Markup('<form method="POST" action=""><input type="hidden" name="action1" value="deleteProduct"><p><label>Select product: <select name="product"><option value="##">Product1</option><option value="##">Product2</option></p>')

                                return render_template('dashboard.html', title=title, header='Delete a product', uName=g.user, contspace=contspace)
                            elif pageAction == "deleteProduct":
                                pID = request.form['product']
                                session['pid'] = pID
                                g.pid = session['pid']
                                contspace = shopPros.deleteProduct(pID)
                                return render_template('dashboard.html', title=title, header='Delete product', uName=g.user, contspace=contspace)

                            elif pageAction == "sEttings":
                                getSettings = dressup.getSettings(aID)
                                session['settings'] = getSettings
                                exists = getSettings['exists']
                                if exists == 'no':
                                    contspace = Markup('''<br /><script src="static/js/jscolor.js"></script> <p>Select a color by clicking on the color picker box.Once you confirm, copy the code in the color picker and use it below. <p>Color picker: <input class="jscolor" onchange="update(this.jscolor)" value="cc66ff"> <!--p id="rect" style="border:1px solid gray; width:161px; height:100px;"--> <script> function update(jscolor) { // 'jscolor' instance can be used as a string document.getElementById('rect').style.backgroundColor = '#' + jscolor } </script><br />>>><form method="POST" action=""><input type="hidden" name="action1" value="setSettings"><p><label>Menu background color: </label><input type="TEXT" name="menubg"></p><p><label>Text color: </label><input type="TEXT" name="textcolor"></p><p><label>Description color: </label><input type="TEXT" name="desccolor"></p><p><label>Price color: </label><input type="TEXT" name="pricecolor"></p><p><label>Product names color: </label><input type="TEXT" name="itemncolor"></p><p><button type="submit">SUBMIT</button><button type="reset">CLEAR FORM</button></p>''')
                                    return render_template('dashboard.html', title=title, header='Settings', uName=g.user, contspace=contspace)
                                elif exists == 'yes':
                                    menubg = getSettings['menubg']
                                    textcolor = getSettings['textcolor']
                                    desccolor = getSettings['desccolor']
                                    pricecolor = getSettings['pricecolor']
                                    itemncolor = getSettings['itemncolor']
                                    contspace = Markup('''<form method="POST" action=""><input type="hidden" name="action1" value="updateSettings"><p><label>Menu background color: </label><input type="TEXT" name="menubg" value="{}"></p><p><label>Text color: </label><input type="TEXT" name="textcolor" value="{}"></p><p><label>Description color: </label><input type="TEXT" name="desccolor" value="{}"></p><p><label>Price color: </label><input type="TEXT" name="pricecolor" value="{}"></p><p><label>Product names color: </label><input type="TEXT" name="itemncolor" value="{}"></p><p><button type="submit">SUBMIT</button><button type="reset">CLEAR FORM</button></p>'''.format(menubg,textcolor,desccolor,pricecolor,itemncolor))
                                    return render_template('dashboard.html', contspace=contspace, title=title, uName=g.user, header='Settings')
                            elif pageAction == "setSettings":
                                menubg = request.form['menubg']
                                textcolor = request.form['textcolor']
                                desccolor = request.form['desccolor']
                                pricecolor = request.form['pricecolor']
                                itemncolor = request.form['itemncolor']
                                contspace = dressup.setSettings(aID,menubg,textcolor,desccolor,pricecolor,itemncolor)
                                return render_template('dashboard.html', contspace=contspace, title=title, uName=g.user, header='Settings')
                            elif pageAction == "updateSettings":
                                menubg = request.form['menubg']
                                textcolor = request.form['textcolor']
                                desccolor = request.form['desccolor']
                                pricecolor = request.form['pricecolor']
                                itemncolor = request.form['itemncolor']
                                    #contspace = Markup('<form method="POST" action=""><input type="hidden" name="action1" value="setSettings"><p><label>Menu background color: </label><input type="TEXT" name="menubg" value="{}"></p><p><label>Text color: </label><input type="TEXT" name="textcolor" value="{}"></p><p><label>Description color: </label><input type="TEXT" name="desccolor" value="{}"></p><p><label>Price color: </label><input type="TEXT" name="pricecolor" value="{}"></p><p><label>Product names color: </label><input type="TEXT" name="itemncolor" value="{}"></p><p><button type="submit">SUBMIT</button><button type="reset">CLEAR FORM</button></p>'.format(menubg,textcolor,desccolor,pricecolor,itemncolor))

                                contspace = dressup.updateSettings(aID,menubg,textcolor,desccolor,pricecolor,itemncolor)
                                return render_template('dashboard.html', contspace=contspace, title=title, uName=g.user, header='Settings')

                            elif pageAction == "addProduct":

                                pName = request.form['pname'].replace("'", "&#39;")
                                pPrice = request.form['pprice'].replace("'", "&#39;")
                                pDescription = request.form['pdescription'].replace("'", "&#39;")
                                pCategory = request.form['pcategory'].replace("'", "&#39;")
                                pSubcategory = request.form['psubcategory'].replace("'", "&#39;")
                                pImage = request.form['pImage']
                                contspace = shopPros.addProduct(aID,pName,pPrice,pDescription,pCategory,pSubcategory,pImage)


                                return render_template('dashboard.html', contspace=contspace, title=title, uName=g.user, header='Add product')
                            elif pageAction == 'updateProductform':
                                contspace = Markup('<form method="POST" action=""><input type="hidden" name="action1" value="addProduct"><input type="hidden" name="styles" value="shop"><label>Product Name: </label><input type="TEXT" name="pname" value="{}"> <br /><label>Product price: </label><input type="TEXT" name="pprice" value="{}"><br /><label>Description: </label><input type="TEXT" name="pdescription" value="{}><br /><label>Category: </label><input type="TEXT" name="pcategory" value="{}><br /><label>Subcategory: </label><input type="TEXT" name="psubcategory" value="{}><label>Image: </label><input type="text" name="pImage" value="{}"><button type="submit">SEND</button> <button type="RESET">CLEAR FORM</button></form>'.format(session['product']['pName'],session['product']['pPrice'],session['product']['pDescription'],session['product']['pCategory'],session['product']['pSubcategory'],session['product']['pImage']))
                                return render_template('dashboard.html', contspace=contspace, title=title, uName=g.user, header='Edit product')
                            elif pageAction == 'updateProductdata':
                                pID = request.form['product']
                                session['pid'] = pID
                                g.pid = session['pid']
                                contspace=shopPros.getProductdata(pID)

                                return render_template('dashboard.html', contspace=contspace, title=title, uName=g.user, header='Edit product')
                            elif pageAction == 'updateProduct':
                                pID = session['pid']
                                pName = request.form['pname'].replace("'", "&#39;")
                                pPrice = request.form['pprice'].replace("'", "&#39;")
                                pDescription = request.form['pdescription'].replace("'", "&#39;")
                                pCategory = request.form['pcategory'].replace("'", "&#39;")
                                pSubcategory = request.form['psubcategory'].replace("'", "&#39;")
                                pImage = request.form['pImage']

                                contspace = shopPros.updateProduct(pID,pName,pPrice,pDescription,pCategory,pSubcategory,pImage)
                                return render_template('dashboard.html', contspace=contspace, title=title, uName=g.user, header='Update product')
                            elif pageAction == 'featuredIform':
                                getFimages = shopPros.getFimages(aID)
                                getFs = getFimages['exists']
                                if getFs == 'no':
                                    contspace = Markup('<p>For best results use 900 x 350 images</p><br /><form method="POST" action=""><input type="hidden" name="action1" value="setFimages"<p><label>1<sup>st</sup> Image(link): </label><input name="firstI" type="TEXT"></p><p><label>1<sup>st</sup> Image(link): </label><input name="secondI" type="TEXT"></p><p><label>3<sup>rd</sup> Image(link): </label><input name="thirdI" type="TEXT"></p><p><button type="submit">SUBMIT</button><button type="reset">CLEAR FORM</button></p>')
                                    return render_template('dashboard.html', contspace=contspace, title=title, uName=g.user, header='Set featured Images')
                                elif getFs == 'yes':
                                    contspace = Markup('<p>For best results use 900 x 350 images</p><br /><form method="POST" action=""><input type="hidden" name="action1" value="setFimages"<p><label>1<sup>st</sup> Image(link): </label><input name="firstI" type="TEXT" value={}></p><p><label>1<sup>st</sup> Image(link): </label><input name="secondI" type="TEXT" value={}></p><p><label>3<sup>rd</sup> Image(link): </label><input name="thirdI" type="TEXT" value={}></p><p><button type="submit">SUBMIT</button><button type="reset">CLEAR FORM</button></p>'.format(getFimages['firstI'],getFimages['secondI'],getFimages['thirdI']))
                                    return render_template('dashboard.html', contspace=contspace, title=title, uName=g.user, header='Set featured Images')
                            elif pageAction == 'setFimages':
                                firstI = request.form['firstI']
                                secondI = request.form['secondI']
                                thirdI = request.form['thirdI']
                                getFimages = shopPros.getFimages(aID)
                                getFs = getFimages['exists']
                                setFimages = shopPros.setFimages(getFs,aID,firstI,secondI,thirdI)
                                contspace= setFimages

                                return render_template('dashboard.html', contspace=contspace, title=title, uName=g.user, header='Featured Images set')













                        contspace = Markup('<p><form method="POST" action=""><label>Change name: </label><input type="TEXT" name="aNAme"><input type="hidden" name="styles" value="shop"><input type="hidden" name="action1" value=""><button type="submit">Change</button></form>. <form method="POST" action=""><input type="radio" name="action1" value="addProductform">Add product <input type="radio" name="action1" value="updateProductform">Update product <br /><input type="radio" name="action1" value="deleteProduct">Delete product <br /><input type="radio" name="action1" value="sEttingsform">Settings <br /><input type="submit"><input type="hidden" name="styles" value="shop"></form><br /><table><tr><td>Add </td><td>Update </td></tr><tr><td>Delete </td><td>Settings </td></tr></table></p>')
                        #form = getformdata.getshop(aID)
                        return render_template('dashboard.html', title=title, contspace=contspace, uName=g.user, header='Edit shop')
                elif checklogin == 'bad':
                    return 'Sorry, you are not logged in or our details were incorrect. Try again'
@app.route("/msgs", methods=['POST'])
def msgs():
    aID = request.form['abcd']
    nmBox = request.form['nmBox'].replace("'", "&#39;")
    emBox = request.form['emBox'].replace("'", "&#39;")
    phBox = request.form['phBox'].replace("'", "&#39;")
    msgBox = request.form['msgBox'].replace("'", "&#39;")
    contspace=Markup(dressup.sendMsg(aID,nmBox,emBox,phBox,msgBox))

    return render_template('index.html',contspace=contspace,title='Message sent',account='out')

@app.route("/msg", methods=['POST'])
def msg():
    aID = request.form['abcd']
    homepage = request.form['homepage']
    nmBox = request.form['nmBox'].replace("'", "&#39;")
    emBox = request.form['emBox'].replace("'", "&#39;")
    phBox = request.form['phBox'].replace("'", "&#39;")
    msgBox = request.form['msgBox'].replace("'", "&#39;")
    contspace=Markup(dressup.sendMsg(aID,nmBox,emBox,phBox,msgBox) + '. <a href="{}">go to homepage</a>'.format(homepage))

    return contspace



@app.route("/submitedits", methods=['GET', 'POST'])
def subeds():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'

    if request.method == "POST":
        fName = request.form['fName']
        lName = request.form['lName']
        aImage = request.form['aImage']
        sAddress = request.form['sAddress']
        pHone = request.form['pHone']
        eMail = request.form['eMail']
        dEscription = request.form['dEscription']
        tItle1 = request.form['tItle1']
        tItle2 = request.form['tItle2']
        tItle3 = request.form['tItle3']
        tItle4 = request.form['tItle4']
        cOmpany1 = request.form['cOmpany1']
        cOmpany2 = request.form['cOmpany2']
        cOmpany3 = request.form['cOmpany3']
        cOmpany4 = request.form['cOmpany4']
        dEscription1 = request.form['dEscription1']
        dEscription2 = request.form['dEscription2']
        dEscription3 = request.form['dEscription3']
        dEscription4 = request.form['dEscription4']
        exDate1 = request.form['exDate1']
        exDate2 = request.form['exDate2']
        exDate3 = request.form['exDate3']
        exDate4 = request.form['exDate4']
        iNstitution1 = request.form['iNstitution1']
        iNstitution2 = request.form['iNstitution2']
        pRogramme1 = request.form['pRogramme1']
        pRogramme2 = request.form['pRogramme2']
        cOurse1 = request.form['cOurse1']
        cOurse2 = request.form['cOurse2']
        gRade1 = request.form['gRade1']
        gRade2 = request.form['gRade2']
        edDate1 = request.form['edDate1']
        edDate2 = request.form['edDate2']
        sKill1 = request.form['sKill1']
        sKill2 = request.form['sKill2']
        sKill3 = request.form['sKill3']
        sKill4 = request.form['sKill4']
        sKill5 = request.form['sKill5']
        sKill6 = request.form['sKill6']
        iNterest1 = request.form['iNterest1']
        iNterest2 = request.form['iNterest2']
        iNterest3 = request.form['iNterest3']
        iNterest4 = request.form['iNterest4']
        iNterest5 = request.form['iNterest5']
        iNterest6 = request.form['iNterest6']
        aWard1 = request.form['aWard1']
        aWard2 = request.form['aWard2']
        aWard3 = request.form['aWard3']
        aWard4 = request.form['aWard4']
        aName = request.form['aName']

        try:
            g.user = session['user']
            g.password = session['password']
            g.uid = session['uid']
            g.edit = session['edit']
        except:
            picspace = ''
            return redirect(url_for('sign_in'))
        else:
            if g.user and g.password:

                uName = g.user
                uPass = g.password
                checklogin = dressup.checklogin(uName,uPass)

                if checklogin == 'good':

                    g.user = session['user']
                    g.password = session['password']
                    g.uid = session['uid']
                    aID = session['edit']
                    #session['edit'] = aID

                    style = dressup.getstyle(aID)


                    if style == 'resume':
                        subs = subedits.resume(style,aID,fName,lName,sAddress,pHone,eMail,dEscription,tItle1,tItle2,tItle3,tItle4,cOmpany1,cOmpany2,cOmpany3,cOmpany4,dEscription1,dEscription2,dEscription3,dEscription4,exDate1,exDate2,exDate3,exDate4,iNstitution1,iNstitution2,pRogramme1,pRogramme2,cOurse1,cOurse2,gRade1,gRade2,edDate1,edDate2,sKill1,sKill2,sKill3,sKill4,sKill5,sKill6,iNterest1,iNterest2,iNterest3,iNterest4,iNterest5,iNterest6,aWard1,aWard2,aWard3,aWard4,aName,aImage)
                    contspace = subs
                    return render_template('dashboard.html', user=g.user, header='Website updated', contspace=contspace)


    elif request.method=="GET":
        return redirect(url_for('dashmodify'))



            #if yes:
                #update relevant table

@app.route("/dashboard-deletewebsite", methods=['POST', 'GET'])
def dashdelete():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    picspace = ''
    contspace = ''
    title = ''


    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        return redirect(url_for('sign_in'))
    else:
        uName = g.user
        uPass = g.password

        checklogin = dressup.checklogin(uName,uPass)
        if checklogin == 'good':

            if request.method == "GET":
                uID = g.uid
                getassets = dressup.getassets(uID)
                contspace = getassets
                return render_template('dashboard.html', header='Delete a website', uName=g.user, contspace=contspace, title=title)
            elif request.method == "POST":
                session['edit'] = request.form['edit']
                g.edit = session['edit']
                aID = g.edit
                style = dressup.getstyle(aID)
                delpage = dressup.delpage(aID,style)
                contspace = delpage
                return render_template('dashboard.html', header='Deleted', uName=g.user, title=title, contspace=contspace)
        elif checklogin == 'bad':
            contspace = 'We could not find something. Try logging in a fresh.'
            return render_template('dashboard.html', header='Delete a website', uName=g.user, contspace=contspace, title=title)



@app.route("/requirements", methods=['GET', 'POST'])
def require():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    if request.method == 'GET':
        title = 'Requirements and website development steps'
        picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')
        contspace = Markup('''<p>You need:</p><p><ol><li><h2 class="titles">A budget</h2><p>When it comes to owning and operating a website, a budget is crucial especially since there are many <a class="links" href="/">options</a>. And again, your budget should reflect the scale of your web projects. A NGO website may cost around $300 if you want a website you can update on your own. A static website will cost less because it is generally faster to make and requires less testing and debugging. But it is a good idea to create a dynamic website which you can change images, text, videos and even more.</p></li><li><h2 class="titles">A design</h2><p>A good design should be beautiful, fast and usable on as many devices as possible. Specifications including RAM, ROM, Internet speed, browser, screen size e.t.c. have a big effect on the user-experience on your website. A design may look very beautiful but it takes an awful long time to load for guyz on slow connections. Again, some old designs look very nice when you view them on the computer but on mobile, they become unusable. Therefore, though some designs may seem more basic than others, the same design may be better suited for more users on more devices. That's why one of our development <a class="links" href="values">values</a> is to create websites that are usable on as many devices as possible. So when we design, we design it to be fast and universaly usable.</p></li><li><h2 class="titles">A <a href="requirements" class="links">domain</a> name</h2><p>A <a href="requirements" class="links">domain</a> name is a good investment. It is possible to host your website for free with just a subdomain name. What is a <a href="requirements" class="links">domain</a> and subdomain name? e.g.: http://BIZBIZ.pythonanywhere.com In the example the <a href="requirements" class="links">domain</a> name is pythonanywhere.com and the subdomain name is BIZBIZ. A <a href="requirements" class="links">domain</a> name can cost anywhere from $0.84 to more than $35 depending on the SLD (.org, .com, .net, e.t.c) and whether it's 'second hand' or new. A .com costs around $10 yearly</p></li><li><h2 class="titles">A <a href="requirements" class="links">hosting</a> plan</h2><p>After you have a <a href="requirements" class="links">domain</a> name, you need to get a <a href="requirements" class="links">hosting</a> plan. This means paying for someones 24/7 server to host your files so that they can be online 24/7. A good <a href="requirements" class="links">hosting</a> plan should guarantee a 99.99% - 100% uptime. <a href="requirements" class="links">hosting</a> plans range in price from one company to another and the best consideration is whether the host offers tools which can bring your website design to life. Avoid free hosting plans; better you go for the free website builder than to purchase a name and get free hosting from a different company.</p></li><ul type="circle"><li>Free <a href="requirements" class="links">hosting</a> plan</li><li>Paid <a href="requirements" class="links">hosting</a> plan</li></ul><li><h2 class="titles">Development Period</h2><p>After you have the design, name and <a href="requirements" class="links">hosting</a> plan you can begin development of your good website and the development time will depend on the overall size of your website and tools being utilized. I cannot stress enough that there are many ways to build a website.</p></li></ol></p><p><form method="POST" action="requirements"><button id="quote" class="dropbtn" type="SUBMIT">REQUEST QUOTE</button><input type="hidden" name="want" value="requestform"></form></p>''')
        return render_template('index.html', account=account, title=title, picspace=picspace, contspace=contspace)
    if request.method == 'POST':
        title = 'Request Quote'
        picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')
        yesOrder = request.form['want']
        if yesOrder == 'request':

            email = request.form['email']
            budget = request.form['budget'].replace("'", "&#39;")
            design = request.form['design'].replace("'", "&#39;")
            domain = request.form['domain'].replace("'", "&#39;")
            hosting = request.form['hosting'].replace("'", "&#39;")
            period = request.form['period'].replace("'", "&#39;")


            contspace=dressup.saveOrder(email,budget,design,domain,hosting,period)
            return render_template('index.html', account=account, title=title, picspace=picspace, contspace=contspace)
        elif yesOrder == 'requestform':
            contspace=Markup('<br /><form method="POST" action="requirements"><p><label>Email: </label><input type="TEXT" name="email"></p><h2 class="titles">What is your budget?</h2><br /><p><textarea name="budget" cols="80" rows="20" style="margin: 0px; width: 818px; height: 319px;"></textarea></p><h2 class="titles">Describe your preferred design</h2><br /><p><textarea name="design" cols="80" rows="20" style="margin: 0px; width: 818px; height: 319px;"></textarea></p><h2 class="titles">What is your preffered domain name?</h2><br /><p><textarea name="domain" cols="80" rows="20" style="margin: 0px; width: 818px; height: 319px;"></textarea></p><h2 class="titles">How would you like to host your website</h2><br /><p><textarea name="hosting" cols="80" rows="20" style="margin: 0px; width: 818px; height: 319px;"></textarea></p><h2 class="titles">How long do we have to develop?</h2><br /><p><textarea name="period" cols="80" rows="20" style="margin: 0px; width: 818px; height: 319px;"></textarea></p><button class="dropbtn" type="submit">GET QUOTE</button> <button type="reset">CLEAR FORM</button><input type="hidden" name="want" value="request"></form>')
            return render_template('index.html', account=account, picspace=picspace,contspace=contspace,title=title)
@app.route("/contact")
def cont():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    title = 'Contact us'
    picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')
    contspace = Markup('<iframe src="https://docs.google.com/forms/d/e/1FAIpQLScfyDAyMuWWr0Bsbp8_ZXgR-TWqGirlt3QQWN03yhevc51RSg/viewform?embedded=true" width="100%" height="500%" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe>')
    return render_template('index.html', account=account, title=title, picspace=picspace, contspace=contspace)

@app.route("/terms")
def ter():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    title = 'Terms of use'
    picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')
    contspace = Markup('<br /><h2 class="titles">TERMS OF USE</h2><p>The user of this service should take proper care of him/herself.</p><p>You may not rush to meet someone you do not know especially, without limitation, to people outside your local area.</p><p>Stay aware that information you submit online including on this website, can be hacked and a bad person could look at the details you provide here. The bad person could use the information against you. Therefore, all users are advised to use separate contacts, names & addresses.</p><p>b) However, automatic systems, user mistakes, acts of God and other factors may cause your real information to come out plainly.</p><p>All payments made to this service during registration are non-refundable. Donations and good will tokens are also accepted. Compliments and comments should be directed to us through the website or other official contacts.</p><p>The service is not perfect. It may encounter glitches but we will work to resolve such glitches.</p><br />')
    return render_template('index.html', account=account, title=title, picspace=picspace, contspace=contspace)

@app.route("/testimonies")
def tes():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    title = 'Testimonies'
    picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')
    #contspace = Markup('<p><table><tr><td><iframe src="https://www.facebook.com/plugins/like.php?href=https%3A%2F%2Fwww.facebook.com%2Fpg%2FBiasharaEmployers&width=450&layout=standard&action=like&size=small&show_faces=true&share=true&height=80&appId=160496944307741" width="450" height="80" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowTransparency="true"></iframe></td></tr><tr><td><iframe src="https://www.facebook.com/plugins/share_button.php?href=http%3A%2F%2Fbizbiz.pythonanywhere.com%2Ffind&layout=button_count&size=small&mobile_iframe=true&appId=160496944307741&width=69&height=20" width="69" height="20" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowTransparency="true"></iframe></td></tr></table><br /><iframe src="https://www.facebook.com/plugins/page.php?href=https%3A%2F%2Fwww.facebook.com%2FBiasharaEmployers&tabs=timeline&width=700&height=500&small_header=false&adapt_container_width=true&hide_cover=false&show_facepile=true&appId=160496944307741" width="700" height="500" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowTransparency="true"></iframe><br />')
    contspace = Markup('<iframe src="https://www.facebook.com/plugins/page.php?href=https%3A%2F%2Fwww.facebook.com%2FBiashara.Web.Development&tabs=timeline&width=340&height=500&small_header=false&adapt_container_width=true&hide_cover=false&show_facepile=true&appId=160496944307741" width="700" height="500" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowTransparency="true"></iframe>')
    return render_template('index.html', account=account, title=title, picspace=picspace, contspace=contspace)

@app.route("/values")
def val():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    title = 'Our Values'
    picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')
    contspace = Markup('<br /><h2 class="titles">Our development values</h2><br /><ol><li><h3 class="h3s">Fast loading- to save time and power costs</h3><p>Performance is our No. 1 priority when we develop websites. It gives us pride when a website loads instantly even on slow networks. Usually, performance is weighed against the visual appearence including animations. We prefer for a website to have less loading time and less crashes which are common for very visual web tools.</p></li><li><h3 class="h3s">Device universal- to increse value and reduce inequality</h3><p>People across the world access the internet on different devices, browsers, disk space and bandwidth. All these affect the internet experience and thats why we avoid giving too much priority to tools which will be disabled on particular devices and browser. For example Javascript is disabled by default on most native browsers.</p></li><li><h3 class="h3s">Stateless- to make website more affordable and easily scalable</h3><p>This means that the server does not carry any unnecessary data. A server can just be as troubled as a phone when it is suddenly full of old media and other data. Usually, when you get a <a href="requirements" class="links">hosting plan</a>, your disk space is limited so you should not store unnecessary data on the sever. This is why we develop our websites and web apps, to operate <a href="privacy" class="links">statelessly</a> when we can.</p></li><li><h3 class="h3s">Uniform interface- to save time and data charges</h3><p>With the help of caching, browsers such as chrome can save a routine resource in temporary memory so it does not need to download or render it every single time. This makes the website load faster and saves on data charges.</p></li></ol>')
    return render_template('index.html', account=account, title=title, picspace=picspace, contspace=contspace)

@app.route("/savedata")
def save():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    fName = request.form['fName']
    lName = request.form['lName']
    sAddress = request.form['sAddress']
    pHone = request.form['pHone']
    eMail = request.form['eMail']
    dEscription = request.form['dEscription']
    eXperience = request.form['eXperience']
    eDucation = request.form['eDucation']
    sKills = request.form['sKills']
    iNterests = request.form['iNterests']
    aWards = request.form['aWards']

    #SAVE DATA TO TABLE
    #PREVIEW WEBSITE

@app.route("/contacts", methods=['GET', 'POST'])
def conts():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    picspace = ''
    title = 'Websites contacts'

    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        return redirect(url_for('sign_in'))
    else:
        uName = session['user']
        uPass = session['password']
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']

        checklogin = dressup.checklogin(uName,uPass)
        if checklogin == 'good':
            if request.method == 'GET':
                uID = session['user']
                getassets = dressup.getassets(uID)
                contspace = getassets
                return render_template('dashboard.html',uName=g.user,header='Select website',contspace=contspace,title=title)
            elif request.method == 'POST':

                try:
                    pageAction = request.form['action1']
                except:

                    aID = request.form['edit']
                    session['edit'] = aID
                    g.edit = session['edit']
                    g.user = session['user']
                    contacts = dressup.getContacts(aID)
                    contspace=Markup(contacts)
                    return render_template('dashboard.html',uName=g.user,header='Edit websites contacts',contspace=contspace,title=title)
                else:
                    pageAction = request.form['action1']
                    if pageAction == 'sendContdata':

                        aID = session['edit']
                        email = request.form['email'].replace("'", "&#39;")
                        about = request.form['about'].replace("'", "&#39;")
                        website = request.form['website'].replace("'", "&#39;")
                        phone = request.form['phone'].replace("'", "&#39;")
                        pAddress = request.form['pAddress'].replace("'", "&#39;")
                        country = request.form['country'].replace("'", "&#39;")
                        city = request.form['city'].replace("'", "&#39;")
                        fb = request.form['fb'].replace("'", "&#39;")
                        tweet = request.form['tweet'].replace("'", "&#39;")
                        lin = request.form['lin'].replace("'", "&#39;")
                        github = request.form['github'].replace("'", "&#39;")

                        sendContdata = dressup.sendContdata(aID,email,about,website,phone,pAddress,country,city,fb,tweet,lin,github)
                        contspace = sendContdata
                        return render_template('dashboard.html',uName=g.user,header='Edit websites contacts',contspace=contspace,title=title)
                    elif pageAction == 'newCont':
                        aID = session['edit']
                        email = request.form['email'].replace("'", "&#39;")
                        about = request.form['about'].replace("'", "&#39;")
                        website = request.form['website'].replace("'", "&#39;")
                        phone = request.form['phone'].replace("'", "&#39;")
                        pAddress = request.form['pAddress'].replace("'", "&#39;")
                        country = request.form['country'].replace("'", "&#39;")
                        city = request.form['city'].replace("'", "&#39;")
                        fb = request.form['fb'].replace("'", "&#39;")
                        tweet = request.form['tweet'].replace("'", "&#39;")
                        lin = request.form['lin'].replace("'", "&#39;")
                        github = request.form['github'].replace("'", "&#39;")

                        newcont = dressup.newCont(aID,email,about,website,phone,pAddress,country,city,fb,tweet,lin,github)
                        contspace = newcont

                        return render_template('dashboard.html',uName=g.user,header='Edit websites contacts',contspace=contspace,title=title)

        elif checklogin == 'bad':
            contspace = 'We could not find something. Try logging in a fresh.'
            return render_template('index.html', account=account, picspace=picspace, contspace=contspace, title=title)

@app.route("/inbox", methods=['POST', 'GET'])
def inboxme():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        picspace = ''
        return redirect(url_for('sign_in'))
    else:

        if g.user and g.password:
            uName = g.user
            uPass = g.password
            checklogin = dressup.checklogin(uName,uPass)
            uID=g.uid


            if checklogin == 'good':
                if request.method == 'GET':

                    contspace = Markup(dressup.getassets(uID))
                    title='Dashboard'
                    return render_template('dashboard.html', uName=g.user, header='Your super Inbox', contspace=contspace)
                elif request.method == 'POST':
                    try:
                        pageAction=request.form['action1']
                    except:
                        aID = request.form['edit']
                        session['edit']=aID
                        contspace = Markup(dressup.makeMail(aID))
                        title='Dashboard'
                        return render_template('dashboard.html', uName=g.user, header='Your own Inbox', contspace=contspace)
                    else:
                        pageAction=request.form['action1']


                        if pageAction == 'delMsg':
                            pID =request.form['delThis']
                            delThis = dressup.delMsg(pID)

                            contspace = Markup(delThis)
                            title='Dashboard'
                            return render_template('dashboard.html', uName=g.user, header='Your own Inbox', contspace=contspace)

                        elif pageAction == 'vThis':
                            pID =request.form['vThis']
                            delThis = dressup.vThis(pID)

                            contspace = Markup(delThis)
                            title='Dashboard'
                            return render_template('dashboard.html', uName=g.user, header='Inbox viewer', contspace=contspace)

            elif checklogin == 'bad':
                picspace = ''
                title = 'Not logged in'
                return render_template('index.html', account=account, title=title, picspace=picspace, contspace='You must be logged in to view the dashboard')
@app.route("/colors", methods=['POST', 'GET'])
def colors():
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        picspace = ''
        return redirect(url_for('sign_in'))
    else:

        if g.user and g.password:
            uName = g.user
            uPass = g.password
            checklogin = dressup.checklogin(uName,uPass)
            uID=g.uid


            if checklogin == 'good':
                if request.method == 'GET':

                    contspace = Markup(dressup.getassets(uID))
                    title='Dashboard'
                    return render_template('dashboard.html', uName=g.user, header='Edit colors', contspace=contspace)
                elif request.method == 'POST':
                    try:
                        pageAction=request.form['action1']
                    except:
                        aID = request.form['edit']
                        session['edit']=aID

                        #contspace= Markup('')
                        #contspace=Markup(agencypro.lookupColors(aID))
                        try:
                            contspace = agencypro.lookupColors(aID)['tpMenu']
                        except:
                            contspace = Markup(agencypro.lookupColors(aID))
                            return render_template('dashboard.html', uName=g.user, header='Edit colors', contspace=contspace)
                        else:
                            lookupColors = agencypro.lookupColors(aID)
                            contspace = 'Fill the text boxes with color codes, which begin with a #. For example <font style="color:#4286f4;">#4286f4</font> or <font style="color:#80f442;">#80f442</font> or <font style="color:#d1578e;">#d1578e</font> or <font style="color:#4b658e;">#4b658e</font> or just use color names like <font style="color:yellow;">yellow</font> or <font style="color:brown;">brown</font> or <font style="color:pink;">pink</font> or <font style="color:green;">green</font>. For more codes google: "<a target="_blank" href="https://www.google.com/search?q=color+picker&oq=color+">Color picker</a>"<br />Place the cursor over the textbox to see what the box is for.<br /><br /><form method="POST" action=""><input type="hidden" name="action1" value="updateColors"> <p><label>Top menu background: </label><input type="text" name="tpMenu" value="{}" title="Set the color for the background of the top menu which has links like SERVICES, PORTFOLIO etc"></p> <p><label>Top menu links: </label><input type="text" name="tpLinks" value="{}" title="Sets the color of the texts in the top menu. Those are: SERVICES, PORTFOLIO, ABOUT, TEAM, CONTACT"></p> <p><label>Welcome to: </label><input type="text" name="welTo" value="{}" title="Sets the color of the -Welcome to- located on the homepage"></p> <p><label>Slogan: </label><input type="text" name="slogan" value="{}" title="Sets the color of slogan/Vision on the homepage"></p> <p><label>Tell me more background: </label><input type="text" name="tMoreb" value="{}" title="Sets the background color of the button written -Tell me more- on the homepage"></p> <p><label>Tell me more text color: </label><input type="text" name="tMoret" value="{}" title="Sets the text color of the button written -Tell me more- on the homepage"></p> <p><label>Headings: </label><input type="text" name="hdNg" value="{}" title="Sets the background color of Headings in your website e.g. PORTFOLIO, MILESTONES, SERVICES and all other headings of the same size"></p> <p><label>Sub headings: </label><input type="text" name="sbHdng" value="{}" title="Sets the background color of subheading under the Headings"></p> <p><label>Titles: </label><input type="text" name="titles" value="{}" title="Sets the background color of titles of portfolio items, services and other texts of the same size"></p> <p><label>Normal text color: </label><input type="text" name="nTxt" value="{}" title="Sets the background color of normal paragraph texts"></p> <!--p><label></label><input type="text" name=""></p> <p><label></label><input type="text" name=""></p> <p><label></label><input type="text" name=""></p--> <p><button type="SUBMIT">SAVE COLORS</button></form></p>'.format(lookupColors['tpMenu'],lookupColors['tpLinks'],lookupColors['welTo'],lookupColors['slogan'],lookupColors['tMoreb'],lookupColors['tMoret'],lookupColors['hdNg'],lookupColors['sbHdng'],lookupColors['titles'],lookupColors['nTxt'])
                            contspace=Markup(contspace)
                            return render_template('dashboard.html', uName=g.user, header='Edit colors', contspace=contspace)
                    else:
                        pageAction=request.form['action1']

                        aID = session['edit']
                        if pageAction == 'newColors':

                            tpMenu= request.form['tpMenu']
                            tpLinks= request.form['tpLinks']
                            welTo= request.form['welTo']
                            slogan= request.form['slogan']
                            tMoreb= request.form['tMoreb']
                            tMoret= request.form['tMoret']
                            hdNg= request.form['hdNg']
                            sbHdng= request.form['sbHdng']
                            titles= request.form['titles']
                            nTxt= request.form['nTxt']
                            contspace = Markup(agencypro.newColors(aID,tpMenu,tpLinks,welTo,slogan,tMoreb,tMoret,hdNg,sbHdng,titles,nTxt))
                            title='Dashboard'
                            return render_template('dashboard.html', uName=g.user, header='Colors', contspace=contspace)

                        elif pageAction == 'updateColors':

                            tpMenu= request.form['tpMenu']
                            tpLinks= request.form['tpLinks']
                            welTo= request.form['welTo']
                            slogan= request.form['slogan']
                            tMoreb= request.form['tMoreb']
                            tMoret= request.form['tMoret']
                            hdNg= request.form['hdNg']
                            sbHdng= request.form['sbHdng']
                            titles= request.form['titles']
                            nTxt= request.form['nTxt']
                            contspace = Markup(agencypro.updateColors(aID,tpMenu,tpLinks,welTo,slogan,tMoreb,tMoret,hdNg,sbHdng,titles,nTxt))
                            title='Dashboard'
                            return render_template('dashboard.html', uName=g.user, header='Colors', contspace=contspace)

@app.errorhandler(500)
def errfourhu(err):
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    title = 'Error occured'
    picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')
    contspace=Markup('An error occured. Try again. And if you keep getting the same, <a class="links" href="contact">contact us</a>.<br />If you were submitting something, try again with less special characters like &#39; and <a class="links" href="contact">let us know</a>')
    return render_template('index.html',account=account, title=title, picspace=picspace, contspace=contspace)

@app.errorhandler(404)
def errfourhu(err):
    try:
        g.user = session['user']
        g.password = session['password']
        g.uid = session['uid']
    except:
        account = 'out'
    else:
        account = 'in'
    title = 'Error occured'
    picspace = Markup('<img style="bgcolor:#a7a8aa;" src="static/me&ochieng.jpg" />')
    contspace = Markup('<h3 class="h3s">That could not be found. Check the address and try again or <a class="links" href="/" style="text-decoration:none;color:green;">go to homepage</a>.</h3>')
    return render_template('index.html',account=account, title=title, picspace=picspace, contspace=contspace)

if __name__ == "__main__":
    app.run(debug = False)
