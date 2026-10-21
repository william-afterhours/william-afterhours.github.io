import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

// 모든 페이지에 공통. 저장소가 생기면 OWNER/REPO를 바꾼다.
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [
    // 공개 전환 때 giscus 앱을 저장소에 설치하고 giscus.app에서 repoId·categoryId를 받아 연다.
    // Component.Comments({
    //   provider: "giscus",
    //   options: {
    //     repo: "OWNER/REPO",
    //     repoId: "",
    //     category: "카드 토론",
    //     categoryId: "",
    //     mapping: "pathname",
    //     strict: true,
    //     reactionsEnabled: true,
    //     inputPosition: "bottom",
    //     lang: "ko",
    //   },
    // }),
  ],
  footer: Component.Footer({
    links: {
      저장소: "https://github.com/OWNER/REPO",
      토론: "https://github.com/OWNER/REPO/discussions",
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
    Component.ContentMeta(),
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
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
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
