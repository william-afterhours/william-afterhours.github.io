import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 설정 — William 연구 저장소용.
 * 빌드 때 site/assemble.sh가 이 파일을 Quartz 소스 루트로 복사한다.
 * 기본값에서 바꾼 것: 제목·로케일·분석 끔·한글 글꼴·템플릿 제외·OG 이미지 끔·Latex 끔.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "William · 초자연 현상 기록",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "ko-KR",
    // GitHub 저장소가 생기면 "<owner>.github.io/<repo>"로 바꾼다 (RSS·사이트맵·절대 링크에만 쓰인다).
    baseUrl: "example.invalid",
    ignorePatterns: ["private", "templates", ".obsidian", "**/_TEMPLATE.md"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Noto Sans KR",
        body: "Noto Sans KR",
        code: "IBM Plex Mono",
      },
      colors: {
        lightMode: {
          light: "#faf8f8",
          lightgray: "#e5e5e5",
          gray: "#b8b8b8",
          darkgray: "#4e4e4e",
          dark: "#2b2b2b",
          secondary: "#284b63",
          tertiary: "#84a59d",
          highlight: "rgba(143, 159, 169, 0.15)",
          textHighlight: "#fff23688",
        },
        darkMode: {
          light: "#161618",
          lightgray: "#393639",
          gray: "#646464",
          darkgray: "#d4d4d4",
          dark: "#ebebec",
          secondary: "#7b97aa",
          tertiary: "#84a59d",
          highlight: "rgba(143, 159, 169, 0.15)",
          textHighlight: "#b3aa0288",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        // 콘텐츠는 복사본이라 git 날짜를 못 읽는다. 카드의 `updated:` 프론트매터를 쓴다.
        priority: ["frontmatter", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      // parseTags: false — 카드의 출처 번호 "#1", "#8의"가 태그로 잡히는 것을 막는다. 태그는 쓰지 않는다.
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false, parseTags: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
    ],
  },
}

export default config
