
/* 冯硕 · Feng Shuo — Studio Archive
   Vanilla ES2019+, no dependencies. Progressive enhancement only. */
(function () {
  'use strict';

  var doc = document, root = doc.documentElement;
  var LANG_KEY = 'fs.lang', THEME_KEY = 'fs.theme';

  /* ---------- storage (guarded: private mode / file:// can throw) ---------- */
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  };

  /* ---------- language ---------- */
  var TITLES = {
    zh: { home: '冯硕 — 绘画作品', works: '作品 — 冯硕', about: '艺术家 — 冯硕', exh: '展览 — 冯硕' },
    en: { home: 'Feng Shuo — Paintings', works: 'Works — Feng Shuo', about: 'Artist — Feng Shuo', exh: 'Exhibitions — Feng Shuo' }
  };

  function setLang(lang, persist) {
    lang = (lang === 'en') ? 'en' : 'zh';
    root.lang = lang;
    root.setAttribute('data-lang', lang);
    if (persist !== false) store.set(LANG_KEY, lang);

    /* swap document title */
    var t = doc.body ? doc.body.getAttribute('data-title-' + lang) : null;
    if (t) doc.title = t;

    /* aria + label state on every toggle on the page */
    var toggles = doc.querySelectorAll('[data-lang-toggle]');
    for (var i = 0; i < toggles.length; i++) {
      var b = toggles[i];
      b.setAttribute('aria-label', lang === 'zh' ? 'Switch to English' : '切换为中文');
      b.setAttribute('aria-pressed', lang === 'en' ? 'true' : 'false');
      var zh = b.querySelector('[data-lang-cur="zh"]');
      var en = b.querySelector('[data-lang-cur="en"]');
      if (zh) zh.className = lang === 'zh' ? 'is-on' : '';
      if (en) en.className = lang === 'en' ? 'is-on' : '';
    }
    /* notify listeners (used by detail pages to swap figure captions) */
    doc.dispatchEvent(new CustomEvent('langchange', { detail: { lang: lang } }));
  }

  var initial = store.get(LANG_KEY);
  if (!initial) {
    var nav = (navigator.language || 'zh').toLowerCase();
    initial = nav.indexOf('zh') === 0 ? 'zh' : 'en';
  }
  setLang(initial, false);

  doc.addEventListener('click', function (e) {
    var t = e.target.closest ? e.target.closest('[data-lang-toggle]') : null;
    if (!t) return;
    e.preventDefault();
    setLang(root.lang === 'zh' ? 'en' : 'zh');
  });

  /* ---------- theme ---------- */
  function setTheme(mode, persist) {
    if (mode === 'paper') root.setAttribute('data-theme', 'paper');
    else root.removeAttribute('data-theme');
    if (persist !== false) store.set(THEME_KEY, mode);
  }
  setTheme(store.get(THEME_KEY) === 'paper' ? 'paper' : 'ink', false);

  doc.addEventListener('click', function (e) {
    var t = e.target.closest ? e.target.closest('[data-theme-toggle]') : null;
    if (!t) return;
    e.preventDefault();
    setTheme(root.getAttribute('data-theme') === 'paper' ? 'ink' : 'paper');
  });

  /* ---------- mobile drawer ---------- */
  var drawer = doc.getElementById('drawer');
  function openDrawer() {
    if (!drawer) return;
    drawer.hidden = false;
    requestAnimationFrame(function () { drawer.classList.add('is-open'); });
    doc.body.style.overflow = 'hidden';
    var first = drawer.querySelector('a,button');
    if (first) first.focus();
  }
  function closeDrawer() {
    if (!drawer || drawer.hidden) return;
    drawer.classList.remove('is-open');
    doc.body.style.overflow = '';
    setTimeout(function () { drawer.hidden = true; }, 480);
  }
  doc.addEventListener('click', function (e) {
    if (e.target.closest && e.target.closest('[data-drawer-open]')) { e.preventDefault(); openDrawer(); }
    if (e.target.closest && e.target.closest('[data-drawer-close]')) { e.preventDefault(); closeDrawer(); }
  });
  doc.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { closeDrawer(); closeLightbox(); }
  });

  /* ---------- reveal on scroll ---------- */
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    doc.querySelectorAll('[data-reveal]').forEach(function (el) { io.observe(el); });
  } else {
    doc.querySelectorAll('[data-reveal]').forEach(function (el) { el.classList.add('is-in'); });
  }

  /* ---------- lightbox (grid pages) ---------- */
  var lb = doc.getElementById('lightbox');
  var lbImg, lbCap;
  if (lb) { lbImg = lb.querySelector('.lb__img'); lbCap = lb.querySelector('.lb__cap'); }

  function openLightbox(src, caption) {
    if (!lb) return;
    lbImg.src = src;
    if (lbCap) lbCap.textContent = caption || '';
    lb.hidden = false;
    requestAnimationFrame(function () { lb.classList.add('is-open'); });
    doc.body.style.overflow = 'hidden';
    lb.focus();
  }
  function closeLightbox() {
    if (!lb || lb.hidden) return;
    lb.classList.remove('is-open');
    doc.body.style.overflow = '';
    setTimeout(function () { lb.hidden = true; lbImg.removeAttribute('src'); }, 320);
  }
  doc.addEventListener('click', function (e) {
    var trg = e.target.closest ? e.target.closest('[data-zoom]') : null;
    if (trg) {
      e.preventDefault();
      openLightbox(trg.getAttribute('data-zoom'), trg.getAttribute('data-zoom-cap') || '');
      return;
    }
    if (e.target === lb || (e.target.closest && e.target.closest('[data-lb-close]'))) closeLightbox();
  });

  /* ---------- year filter ---------- */
  var filterBar = doc.querySelector('[data-filters]');
  if (filterBar) {
    filterBar.addEventListener('click', function (e) {
      var chip = e.target.closest('[data-year]');
      if (!chip) return;
      e.preventDefault();
      var y = chip.getAttribute('data-year');
      filterBar.querySelectorAll('[data-year]').forEach(function (c) {
        c.setAttribute('aria-pressed', c === chip ? 'true' : 'false');
      });
      var n = 0;
      doc.querySelectorAll('[data-work-year]').forEach(function (card) {
        var show = (y === 'all') || (card.getAttribute('data-work-year') === y);
        card.style.display = show ? '' : 'none';
        if (show) n++;
      });
      doc.querySelectorAll('[data-year-group]').forEach(function (grp) {
        var showGrp = (y === 'all') || (grp.getAttribute('data-year-group') === y);
        grp.style.display = showGrp ? '' : 'none';
      });
      var counter = doc.querySelector('[data-count]');
      if (counter) counter.textContent = n;
      if (history.replaceState) {
        var u = new URL(location.href);
        if (y === 'all') u.searchParams.delete('year'); else u.searchParams.set('year', y);
        history.replaceState(null, '', u);
      }
    });
    /* honour ?year= on load */
    var qy = new URLSearchParams(location.search).get('year');
    if (qy) {
      var target = filterBar.querySelector('[data-year="' + qy + '"]');
      if (target) target.click();
    }
  }

  /* ---------- header shadow on scroll ---------- */
  var head = doc.querySelector('.site-head');
  if (head) {
    var onScroll = function () {
      if (window.scrollY > 12) head.classList.add('is-stuck');
      else head.classList.remove('is-stuck');
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---------- keyboard nav between works ---------- */
  doc.addEventListener('keydown', function (e) {
    if (e.target.matches && e.target.matches('input,textarea,select')) return;
    if (e.key === 'ArrowLeft') {
      var p = doc.querySelector('[data-nav-prev]'); if (p) location.href = p.getAttribute('href');
    } else if (e.key === 'ArrowRight') {
      var n2 = doc.querySelector('[data-nav-next]'); if (n2) location.href = n2.getAttribute('href');
    }
  });

  /* expose for inline use */
  window.FS = { setLang: setLang, setTheme: setTheme };
})();
