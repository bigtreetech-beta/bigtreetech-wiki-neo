import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

import {default as custom_code_themes} from './src/theme/prism-custom-code-themes';

import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'Bigtreetech WiKi NEO',
  tagline: '新文档还在迁移中',
  favicon: 'img/favicon.ico',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // Set the production url of your site here
  url: 'https://bttwiki.com',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'bigtreetech', // Usually your GitHub org/user name.
  projectName: 'wiki', // Usually your repo name.
  
  onBrokenLinks: 'throw',
  
  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'zh-Hans',
    locales: ['zh-Hans'],
  },

  markdown: {
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          
          // math
          remarkPlugins: [remarkMath],
          rehypePlugins: [rehypeKatex],
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          // editUrl:
          //   'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          // editUrl:
          //   'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
          // Useful options to enforce blogging best practices
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  stylesheets: [
    {
      href: '/katex/katex.min.css',
      type: 'text/css',
    },
  ],

  themes: [
    // ... Your other themes.
    [
      require.resolve("@easyops-cn/docusaurus-search-local"),
      /** @type {import("@easyops-cn/docusaurus-search-local").PluginOptions} */
      ({
        // ... Your options.
        // `hashed` is recommended as long-term-cache of index file is possible.
        hashed: true,

        // For Docs using Chinese, it is recomended to set:
        language: ["en", "zh"],

        // If you're using `noIndex: true`, set `forceIgnoreNoIndex` to enable local index:
        // forceIgnoreNoIndex: true,
      }),
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/docusaurus-social-card.jpg',
    navbar: {
      title: 'Bigtreetech Wiki',
      logo: {
        alt: 'bigtreetech-logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'boardSidebar',
          position: 'left',
          label: 'Board',
        },
        
        {
          type: 'docSidebar',
          sidebarId: 'extruderSidebar',
          position: 'left',
          label: 'Extruder',
        },

        {
          type: 'docSidebar',
          sidebarId: 'moduleSidebar',
          position: 'left',
          label: 'Module',
        },

        {
          type: 'docSidebar',
          sidebarId: 'pandaSidebar',
          position: 'left',
          label: 'Panda Series',
        },

        {to: '/blog', label: 'Blog', position: 'left'},
        {
          href: 'https://github.com/bigtreetech-beta/bigtreetech-wiki-neo',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Tutorial',
              to: '/docs/intro',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'BIGTREETECH Official Group',
              href: 'https://www.facebook.com/groups/bigtreetech',
            },
            {
              label: 'Discord',
              href: 'https://discord.gg/hhZsV7zk',
            },
            {
              label: 'Reddit',
              href: 'https://www.reddit.com/r/BIGTREETECH/',
            },
          ],
        },
        {
          title: 'Support',
          items: [
            {
            label: 'Submit Support Ticket',
            href: 'https://biqu3d.com/pages/submit-a-ticket',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/bigtreetech',
            }
          ]
        },
        {
          title: 'More',
          items: [
            {
              label: 'BIGTREETECH Official Website',
              href: 'https://bigtree-tech.com/',
            },
            {
              label: 'BIQU Official Website',
              href: 'https://biqu3d.com/',
            },
            {
              label: 'Online Store',
              href: 'https://biqu.equipment',
            }
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} 必趣创新科技(深圳)有限公司 </br> <a href="https://beian.miit.gov.cn/" target="_blank">粤ICP备2024178516号</a>`,
    },
    prism: {
      theme: custom_code_themes,
      darkTheme: custom_code_themes,
      additionalLanguages: ['bash'],
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
