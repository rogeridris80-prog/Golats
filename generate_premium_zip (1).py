from pathlib import Path
import zipfile
import shutil

base = Path("/mnt/data/Wedding-Invitation-Herman-Megawaty-Final")
(base/"css").mkdir(parents=True, exist_ok=True)
(base/"js").mkdir(parents=True, exist_ok=True)
(base/"assets/img").mkdir(parents=True, exist_ok=True)
(base/"assets/music").mkdir(parents=True, exist_ok=True)

# Gunakan foto baru sebagai cover utama
cover_photo = Path("/mnt/data/2.jpg")
if cover_photo.exists():
    shutil.copy(cover_photo, base/"assets/img/foto1.jpg")
else:
    fallback_cover = Path("/mnt/data/77878.jpg")
    if fallback_cover.exists():
        shutil.copy(fallback_cover, base/"assets/img/foto1.jpg")

# Foto gallery
gallery_photo = Path("/mnt/data/1.jpg")
if gallery_photo.exists():
    shutil.copy(gallery_photo, base/"assets/img/foto2.jpg")
else:
    fallback_gallery = Path("/mnt/data/77881.jpg")
    if fallback_gallery.exists():
        shutil.copy(fallback_gallery, base/"assets/img/foto2.jpg")

# Jika ada musik sax instrumental yang sudah Anda miliki
sax_music = Path("/mnt/data/sax-wedding.mp3")
if sax_music.exists():
    shutil.copy(sax_music, base/"assets/music/wedding.mp3")

# HTML utama
(base/"index.html").write_text("""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Herman & Megawaty | Wedding Invitation</title>
  <meta name="description" content="Undangan Pernikahan Herman & Megawaty" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <div class="page-shell">
    <header class="hero">
      <div class="hero-glow"></div>
      <nav class="topbar">
        <span>Wedding Invitation</span>
      </nav>

      <div class="hero-content">
        <div class="portrait-ring">
          <img src="assets/img/foto1.jpg" alt="Herman & Megawaty" class="hero-photo">
        </div>

        <p class="eyebrow">The Wedding of</p>
        <h1>Herman <span>&</span> Megawaty</h1>
        <p class="date-text">Senin, 02 November 2026</p>
        <button class="main-btn" onclick="openInvitation()">Buka Undangan</button>
      </div>
    </header>

    <main>
      <section id="details" class="section-card">
        <div class="section-title">
          <p class="eyebrow subtle">Our Invitation</p>
          <h2>Undangan Pernikahan</h2>
        </div>

        <div class="event-box">
          <div class="event-item">
            <span class="label">Hari</span>
            <strong>Senin</strong>
          </div>
          <div class="event-item">
            <span class="label">Tanggal</span>
            <strong>02 Nov 2026</strong>
          </div>
          <div class="event-item">
            <span class="label">Waktu</span>
            <strong>10.00 WIB</strong>
          </div>
        </div>

        <div class="venue">
          <p>Desa Enda Portibi Simorangkir Sidua Huta</p>
          <p>Kecamatan Siatas Barita</p>
        </div>
      </section>

      <section class="section-card">
        <div class="section-title">
          <p class="eyebrow subtle">Bride & Groom</p>
          <h2>Pasangan Kami</h2>
        </div>

        <div class="couple-grid">
          <div class="person">
            <h3>Herman Advensius Lumban Tobing</h3>
            <p>Putra dari Bapak/Ibu<br>St. L. Lumbantobing dan S. Br Manik</p>
          </div>

          <div class="ampersand">&</div>

          <div class="person">
            <h3>Megawaty Ruth Erni Manurung</h3>
            <p>Putri dari Bapak/Ibu<br>H. Manurung dan D. Hutabarat</p>
          </div>
        </div>
      </section>

      <section class="section-card">
        <div class="section-title">
          <p class="eyebrow subtle">Moments</p>
          <h2>Gallery</h2>
        </div>

        <div class="gallery-grid">
          <img src="assets/img/foto2.jpg" alt="Gallery photo">
          <img src="assets/img/foto1.jpg" alt="Gallery photo">
        </div>
      </section>

      <section class="section-card">
        <div class="section-title">
          <p class="eyebrow subtle">Message</p>
          <h2>Pesan Kami</h2>
        </div>
        <p class="message">
          Dengan hati yang tulus dan penuh syukur, kami mengundang Bapak/Ibu/Saudara/i
          untuk hadir dan menjadi saksi bahagia dalam hari istimewa kami.
        </p>
      </section>

      <section class="section-card cta-box">
        <div class="section-title">
          <p class="eyebrow subtle">RSVP</p>
          <h2>Konfirmasi Kehadiran</h2>
        </div>
        <p>Kami menantikan kehadiran Bapak/Ibu/Saudara/i dalam momen bahagia kami.</p>
        <a href="https://your-rsvp-link.com" target="_blank" rel="noopener" class="main-btn">Konfirmasi Kehadiran</a>
      </section>

      <section class="section-card cta-box">
        <div class="section-title">
          <p class="eyebrow subtle">Download</p>
          <h2>Undangan Digital</h2>
        </div>
        <p>Silakan unduh undangan ini untuk dibagikan kepada keluarga dan sahabat.</p>
        <a href="https://your-public-download-link.com/Wedding-Invitation-Herman-Megawaty-Final-Premium-Luxury.zip" target="_blank" rel="noopener" class="main-btn">Download Undangan</a>
      </section>
    </main>
  </div>

  <audio id="music" loop>
    <source src="assets/music/wedding.mp3" type="audio/mpeg">
  </audio>

  <script src="js/script.js"></script>
</body>
</html>
""", encoding="utf-8")

# CSS premium luxury
(base/"css/style.css").write_text("""
:root {
  --bg-1: #f5efe9;
  --bg-2: #e6d9cc;
  --paper: rgba(255,255,255,0.5);
  --gold-1: #c7a874;
  --gold-2: #8d6d3a;
  --ink: #1d1a18;
  --muted: #534b46;
  --line: rgba(141, 109, 58, 0.25);
  --shadow: 0 18px 40px rgba(25, 19, 14, 0.12);
}

* { box-sizing: border-box; }

html { scroll-behavior: smooth; }

body {
  margin: 0;
  font-family: 'Inter', sans-serif;
  background: linear-gradient(180deg, var(--bg-1), var(--bg-2));
  color: var(--ink);
}

img { max-width: 100%; display: block; }

.page-shell {
  max-width: 1100px;
  margin: 0 auto;
  padding: 18px 18px 80px;
}

.hero {
  position: relative;
  min-height: 760px;
  border-radius: 28px;
  overflow: hidden;
  box-shadow: var(--shadow);
  background:
    linear-gradient(180deg, rgba(22,16,13,0.18), rgba(22,16,13,0.38)),
    url('assets/img/foto1.jpg') center/cover no-repeat;
}

.hero-glow {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(circle at center, rgba(255,255,255,0.15), rgba(0,0,0,0.2) 65%);
}

.topbar {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 2;
  text-align: center;
  padding: 22px 20px;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  font-size: 0.72rem;
  color: rgba(255,255,255,0.8);
}

.hero-content {
  position: relative;
  z-index: 2;
  min-height: 760px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  color: white;
  padding: 40px 20px;
}

.portrait-ring {
  width: 300px;
  height: 300px;
  border-radius: 50%;
  padding: 8px;
  background: linear-gradient(135deg, rgba(255,255,255,0.9), rgba(230,217,204,0.25));
  box-shadow: 0 18px 35px rgba(0,0,0,0.18);
  margin-bottom: 24px;
}

.hero-photo {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
  border: 4px solid rgba(255,255,255,0.4);
}

.eyebrow {
  margin: 0 0 14px;
  letter-spacing: 0.28em;
  text-transform: uppercase;
  font-size: 0.72rem;
  color: var(--gold-1);
}

.eyebrow.subtle {
  color: var(--gold-2);
}

h1, h2, h3 {
  margin: 0;
  font-family: 'Cormorant Garamond', serif;
  font-weight: 600;
}

h1 {
  font-size: clamp(3.2rem, 5vw, 6.2rem);
  line-height: 0.9;
  letter-spacing: 0.04em;
  text-shadow: 0 4px 12px rgba(0,0,0,0.18);
}

h1 span {
  color: #f1d5a1;
  margin: 0 10px;
}

.date-text {
  margin: 18px 0 22px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  font-size: 0.9rem;
  color: rgba(255,255,255,0.88);
}

.main-btn {
  display: inline-block;
  text-decoration: none;
  border: none;
  border-radius: 999px;
  padding: 16px 32px;
  background: linear-gradient(135deg, var(--gold-1), var(--gold-2));
  color: #fffaf4;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 0 14px 25px rgba(141, 109, 58, 0.28);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.main-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 18px 28px rgba(141, 109, 58, 0.36);
}

.section-card {
  margin-top: 28px;
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 24px;
  box-shadow: var(--shadow);
  padding: 42px 28px;
  backdrop-filter: blur(4px);
}

.section-title {
  text-align: center;
  margin-bottom: 24px;
}

.section-title h2 {
  font-size: clamp(2.4rem, 4vw, 4rem);
  color: #201b1a;
}

.event-box {
  max-width: 760px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 18px;
}

.event-item {
  background: rgba(255,255,255,0.4);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 24px 12px;
  text-align: center;
}

.label {
  display: block;
  margin-bottom: 10px;
  text-transform: uppercase;
  letter-spacing: 0.2em;
  font-size: 0.68rem;
  color: var(--muted);
}

.event-item strong {
  font-size: 1.2rem;
  color: var(--ink);
}

.venue {
  text-align: center;
  color: var(--muted);
  line-height: 1.8;
  font-size: 1.05rem;
  margin-top: 22px;
}

.couple-grid {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  gap: 24px;
  align-items: center;
  max-width: 900px;
  margin: 0 auto;
}

.person {
  text-align: center;
}

.person h3 {
  font-size: clamp(2rem, 3vw, 2.8rem);
  margin-bottom: 10px;
  color: #261d1a;
}

.person p {
  margin: 0;
  color: var(--muted);
  line-height: 1.85;
}

.ampersand {
  font-family: 'Cormorant Garamond', serif;
  font-size: 4.3rem;
  color: var(--gold-2);
  font-weight: 700;
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0,1fr));
  gap: 18px;
  max-width: 900px;
  margin: 0 auto;
}

.gallery-grid img {
  width: 100%;
  height: 420px;
  object-fit: cover;
  border-radius: 18px;
  box-shadow: var(--shadow);
}

.message {
  max-width: 760px;
  margin: 0 auto;
  font-size: 1.05rem;
  color: var(--muted);
  line-height: 1.9;
  text-align: center;
}

.cta-box {
  text-align: center;
}

.cta-box p {
  margin: 0 auto 24px;
  max-width: 720px;
  line-height: 1.9;
  color: var(--muted);
}

@media (max-width: 760px) {
  .hero { min-height: 620px; }
  .hero-content { min-height: 620px; }
  .portrait-ring { width: 230px; height: 230px; }
  .event-box { grid-template-columns: 1fr; }
  .couple-grid { grid-template-columns: 1fr; }
  .ampersand { display: none; }
  .gallery-grid { grid-template-columns: 1fr; }
}
""", encoding="utf-8")

# JS
(base/"js/script.js").write_text("""
function openInvitation() {
  const detailSection = document.getElementById('details');
  if (detailSection) {
    detailSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  const audio = document.getElementById('music');
  if (audio) {
    audio.play().catch(() => {});
  }
}
""", encoding="utf-8")

# ZIP
zip_path = Path("/mnt/data/Wedding-Invitation-Herman-Megawaty-Final-Premium-Luxury.zip")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for file in base.rglob("*"):
        if file.is_file():
            z.write(file, file.relative_to(base))

print(f"ZIP dibuat: {zip_path}")