import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"
// 저자란(글쓴이 · 날짜 · 읽는 시간). site/components/에서 assemble.sh가 복사한다.
import Byline from "./quartz/components/Byline"

// 모든 페이지에 공통.
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [
    // 공개 전환 때 giscus 앱을 저장소에 설치하고 giscus.app에서 repoId·categoryId를 받아 연다.
    // Component.Comments({
    //   provider: "giscus",
    //   options: {
    //     repo: "william-afterhours/william-afterhours.github.io",
    //     repoId: "",
    //     category: "카드 토론",
    //     categoryId: "",
    //     mapping: "pathname",
    //     strict: true,
    //     reactionsEnabled: true,
    //     inputPosition: "bottom",
    //     lang: "en",
    //   },
    // }),
  ],
  footer: Component.Footer({
    links: {
      "Written by William": "https://github.com/william-afterhours",
      Repository: "https://github.com/william-afterhours/william-afterhours.github.io",
      Discussions: "https://github.com/william-afterhours/william-afterhours.github.io/discussions",
      한국어: "/ko/",
    },
  }),
}

// 사건 카드·엔티티 같은 단일 문서 페이지
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.ConditionalRender({
      component: Component.Breadcrumbs(),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ArticleTitle(),
    Byline({ defaultAuthor: "William" }),
    Component.TagList(),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
        { Component: Component.ReaderMode() },
      ],
    }),
    Component.Explorer(),
  ],
  right: [
    Component.Graph(),
    Component.DesktopOnly(Component.TableOfContents()),
    Component.Backlinks(),
  ],
}

// 폴더·태그 목록 페이지
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Byline({ defaultAuthor: "William" })],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
      ],
    }),
    Component.Explorer(),
  ],
  right: [],
}
