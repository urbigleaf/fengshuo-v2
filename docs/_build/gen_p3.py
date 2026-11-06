# -*- coding: utf-8 -*-
from gen_p2 import *

# ---------------- about
portrait = by_slug.get("non-paradise") or works[0]
about = (
'<div class="page-head"><div class="wrap">'
'<span class="kicker"><span data-lang="zh">艺术家</span><span data-lang="en">Artist</span></span>'
'<h1 class="page-head__title"><span data-lang="zh">冯硕</span><span data-lang="en">Feng Shuo</span></h1>'
'<p class="page-head__sub"><span data-lang="zh">1970 年生于北京。1994 年毕业于中央美术学院油画系第三画室；现为中央戏剧学院舞台美术系副教授、硕士研究生导师，工作生活于北京。</span>'
'<span data-lang="en">Born in Beijing in 1970. Graduated from the Third Studio of the Oil Painting Department, Central Academy of Fine Arts in 1994; Associate Professor and postgraduate supervisor in the Stage Design Department, Central Academy of Drama. Lives and works in Beijing.</span></p>'
'</div></div>'

'<section class="sect"><div class="wrap">'
'<div class="split">'
'<div class="split__media" data-reveal>' + picture(portrait, "../", "(max-width:860px) 92vw,42vw") + '</div>'
'<div class="prose prose--zh" data-reveal>'
'<p data-lang="zh">冯硕的绘画始终在两种状态之间摆动：一种是寓言式的、克制的叙述——画面平整，形象静默，像被抽空了时间；另一种是狂欢式的、拥挤的喧闹——身体、动物与孩童彼此叠压，秩序在笑声里失效。</p>'
'<p data-lang="en">Feng Shuo’s painting oscillates between two states: a fabled, restrained narration — flat surfaces, silent figures, as if time had been drained out of them; and a carnivalesque, crowded clamour — bodies, animals and children pressed against one another until order collapses into laughter.</p>'
'<p data-lang="zh">他不描绘故事，而描绘故事被讲述的现场：谁在看，谁被看，谁假装没有看见。动物常被赋予人的表情，孩童则带着不合年龄的从容——两者都是把观者推向自我审视的镜子。</p>'
'<p data-lang="en">He does not depict stories but the scene of their telling: who looks, who is looked at, who pretends not to see. Animals wear human expressions; children carry a composure beyond their years — both are mirrors that push the viewer back onto himself or herself.</p>'
'<p data-lang="zh">墨黑的底色让色彩成为事件：陶土红是一次定罪，砒霜绿是一次和解，青瓷是一次遗忘。色彩不解释情绪，它只是把情绪留在画布上，任其发酵。</p>'
'<p data-lang="en">Against a lacquer-black ground, colour becomes an event: terracotta is a conviction, arsenic green a reconciliation, celadon an act of forgetting. Colour does not explain emotion; it simply leaves emotion on the canvas to ferment.</p>'
'<p data-lang="zh">2008 年在纽约 Marlborough Chelsea 的个展「寓言」与 2012 年的「狂欢」是他两个阶段的中点。前者以静默收束，后者以喧闹展开，而问题始终是同一个：我们如何在观看中成为共谋。</p>'
'<p data-lang="en">The 2008 solo exhibition <em>Tales</em> at Marlborough Chelsea, New York, and <em>Carnival</em> in 2012 mark two midpoints: the first closes in silence, the second opens in noise. The question remains the same: how do we become complicit in the act of looking.</p>'
'</div></div></div></section>'

'<section class="sect sect--tight"><div class="wrap"><div class="facts">'
'<div class="fact"><span class="fact__n">1970</span><span class="fact__l"><span data-lang="zh">生于北京</span><span data-lang="en">Born, Beijing</span></span></div>'
'<div class="fact"><span class="fact__n">1994</span><span class="fact__l"><span data-lang="zh">中央美院油画系</span><span data-lang="en">CAFA, Oil Painting</span></span></div>'
'<div class="fact"><span class="fact__n">2008</span><span class="fact__l"><span data-lang="zh">寓言 · 纽约</span><span data-lang="en">Tales, New York</span></span></div>'
'<div class="fact"><span class="fact__n">2012</span><span class="fact__l"><span data-lang="zh">狂欢</span><span data-lang="en">Carnival</span></span></div>'
'</div></div></section>'

'<section class="sect"><div class="wrap">'
'<div class="sect-head"><div class="sect-head__l">'
'<span class="kicker"><span data-lang="zh">简历</span><span data-lang="en">CV</span></span>'
'<h2 class="sect-title"><span data-lang="zh">展览与经历</span><span data-lang="en">Exhibitions &amp; Affiliations</span></h2>'
'</div><a class="sect-link" href="../exhibitions/"><span data-lang="zh">展览文献</span><span data-lang="en">Exhibition texts</span>'
'<svg viewBox="0 0 24 24" ' + IC + ' aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a></div>'
'<div class="exh-list">'
'<a class="exh exh--linked" href="../exhibitions/2012-carnival.html"><img class="exh__thumb" src="../assets/img/exh/poster-2012-512.jpg" width="512" height="1024" loading="lazy" alt=""><span class="exh__year">2012</span><span><span class="exh__t" data-lang="zh">狂欢</span><span class="exh__t" data-lang="en">Carnival</span>'
'<span class="exh__m"><span data-lang="zh">个展</span><span data-lang="en">Solo exhibition</span></span></span><span class="exh__arrow">&rarr;</span></a>'
'<a class="exh exh--linked" href="../exhibitions/2008-tales.html"><img class="exh__thumb" src="../assets/img/exh/exh-2008-03-400.jpg" width="400" height="300" loading="lazy" alt=""><span class="exh__year">2008</span><span><span class="exh__t">Tales / <span data-lang="zh">寓言</span><span data-lang="en">寓言</span></span>'
'<span class="exh__m">Marlborough Chelsea, New York · 2008.04.17 — 05.17</span></span><span class="exh__arrow">&rarr;</span></a>'
'<div class="exh"><span class="exh__year">1994</span><span><span class="exh__t" data-lang="zh">中央美术学院油画系毕业</span><span class="exh__t" data-lang="en">Graduated, CAFA Oil Painting</span>'
'<span class="exh__m"><span data-lang="zh">第三画室</span><span data-lang="en">Third Studio</span></span></span><span class="exh__arrow">&rarr;</span></div>'
'<div class="exh"><span class="exh__year"><span data-lang="zh">现在</span><span data-lang="en">Now</span></span><span><span class="exh__t" data-lang="zh">中央戏剧学院舞台美术系 副教授</span>'
'<span class="exh__t" data-lang="en">Associate Professor, Stage Design, Central Academy of Drama</span>'
'<span class="exh__m"><span data-lang="zh">硕士研究生导师</span><span data-lang="en">Postgraduate supervisor</span></span></span><span class="exh__arrow">&rarr;</span></div>'
'</div></div></section>'

'<section class="sect"><div class="wrap"><div class="sect-head"><div class="sect-head__l">'
'<span class="kicker"><span data-lang="zh">作品</span><span data-lang="en">Works</span></span>'
'<h2 class="sect-title"><span data-lang="zh">从作品中开始</span><span data-lang="en">Begin with the work</span></h2>'
'</div></div>' + grid([by_slug[s] for s in ("black-sun","economics","non-paradise","goat-girl") if s in by_slug], "../") +
'</div></section>')

w("about/index.html", page(about, 1, "about",
  "艺术家 — 冯硕", "Artist — Feng Shuo",
  "冯硕，1970 年生于北京，1994 年毕业于中央美术学院油画系；中央戏剧学院舞美系副教授。",
  "Feng Shuo, born Beijing 1970; CAFA Oil Painting 1994; Associate Professor, Central Academy of Drama."))
print("about ok")

# ---------------- exhibitions
exh_page = (
'<div class="page-head"><div class="wrap">'
'<span class="kicker"><span data-lang="zh">文献</span><span data-lang="en">Documents</span></span>'
'<h1 class="page-head__title"><span data-lang="zh">展览</span><span data-lang="en">Exhibitions</span></h1>'
'<p class="page-head__sub"><span data-lang="zh">两次个展的现场记录与评论文本。</span>'
'<span data-lang="en">Installation records and critical texts from two solo exhibitions.</span></p></div></div>'

'<section class="sect"><div class="wrap"><div class="exh-list">'
'<a class="exh exh--linked" href="../exhibitions/2008-tales.html"><img class="exh__thumb" src="../assets/img/exh/exh-2008-03-400.jpg" width="400" height="300" loading="lazy" alt=""><span class="exh__year">2008</span><span>'
'<span class="exh__t" data-lang="zh">寓言 · Tales</span><span class="exh__t" data-lang="en">Tales</span>'
'<span class="exh__m">Marlborough Chelsea, New York · 2008.04.17 — 05.17</span></span>'
'<span class="exh__arrow">&rarr;</span></a>'
'<a class="exh exh--linked" href="../exhibitions/2012-carnival.html"><img class="exh__thumb" src="../assets/img/exh/poster-2012-512.jpg" width="512" height="1024" loading="lazy" alt=""><span class="exh__year">2012</span><span>'
'<span class="exh__t" data-lang="zh">狂欢 · Carnival</span><span class="exh__t" data-lang="en">Carnival</span>'
'<span class="exh__m">© Tony Godfrey 2011 · <span data-lang="zh">王凯梅 译</span><span data-lang="en">translated by Wang Kaimei</span></span></span>'
'<span class="exh__arrow">&rarr;</span></a>'
'</div></div></section>'

'<section class="sect" id="tales"><div class="wrap">'
'<div class="sect-head"><div class="sect-head__l"><span class="kicker">2008 · New York</span>'
'<h2 class="sect-title" data-lang="zh">寓言 · Tales</h2><h2 class="sect-title" data-lang="en">Tales</h2></div></div>'
'<div class="split split--rev">'
'<div class="prose" data-reveal>'
'<p data-lang="zh">2008 年 4 月 17 日至 5 月 17 日，冯硕个展「寓言」在纽约 Marlborough Chelsea 举行。展览集中的是此前数年的绘画：画面被压平，人物与动物共处一个没有透视的空间，像一页被翻开的寓言。</p>'
'<p data-lang="en">From 17 April to 17 May 2008, Feng Shuo’s solo exhibition <em>Tales</em> was held at Marlborough Chelsea, New York. It gathered paintings from the preceding years: flattened surfaces in which figures and animals share a space without perspective, like a fable held open.</p>'
'<p data-lang="zh">寓言的危险在于它总是指向一个道德结论。冯硕的抵抗方式是：不给结论。他让画面停在讲述即将开始、也即将失败的那个瞬间。</p>'
'<p data-lang="en">The danger of fable is that it always points to a moral. Feng Shuo resists by refusing the conclusion — the image stops at the instant when the telling is about to begin and is about to fail.</p>'
'</div><div class="split__media" data-reveal>' + picture(by_slug["divine-detective"], "../", "(max-width:860px) 92vw,44vw") + '</div>'
'</div></div></section>'

'<section class="sect" id="carnival"><div class="wrap">'
'<div class="sect-head"><div class="sect-head__l"><span class="kicker">2012</span>'
'<h2 class="sect-title" data-lang="zh">狂欢 · Carnival</h2><h2 class="sect-title" data-lang="en">Carnival</h2></div></div>'
'<div class="prose" data-reveal>'
'<p data-lang="zh">2012 年的「狂欢」把「寓言」中的静默彻底反转。画面变得拥挤，色彩变得响亮，身体彼此挤压、推搡、嬉闹——但笑声并没有带来解放，它更像是一种被组织起来的失序。</p>'
'<p data-lang="en"><em>Carnival</em> (2012) reverses the silence of <em>Tales</em>. The surfaces grow crowded, the colour loud; bodies press, shove and play — yet the laughter brings no liberation. It is closer to an organised disorder.</p>'
'<blockquote data-lang="zh">狂欢不是逃离秩序，而是秩序允许自己被暂时颠倒的那一段时间。</blockquote>'
'<blockquote data-lang="en">Carnival is not an escape from order; it is the interval in which order permits itself to be briefly overturned.</blockquote>'
'<p data-lang="zh">展览文本由 Tony Godfrey 撰写（© 2011），王凯梅翻译。相关影像记录见 Bilibili <a href="https://www.bilibili.com/video/BV1XP4y1b7bb" rel="noopener">BV1XP4y1b7bb</a>。</p>'
'<p data-lang="en">The exhibition text was written by Tony Godfrey (© 2011) and translated by Wang Kaimei. Related footage: Bilibili <a href="https://www.bilibili.com/video/BV1XP4y1b7bb" rel="noopener">BV1XP4y1b7bb</a>.</p>'
'</div></div></section>'

'<section class="sect"><div class="wrap"><div class="sect-head"><div class="sect-head__l">'
'<span class="kicker"><span data-lang="zh">同期作品</span><span data-lang="en">Works from the period</span></span>'
'<h2 class="sect-title"><span data-lang="zh">2008 — 2012</span><span data-lang="en">2008 — 2012</span></h2></div></div>'
+ grid([x for x in works if x["year"] in (2008, 2010, 2011)][:8], "../") +
'</div></section>')

w("exhibitions/index.html", page(exh_page, 1, "exh",
  "展览 — 冯硕", "Exhibitions — Feng Shuo",
  "冯硕个展文献：2008 年纽约 Marlborough Chelsea「寓言」，2012 年「狂欢」。",
  "Solo exhibitions: Tales, Marlborough Chelsea, New York 2008; Carnival 2012."))
print("exhibitions ok")
