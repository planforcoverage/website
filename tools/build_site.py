import os, re
S=os.path.join(os.path.dirname(os.path.abspath(__file__)),'')

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PHONE = "(424) 362-9253"
PHONE_TEL = "+14243629253"
EMAIL = "ebecker@planforcoverage.com"
CA_LIC = "Eric Becker · CA Insurance License #0I16359 · NPN 16853098"
STATES = ["California","Arizona","Florida","Georgia","Michigan","Ohio","Oregon","Tennessee","Texas","Utah"]

SERVICES = [
 ("major-medical","Major Medical","ACA marketplace and off-exchange plans for individuals, families and the self-employed."),
 ("accident","Accident Insurance","Cash benefits paid directly to you after an injury, to cover what your health plan doesn't."),
 ("hospital-indemnity","Hospital Indemnity","A fixed daily benefit for hospital stays that helps absorb deductibles and lost income."),
 ("critical-illness","Critical Illness","A lump sum on diagnosis of a covered condition such as cancer, heart attack or stroke."),
 ("dental","Dental","Standalone dental plans for cleanings, fillings, crowns and more."),
 ("vision","Vision","Exams, frames, lenses and contacts at a predictable cost."),
]

def nav(depth):
    p = "../" * depth
    svc = "".join(f'<li><a href="{p}services/{s}.html">{n}</a></li>' for s,n,_ in SERVICES)
    return f"""
<header class="site-header">
  <a class="brand" href="{p}index.html"><span class="brand-mark" aria-hidden="true"></span>Plan For Coverage</a>
  <button class="nav-toggle" aria-expanded="false" aria-controls="nav">Menu</button>
  <nav id="nav" class="nav">
    <ul>
      <li><a href="{p}index.html">Home</a></li>
      <li class="has-sub"><a href="{p}services/index.html">Services</a>
        <ul class="sub">{svc}<li><a href="{p}services/medicare.html">Medicare referrals</a></li></ul>
      </li>
      <li><a href="{p}california/index.html">California</a>
      </li>
      <li><a href="{p}about.html">About</a></li>
      <li><a href="{p}contact.html">Contact</a></li>
    </ul>
    <a class="btn btn-amber nav-cta" href="{p}contact.html">Request a quote</a>
  </nav>
</header>"""

def footer(depth):
    p = "../" * depth
    return f"""
<footer class="site-footer">
  <div class="foot-grid">
    <div>
      <p class="foot-brand">Plan For Coverage</p>
      <p>Independent health and life insurance broker based in California, licensed in ten states.</p>
      <p>{CA_LIC}</p>
    </div>
    <div>
      <h3>Eric Becker, broker</h3>
      <p>Cell: <a href="tel:{PHONE_TEL}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <h3>Hours</h3>
      <p>Monday – Friday, 9:00 am – 5:00 pm Pacific<br>Evenings and weekends by appointment</p>
    </div>
    <div>
      <h3>Pages</h3>
      <p><a href="{p}services/index.html">Services</a><br><a href="{p}about.html">About</a><br><a href="{p}contact.html">Request a quote</a><br><a href="{p}privacy.html">Privacy policy</a></p>
    </div>
  </div>
  <p class="foot-legal">© 2026 Plan For Coverage. Licensed in {", ".join(STATES)}. Not affiliated with or endorsed by Medicare, CMS or any government agency. Plan availability and benefits vary by state and carrier; this site is general information, not an offer of coverage.</p>
</footer>
<script src="{p}assets/site.js"></script>"""

def page(path, title, desc, body, depth=0):
    p = "../" * depth
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Plan For Coverage</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Public+Sans:wght@400;500;600&display=swap">
<link rel="stylesheet" href="{p}assets/style.css">
<link rel="canonical" href="https://planforcoverage.com/{path if path!="index.html" else ""}">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"InsuranceAgency","name":"Plan For Coverage","founder":{{"@type":"Person","name":"Eric Becker"}},"url":"https://planforcoverage.com/","telephone":"{PHONE_TEL}","email":"{EMAIL}","areaServed":[{",".join('{"@type":"State","name":"'+st+'"}' for st in STATES)}],"knowsAbout":["Health insurance","Covered California","Major medical","Accident insurance","Hospital indemnity","Critical illness insurance","Dental insurance","Vision insurance"]}}</script>
</head>
<body>
{nav(depth)}
<main>
{body}
</main>
{footer(depth)}
</body>
</html>"""
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f: f.write(html)

def cta_band(depth=0):
    p = "../" * depth
    return f"""
<section class="cta-band">
  <div class="wrap">
    <h2>Not sure which plan fits? Let's talk it through.</h2>
    <p>A 15‑minute call is usually enough to narrow it down. No cost, no obligation, and your information stays with me.</p>
    <div class="actions">
      <a class="btn btn-amber" href="tel:{PHONE_TEL}">Call {PHONE}</a>
      <a class="btn btn-ghost-light" href="{p}contact.html">Request a quote</a>
    </div>
  </div>
</section>"""

# ---------- HOME ----------
cards = "".join(f"""
  <a class="svc" href="services/{s}.html">
    <h3>{n}</h3><p>{d}</p>
  </a>""" for s,n,d in SERVICES)
states_html = "".join(f"<li>{s}</li>" for s in STATES)
home = f"""
<section class="hero">
  <img class="hero-art" src="assets/hero-la.svg" alt="" aria-hidden="true">
  <div class="wrap hero-copy">
    <h1>Health coverage, explained by one person who picks up the phone.</h1>
    <p class="lede">I'm an independent broker in California, certified with Covered California. I help individuals, families and the self‑employed choose major medical plans and the supplements that fill the gaps — without the call‑center runaround.</p>
    <div class="actions">
      <a class="btn btn-amber" href="tel:{PHONE_TEL}">Call {PHONE}</a>
      <a class="btn btn-ghost" href="contact.html">Request a quote</a>
      <a class="btn btn-ghost" href="quote.html">Try a live quote</a>
    </div>
    <p class="hero-note">Working with a broker costs you nothing. Carriers pay me; your premium is the same either way.</p>
  </div>
</section>

<section class="states">
  <div class="wrap">
    <p class="states-label">Licensed in</p>
    <ul class="state-list">{states_html}</ul>
  </div>
</section>

<section class="values">
  <div class="wrap three">
    <div>
      <h2>Independent advice</h2>
      <p>I'm not tied to one carrier. I compare plans from the major insurers in your state and tell you plainly which one I'd pick for your situation.</p>
    </div>
    <div>
      <h2>Built around your needs</h2>
      <p>Doctors you want to keep, prescriptions you take, how often you travel — the right plan depends on details. I ask first, then recommend.</p>
    </div>
    <div>
      <h2>Your information stays here</h2>
      <p>Nothing you send me is sold or shared with lead buyers. One broker, one conversation, no barrage of calls.</p>
    </div>
  </div>
</section>

<section class="services-overview">
  <div class="wrap">
    <h2>What I can help you with</h2>
    <div class="svc-grid">{cards}
    </div>
    <p class="aside">Turning 65 or already on Medicare? <a href="services/medicare.html">I don't sell Medicare plans, but I can refer you to someone I trust.</a></p>
  </div>
</section>

<section class="how">
  <div class="wrap narrow">
    <h2>How it works</h2>
    <ol class="steps">
      <li><strong>Tell me about your situation.</strong> Call, or send the short form on the contact page. Household, state, doctors, budget.</li>
      <li><strong>I shop the options.</strong> Usually within one business day you'll get two or three plans with the trade‑offs spelled out.</li>
      <li><strong>Enroll with help, not a hotline.</strong> I handle the paperwork and stay your point of contact after the policy starts.</li>
    </ol>
  </div>
</section>
{cta_band()}
"""
page("index.html","Independent health insurance broker in California","Independent health insurance broker in California, licensed in ten states. Major medical plus accident, hospital, critical illness, dental and vision coverage.",home)

# ---------- SERVICES INDEX ----------
svc_index = f"""
<section class="page-head"><div class="wrap"><h1>Services</h1>
<p class="lede">Major medical is the foundation. Supplemental plans pay cash to you when something happens, so a deductible or a hospital stay doesn't turn into a financial problem.</p></div></section>
<section class="services-overview"><div class="wrap"><div class="svc-grid">{cards.replace('services/','')}
</div>
<p class="aside"><a href="medicare.html">Medicare referrals →</a></p>
</div></section>
{cta_band(1)}"""
page("services/index.html","Services","Major medical, accident, hospital indemnity, critical illness, dental and vision plans from an independent broker.",svc_index,1)

# ---------- SERVICE PAGES ----------
def svc_page(slug, name, intro, who, covers, notes):
    who_html = "".join(f"<li>{w}</li>" for w in who)
    cov_html = "".join(f"<li>{c}</li>" for c in covers)
    body = f"""
<section class="page-head"><div class="wrap">
<p class="crumb"><a href="index.html">Services</a></p>
<h1>{name}</h1>
<p class="lede">{intro}</p></div></section>
<section class="detail"><div class="wrap two">
  <div>
    <h2>Who it's for</h2>
    <ul class="plain">{who_html}</ul>
    <h2>What it typically covers</h2>
    <ul class="plain">{cov_html}</ul>
  </div>
  <div class="notes">
    <h2>Good to know</h2>
    {notes}
  </div>
</div></section>
{cta_band(1)}"""
    page(f"services/{slug}.html", name, intro, body, 1)

svc_page("major-medical","Major Medical",
 "Comprehensive health insurance — the plan that covers doctor visits, hospital care, prescriptions and preventive services. Available through the ACA marketplace (Covered California and other state exchanges) or directly from carriers.",
 ["Individuals and families without employer coverage","Self‑employed people and small‑business owners","Early retirees not yet eligible for Medicare","Anyone who lost coverage through a job change, move or divorce"],
 ["Preventive care at no cost","Office visits, specialists and urgent care","Hospitalization and surgery","Prescription drugs","Maternity, mental health and the other essential health benefits"],
 """<p><strong>Open enrollment</strong> runs each fall for coverage starting January 1. Outside that window you need a qualifying life event — losing coverage, moving, marriage, a new child — to enroll.</p>
 <p><strong>Subsidies</strong> based on household income can lower the premium substantially. I'll run the numbers with you before we look at plans.</p>
 <p><strong>Networks matter.</strong> The cheapest plan is rarely the right one if your doctor isn't in it. Bring a list of the doctors and prescriptions you want to keep.</p>""")

svc_page("accident","Accident Insurance",
 "Pays a fixed cash benefit when you're hurt — a broken bone, a sprain, stitches, an ER visit. The money goes to you, not the hospital, so you can put it toward your deductible, a missed paycheck or anything else.",
 ["Families with active kids","People on high‑deductible health plans","Anyone who works with their hands or plays hard on weekends"],
 ["Emergency room and urgent care visits","Fractures, dislocations and lacerations","Ambulance transport","Follow‑up care and physical therapy","Accidental death and dismemberment"],
 """<p>Accident plans are usually inexpensive and have no network: you see whoever you want and file a claim afterward.</p>
 <p>They don't replace major medical. They sit beside it to cover the out‑of‑pocket costs that pile up fast after an injury.</p>""")

svc_page("hospital-indemnity","Hospital Indemnity",
 "A set dollar amount paid for each day you're admitted to the hospital, plus benefits for admission, ICU and sometimes outpatient surgery. It's one of the simplest ways to protect against a high deductible.",
 ["People on Bronze or high‑deductible plans","Households that couldn't absorb a surprise $5,000–$9,000 bill","Expecting parents (many plans cover childbirth stays after a waiting period)"],
 ["Lump sum on hospital admission","Daily benefit for each day confined","Higher daily benefit for intensive care","Optional riders for outpatient surgery, ER and diagnostic tests"],
 """<p>Benefits are paid directly to you regardless of what the hospital charges or what your health plan pays.</p>
 <p>Most plans have a waiting period for pre‑existing conditions and for maternity, so it's best to buy before you need it.</p>""")

svc_page("critical-illness","Critical Illness",
 "A lump‑sum payment when you're diagnosed with a covered condition — commonly cancer, heart attack, stroke, kidney failure or major organ transplant. Use it for treatment costs, travel, time off work or keeping the mortgage paid.",
 ["Anyone with a family history of cancer or heart disease","Sole earners and self‑employed people whose income stops when they can't work","People who want a defined safety net beyond their health plan"],
 ["Cancer (invasive and, often, a partial benefit for early‑stage)","Heart attack and stroke","Kidney failure and organ transplant","Optional riders for additional conditions and wellness screenings"],
 """<p>Benefit amounts typically range from $10,000 to $50,000 or more; premiums depend on age, tobacco use and the amount chosen.</p>
 <p>Many plans include a small annual wellness benefit that pays you for routine screenings, which can offset much of the premium.</p>""")

svc_page("dental","Dental",
 "Standalone dental plans for adults and families. Most major medical plans don't include adult dental, so this is usually a separate policy with its own network and benefit schedule.",
 ["Adults whose health plan has no dental benefit","Families with kids heading into braces","Anyone putting off a crown or implant because of cost"],
 ["Cleanings, exams and X‑rays, usually at no cost","Fillings and extractions","Crowns, bridges, root canals and dentures","Orthodontia on select plans"],
 """<p>Watch for waiting periods on major work and annual maximums (commonly $1,000–$2,000). I'll point out which plans waive waiting periods if you've had prior coverage.</p>
 <p>Dental and vision can often be bundled for a small discount.</p>""")

svc_page("vision","Vision",
 "Low‑cost plans that cover eye exams, glasses and contacts at a predictable price, with discounts on LASIK and extra pairs.",
 ["Anyone who wears glasses or contacts","Families with school‑age kids","People whose health plan only covers pediatric vision"],
 ["Annual eye exam","Frames and lenses allowance","Contact lens allowance","Discounts on lens upgrades and laser correction"],
 """<p>Vision plans are inexpensive, often under $15 a month, and generally pay for themselves with one pair of glasses.</p>
 <p>Check that your optometrist is in network before enrolling; I can look it up for you.</p>""")

medicare = f"""
<section class="page-head"><div class="wrap">
<p class="crumb"><a href="index.html">Services</a></p>
<h1>Medicare referrals</h1>
<p class="lede">I'm not appointed to sell Medicare Advantage, Medicare Supplement or Part D plans, and I don't pretend otherwise. If you're turning 65, retiring, or already on Medicare and want a review, I'll connect you with a Medicare specialist I trust.</p></div></section>
<section class="detail"><div class="wrap two">
  <div>
    <h2>When a referral makes sense</h2>
    <ul class="plain">
      <li>You're within a few months of your 65th birthday</li>
      <li>You're leaving employer coverage after 65</li>
      <li>You want someone to review your current Medicare plan during Annual Enrollment (October 15 – December 7)</li>
      <li>A spouse is on Medicare while you still need an individual plan — I can handle your side and coordinate the rest</li>
    </ul>
  </div>
  <div class="notes">
    <h2>What I can still help with</h2>
    <p>Dental, vision, hospital indemnity and critical illness plans are available to people on Medicare and often fill gaps that Medicare leaves. Those I can quote directly.</p>
    <p>For official information, visit <a href="https://www.medicare.gov" rel="noopener">medicare.gov</a> or call 1‑800‑MEDICARE.</p>
  </div>
</div></section>
{cta_band(1)}"""
page("services/medicare.html","Medicare referrals","I don't sell Medicare plans but can refer you to a trusted Medicare specialist, and can still help with dental, vision and supplemental coverage.",medicare,1)

# ---------- ABOUT ----------
about = f"""
<section class="page-head"><div class="wrap"><h1>About</h1>
<p class="lede">Plan For Coverage is a one‑person brokerage run by Eric Becker. When you call, you get me — not a queue.</p></div></section>
<section class="detail"><div class="wrap two">
  <div class="prose">
    <h2>Why a solo broker</h2>
    <p>Most people buy health insurance once a year, under time pressure, from a website that doesn't explain much. The big agencies fix that with volume: a form, a lead, a dialer. I'd rather fix it with attention. I take on a manageable number of clients, learn their situations, and stay available year‑round when a claim gets denied or a doctor leaves the network.</p>
    <h2>Licensing</h2>
    <p>I hold Life and Health licenses and am based in California, with non‑resident licenses in Arizona, Florida, Georgia, Michigan, Ohio, Oregon, Tennessee, Texas and Utah. California Insurance License #0I16359, National Producer Number 16853098.</p>
    <p>I'm a Covered California certified insurance agent, so I can enroll you on the exchange with any subsidy you qualify for, as well as off‑exchange and in the other states I serve.</p>
    <p>I am not appointed to sell Medicare products. If you need Medicare help I'll <a href="services/medicare.html">refer you to a specialist</a> rather than guess.</p>
    <h2>How I'm paid</h2>
    <p>Insurance carriers pay brokers a commission that's already built into the premium. You pay the same price whether you enroll through me, through the exchange directly, or through a call center — so there's no fee for my help.</p>
  </div>
  <div class="notes">
    <h2>Licensed in</h2>
    <ul class="plain">{states_html}</ul>
    <h2>Contact</h2>
    <p>Eric Becker<br>Cell: <a href="tel:{PHONE_TEL}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
  </div>
</div></section>
{cta_band()}"""
page("about.html","About","Plan For Coverage is a solo independent health and life insurance brokerage based in California, licensed in ten states.",about)

# ---------- CONTACT ----------
state_opts = "".join(f'<option>{s}</option>' for s in STATES) + '<option>Other (I may be able to refer you)</option>'
svc_opts = '<option value="">Choose one</option>' + "".join(f'<option>{n}</option>' for _,n,_ in SERVICES) + '<option>Medicare referral</option><option>Not sure yet</option>'
contact = f"""
<section class="page-head"><div class="wrap"><h1>Request a quote</h1>
<p class="lede">Send a few details and I'll reply within one business day with options. Prefer to talk? Call <a href="tel:{PHONE_TEL}">{PHONE}</a>. Want instant estimates first? <a href="quote.html">Try the live quote tool</a>.</p></div></section>
<section class="detail"><div class="wrap two">
  <form class="quote-form" action="https://formspree.io/f/mdeegqng" method="POST">
    <label>Name <input name="name" required autocomplete="name"></label>
    <label>Email <input type="email" name="email" required autocomplete="email"></label>
    <label>Phone <input type="tel" name="phone" autocomplete="tel"></label>
    <label>State you live in <select name="state" required><option value="">Choose a state</option>{state_opts}</select></label>
    <label>What are you looking for? <select name="interest">{svc_opts}</select></label>
    <label>How many people need coverage? <input name="household" placeholder="e.g. 2 adults, 1 child"></label>
    <label>Anything else I should know? <textarea name="notes" rows="5" placeholder="Doctors you want to keep, prescriptions, budget, when you need coverage to start"></textarea></label>
    <label class="check"><input type="checkbox" name="consent" required> I agree to be contacted by phone, text or email about my request. Message and data rates may apply; reply STOP to opt out. See the <a href="privacy.html">privacy policy</a>.</label>
    <button class="btn btn-amber" type="submit">Send request</button>
    <p class="form-note">Your information is used only to prepare your quote. It is never sold or shared with lead buyers.</p>
  </form>
  <div class="notes">
    <h2>What happens next</h2>
    <p>I'll look at the carriers available in your state, check the doctors and prescriptions you listed, and send back two or three plans with the trade‑offs explained. Then we can talk, or you can enroll with my help.</p>
    <h2>Hours</h2>
    <p>Monday – Friday, 9:00 am – 5:00 pm Pacific<br>Evenings and weekends by appointment</p>
    <h2>Already a client?</h2>
    <p>Call or email any time about claims, ID cards, network changes or 1095‑A forms.</p>
  </div>
</div></section>"""
page("contact.html","Request a quote","Request a health insurance quote from an independent broker licensed in California and nine other states.",contact)

# ---------- LIVE QUOTE ----------
quote = """
<section class="page-head"><div class="wrap"><h1>Live quote</h1>
<p class="lede">Instant estimates for plan year 2027. Enter a ZIP code, ages, and an annual household income estimate, and see plans sorted cheapest first. This is an estimate, not an offer of coverage — the final premium and tax credit are determined when you apply.</p></div></section>
<section class="detail"><div class="wrap two">
  <form class="quote-form" id="live-quote-form">
    <label>ZIP code <input name="zip" inputmode="numeric" pattern="\\d{5}" maxlength="5" required placeholder="e.g. 91724"></label>
    <label>Ages, comma-separated <input name="ages" required placeholder="e.g. 40 or 40, 38"></label>
    <label>Annual household income estimate ($) <input name="income" type="number" min="0" step="1000" required placeholder="e.g. 40000"></label>
    <label class="check"><input type="checkbox" name="tobacco"> Primary applicant uses tobacco</label>
    <button class="btn btn-amber" type="submit">Get live quotes</button>
    <p class="form-note">Plan year 2027, coverage effective January 1, 2027. No name, date of birth, or Social Security number is collected by this tool. ZIP, ages, income estimate, and tobacco status are sent to the quoting service only to generate these estimates, and nothing is stored on this site.</p>
  </form>
  <div class="notes">
    <h2>What happens next</h2>
    <p>Use the estimates to narrow it down, then <a href="contact.html">send a quote request</a> or call <a href="tel:+14243629253">(424) 362-9253</a> and I'll help you enroll — through Covered California in California, Explore Health in Oregon, Georgia Access in Georgia, or HealthSherpa in the other states I serve.</p>
    <h2>Good to know</h2>
    <p>Plans marked as not directly enrollable here are quote/display only; enrollment for those goes through the state exchange or with my help. Subsidy amounts shown are estimates based on the income you entered.</p>
  </div>
</div></section>
<section class="detail"><div class="wrap">
  <div id="quote-status" class="quote-status" role="status"></div>
  <div id="quote-results" class="plan-grid"></div>
  <div id="quote-fallback">
    <div class="quote-error"><p><strong>Live quotes are unavailable right now.</strong> Send the details below instead and I'll reply within one business day with options.</p></div>
    <form class="quote-form" action="https://formspree.io/f/mdeegqng" method="POST" style="margin-top:20px">
      <label>Name <input name="name" required autocomplete="name"></label>
      <label>Email <input type="email" name="email" required autocomplete="email"></label>
      <label>ZIP code <input name="zip" inputmode="numeric" pattern="\\d{5}" maxlength="5"></label>
      <label>Ages <input name="ages" placeholder="e.g. 40 or 40, 38"></label>
      <label>Annual household income estimate <input name="income" type="number" min="0" step="1000"></label>
      <label>Anything else? <textarea name="notes" rows="4" placeholder="Doctors, prescriptions, budget, when you need coverage"></textarea></label>
      <input type="hidden" name="interest" value="Live quote request (API fallback)">
      <button class="btn btn-amber" type="submit">Send quote request</button>
    </form>
  </div>
</div></section>
<script>
(function(){
  var form = document.getElementById('live-quote-form');
  var status = document.getElementById('quote-status');
  var results = document.getElementById('quote-results');
  var fallback = document.getElementById('quote-fallback');
  function money(v){
    if (v === null || v === undefined || v === '') return '—';
    var n = Number(v);
    return isNaN(n) ? String(v) : '$' + n.toFixed(2);
  }
  function esc(s){
    return String(s === null || s === undefined ? '' : s).replace(/[&<>"']/g, function(c){
      return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];
    });
  }
  form.addEventListener('submit', async function(e){
    e.preventDefault();
    fallback.style.display = 'none';
    results.innerHTML = '';
    var zip = form.zip.value.trim();
    var ages = form.ages.value.split(',').map(function(x){ return parseInt(x.trim(), 10); }).filter(function(x){ return !isNaN(x); });
    var income = parseFloat(form.income.value);
    if (!/^\\d{5}$/.test(zip) || ages.length === 0 || isNaN(income)){
      status.innerHTML = '<div class="quote-error">Please enter a 5-digit ZIP code, at least one age, and an income estimate.</div>';
      return;
    }
    status.textContent = 'Getting quotes…';
    var tobacco = ages.map(function(_, i){ return i === 0 ? form.tobacco.checked : false; });
    try {
      var resp = await fetch('https://api.planforcoverage.com/v1/quote', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({zip_code: zip, household_size: ages.length, annual_household_income: income, ages: ages, tobacco: tobacco, plan_year: 2027, effective_date: '2027-01-01'})
      });
      var data = await resp.json();
      if (!resp.ok || !data.data || !data.data.plans){
        throw new Error((data && data.detail) ? data.detail : 'Quote service returned an error.');
      }
      var plans = data.data.plans;
      if (plans.length === 0){
        status.textContent = 'No plans returned for that ZIP. Try a nearby ZIP, or send a quote request below.';
        fallback.style.display = 'block';
        return;
      }
      status.textContent = plans.length + ' plans, sorted cheapest net premium first. Estimates for plan year 2027.';
      results.innerHTML = plans.map(function(p){
        var pr = p.pricing || {};
        var det = p.details || {};
        var docs = p.documents || {};
        var links = [];
        if (docs.sbc_url) links.push('<a href="' + esc(docs.sbc_url) + '" target="_blank" rel="noopener">Summary of benefits</a>');
        if (docs.formulary_url) links.push('<a href="' + esc(docs.formulary_url) + '" target="_blank" rel="noopener">Formulary</a>');
        return '<article class="plan-card"><h3>' + esc(p.display_name || p.name || 'Plan') + '</h3>'
          + '<p class="issuer">' + esc((p.issuer && p.issuer.name) || '') + '</p>'
          + '<p class="net">' + money(pr.net_premium) + ' <small>/ month net</small></p>'
          + '<dl><dt>Full price</dt><dd>' + money(pr.gross_premium) + ' / month</dd>'
          + '<dt>Subsidy / APTC</dt><dd>' + money(pr.subsidy_applied) + ' / month</dd>'
          + '<dt>Metal level</dt><dd>' + esc(det.metal_level || '—') + '</dd>'
          + '<dt>Plan type</dt><dd>' + esc(det.plan_type || '—') + '</dd>'
          + '<dt>Deductible (individual)</dt><dd>' + money(det.deductible_individual) + '</dd>'
          + '<dt>Out-of-pocket max (individual)</dt><dd>' + money(det.moop_individual) + '</dd>'
          + '<dt>Direct enrollment here</dt><dd>' + (p.api_enrollable ? 'Yes' : 'No — via exchange / broker help') + '</dd></dl>'
          + (links.length ? '<p>' + links.join(' · ') + '</p>' : '')
          + '</article>';
      }).join('');
    } catch (err) {
      status.innerHTML = '<div class="quote-error">Live quotes could not be loaded: ' + esc(err.message) + '</div>';
      fallback.style.display = 'block';
    }
  });
})();
</script>"""
page("quote.html","Live quote","Instant health insurance plan estimates for plan year 2027 from an independent broker licensed in ten states.",quote)

# ---------- PRIVACY ----------
privacy = f"""
<section class="page-head"><div class="wrap"><h1>Privacy policy</h1>
<p class="lede">Last updated October 2026</p></div></section>
<section class="detail"><div class="wrap narrow prose">
<h2>What I collect</h2>
<p>When you request a quote I collect the information you provide: name, contact details, state of residence, household size and any notes about your coverage needs. If you enroll in a plan, carriers will require additional information such as dates of birth, income (for subsidy eligibility) and Social Security numbers, which are collected on the carrier's or exchange's secure forms, not on this website.</p>
<h2>How I use it</h2>
<p>Your information is used to prepare quotes, enroll you in coverage you choose, service your policy and contact you about your request. I do not sell your information, and I do not share it with lead generators, marketers or other agents.</p>
<h2>Text messages</h2>
<p>By providing a phone number and checking the consent box, you agree to receive calls and text messages from Plan For Coverage about your request. Message frequency varies. Message and data rates may apply. Reply STOP to opt out or HELP for help. Consent is not a condition of purchase.</p>
<h2>Third parties</h2>
<p>The quote form is processed by a form service that transmits submissions to me by email. This site is hosted on GitHub Pages, which may log standard server data such as IP addresses. No analytics or advertising cookies are set by this site.</p>
<h2>Your choices</h2>
<p>You may ask me to correct or delete the information I hold about you at any time by emailing <a href="mailto:{EMAIL}">{EMAIL}</a>, subject to record‑keeping requirements imposed by insurance regulators.</p>
</div></section>"""
page("privacy.html","Privacy policy","How Plan For Coverage collects, uses and protects your information.",privacy)


# ---------- CALIFORNIA CITY PAGES ----------
CITIES = [l.strip().split("|") for l in open(S+"ca_cities.txt") if l.strip()]
def slug(n): return re.sub(r"[^a-z0-9]+","-",n.lower()).strip("-")
city_links = "".join(f'<li><a href="{slug(c)}.html">{c}</a></li>' for c,_ in CITIES)
ca_index = f"""
<section class="page-head"><div class="wrap"><h1>Health insurance across California</h1>
<p class="lede">I'm a California‑based broker certified with Covered California, and I work with clients statewide by phone and video. Choose your city for local plan and carrier notes.</p></div></section>
<section class="detail"><div class="wrap"><ul class="city-list">{city_links}</ul>
<p class="aside">Don't see your city? Every California resident can work with me — <a href="../contact.html">request a quote</a> and tell me where you live.</p></div></section>
{cta_band(1)}"""
page("california/index.html","Health insurance broker serving California cities","Independent, Covered California certified broker serving cities across California. Major medical, dental, vision and supplemental plans.",ca_index,1)
for city, county in CITIES:
    cs = slug(city)
    body = f"""
<section class="page-head"><div class="wrap">
<p class="crumb"><a href="index.html">California</a></p>
<h1>Health insurance in {city}, CA</h1>
<p class="lede">Independent broker help for {city} and {county} County residents: Covered California marketplace plans, off‑exchange major medical, and accident, hospital, critical illness, dental and vision coverage.</p></div></section>
<section class="detail"><div class="wrap two">
  <div class="prose">
    <h2>Shopping for a plan in {city}</h2>
    <p>Covered California offers plans by region, and the carriers and networks available in {county} County are not the same as in other parts of the state. I'll check which insurers offer coverage at your {city} address, which of your doctors are in each network, and whether your household qualifies for a premium subsidy.</p>
    <h2>What I can help {city} residents with</h2>
    <ul class="plain">
      <li><a href="../services/major-medical.html">Major medical</a> through Covered California or directly from a carrier</li>
      <li><a href="../services/accident.html">Accident</a>, <a href="../services/hospital-indemnity.html">hospital indemnity</a> and <a href="../services/critical-illness.html">critical illness</a> plans to cover deductibles</li>
      <li><a href="../services/dental.html">Dental</a> and <a href="../services/vision.html">vision</a></li>
      <li>Referrals to a Medicare specialist if you're turning 65</li>
    </ul>
    <h2>How we'd work together</h2>
    <p>Everything happens by phone, email or video — there's no office to drive to. Call <a href="tel:{PHONE_TEL}">{PHONE}</a> or <a href="../contact.html">send the quote form</a> and I'll reply within one business day.</p>
  </div>
  <div class="notes">
    <h2>At a glance</h2>
    <p><strong>Area served:</strong> {city} and {county} County<br>
    <strong>Marketplace:</strong> Covered California<br>
    <strong>Broker fee:</strong> None — carriers pay the commission<br>
    <strong>Also licensed in:</strong> Arizona, Florida, Georgia, Michigan, Ohio, Oregon, Tennessee, Texas, Utah</p>
    <h2>Nearby</h2>
    <p><a href="index.html">All California cities</a></p>
  </div>
</div></section>
{cta_band(1)}"""
    page(f"california/{cs}.html", f"Health insurance in {city}, CA", f"Independent health insurance broker serving {city}, CA ({county} County). Covered California plans, major medical, dental, vision and supplemental coverage. No broker fee.", body, 1)

# sitemap + robots
BASE="https://planforcoverage.com"
urls=["","services/index.html","about.html","contact.html","quote.html","privacy.html","california/index.html"]+[f"services/{s}.html" for s,_,_ in SERVICES]+["services/medicare.html"]+[f"california/{slug(c)}.html" for c,_ in CITIES]
with open(os.path.join(OUT,"sitemap.xml"),"w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for u in urls: f.write(f"  <url><loc>{BASE}/{u}</loc></url>\n")
    f.write("</urlset>\n")
with open(os.path.join(OUT,"robots.txt"),"w") as f: f.write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")

# ---------- ASSETS ----------
os.makedirs(os.path.join(OUT,"assets"), exist_ok=True)
with open(os.path.join(OUT,"assets/style.css"),"w") as f: f.write(open(S+"style.css").read())
import shutil; shutil.copy(S+"hero-la.svg", os.path.join(OUT,"assets/hero-la.svg"))
with open(os.path.join(OUT,"assets/site.js"),"w") as f: f.write(open(S+"site.js").read())
open(os.path.join(OUT,".nojekyll"),"w").close()
with open(os.path.join(OUT,"CNAME"),"w") as f: f.write("planforcoverage.com\n")
print("built")
