from __future__ import annotations

from html import escape
from pathlib import Path


ORGANIZATION = {
    "name": "Университет «Синергия»",
    "full_name": (
        "Автономная некоммерческая организация высшего образования "
        "«Московский университет «Синергия»"
    ),
    "location": "Российская Федерация, город Москва",
    "activity": (
        "Высшее, среднее профессиональное и дополнительное образование, "
        "научная, методическая и проектная деятельность."
    ),
    "site": "https://synergy.ru/",
}

FONT_VARIANTS = [
    ("Фирменный", "Synergy Sans", "'Synergy Sans', Arial, sans-serif", "400"),
    ("Вариант 1", "Arial", "Arial, sans-serif", "400"),
    ("Вариант 2", "Georgia", "Georgia, serif", "400"),
    ("Вариант 3", "Trebuchet MS", "'Trebuchet MS', sans-serif", "400"),
    ("Вариант 4", "Verdana", "Verdana, sans-serif", "400"),
    ("Вариант 5", "Times New Roman", "'Times New Roman', serif", "400"),
]


def build_card(label: str, font_name: str, font_stack: str, weight: str) -> str:
    return f"""<article class="specimen" style="--specimen-font: {font_stack}; --specimen-weight: {weight}">
  <div class="specimen__meta">
    <span>{escape(label)}</span>
    <strong>{escape(font_name)}</strong>
  </div>
  <div class="specimen__sample">
    <p class="specimen__alphabet">Аа Бб Вв Гг Дд Ее Ёё Жж Зз</p>
    <h3>{escape(ORGANIZATION['name'])}</h3>
    <p>{escape(ORGANIZATION['full_name'])}</p>
    <p><b>Место нахождения:</b> {escape(ORGANIZATION['location'])}</p>
  </div>
</article>"""


def build_page() -> str:
    cards = "\n".join(build_card(*variant) for variant in FONT_VARIANTS)
    return f"""<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Информация об Университете «Синергия» и сравнение шести шрифтов.">
  <title>{escape(ORGANIZATION['name'])} — кейс-задача № 5</title>
  <style>
    @font-face {{
      font-family: "Synergy Sans";
      src: url("fonts/SynergySans-VF.ttf") format("truetype");
      font-style: normal;
      font-weight: 100 900;
      font-display: swap;
    }}

    :root {{
      --red: #ed131c;
      --black: #000000;
      --gray: #e0e1e5;
      --white: #ffffff;
      --orange: #ff8c00;
      --yellow: #ffd500;
      --lime: #d1e000;
      --teal: #00a299;
      --blue: #00a6ff;
      --purple: #681789;
      --radius-lg: 32px;
      --radius-md: 22px;
      --shadow: 0 24px 70px rgb(0 0 0 / 10%);
    }}

    * {{ box-sizing: border-box; }}

    html {{ scroll-behavior: smooth; }}

    body {{
      margin: 0;
      color: var(--black);
      background: var(--gray);
      font-family: "Synergy Sans", Arial, sans-serif;
    }}

    a {{ color: inherit; }}

    .page {{
      width: min(1380px, calc(100% - 32px));
      margin: 16px auto;
    }}

    .topbar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
      padding: 16px 22px;
      margin-bottom: 16px;
      background: var(--white);
      border-radius: 18px;
    }}

    .wordmark {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      font-size: 18px;
      font-weight: 800;
      letter-spacing: .02em;
      text-transform: uppercase;
    }}

    .wordmark::before {{
      width: 18px;
      height: 18px;
      background: var(--red);
      content: "";
    }}

    .case-label {{
      color: #5f6065;
      font-size: 14px;
      font-weight: 600;
    }}

    .hero {{
      position: relative;
      display: grid;
      grid-template-columns: minmax(0, 1.35fr) minmax(300px, .65fr);
      min-height: 640px;
      overflow: hidden;
      background: var(--white);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow);
    }}

    .hero__content {{
      position: relative;
      z-index: 2;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: clamp(36px, 6vw, 86px);
    }}

    .eyebrow {{
      display: inline-block;
      width: fit-content;
      padding: 9px 14px;
      color: var(--white);
      background: var(--red);
      border-radius: 999px;
      font-size: 13px;
      font-weight: 800;
      letter-spacing: .06em;
      text-transform: uppercase;
    }}

    h1 {{
      max-width: 880px;
      margin: 28px 0 26px;
      font-size: clamp(42px, 6.2vw, 92px);
      font-weight: 500;
      letter-spacing: -.055em;
      line-height: .92;
    }}

    .hero__name {{
      max-width: 760px;
      margin: 0;
      font-size: clamp(26px, 3.5vw, 52px);
      font-weight: 800;
      line-height: 1;
    }}

    .hero__facts {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 14px;
      margin-top: 48px;
    }}

    .fact {{
      padding: 20px;
      background: #f5f5f6;
      border-radius: 18px;
    }}

    .fact span {{
      display: block;
      margin-bottom: 7px;
      color: #6b6c71;
      font-size: 12px;
      font-weight: 800;
      letter-spacing: .07em;
      text-transform: uppercase;
    }}

    .fact p {{ margin: 0; line-height: 1.45; }}

    .hero__art {{
      position: relative;
      min-height: 420px;
      background: var(--purple);
    }}

    .shape {{ position: absolute; }}
    .shape--red {{ inset: 0 48% 52% 0; background: var(--red); }}
    .shape--yellow {{ inset: 0 0 52% 52%; background: var(--yellow); border-radius: 0 0 0 100%; }}
    .shape--blue {{ inset: 52% 0 0 0; background: var(--blue); border-radius: 100% 0 0; }}
    .shape--white {{
      top: 50%;
      left: 50%;
      width: 36%;
      aspect-ratio: 1;
      background: var(--white);
      transform: translate(-50%, -50%) rotate(45deg);
    }}
    .shape--teal {{
      right: 8%;
      bottom: 7%;
      width: 24%;
      aspect-ratio: 1;
      background: var(--teal);
      border-radius: 50%;
    }}

    .section {{
      padding: clamp(38px, 5vw, 74px);
      margin-top: 16px;
      background: var(--white);
      border-radius: var(--radius-lg);
    }}

    .section__heading {{
      display: grid;
      grid-template-columns: minmax(0, 1fr) minmax(240px, .45fr);
      align-items: end;
      gap: 30px;
      margin-bottom: 34px;
    }}

    h2 {{
      margin: 0;
      font-size: clamp(38px, 5vw, 70px);
      font-weight: 600;
      letter-spacing: -.045em;
      line-height: .98;
    }}

    .section__heading p {{ margin: 0; color: #5f6065; line-height: 1.55; }}

    .specimens {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 16px;
    }}

    .specimen {{
      overflow: hidden;
      border: 1px solid #d9dade;
      border-radius: var(--radius-md);
    }}

    .specimen:first-child {{
      grid-column: 1 / -1;
      border-color: var(--red);
      box-shadow: inset 0 0 0 1px var(--red);
    }}

    .specimen__meta {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      padding: 13px 18px;
      background: #f2f2f3;
      font-family: "Synergy Sans", Arial, sans-serif;
      font-size: 13px;
    }}

    .specimen:first-child .specimen__meta {{ color: var(--white); background: var(--red); }}

    .specimen__meta span {{ font-weight: 800; text-transform: uppercase; }}

    .specimen__sample {{
      min-height: 285px;
      padding: clamp(22px, 3vw, 38px);
      font-family: var(--specimen-font);
      font-weight: var(--specimen-weight);
    }}

    .specimen__alphabet {{ margin: 0 0 22px; color: #78797e; font-size: 14px; }}

    .specimen h3 {{ margin: 0 0 18px; font-size: clamp(28px, 3vw, 46px); line-height: 1; }}
    .specimen p {{ line-height: 1.5; }}

    .footer {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 24px;
      padding: 22px;
      margin-top: 16px;
      color: var(--white);
      background: var(--black);
      border-radius: 18px;
    }}

    .footer p {{ margin: 0; }}

    .footer a {{
      padding: 10px 14px;
      color: var(--black);
      background: var(--white);
      border-radius: 999px;
      font-weight: 700;
      text-decoration: none;
    }}

    .footer a:hover,
    .footer a:focus-visible {{ color: var(--white); background: var(--red); }}

    @media (max-width: 900px) {{
      .hero {{ grid-template-columns: 1fr; }}
      .hero__art {{ min-height: 300px; }}
      .section__heading {{ grid-template-columns: 1fr; }}
    }}

    @media (max-width: 680px) {{
      .page {{ width: min(100% - 20px, 1380px); margin: 10px auto; }}
      .topbar, .footer {{ align-items: flex-start; flex-direction: column; }}
      .hero__content, .section {{ padding: 28px 22px; }}
      .hero__facts, .specimens {{ grid-template-columns: 1fr; }}
      .specimen:first-child {{ grid-column: auto; }}
      .specimen__sample {{ min-height: auto; }}
    }}
  </style>
</head>
<body>
  <div class="page">
    <header class="topbar">
      <div class="wordmark">Университет Синергия</div>
      <div class="case-label">Производственная практика · кейс-задача № 5</div>
    </header>

    <main>
      <section class="hero" aria-labelledby="page-title">
        <div class="hero__content">
          <div>
            <span class="eyebrow">Практическая подготовка</span>
            <h1 id="page-title">Наименование организации на базе, которой Вы проходите практическую подготовку</h1>
            <p class="hero__name">{escape(ORGANIZATION['name'])}</p>
          </div>
          <div class="hero__facts">
            <div class="fact">
              <span>Полное наименование</span>
              <p>{escape(ORGANIZATION['full_name'])}</p>
            </div>
            <div class="fact">
              <span>Основная деятельность</span>
              <p>{escape(ORGANIZATION['activity'])}</p>
            </div>
          </div>
        </div>
        <div class="hero__art" aria-hidden="true">
          <span class="shape shape--red"></span>
          <span class="shape shape--yellow"></span>
          <span class="shape shape--blue"></span>
          <span class="shape shape--white"></span>
          <span class="shape shape--teal"></span>
        </div>
      </section>

      <section class="section" aria-labelledby="fonts-title">
        <div class="section__heading">
          <h2 id="fonts-title">Фирменный шрифт и пять вариантов</h2>
          <p>В каждом блоке показан один и тот же текст, поэтому начертания можно сравнить напрямую. Первый образец использует официальный Synergy Sans из локального файла.</p>
        </div>
        <div class="specimens">
          {cards}
        </div>
      </section>
    </main>

    <footer class="footer">
      <p>{escape(ORGANIZATION['location'])}</p>
      <a href="{escape(ORGANIZATION['site'])}">Официальный сайт Университета</a>
    </footer>
  </div>
</body>
</html>
"""


def main() -> None:
    output = Path(__file__).with_name("synergy.html")
    output.write_text(build_page(), encoding="utf-8")
    print(f"Создан файл: {output}")


if __name__ == "__main__":
    main()
