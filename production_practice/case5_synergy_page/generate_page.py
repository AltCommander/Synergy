from __future__ import annotations

from html import escape
from pathlib import Path
from textwrap import dedent


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
    ("Фирменный шрифт — Synergy Sans", "'Synergy Sans', Arial, sans-serif"),
    ("Вариант 1 — Arial", "Arial, sans-serif"),
    ("Вариант 2 — Georgia", "Georgia, serif"),
    ("Вариант 3 — Trebuchet MS", "'Trebuchet MS', sans-serif"),
    ("Вариант 4 — Verdana", "Verdana, sans-serif"),
    ("Вариант 5 — Times New Roman", "'Times New Roman', serif"),
]


def build_card(label: str, font_stack: str) -> str:
    return dedent(
        f"""
        <article class="card" style="font-family: {font_stack}">
          <p class="tag">{escape(label)}</p>
          <h2>{escape(ORGANIZATION['name'])}</h2>
          <p>{escape(ORGANIZATION['full_name'])}</p>
          <p><strong>Место нахождения:</strong> {escape(ORGANIZATION['location'])}</p>
          <p><strong>Деятельность:</strong> {escape(ORGANIZATION['activity'])}</p>
        </article>
        """
    ).strip()


def build_page() -> str:
    cards = "\n".join(build_card(*variant) for variant in FONT_VARIANTS)
    return dedent(
        f"""\
        <!doctype html>
        <html lang="ru">
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <title>{escape(ORGANIZATION['name'])}</title>
          <style>
            @font-face {{
              font-family: "Synergy Sans";
              src: url("fonts/SynergySans-Regular.woff2") format("woff2");
              font-style: normal;
              font-weight: 400;
              font-display: swap;
            }}
            @font-face {{
              font-family: "Synergy Sans";
              src: url("fonts/SynergySans-Bold.woff2") format("woff2");
              font-style: normal;
              font-weight: 700;
              font-display: swap;
            }}
            :root {{
              --accent: #f04b35;
              --ink: #191919;
              --paper: #f3f3f1;
              --card: #ffffff;
            }}
            * {{ box-sizing: border-box; }}
            body {{
              margin: 0;
              color: var(--ink);
              background: var(--paper);
              font-family: "Synergy Sans", Arial, sans-serif;
            }}
            header {{
              padding: clamp(40px, 8vw, 84px) max(6vw, 24px);
              color: #ffffff;
              background: #111111;
            }}
            header h1 {{
              max-width: 920px;
              margin: 0 0 16px;
              font-size: clamp(36px, 7vw, 76px);
              line-height: 1;
            }}
            header p {{
              max-width: 780px;
              margin: 0;
              font-size: 18px;
              line-height: 1.55;
            }}
            main {{
              width: min(1120px, 88vw);
              margin: 38px auto 64px;
            }}
            .grid {{
              display: grid;
              grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
              gap: 18px;
            }}
            .card {{
              padding: 26px;
              background: var(--card);
              border-radius: 18px;
              box-shadow: 0 10px 30px rgb(0 0 0 / 7%);
            }}
            .card h2 {{ margin: 10px 0 14px; font-size: 28px; line-height: 1.12; }}
            .card p {{ line-height: 1.55; }}
            .tag {{ color: var(--accent); font-weight: 700; }}
            .source {{ margin-top: 28px; }}
            a {{ color: #c63725; }}
          </style>
        </head>
        <body>
          <header>
            <h1>{escape(ORGANIZATION['name'])}</h1>
            <p>{escape(ORGANIZATION['activity'])}</p>
          </header>
          <main>
            <section class="grid" aria-label="Варианты фирменного оформления">
              {cards}
            </section>
            <p class="source">
              <a href="{ORGANIZATION['site']}">Официальный сайт Университета</a>
            </p>
          </main>
        </body>
        </html>
        """
    )


def main() -> None:
    output = Path(__file__).with_name("synergy.html")
    output.write_text(build_page(), encoding="utf-8")
    print(f"Создан файл: {output}")


if __name__ == "__main__":
    main()
