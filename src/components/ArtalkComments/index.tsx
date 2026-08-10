import React, { useEffect } from 'react';
import { useLocation } from '@docusaurus/router';
import { useColorMode } from '@docusaurus/theme-common';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

import MeowCommentsUI from 'meow-comment-ui';
import 'meow-comment-ui/MeowCommentUI.css'

export default function ArtalkComments() {
    const location = useLocation();
    const { colorMode } = useColorMode();
    const { i18n } = useDocusaurusContext();

    const localeMap: Record<string, string> = {
        'en': 'en-US',
        'zh-Hans': 'zh-CN',
    };

    const artalkLocale = localeMap[i18n.currentLocale] || 'en-US';

    useEffect(() => {
        if (typeof window === 'undefined') return;

        const artalk = MeowCommentsUI.init({
            el: '#artalk-container',
            pageKey: location.pathname,
            pageTitle: document.title,
            baseUrl: 'https://artcdn.bttwiki.com',
            darkMode: colorMode === 'dark',
            locale: artalkLocale,
        });

        return () => artalk.destroy();
    }, [location.pathname, colorMode, i18n.currentLocale]);

    return <div id="artalk-container" />;
}
