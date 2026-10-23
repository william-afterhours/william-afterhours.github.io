import { Date, getDate } from "./Date"
import { QuartzComponentConstructor, QuartzComponentProps } from "./types"
import readingTime from "reading-time"
import { classNames } from "../util/lang"
import { i18n, ValidLocale } from "../i18n"
import { JSX } from "preact"

/**
 * Author · date · reading time on one line, replacing Quartz's ContentMeta.
 * The author comes from frontmatter `author`, else defaultAuthor. The author's
 * name lives here, not in the site title (owner's instruction, 2026-10-23).
 * Pages with frontmatter `lang: ko` get Korean labels and date format.
 * site/assemble.sh copies this file into quartz/components/ at build time.
 */
interface BylineOptions {
  defaultAuthor: string
  authorHref?: string
  showReadingTime: boolean
}

const defaultOptions: BylineOptions = {
  defaultAuthor: "William",
  showReadingTime: true,
}

export default ((opts?: Partial<BylineOptions>) => {
  const o: BylineOptions = { ...defaultOptions, ...opts }

  function Byline({ cfg, fileData, displayClass }: QuartzComponentProps) {
    const fm = fileData.frontmatter as Record<string, unknown> | undefined
    const author =
      typeof fm?.author === "string" && fm.author.trim() !== "" ? fm.author : o.defaultAuthor
    const isKo = fm?.lang === "ko"
    const locale: ValidLocale = isKo ? "ko-KR" : cfg.locale
    const label = isKo ? "글" : "By"

    const segments: JSX.Element[] = []
    segments.push(
      <span class="byline-author">
        {label} {o.authorHref ? <a href={o.authorHref}>{author}</a> : <b>{author}</b>}
      </span>,
    )
    const date = fileData.dates ? getDate(cfg, fileData) : undefined
    if (date) {
      segments.push(<Date date={date} locale={locale} />)
    }
    if (o.showReadingTime && fileData.text) {
      const minutes = Math.ceil(readingTime(fileData.text).minutes)
      // Quartz's ko-KR locale keeps "min read" in English; write it in Korean here.
      const text = isKo
        ? `읽는 데 ${minutes}분`
        : i18n(locale).components.contentMeta.readingTime({ minutes })
      segments.push(<span>{text}</span>)
    }
    return <p class={classNames(displayClass, "byline")}>{segments}</p>
  }

  Byline.css = `
.byline {
  margin-top: 0;
  color: var(--gray);
}
.byline > *:not(:last-child)::after {
  content: " · ";
}
.byline .byline-author b {
  font-weight: 500;
  color: var(--darkgray);
}
.byline .byline-author a {
  color: var(--darkgray);
}
`
  return Byline
}) satisfies QuartzComponentConstructor
